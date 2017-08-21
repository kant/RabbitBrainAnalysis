"""

We extract a T2 map for each of the MSME T2 processed.
Images are kept whole and not trimmed by any mask, as the eye information is fundamental.

Input are 4 different MSME processing output:
> original, no corrections -> <id>_MSME.nii.gz
> original BFC             -> <id>_MSME_bfc.nii.gz
> upsampled to S0          -> <id>_MSME_up.nii.gz
> upsampled to S0 BFC      -> <id>_MSME_bfc_up.nii.gz

And the TE during the acquisition.

OUTPUT are the four corresponding estimated T2maps.


> from original, no corrections -> <id>_T2ma.nii.gz
> form original BFC             -> <id>_T2ma_bfc.nii.gz
> from upsampled to S0          -> <id>_T2ma_up.nii.gz
> from upsampled to S0 BFC      -> <id>_T2ma_bfc_up.nii.gz
"""

import os
from os.path import join as jph
import numpy as np
import nibabel as nib
import pickle

from tools.definitions import root_study_rabbits, pfo_subjects_parameters
from pipeline_project.A0_main.main_controller import ListSubjectsManager
from pipeline_project.A0_main.subject_parameters_manager import list_all_subjects

from labels_manager.tools.aux_methods.utils import print_and_run
from labels_manager.tools.aux_methods.utils_nib import set_new_data
from labels_manager.tools.aux_methods.sanity_checks import check_path_validity
from tools.definitions import root_fit_apps


def process_T2_map_per_subject(sj, controller):

    print('\nProcessing T2 map {} started.\n'.format(sj))

    sj_parameters = pickle.load(open(jph(pfo_subjects_parameters, sj), 'r'))

    group = sj_parameters['group']
    category = sj_parameters['category']

    pfo_input_sj_MSME = jph(root_study_rabbits, '01_nifti', group, category, sj, sj + '_MSME')
    pfo_output_sj = jph(root_study_rabbits, 'A_data', group, category, sj)
    pfo_mod = jph(pfo_output_sj, 'mod')

    # input sanity check:
    if sj not in list_all_subjects(pfo_subjects_parameters):
        raise IOError('Subject parameters not known')
    if not os.path.exists(pfo_input_sj_MSME):
        raise IOError('Input folder MSME does not exist.')
    if not os.path.exists(pfo_output_sj):
        raise IOError('Output folder MSME does not exist.')
    if not os.path.exists(pfo_mod):
        raise IOError('Output folder MSME does not exist.')

    # --  Generate intermediate and output folder
    pfo_tmp = jph(pfo_output_sj, 'z_tmp', 'z_T2map')

    print_and_run('mkdir -p {}'.format(pfo_tmp))

    suffix = ['', '_bfc', '_up', '_bfc_up']

    if controller['get acquisition echo time']:
        pfi_visu_pars = jph(pfo_input_sj_MSME, sj + '_MSME_visu_pars.npy')
        assert check_path_validity(pfi_visu_pars)
        pfi_echo_times = jph(pfo_tmp, sj + '_echo_times.txt')
        visu_pars_dict = np.load(pfi_visu_pars)
        np.savetxt(fname=pfi_echo_times, X=visu_pars_dict.item().get('VisuAcqEchoTime'), fmt='%10.2f', newline=' ')

    if controller['process each MSME input']:
        pfi_echo_times = jph(pfo_tmp, sj + '_echo_times.txt')
        assert os.path.exists(pfi_echo_times)
        TE = np.loadtxt(pfi_echo_times)
        echo_delta = TE[2] - TE[1]
        # original
        for s in suffix:
            pfi_original_MSME = jph(pfo_mod, sj + '_MSME{}.nii.gz'.format(s))
            check_path_validity(pfi_original_MSME)
            pfi_T2map = jph(pfo_tmp, sj + '_T2map{}.nii.gz'.format(s))
            cmd1 = root_fit_apps + 'fit_qt2 -source {0} -TE {1} -t2map {2}'.format(pfi_original_MSME,
                                                                                   echo_delta, pfi_T2map)
            print cmd1
            print_and_run(cmd1)

    if controller['correct origin']:  # some versions of niftyfit for fit_qt2 are dividing by 0 in the origin.
        for s in suffix:
            pfi_T2map = jph(pfo_tmp, sj + '_T2map{}.nii.gz'.format(s))
            check_path_validity(pfi_T2map)
            pfi_T2map_corrected = jph(pfo_tmp, sj + '_corrected_T2map{}.nii.gz'.format(s))
            # clean upper outliers (Mean + 2 * StandardDeviation) ... They are more than outliers!
            im_s = nib.load(pfi_T2map)
            places_not_outliers = im_s.get_data() < 1000  # np.mean(im_s.get_data()) + 2 * np.std(im_s.get_data())
            im_s.get_data()[:] = places_not_outliers * im_s.get_data()
            im_corrected = set_new_data(im_s, places_not_outliers * im_s.get_data())
            nib.save(im_corrected, pfi_T2map_corrected)

    if controller['save results']:
        pfo_mod_T2map = jph(pfo_mod, 'T2_maps')
        cmd = 'mkdir -p {}'.format(pfo_mod_T2map)
        print_and_run(cmd)
        for s in suffix:
            pfi_T2map_corrected = jph(pfo_tmp, sj + '_corrected_T2map{}.nii.gz'.format(s))
            check_path_validity(pfi_T2map_corrected)
            pfi_T2map = jph(pfo_mod_T2map, sj + '_T2map{}.nii.gz'.format(s))
            cmd = 'cp {0} {1}'.format(pfi_T2map_corrected, pfi_T2map)
            print_and_run(cmd)


def process_t2_maps_from_list(subj_list, controller):

    print '\n\n Processing t2 subjects from list {0} \n'.format(subj_list)

    for sj in subj_list:
        process_T2_map_per_subject(sj, controller)


if __name__ == '__main__':

    print('process T2Maps, local run. ')

    controller_steps = {'get acquisition echo time'  : False,
                        'process each MSME input'    : False,
                        'correct origin'             : True,
                        'save results'               : True}

    lsm = ListSubjectsManager()

    lsm.execute_PTB_ex_skull = False
    lsm.execute_PTB_ex_vivo = False
    lsm.execute_PTB_in_vivo = False
    lsm.execute_PTB_op_skull = False
    lsm.execute_ACS_ex_vivo = False

    lsm.input_subjects = ['3103', ]

    lsm.update_ls()

    process_t2_maps_from_list(lsm.ls, controller_steps)
