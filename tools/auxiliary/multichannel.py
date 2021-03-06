import numpy as np
import nibabel as nib
import os

from nilabels.tools.aux_methods.utils_nib import set_new_data
from nilabels.tools.aux_methods.utils import print_and_run


def generate_multichannel(list_data, channels_axis=3, normalize=True):
    """
    From a list of data (matrices of an image of the same shape) return the multichannel equivalent, where each
     channel is stored in the channel dimension, and can be normalised (all data between 0 and 1.)
    :param list_data: [data1, data2, ...]
    :param channels_axis:
    :param normalize:
    :return: data so that data[..., 0] = data0, data[... , 1] = data1, ...
    """
    def flatten(l):
        return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]

    list_data = [np.squeeze(l) for l in list_data]

    shapes_list = [l.shape for l in list_data]
    omega_list = [d[:channels_axis] for d in shapes_list]

    if not omega_list.count(omega_list[0]) == len(omega_list):
        raise IOError

    for k in range(len(list_data)):
        if len(list_data[k].shape) == channels_axis + 1:
            splitted = []
            for t in range(list_data[k].shape[channels_axis]):
                splitted += [list_data[k][..., t], ]
            list_data[k] = splitted

    list_data = flatten(list_data)

    for i, k in enumerate(list_data):
        print 'generate multichannel, chanenel {0}, has max value {1}'.format(i, np.nanmax(k))

    if normalize:
        list_data = [1.0 / np.nanmax(k) * k for k in list_data]

    return np.stack(list_data, axis=channels_axis)


def generate_multichannel_paths(list_pfi_image_input, pfi_multichannel_output, channels_axis=3, normalize=True):

    data_list = [nib.load(list_pfi_image_input[0]).get_data(), ]

    for pfi in list_pfi_image_input[1:]:
        nib_im = nib.load(pfi)
        data_list.append(nib_im.get_data())
    else:
        nib_im = None

    new_data = generate_multichannel(data_list, channels_axis=channels_axis, normalize=normalize)

    nib.save(set_new_data(nib_im, new_data), pfi_multichannel_output)
    print 'Multichannel data saved in the file {0} with shape {1}.'.format(pfi_multichannel_output, new_data.shape)


def stack_a_list_of_images_from_list_pfi(list_pfi, pfi_stack):
    for p in list_pfi:
        assert os.path.exists(p), p

    if len(list_pfi) == 1:
        cmd = 'cp {} {}'.format(list_pfi[0], pfi_stack)
        print_and_run(cmd)
    else:
        print('stack {0} in {1}'.format(list_pfi, pfi_stack))
        pfi_first = list_pfi[0]
        num_images_to_merge = len(list_pfi) - 1
        cmd = 'seg_maths {0} -merge {1} 4'.format(pfi_first, num_images_to_merge)
        for p in list_pfi[1:]:
            cmd += ' {0} '.format(p)
        cmd += ' {0} '.format(pfi_stack)
        print_and_run(cmd)