import os
import numpy as np
from os.path import join as jph

from definitions import root_pilot_study_pantopolium
from pipeline_project.U_utils.main_controller import RunParameters


def link_folder_content_into_folder(folder_source, folder_target):

    assert os.path.exists(folder_source)
    assert os.path.exists(folder_target)

    fi_list = np.sort(list(set(os.listdir(folder_source)) - {'.DS_Store'}))

    for fi in fi_list:
        cmd = 'ln -s {0} {1}'.format(jph(folder_source, fi), jph(folder_target))
        os.system(cmd)


def create_alias_for_group(pfo_source, pfo_target):

    assert os.path.exists(pfo_source)
    assert os.path.exists(pfo_target)

    subj_list = np.sort(list(set(os.listdir(pfo_source)) - {'.DS_Store'}))

    print '\n\n LINKING SUBJECTS from {0} to {1}:\n {2}\n'.format(pfo_source, pfo_target, subj_list)

    for sj in subj_list:
        pfi_where_to_store_alias = jph(pfo_target, sj, 'a_' + sj)

        cmd1 = 'mkdir -p {}'.format(jph(pfo_target, sj))
        os.system(cmd1)
        cmd2 = 'mkdir -p {}'.format(pfi_where_to_store_alias)
        os.system(cmd2)

        # TMP:
        cmd3 = 'rm -r {}'.format(jph(pfo_target, sj, 'a_'))
        os.system(cmd3)

        link_folder_content_into_folder(jph(pfo_source, sj), pfi_where_to_store_alias)


def execute_generate_alias(rp):

    assert os.path.isdir(root_pilot_study_pantopolium), 'Connect pantopolio!'
    assert isinstance(rp, RunParameters)

    root_nifti = jph(root_pilot_study_pantopolium, '01_nifti')
    root_data = jph(root_pilot_study_pantopolium, 'A_data')

    if rp.execute_PTB_ex_skull:
        pfo_PTB_ex_skull = jph(root_nifti, 'PTB', 'ex_skull')
        assert os.path.exists(pfo_PTB_ex_skull), pfo_PTB_ex_skull
        pfo_PTB_ex_skull_data = jph(root_data, 'PTB', 'ex_skull')
        create_alias_for_group(pfo_PTB_ex_skull, pfo_PTB_ex_skull_data)

    if rp.execute_PTB_ex_vivo:
        pfo_PTB_ex_vivo = jph(root_nifti, 'PTB', 'ex_vivo')
        assert os.path.exists(pfo_PTB_ex_vivo), pfo_PTB_ex_vivo
        pfo_PTB_ex_vivo_data = jph(root_data, 'PTB', 'ex_vivo')
        create_alias_for_group(pfo_PTB_ex_vivo, pfo_PTB_ex_vivo_data)

    if rp.execute_PTB_in_vivo:
        pfo_PTB_in_vivo = jph(root_nifti, 'PTB', 'in_vivo')
        assert os.path.exists(pfo_PTB_in_vivo), pfo_PTB_in_vivo
        pfo_PTB_in_vivo_data = jph(root_data, 'PTB', 'in_vivo')
        create_alias_for_group(pfo_PTB_in_vivo, pfo_PTB_in_vivo_data)

    if rp.execute_PTB_op_skull:
        pfo_PTB_op_skull = jph(root_nifti, 'PTB', 'op_skull')
        assert os.path.exists(pfo_PTB_op_skull), pfo_PTB_op_skull
        pfo_PTB_op_skull_data = jph(root_data, 'PTB', 'op_skull')
        create_alias_for_group(pfo_PTB_op_skull, pfo_PTB_op_skull_data)

    if rp.execute_ACS_ex_vivo:
        pfo_ACS_ex_vivo = jph(root_nifti, 'ACS', 'ex_vivo')
        assert os.path.exists(pfo_ACS_ex_vivo), pfo_ACS_ex_vivo
        pfo_ACS_ex_vivo_data = jph(root_data, 'ACS', 'ex_vivo')
        create_alias_for_group(pfo_ACS_ex_vivo, pfo_ACS_ex_vivo_data)


if __name__ == '__main__':

    rpa = RunParameters()

    rpa.execute_PTB_ex_skull = True
    rpa.execute_PTB_ex_vivo = True
    rpa.execute_PTB_in_vivo = True
    rpa.execute_PTB_op_skull = True
    rpa.execute_ACS_ex_vivo = True

    rpa.subjects = None

    execute_generate_alias(rpa)
