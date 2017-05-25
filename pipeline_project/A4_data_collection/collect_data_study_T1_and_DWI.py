import os
from os.path import join as jph

import numpy as np

from definitions import root_docs_dropbox, root_pilot_study_pantopolium
from pipeline_project.A0_main.main_controller import RunParameters
from tools.measurements.compile_record import compile_record


def compile_record_per_group(pfo_input_data, tuple_subjects=None):
    assert os.path.exists(pfo_input_data)
    subj_list = np.sort(list(set(os.listdir(pfo_input_data)) - {'.DS_Store'}))
    if tuple_subjects is not None:
        subj_list = tuple_subjects

    print '\n\n Collecting data for a group of subjects. ' \
          'Target group folder {0}\n' \
          'Subjects {1}\n'.format(pfo_input_data, subj_list)

    for sj in subj_list:
        # grab modalities
        pfo_sj = jph(pfo_input_data, sj)
        pfi_T1 = jph(pfo_sj, 'mod', sj + '_T1.nii.gz')
        pfi_FA = jph(pfo_sj, 'mod', sj + '_FA.nii.gz')
        pfi_ADC = jph(pfo_sj, 'mod', sj + '_MD.nii.gz')
        # -
        can_collect_data = True
        if not os.path.exists(pfi_T1):
            print('RECORD DATA not possible for subject {}. T1 not present'.format(sj))
            print pfi_T1
            can_collect_data = False
        if not os.path.exists(pfi_FA):
            print('RECORD DATA not possible for subject {}. FA not present'.format(sj))
            can_collect_data = False
        if not os.path.exists(pfi_ADC):
            print('RECORD DATA not possible for subject {}. ADC not present'.format(sj))
            can_collect_data = False
        # grab segmentations
        pfi_segm_T1_sj = jph(pfo_sj, 'segm', sj + '_T1_segm.nii.gz')
        pfi_segm_S0_sj = jph(pfo_sj, 'segm', sj + '_S0_segm.nii.gz')
        if not os.path.exists(pfi_segm_T1_sj):
            print('RECORD DATA not possible for subject {}. Segmentation T1 not present'.format(sj))
            can_collect_data = False
        if not os.path.exists(pfi_segm_S0_sj):
            print('RECORD DATA not possible for subject {}. Segmentation S0 not present'.format(sj))
            can_collect_data = False
        if can_collect_data:

            pfo_output_record_sj = jph(pfo_input_data, sj, 'records')
            cmd = 'mkdir -p {}'.format(pfo_output_record_sj)
            os.system(cmd)
            # grab label descriptor
            pfi_multi_labels_descr = jph(root_pilot_study_pantopolium, 'A_data', 'Utils', 'multi_label_descriptor.txt')
            assert os.path.exists(pfi_multi_labels_descr)
            # grab excel table
            pfi_excel_table = jph(root_docs_dropbox, 'REoP_Pilot_MRI_Data.xlsx')
            assert os.path.exists(pfi_excel_table)

            print '\n\n DATA PARSING SUBJECT {} \n\n'.format(sj)

            # Compile records
            compile_record(pfi_T1=pfi_T1,
                           pfi_FA=pfi_FA,
                           pfi_ADC=pfi_ADC,
                           pfi_multi_lab_descriptor=pfi_multi_labels_descr,
                           pfi_segm_T1=pfi_segm_T1_sj,
                           pfi_segm_FA=pfi_segm_S0_sj,
                           pfi_segm_ADC=pfi_segm_S0_sj,
                           pfi_excel_table=pfi_excel_table,
                           subject_name=sj,
                           pfo_output=pfo_output_record_sj,
                           save_human_readable=True,
                           create_output_folder_if_not_present=True
                           )


def compile_record_T1_DWI(rp):

    assert os.path.isdir(root_pilot_study_pantopolium), 'Connect pantopolio!'
    assert isinstance(rp, RunParameters)

    root_data    = jph(root_pilot_study_pantopolium, 'A_data')

    if rp.execute_PTB_ex_skull:
        pfo_PTB_ex_skull_data = jph(root_data, 'PTB', 'ex_skull')
        assert os.path.exists(pfo_PTB_ex_skull_data)
        compile_record_per_group(pfo_PTB_ex_skull_data, rp.subjects)

    if rp.execute_PTB_ex_vivo:
        pfo_PTB_ex_vivo_data = jph(root_data, 'PTB', 'ex_vivo')
        assert os.path.exists(pfo_PTB_ex_vivo_data)
        compile_record_per_group(pfo_PTB_ex_vivo_data, rp.subjects)

    if rp.execute_PTB_in_vivo:
        pfo_PTB_in_vivo_data = jph(root_data, 'PTB', 'in_vivo')
        assert os.path.exists(pfo_PTB_in_vivo_data)
        compile_record_per_group(pfo_PTB_in_vivo_data, rp.subjects)

    if rp.execute_PTB_op_skull:
        pfo_PTB_op_skull_data = jph(root_data, 'PTB', 'op_skull')
        assert os.path.exists(pfo_PTB_op_skull_data)
        compile_record_per_group(pfo_PTB_op_skull_data, rp.subjects)

    if rp.execute_ACS_ex_vivo:
        pfo_ACS_ex_vivo_data = jph(root_data, 'ACS', 'ex_vivo')
        assert os.path.exists(pfo_ACS_ex_vivo_data)
        compile_record_per_group(pfo_ACS_ex_vivo_data, rp.subjects)


if __name__ == '__main__':
    print('Collect data, local run. ')

    # rpa = RunParameters()

    # rpa.execute_PTB_ex_skull = False
    # rpa.execute_PTB_ex_vivo = True
    # rpa.execute_PTB_in_vivo = True
    # rpa.execute_PTB_op_skull = False
    # rpa.execute_ACS_ex_vivo = False

    # rpa.subjects = None
    # rpa.update_params()
    # rpa.subjects = ['2702', ]
    # rpa.update_params()

    # compile_record_T1_DWI(rpa)