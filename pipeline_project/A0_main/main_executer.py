import os

from pipeline_project.A0_main.main_controller import RunParameters, templ_subjects
from definitions import root_study_pantopolium, root_study_dropbox

from pipeline_project.A1_convert_and_clean.apply_converter_to_all_data import execute_converter
from pipeline_project.A1_convert_and_clean.clean_converted_data import execute_cleaner
from pipeline_project.A1_convert_and_clean.create_aliases_in_data_folder import execute_generate_alias

from pipeline_project.A2_process_modalities.process_T1 import execute_processing_T1
from pipeline_project.A2_process_modalities.process_DWI import execute_processing_DWI
from pipeline_project.A2_process_modalities.process_MSME import execute_processing_MSME

from pipeline_project.A3_register_template_over_all_subjects.propagate_and_fuse_main import execute_propag_and_fuse_all

from pipeline_project.A4_data_collection.collect_data_study_T1_and_DWI import compile_record_T1_DWI
from pipeline_project.A4_data_collection.collect_data_study_MSME import compile_record_MSME

from pipeline_project.U_utils.upate_shared_results import send_data_to_hannes
from pipeline_project.U_utils.copy_to_excel_file import save_data_into_excel_file


if __name__ == '__main__':

    assert os.path.isdir(root_study_pantopolium), 'Connect pantopolio!'

    ''' Set parameters per subjects or per group '''

    rpa = RunParameters()

    # rpa.execute_PTB_ex_skull = False
    # rpa.execute_PTB_ex_vivo  = False
    # rpa.execute_PTB_in_vivo  = False
    # rpa.execute_PTB_op_skull = False
    # rpa.execute_ACS_ex_vivo  = True

    rpa.subjects = ['3505', '3507', '3602', '3604', '3606',]
    #  '3307', '3404']  # '2608', '2702'
    rpa.update_params()

    ''' Set steps '''

    step_A1      = False
    step_A2_T1   = False
    step_A2_MSME = False
    step_A2_DWI  = False
    step_A3      = False
    step_A4      = True
    step_A5      = True

    ''' Step A1 - convert, clean and create aliases '''
    if step_A1:
        print('\nStep A1\n')
        execute_converter(rpa)
        execute_cleaner(rpa)
        execute_generate_alias(rpa)

    ''' Step A2 - T1 '''
    if step_A2_T1:
        print('\nStep A2 T1\n')
        controller_A2_T1 = {'orient to standard'  : False,
                            'register roi masks'  : False,
                            'propagate roi masks' : True,
                            'adjust mask'         : True,
                            'cut masks'           : True,
                            'step bfc'            : True,
                            'create lesion mask'  : True,
                            'create reg masks'    : True,
                            'save results'        : True}

        execute_processing_T1(controller_A2_T1, rpa)

    ''' Step A2 - MSME '''
    if step_A2_MSME:
        print('\nStep A2 MSME\n')
        controller_MSME = {'squeeze'               : True,
                            'orient to standard'   : True,
                            'oversample'           : True,
                            'extract first layers' : True,
                            'register roi masks'   : True,
                            'propagate roi masks'  : True
                           }

        execute_processing_MSME(controller_MSME, rpa)

    ''' Step A2 - DWI '''
    if step_A2_DWI:
        print('\nStep A2 DWI\n')
        controller_DWI = {'squeeze'                : False,
                            'orient to standard'   : True,
                            'register roi masks'   : True,
                            'propagate roi masks'  : True,
                            'adjust mask'          : True,
                            'cut mask dwi'         : True,
                            'cut mask b0'          : True,
                            'correct slope'        : True,
                            'eddy current'         : True,
                            'fsl tensor fitting'   : True,
                            'adjust dti-based mod' : True,
                            'bfc b0'               : True,
                            'create lesion mask'   : True,
                            'create reg masks'     : True,
                            'save results'         : True}

        execute_processing_DWI(controller_DWI, rpa)

    ''' Step A3 - Propagate template '''
    if step_A3:
        print('\nStep A3\n')
        controller_fuser_ = {'set header bicommissural'  : True,
                             'aff alignment'             : True,
                             'Propagate aff to segm'     : True,
                             'Propagate aff to mask'     : True,
                             'Get differential BFC'      : True,
                             'N-rig alignment'           : True,
                             'Propagate to target n-rig' : True,
                             'Smooth result'             : True,
                             'Stack warps and segm'      : True,
                             'Fuse'                      : True,
                             'save result'               : True
                             }

        controller_propagator_ = {'set header bicommissural' : True,
                                  'rig alignment'            : True,
                                  'Propagate aff to segm'    : True,
                                  'Propagate aff to mask'    : True,
                                  'Smooth'                   : True,
                                  'save result'              : True}

        controller_inter_modality_propagator_ = {'compensate squeezing'     : True,
                                                 'rig register to S0'       : True,
                                                 'rig propagate to S0'      : True,
                                                 'rig register to MSME_up'  : True,
                                                 'rig propagate to MSME_up' : True,
                                                 'MSME_up to MSME'          : True}
        pfo_templ_subjects_input = os.path.join(root_study_dropbox, 'A_internal_template')
        list_templ_subjects_input = templ_subjects

        execute_propag_and_fuse_all(controller_fuser_, controller_propagator_, controller_inter_modality_propagator_,
                                    pfo_templ_subjects_input, list_templ_subjects_input, rpa)

    ''' Step A4 - Data collection '''
    if step_A4:
        print('\nStep A4\n')
        compile_record_T1_DWI(rpa)
        compile_record_MSME(rpa)

    if step_A5:
        send_data_to_hannes(rpa, records_only=False)
        save_data_into_excel_file(rpa)
