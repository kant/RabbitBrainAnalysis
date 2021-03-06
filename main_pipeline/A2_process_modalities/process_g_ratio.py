import os
import numpy as np
from os.path import join as jph
import pickle

from tools.definitions import root_study_rabbits, root_fit_apps, pfo_subjects_parameters
from tools.auxiliary.utils import print_and_run
from nilabels.tools.aux_methods.sanity_checks import check_path_validity
from main_pipeline.A0_main.main_controller import ListSubjectsManager
from main_pipeline.A0_main.subject_parameters_manager import list_all_subjects


def transpose_matrix_in_txt(pfi_input, pfi_output):
    m = np.loadtxt(pfi_input)
    np.savetxt(fname=pfi_output, X=m.T)


def process_g_ratio_per_subject(sj, controller):

    print('\nProcessing g-ratio {} started.\n'.format(sj))

    if sj not in list_all_subjects(pfo_subjects_parameters):
        raise IOError('Subject parameters not known. Subject {}'.format(sj))

    sj_parameters = pickle.load(open(jph(pfo_subjects_parameters, sj), 'r'))

    study    = sj_parameters['study']
    category = sj_parameters['category']

    DWI_suffix = sj_parameters['names_architecture']['DWI']  # default is DWI

    pfo_input_sj_DWI  = jph(root_study_rabbits, '02_nifti', study, category, sj, '{}_{}'.format(sj, DWI_suffix))
    pfo_input_sj_MSME = jph(root_study_rabbits, '02_nifti', study, category, sj, sj + '_MSME')
    pfo_output_sj     = jph(root_study_rabbits, 'A_data', study, category, sj)

    # input sanity check:
    if not os.path.exists(pfo_input_sj_DWI):
        print('DWI modality not given in the input folder after Nifti conversion. Bypass methods involving DWI')
        return
    if not os.path.exists(pfo_input_sj_MSME):
        print('MSME modality not given in the input folder after Nifti conversion. Bypass methods involving MSME')
        return
    if not os.path.exists(pfo_output_sj):
        raise IOError('Output folder subject {} does not exist.'.format(pfo_output_sj))

    # --  Generate intermediate and output folder

    pfo_mod  = jph(pfo_output_sj, 'mod')
    pfo_segm = jph(pfo_output_sj, 'segm')
    pfo_mask = jph(pfo_output_sj, 'masks')
    pfo_tmp  = jph(pfo_output_sj, 'z_tmp', 'z_gr{}'.format(DWI_suffix))

    print_and_run('mkdir -p {}'.format(pfo_output_sj))
    print_and_run('mkdir -p {}'.format(pfo_mod))
    print_and_run('mkdir -p {}'.format(pfo_segm))
    print_and_run('mkdir -p {}'.format(pfo_mask))
    print_and_run('mkdir -p {}'.format(pfo_tmp))

    # --

    if controller['transpose_bvals_bvects']:
        print('- Transpose b-vals and b-vects')
        pfi_bvals  = jph(pfo_input_sj_DWI, '{}_{}_DwEffBval.txt'.format(sj, DWI_suffix))
        pfi_bvects = jph(pfo_input_sj_DWI, '{}_{}_DwGradVec.txt'.format(sj, DWI_suffix))
        assert check_path_validity(pfi_bvals)
        assert check_path_validity(pfi_bvects)
        pfi_transposed_bvals = jph(pfo_tmp, '{}_{}_DwEffBval_T.txt'.format(sj, DWI_suffix))
        pfi_transposed_vects = jph(pfo_tmp, '{}_{}_DwGradVec_T.txt'.format(sj, DWI_suffix))
        m = np.loadtxt(pfi_bvals)
        np.savetxt(fname=pfi_transposed_bvals, X=m.T, delimiter=' ', newline=' ', fmt='%10.8f')
        m = np.loadtxt(pfi_bvects)
        np.savetxt(fname=pfi_transposed_vects, X=m.T, fmt='%10.8f')

    if controller['get_acquisition_echo_time']:
        pfi_visu_pars = jph(pfo_input_sj_MSME, sj + '_MSME_visu_pars.npy')
        assert check_path_validity(pfi_visu_pars), pfi_visu_pars
        pfi_echo_times = jph(pfo_tmp, sj + '_echo_times.txt')
        visu_pars_dict = np.load(pfi_visu_pars)
        np.savetxt(fname=pfi_echo_times, X=visu_pars_dict.item().get('VisuAcqEchoTime'), fmt='%10.2f', newline=' ')

    if controller['noddi']:
        print('- Noddi execution')
        # check if there is a DWI already processed in the TMP folder of the same subject:
        pfo_tmp_dwi = jph(pfo_output_sj, 'z_tmp', 'z_' + DWI_suffix)
        pfi_dwi_eddy_corrected = jph(pfo_tmp_dwi, '{}_{}_eddy.nii.gz'.format(sj, DWI_suffix))

        pfi_roi_mask           = jph(pfo_mask, '{}_S0_roi_mask.nii.gz'.format(sj))

        pfi_transposed_bvals   = jph(pfo_tmp, '{}_{}_DwEffBval_T.txt'.format(sj, DWI_suffix))
        pfi_transposed_vects   = jph(pfo_tmp, '{}_{}_DwGradVec_T.txt'.format(sj, DWI_suffix))
        pfi_echo_times         = jph(pfo_tmp, '{}_echo_times.txt'.format(sj))

        assert check_path_validity(pfi_dwi_eddy_corrected), 'Need to run process_DWI first?'
        assert check_path_validity(pfi_transposed_bvals)
        assert check_path_validity(pfi_transposed_vects)
        assert check_path_validity(pfi_roi_mask)
        assert check_path_validity(pfi_echo_times)
        pfi_output_noddi = jph(pfo_tmp, '{}_nod.nii.gz'.format(sj))
        cmd = root_fit_apps + 'fit_dwi -source {0} -mask {1} -bval {2} -bvec {3} -TE {4} -mcmap {5} -nod'.format(
            pfi_dwi_eddy_corrected, pfi_roi_mask, pfi_transposed_bvals, pfi_transposed_vects, pfi_echo_times,
            pfi_output_noddi)
        print_and_run(cmd)

    if controller['save_T2times']:
        if sj_parameters['category'] == 'ex_vivo':
            t2_times = (8, 50, 60)  # (15, 80, 110) 30, 160, 200 - 14, 70, 100
        elif sj_parameters['category'] == 'in_vivo':
            t2_times = (10, 60, 80)
        else:
            t2_times = (10, 60, 80)
        pfi_T2_times = jph(pfo_tmp, sj + '_t2_times.txt')
        np.savetxt(fname=pfi_T2_times, X=np.array(t2_times), fmt='%10.10f', newline=' ')

    if controller['fit_msme']:
        pfi_msme_inS0 = jph(pfo_mod, sj + '_MSMEinS0.nii.gz')
        pfi_roi_mask = jph(pfo_mask, sj + '_S0_roi_mask.nii.gz')
        pfi_echo_times = jph(pfo_tmp, sj + '_echo_times.txt')
        pfi_T2_times = jph(pfo_tmp, sj + '_t2_times.txt')
        assert check_path_validity(pfi_msme_inS0), 'Need to run process_MSME first?'
        assert check_path_validity(pfi_roi_mask)
        assert check_path_validity(pfi_echo_times)
        assert check_path_validity(pfi_T2_times)
        pfi_mwf = jph(pfo_tmp, sj + '_vmvf.nii.gz')
        cmd = root_fit_apps + 'fit_qt2 -source {0} -mask {1} -nc 3 -TElist {2} -T2list {3} -mwf {4}'.format(
            pfi_msme_inS0, pfi_roi_mask, pfi_echo_times, pfi_T2_times, pfi_mwf)
        print cmd
        print_and_run(cmd)
        assert check_path_validity(pfi_mwf)
        if not os.path.exists(pfi_mwf):
            raise IOError('Something went wrong in using fit_qt2...')

    if controller['extract_first_tp_noddi']:
        pfi_noddi = jph(pfo_tmp, sj + '_nod.nii.gz')
        assert check_path_validity(pfi_noddi)
        pfi_vin = jph(pfo_tmp, sj + '_vin.nii.gz')
        cmd = 'seg_maths {0} -tp 0 {1}'.format(pfi_noddi, pfi_vin)
        print_and_run(cmd)

    if controller['compute_gratio']:
        pfi_mwf = jph(pfo_tmp, sj + '_vmvf.nii.gz')
        pfi_vin = jph(pfo_tmp, sj + '_vin.nii.gz')
        assert check_path_validity(pfi_mwf)
        assert check_path_validity(pfi_vin)
        pfi_tmp = jph(pfo_tmp, sj + '_tmp_g_ratio.nii.gz')
        pfi_g_ratio = jph(pfo_tmp, sj + '_g_ratio.nii.gz')
        cmd1 = 'seg_maths {0} -mul -1. {1}'.format(pfi_mwf, pfi_tmp)
        cmd2 = 'seg_maths {0} -add 1.0 {0}'.format(pfi_tmp)
        cmd3 = 'seg_maths {0} -mul {1} {0}'.format(pfi_tmp, pfi_vin)
        cmd4 = 'seg_maths {0} -div {1} {1}'.format(pfi_mwf, pfi_tmp)
        cmd5 = 'seg_maths {0} -add 1.0 {0}'.format(pfi_tmp)
        cmd6 = 'seg_maths {0} -recip {0}'.format(pfi_tmp)
        cmd7 = 'seg_maths {0} -sqrt {0}'.format(pfi_tmp)
        cmd8 = 'seg_maths {0} -uthr 0.999999999 {1}'.format(pfi_tmp, pfi_g_ratio)
        print_and_run(cmd1)
        print_and_run(cmd2)
        print_and_run(cmd3)
        print_and_run(cmd4)
        print_and_run(cmd5)
        print_and_run(cmd6)
        print_and_run(cmd7)
        print_and_run(cmd8)

    if controller['save_results']:
        pfi_g_ratio = jph(pfo_tmp, sj + '_g_ratio.nii.gz')
        assert check_path_validity(pfi_g_ratio)
        pfi_g_ratio_final = jph(pfo_mod, sj + '_g_ratio.nii.gz')
        cmd = 'cp {} {} '.format(pfi_g_ratio, pfi_g_ratio_final)
        print_and_run(cmd)


def process_g_ratio_from_list(subj_list, controller):

    print '\n\n Processing g-ratio subjects from list {0} \n'.format(subj_list)

    for sj in subj_list:
        process_g_ratio_per_subject(sj, controller)


if __name__ == '__main__':
    print('process g-ratio, local run. ')

    controller_steps = {'transpose_bvals_bvects'    : False,
                        'get_acquisition_echo_time' : True,
                        'noddi'                     : True,
                        'save_T2times'              : False,
                        'fit_msme'                  : False,
                        'extract_first_tp_noddi'    : False,
                        'compute_gratio'            : False,
                        'save_results'              : False}

    lsm = ListSubjectsManager()

    lsm.execute_PTB_ex_skull = False
    lsm.execute_PTB_ex_vivo  = False
    lsm.execute_PTB_in_vivo  = False
    lsm.execute_PTB_op_skull = False
    lsm.execute_ACS_ex_vivo  = False

    lsm.input_subjects = ['12503', ]

    lsm.update_ls()

    process_g_ratio_from_list(lsm.ls, controller_steps)
