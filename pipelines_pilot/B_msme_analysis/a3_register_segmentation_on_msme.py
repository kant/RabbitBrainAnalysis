"""
Analysis are preformed in bicommissural orientation, but for a better registration of the
latest segmentation,
"""
import numpy as np
import os
from os.path import join as jph

from definitions import root_pilot_study_dropbox
from tools.auxiliary.utils import print_and_run, adjust_header_from_transformations

"""
After importing the data in proper structure and having them with header properly oriented,
still need to squeeze, to orient according to MNI and to clean q-form and s-form.
"""

# controller
control = {'safety on'                        : False,
           'create interm folder'             : True,
           'set header bicommissural'         : True,  # create the image with bicomm header
           'get roi segmentation'             : True,
           'propagate to oversampled'         : True,
           'undersample the propagated'       : True}

# extra_cmd_reg_alaldin = '-speeeeed'
extra_cmd_reg_alaldin = ''

# main paths
root_pilot_study_msme_ex_vivo = jph(root_pilot_study_dropbox, 'A_msme_t2_analysis', 'ex_vivo')  # add z_ for tests
root_pilot_study_internal_template = jph(root_pilot_study_dropbox, 'A_internal_template')
pfo_utils = jph(root_pilot_study_dropbox, 'A_msme_t2_analysis', 'ex_vivo', 'Utils')
pfo_masks = jph(pfo_utils, 'masks')
pfi_aff_id = jph(pfo_utils, 'aff_id.txt')

pfi_msme_1201_ups = jph(root_pilot_study_msme_ex_vivo, '1201', 'mod', '1201_MSME_ups_layer1.nii.gz')
pfi_reg_mask_1201_standard  = jph(pfo_masks, '1201_registration_mask.nii.gz')
pfi_reg_mask_1201_upsampled = jph(pfo_masks, '1201_registration_mask_ups.nii.gz')

pfi_msme_2502_ups = jph(root_pilot_study_msme_ex_vivo, '2502', 'mod', '2502_MSME_ups_layer1.nii.gz')
pfi_reg_mask_2502_standard  = jph(pfo_masks, '2502_registration_mask.nii.gz')
pfi_reg_mask_2502_upsampled = jph(pfo_masks, '2502_registration_mask_ups.nii.gz')

for p in [root_pilot_study_msme_ex_vivo, pfo_utils, pfo_masks, pfi_reg_mask_1201_standard, pfi_reg_mask_1201_upsampled,
          pfi_reg_mask_2502_standard, pfi_reg_mask_2502_upsampled, pfi_msme_1201_ups, pfi_msme_2502_ups, pfi_aff_id]:
    if not os.path.exists(p):
        raise IOError('Path {} not defined'.format(p))

# subjects
list_subjects = np.sort(list(set(os.listdir(root_pilot_study_msme_ex_vivo)) -
                             {'.DS_Store', 'Utils', '1505', '2608', '2702'}))  # re-add 1505, 2608, 2702
print(list_subjects)


