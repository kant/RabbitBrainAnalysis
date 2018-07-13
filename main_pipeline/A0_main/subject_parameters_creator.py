import os
import numpy as np

from tools.definitions import pfo_subjects_parameters
from main_pipeline.A0_main.subject_parameters_manager import SubjectParameters, get_list_names_subjects_in_atlas, \
    check_subjects_situation


def reset_parameters_files(pfo_where_to_save):
    """
    Create an instance of SubjectParameter, for each subject of the study with parameters properly setted (MANUALLY),
    and then save them (or replace them) in the appropriate folder ERASING the previous one.
    :param pfo_where_to_save: path to file to the folder. This will be the storage room for each subject in the
    study.

    HERE IS WHERE YOU SET THE PRIVATE PARAMETERS OF EACH SUBJECT.
    (of course there are better ways -sql lite, excel, ...) but this is fast, free and super flexible).

    Bias field parameters order
    -------------
    convergenceThreshold = 0.001
    maximumNumberOfIterations = (50, 50, 50, 50)
    biasFieldFullWidthAtHalfMaximum = 0.15
    wienerFilterNoise = 0.01
    numberOfHistogramBins = 200
    numberOfControlPoints = (4, 4, 4)
    splineOrder = 3

    Angles order
    ----------
    Axial Angle, angle of the axial orientation sign from L to R,
    from initial position to aligned with axis (yaw).
    Bicomm (or coronal) Angle is the opening angle from bicomm to histological in rad (pitch).
    Sagittal Angle sign from L to R from initial position to aligned with axis (roll)

    :return: Storage room filled with the adequate parameters.
    """

    # TODO move to individual JSON files. Build an interface for the JSON files. Then eliminate this shameful module.

    # some parameters:
    bfp_slow = [0.001, (50, 50, 50, 50), 0.15, 0.01, 200, (4, 4, 4), 3]
    # bfp_fast = [0.01, (50, 40, 30, 20), 0.15, 0.01, 200, (4, 4, 4), 3]

    # eliminate if exists and re-create the folder where to save the data:
    if os.path.exists(pfo_where_to_save):
        os.system('rm -r {0}'.format(pfo_where_to_save))
        print('Folder {} deleted.'.format(pfo_where_to_save))
    os.system('mkdir {0}'.format(pfo_where_to_save))
    print('Folder {} created.'.format(pfo_where_to_save))
    # all the subjects

    ''' PTB ex skull: ---------------------------------------------------------------------- '''

    sp = SubjectParameters('0104')
    sp.study                  = 'PTB'
    sp.category               = 'ex_skull'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 300
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.mask_dilation          = 1
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.options_S0             = {'window_percentile'  : (0.1, 99.9),
                                 'mask_dilation'     : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (0.1, 99.9),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0209')
    sp.study                  = 'PTB'
    sp.category               = 'ex_skull'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 300
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.options_S0             = {'window_percentile'  : (0.1, 99.9),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (0.1, 99.9),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0303')
    sp.study                  = 'PTB'
    sp.category               = 'ex_skull'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 300
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.options_S0             = {'window_percentile'  : (0.1, 99.9),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (0.1, 99.9),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0307')
    sp.study                  = 'PTB'
    sp.category               = 'ex_skull'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 300
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.options_S0             = {'window_percentile'  : (0.1, 99.9),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (0.1, 99.9),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0308')
    sp.study                  = 'PTB'
    sp.category               = 'ex_skull'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 300
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.options_S0             = {'window_percentile'  : (0.1, 99.9),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (0.1, 99.9),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0309')
    sp.study                  = 'PTB'
    sp.category               = 'ex_skull'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 300
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.options_S0             = {'window_percentile'  : (0.1, 99.9),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (0.1, 99.9),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' PTB ex vivo: ---------------------------------------------------------------------- '''

    sp = SubjectParameters('1201')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 2}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 1.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1203')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 2}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 3.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1305')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 2}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 0.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1404')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : -0.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1505')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Dupmed due to excess of perivascular spaces enlargement.'
    sp.in_atlas               = False
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1507')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1510')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 12, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : -3.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1702')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Bubble parietal and occipital cortex Left'
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 2.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1805')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 12, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Bubble parietal left'
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 2}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 4,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2002')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 12, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : -3,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2502')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Low resolution original T1 (upsampled for template)'
    sp.in_atlas               = True
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 1.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2503')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 8, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = False
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 2}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 3,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2608')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 0.001
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = False
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 1,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2702')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 0.001
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = False
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 1}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (15, 90),
                                 'maks_dilation'      : 0.5,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('3301')
    sp.study                  = 'PTB'
    sp.category               = 'ex_vivo'
    sp.angles                 = [[0, np.pi / 8, 0], [0, np.pi / 6, 0]]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 0.001
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'DWI slab-like motion artefact, T1 wrapping artefact'
    sp.in_atlas               = True
    sp.b0_level               = 7
    sp.options_S0             = {'window_percentile'  : (1, 95),
                                 'mask_dilation'      : 3}
    sp.options_T1             = {'roi_mask'           : "Pivotal",
                                 'window_percentile'  : (5, 90),
                                 'maks_dilation'      : 2,
                                 'pivot'              : '1305',
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True}
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('3303')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [[0, np.pi / 8, 0], [0, np.pi / 6, 0]]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (5, 90)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 2
    sp.S0_mask_dilation = 3
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 motion and warping artefact, DWI severe motion artefact.'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('3404')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [[0, np.pi / 8, 0], [0, np.pi / 6, 0]]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (5, 90)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = True
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4302')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (18, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 0
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefacts'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4303')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefact DWI unusable - extra DWI in external study'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4304')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefacts'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4305')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefacts'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4406')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'No T1'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4501')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (15, 95)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 5
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping, DWI severe motion'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4504')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 small warping on cortex, small bubble on medial prefrontal cortex'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4507')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefact, DWI heavy motion artefact'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4601')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefact, DWI heavy motion artefact'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4602')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefact, DWI some motion artefact.'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4603')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = 'T1 warping artefact, DWI motion artefact.'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4901')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_T1 = {'roi_mask' : "BTMA",  # Can be BTMA, MA, Pivotal
                     'pivot'    : '2502',  # name of a template reference to get the roi mask or a first approximation (if in vivo '1504t1')
                     'slim'     : False,  # if you want to have the slim mask. 'roi_mask' must be "BTMA" or "MA" for it to be true.
                     'crop_roi' : False,  # To cut the T1 according to the ROI mask.
                     'lesion_mask_method' : 0,  # can be the total number of gaussians for a MoG approach, or 0 if you want to use the given percentile
                     'median_filter' : True  # if 'reg_mask' > 1 as pre-processing before the gaussians.
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4903')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('4905')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 12, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('5001')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 12, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('5003')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 12, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('5007')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 12, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('5009')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 12, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (74.8, 97)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = -2
    sp.S0_mask_dilation = 0
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12001')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [[0, np.pi / 12, 0], [0, np.pi / 8, 0]]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (10, 90)
    sp.S0_window_percentile = (5, 95)
    sp.T1_mask_dilation = 2
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' PTB TEST ---------------------------------------------------------------------- '''

    sp = SubjectParameters('Test67')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12001test')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('10508')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12002')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('Trial0702')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('TrialRSUC')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('TrialRSUC')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('F1Test')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('F2Test')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('11806')
    sp.study = 'TestStudy'
    sp.category = 'ex_vivo'
    sp.angles = [0, 0, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 0.001
    sp.T1_window_percentile = (12, 92)
    sp.S0_window_percentile = (1, 95)
    sp.T1_mask_dilation = 1
    sp.S0_mask_dilation = 2
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = '20 days old, some tissue decay.'
    sp.in_atlas = False
    sp.b0_level = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' PTB in-vivo ---------------------------------------------------------------------- '''

    sp = SubjectParameters('0802t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0904t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1501t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1504t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1508t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1509t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 5, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('1511t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2202t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2205t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2206t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2502t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2503t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2605t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Coil problem'
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('2702t1')
    sp.study                  = 'PTB'
    sp.category               = 'in_vivo'
    sp.angles                 = [0, np.pi / 12, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Coil problem'
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' PTB op-skull ---------------------------------------------------------------------- '''

    sp = SubjectParameters('0602')
    sp.study                  = 'PTB'
    sp.category               = 'op_skull'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0603')
    sp.study                  = 'PTB'
    sp.category               = 'op_skull'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 25
    sp.T1_window_percentile   = (10, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' ACS ex-vivo ---------------------------------------------------------------------- '''

    sp = SubjectParameters('0213103')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 20, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213108')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 20, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213301')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 20, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213307')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 20, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Dumped, too much ghosting in the DWI.'
    sp.in_atlas            = False
    sp.b0_level = 6
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213401')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, 0, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213403')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213404')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 25, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213405')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 25, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (2, 96)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213501')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 25, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213505')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 4, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Dumped as too much ghosting artefact in the MRI'
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213507')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213602')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 8, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Almost dumped, ghosted DWI can provide noisy information.'
    sp.in_atlas            = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213604')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = 'Dupmed, too much ghosting in the DWI'
    sp.in_atlas               = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('0213606')
    sp.study                  = 'ACS'
    sp.category               = 'ex_vivo02'
    sp.angles                 = [0, np.pi / 6, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.T1_window_percentile   = (5, 98)
    sp.S0_window_percentile   = (1, 99)
    sp.T1_mask_dilation       = 1
    sp.S0_mask_dilation       = 1
    sp.DWI_squashed           = True
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = False
    sp.b0_level               = 7
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' --------- ACS ex-vivo 01 ------'''

    sp = SubjectParameters('12307')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12308')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12309')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12402')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.b0_to_use_in_fsldti = [0, 1, 2]  # TODO Investigate further!!
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',  
                     'pivot'              : '1305',  
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,  
                     'crop_roi'           : False,  
                     'lesion_mask_method' : 0,
                     'median_filter'      : True  
                     }

    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12504')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12505')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12607')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12608')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12609')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('12610')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 6, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13102')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13201')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13401')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13402')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13403')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13202')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13403retest')
    sp.study = 'ACS'
    sp.category = 'ex_vivo01'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13003')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13004')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13005')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    sp = SubjectParameters('13006')
    sp.study = 'PTB'
    sp.category = 'ex_vivo'
    sp.angles = [0, np.pi / 8, 0]
    sp.translation = [0, 0, 0]
    sp.threshold = 18
    sp.DWI_squashed = False
    sp.bias_field_parameters = bfp_slow
    sp.MSME_acquisition = 'high_res'
    sp.comment = ''
    sp.in_atlas = False
    sp.b0_level = 7
    sp.options_S0 = {'window_percentile' : (1, 99),
                     'mask_dilation'     : 1
                     }
    sp.options_T1 = {'roi_mask'           : 'BTMA',
                     'pivot'              : '1305',
                     'mask_dilation'      : 5,
                     'window_percentile'  : (5, 98),
                     'slim'               : False,
                     'crop_roi'           : False,
                     'lesion_mask_method' : 0,
                     'median_filter'      : True
                     }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp

    ''' --------- 8 Weeks old ------'''

    sp = SubjectParameters('125930')
    sp.study                  = 'W8'
    sp.category               = 'first_trial'
    sp.angles                 = [0, np.pi / 8, 0]
    sp.translation            = [0, 0, 0]
    sp.threshold              = 18
    sp.DWI_squashed           = False
    sp.bias_field_parameters  = bfp_slow
    sp.MSME_acquisition       = 'high_res'
    sp.comment                = ''
    sp.in_atlas               = False
    sp.b0_level               = 7
    sp.options_S0             = {'window_percentile' : (1, 99),
                                 'mask_dilation'     : 1
                                 }
    sp.options_T1             = {'roi_mask'           : 'BTMA',
                                 'pivot'              : '1305',
                                 'mask_dilation'      : 5,
                                 'window_percentile'  : (5, 98),
                                 'slim'               : False,
                                 'crop_roi'           : False,
                                 'lesion_mask_method' : 0,
                                 'median_filter'      : True
                                 }
    sp.save_as_txt(pfo_where_to_save)
    sp.dump_with_pickle(pfo_where_to_save)
    del sp


if __name__ == '__main__':

    reset_parameters_files(pfo_subjects_parameters)
    sjs = get_list_names_subjects_in_atlas(pfo_subjects_parameters)

    print('Subjects summary: ')
    check_subjects_situation(pfo_subjects_parameters)
    print('\nTemplate:')
    # print sjs
