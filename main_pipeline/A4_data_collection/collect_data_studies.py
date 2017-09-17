import os
from os.path import join as jph
import pickle

from main_pipeline.A0_main.main_controller import ListSubjectsManager
from tools.definitions import root_study_rabbits, pfi_excel_table_all_data, pfo_subjects_parameters, \
    root_internal_template
from tools.measurements.compile_record import compile_record
from tools.auxiliary.utils import print_and_run


def compile_records_from_subject_list(subj_list):

    print '\n\n Collecting data subjects in the list {}'.format(subj_list)

    for sj in subj_list:
        # grab modalities
        sj_parameters = pickle.load(open(jph(pfo_subjects_parameters, sj), 'r'))

        study = sj_parameters['study']
        category = sj_parameters['category']
        pfo_input_data = jph(root_study_rabbits, 'A_data', study, category)
        pfo_sj = jph(pfo_input_data, sj)
        pfi_T1 = jph(pfo_sj, 'mod', sj + '_T1.nii.gz')
        pfi_FA = jph(pfo_sj, 'mod', sj + '_FA.nii.gz')
        pfi_ADC = jph(pfo_sj, 'mod', sj + '_MD.nii.gz')
        pfi_g_ratio = jph(pfo_sj, 'mod', sj + '_g_ratio.nii.gz')
        # -
        # grab segmentations
        selected_segmentation = '_MV_s'
        pfi_segm_T1_sj = jph(pfo_sj, 'segm', sj + '_T1_segm{}.nii.gz'.format(selected_segmentation))
        pfi_segm_S0_sj = jph(pfo_sj, 'segm', sj + '_S0_segm{}.nii.gz'.format(selected_segmentation))
        pfi_segm_g_ratio = pfi_segm_S0_sj

        pfo_output_record_sj = jph(pfo_input_data, sj, 'records')
        cmd = 'mkdir -p {}'.format(pfo_output_record_sj)
        print_and_run(cmd)
        # grab label descriptor
        pfi_multi_labels_descr = jph(root_internal_template, 'LabelsDescriptors', 'multi_labels_descriptor.txt')
        assert os.path.exists(pfi_multi_labels_descr)
        assert os.path.exists(pfi_excel_table_all_data)

        print '\n\n DATA PARSING SUBJECT {} \n\n'.format(sj)

        # Compile records
        compile_record(pfi_T1=pfi_T1,
                       pfi_FA=pfi_FA,
                       pfi_ADC=pfi_ADC,
                       pfi_g_ratio=pfi_g_ratio,
                       pfi_multi_lab_descriptor=pfi_multi_labels_descr,
                       pfi_segm_T1=pfi_segm_T1_sj,
                       pfi_segm_FA=pfi_segm_S0_sj,
                       pfi_segm_ADC=pfi_segm_S0_sj,
                       pfi_segm_g_ratio=pfi_segm_g_ratio,
                       pfi_excel_table=pfi_excel_table_all_data,
                       subject_name=sj,
                       pfo_output=pfo_output_record_sj,
                       save_human_readable=True,
                       create_output_folder_if_not_present=True
                       )


if __name__ == '__main__':
    print('Collect data, local run. ')

    lsm = ListSubjectsManager()

    # lsm.execute_PTB_ex_skull = False
    # lsm.execute_PTB_ex_vivo = False
    # lsm.execute_PTB_in_vivo = True
    # lsm.execute_PTB_op_skull = False
    # lsm.execute_ACS_ex_vivo = False

    lsm.input_subjects = ['3103', ]
    lsm.update_ls()

    compile_records_from_subject_list(lsm.ls)
    # execute_processing_DWI(controller_steps, rpa_dwi)