for sj in list_subjects:

    print('\n\n SUBJECT {}\n\n'.format(sj))

    if sj in ['1505', '2503', '2608', '2702']:
        sj_path = 'Dump/' + sj
    else:
        sj_path = sj

    ''' Input - ONLY FIRST LAYERS ARE CONSIDERED: '''

    # target MSME
    pfi_sj_standard = jph(root_pilot_study_msme_ex_vivo, sj, 'mod', sj + '_MSME_layer1.nii.gz')
    pfi_sj_oversampled = jph(root_pilot_study_msme_ex_vivo, sj, 'mod', sj + '_MSME_ups_layer1.nii.gz')
    pfi_T1_sj = jph(root_pilot_study_internal_template, sj_path, 'all_modalities', sj + '_T1.nii.gz')
    pfi_T1_roi_mask_sj = jph(root_pilot_study_internal_template, sj_path, 'masks', sj + '_roi_mask.nii.gz')

    # manually adjusted segmentations
    pfo_source = jph(root_pilot_study_dropbox, 'A_internal_template', sj_path)
    if os.path.exists(jph(pfo_source, 'segm', 'approved', sj + '_propagate_me_3.nii.gz')):
        pfi_segm_sj = jph(pfo_source, 'segm', 'approved', sj + '_propagate_me_3.nii.gz')
    elif os.path.exists(jph(pfo_source, 'segm', 'approved', sj + '_propagate_me_2.nii.gz')):
        pfi_segm_sj = jph(pfo_source, 'segm', 'approved', sj + '_propagate_me_2.nii.gz')
    else:
        pfi_segm_sj = jph(pfo_source, 'segm', 'approved', sj + '_propagate_me_1.nii.gz')

    for p in [pfi_sj_standard, pfi_sj_oversampled, pfi_segm_sj, pfi_T1_sj, pfi_T1_roi_mask_sj]:
        if not os.path.exists(p):
            raise IOError('Path {} not defined'.format(p))

    ''' Intermediate data '''

    pfo_intermediate_folder   = jph(root_pilot_study_msme_ex_vivo, sj, 'z_interm_data')

    pfi_T1_sj_bicomm_header          = jph(pfo_intermediate_folder, sj + '_T1_bicomm_header.nii.gz')
    pfi_T1_roi_mask_sj_bicomm_header = jph(pfo_intermediate_folder, sj + '_T1_roi_mask_bicomm_header.nii.gz')
    pfi_segm_sj_bicomm_header        = jph(pfo_intermediate_folder, sj + '_segm_roi_mask_bicomm_header.nii.gz')
    pfi_msme_1201_ups_on_sj          = jph(pfo_intermediate_folder, '1201_ups_on_' + sj + '.nii.gz')
    pfi_aff_msme_1201_ups_on_sj      = jph(pfo_intermediate_folder, '1201_ups_on_' + sj + '_aff.txt')
    pfi_T1_on_msme_sj                = jph(pfo_intermediate_folder, sj + '_T1_on_msme.nii.gz')
    pfi_aff_T1_on_msme_sj            = jph(pfo_intermediate_folder, sj + '_T1_on_msme_aff.txt')

    ''' Output '''

    pfi_reg_mask_ups_sj = jph(root_pilot_study_msme_ex_vivo, sj, 'segm', sj + '_roi_reg_mask_ups.nii.gz')
    pfi_propagated_segmentation_std = jph(root_pilot_study_msme_ex_vivo, sj, 'segm', sj + '_segm.nii.gz')
    pfi_propagated_segmentation_ups = jph(root_pilot_study_msme_ex_vivo, sj, 'segm', sj + '_segm_ups.nii.gz')

    ''' PIPELINE '''

    if control['create interm folder']:
        cmd = 'mkdir -p {}'.format(pfo_intermediate_folder)
        print_and_run(cmd, safety_on=control['safety on'])

    if control['set header bicommissural']:

        cmd0 = 'cp {0} {1}'.format(pfi_T1_sj, pfi_T1_sj_bicomm_header)
        cmd1 = 'cp {0} {1}'.format(pfi_segm_sj, pfi_segm_sj_bicomm_header)
        cmd2 = 'cp {0} {1}'.format(pfi_T1_roi_mask_sj, pfi_T1_roi_mask_sj_bicomm_header)
        print_and_run(cmd0, safety_on=control['safety on'])
        print_and_run(cmd1, safety_on=control['safety on'])
        print_and_run(cmd2, safety_on=control['safety on'])

        if sj not in ['1805', '2002', '2502']:  # change orientations of all the others

            theta = np.pi / float(3)
            if not control['safety on']:
                adjust_header_from_transformations(pfi_T1_sj_bicomm_header, pfi_T1_sj_bicomm_header,
                                                   theta=theta, trasl=(0, 0, 0))
                adjust_header_from_transformations(pfi_segm_sj_bicomm_header, pfi_segm_sj_bicomm_header,
                                                   theta=theta, trasl=(0, 0, 0))
                adjust_header_from_transformations(pfi_T1_roi_mask_sj_bicomm_header, pfi_T1_roi_mask_sj_bicomm_header,
                                                   theta=theta, trasl=(0, 0, 0))

    if control['get roi segmentation']:

        if sj == '1201':
            cmd = 'cp {0} {1}'.format(pfi_reg_mask_1201_upsampled, pfi_reg_mask_ups_sj)
            print_and_run(cmd, safety_on=control['safety on'])
        elif sj == '2502':
            cmd = 'cp {0} {1}'.format(pfi_reg_mask_2502_upsampled, pfi_reg_mask_ups_sj)
            print_and_run(cmd, safety_on=control['safety on'])
        else:
            cmd0 = 'reg_aladin -ref {0} -flo {1} -aff {2} -res {3} -rigOnly {4}'.format(pfi_sj_oversampled,
                                                                                    pfi_msme_1201_ups,
                                                                                    pfi_aff_msme_1201_ups_on_sj,
                                                                                    pfi_msme_1201_ups_on_sj,
                                                                                    extra_cmd_reg_alaldin)
            cmd1 = 'reg_resample -ref {0} -flo {1} -trans {2} -res {3} -inter 0'.format(pfi_sj_oversampled,
                                                                                          pfi_reg_mask_1201_upsampled,
                                                                                          pfi_aff_msme_1201_ups_on_sj,
                                                                                          pfi_reg_mask_ups_sj)
            print_and_run(cmd0, safety_on=control['safety on'])
            print_and_run(cmd1, safety_on=control['safety on'])

    if control['propagate to oversampled']:

        if not control['safety on']:
            for p in [pfi_reg_mask_ups_sj, pfi_T1_sj_bicomm_header, pfi_segm_sj_bicomm_header]:
                if not os.path.exists(p):
                    raise IOError('non existing ' + p)

        cmd0 = 'reg_aladin -ref {0} -rmask {1} -flo {2} -fmask {3} -aff {4} -res {5} -rigOnly'.format(
                            pfi_sj_oversampled,
                            pfi_reg_mask_ups_sj,
                            pfi_T1_sj_bicomm_header,
                            pfi_T1_roi_mask_sj,
                            pfi_aff_T1_on_msme_sj,
                            pfi_T1_on_msme_sj)

        cmd1 = 'reg_resample -ref {0} -flo {1} -trans {2} -res {3} -inter 0'.format(pfi_sj_oversampled,
                                                                                    pfi_segm_sj_bicomm_header,
                                                                                    pfi_aff_T1_on_msme_sj,
                                                                                    pfi_propagated_segmentation_ups)

        print_and_run(cmd0, safety_on=control['safety on'])
        print_and_run(cmd1, safety_on=control['safety on'])

    if control['undersample the propagated']:

        if not control['safety on']:
            assert os.path.exists(pfi_propagated_segmentation_ups)

        cmd = 'reg_resample -ref {0} -flo {1} -trans {2} -res {3} -inter 0'.format(pfi_sj_standard,
                                                                                   pfi_propagated_segmentation_ups,
                                                                                   pfi_aff_id,
                                                                                   pfi_propagated_segmentation_std)
        print_and_run(cmd, safety_on=control['safety on'])
