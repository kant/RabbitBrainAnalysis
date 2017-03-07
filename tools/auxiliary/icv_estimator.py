import numpy as np
import os
from os.path import join as jph
from scipy.linalg import expm, logm

from tools.label_manager.caliber import volume_from_binary_segmentation_path
from scipy.optimize import minimize

from tools.auxiliary.utils import print_and_run


class ICV_estimator(object):

    def __init__(self, pfi_list_subjects_to_register, pfo_output, S=None, m=None,
                      n=0.001, a=0.001, b=0.1, alpha=0.001, beta=0.1):
        # input subjects
        self.pfi_list_subjects_to_register = pfi_list_subjects_to_register
        self.pfo_output = pfo_output
        self.num_subjects = len(pfi_list_subjects_to_register)
        self.subjects_id = None
        # optimisation function parameters
        self.S = S
        self.m = m
        self.n = n
        self.a = a
        self.b = b
        self.alpha = alpha
        self.beta = beta

        self.__initialise_list_id__()

    def __initialise_list_id__(self):
        self.subjects_id = [os.path.dirname(s).split('.')[0]
                            for s in self.pfi_list_subjects_to_register
                            if (s.endswith('.nii') or s.endswith('.nii.gz'))]

    def generate_transformations(self):

        cmd_1 = 'mkdir -p {0} '.format(self.pfo_output_folder, 'warped')
        cmd_2 = 'mkdir -p {0} '.format(jph(self.pfo_output_folder, 'transformations'))
        print_and_run(cmd_1)
        print_and_run(cmd_2)

        # coregister subjects and save the matrix transformations in the jph(pfo_output_folder, 'transformations')
        for i in xrange(0, self.num_subjects):
            for j in xrange(i + 1, self.num_subjects):  # assuming registration symmetric.
                fname_i_j = self.subjects_id[i] + '_' + self.subjects_id[j]
                fname_j_i = self.subjects_id[j] + '_' + self.subjects_id[i]
                pfi_aff_i_j = jph(self.pfo_output, 'transformations', fname_i_j + '.txt')
                pfi_res_i_j = jph(self.pfo_output, 'warped', fname_i_j + '.nii.gz')
                pfi_aff_j_i = jph(self.pfo_output, 'transformations', fname_j_i + '.txt')
                pfi_res_j_i = jph(self.pfo_output, 'warped', fname_j_i + '.nii.gz')

                cmd_reg_i_j = 'reg_aladin -ref {0} -flo {1} -aff {2} -res {3} -speeeeed '.format(
                            self.pfi_list_subjects_to_register[i], self.pfi_list_subjects_to_register[j],
                            pfi_aff_i_j, pfi_res_i_j)
                cmd_reg_j_i = 'reg_aladin -ref {0} -flo {1} -aff {2} -res {3} -speeeeed '.format(
                            self.pfi_list_subjects_to_register[j], self.pfi_list_subjects_to_register[i],
                            pfi_aff_j_i, pfi_res_j_i)

                print_and_run(cmd_reg_i_j)
                print_and_run(cmd_reg_j_i)

    def compute_S(self):

        for i in xrange(self.num_subjects):
            for j in xrange(i+1, self.num_subjects):

                fname_i_j = self.subjects_id[i] + '_' + self.subjects_id[j]
                fname_j_i = self.subjects_id[j] + '_' + self.subjects_id[i]

                pfi_aff_i_j = jph(pfo_transformations, 'transformations',
                                  self.subjects_id[i] + '_' + self.subjects_id[j] + '.txt')
                pfi_aff_j_i = jph(pfo_transformations, 'transformations',
                                  self.subjects_id[j] + '_' + self.subjects_id[i] + '.txt')

                S[i,j] = np.linalg.det( np.loatxt(pfi_aff_i_j) )
                S[j,i] = np.linalg.det( np.loatxt(pfi_aff_j_i) )

        self.S = S

    def compute_m_from_list_masks(self, pfi_list_brain_masks, increase_volume_estimate=0.05):
        # compute m from a list of propagated segmentation of the brain.
        # the icv is the volume of the propagated segmentations * (1 + increase_volume_estimate)
        pass

    def icv_estimator(self):
        """
        :param S: antysimmetric squared matrix S_ij, log(det(mean of transf))
                can be computed as
                    S_ij = det( log ( expm (0.5 (logm(A_ij) + logm(A_ji))) ) )
        :param m: prior mean ICV, as the mean of the volume of the propagated brain segmentation
        as an initial value for the ICV.
        """

        assert S.shape[0] == S.shape[1]

        log_estimate_v = m * np.ones(S.shape[0], dtype=np.float64)

        def cost(v, S=S, m=m, n=n, a=a, b=b, alpha=alpha, beta=beta):

            sum_abs_log_diff = 0
            for i in xrange(len(v)):
                for j in xrange(i+1, len(v)):
                    sum_abs_log_diff += np.abs(S[i,j] - v[i] + v[j])
            mean_v = np.mean(v)
            N = S.shape[0]

            a1 = alpha + np.linalg.det(S)
            a2 = np.log( beta + sum_abs_log_diff )
            a3 = (2 * a + N) / float(2)
            a4 = np.log( b + 0.5 * np.sum( [(v_i + mean_v) ** 2 for v_i in list(v)] ) +  (N * n * (mean_v - m) ** 2) / (2 * (N + n)) )
            return a1 * a2 + a3 * a4

        log_answer = minimize(cost(v, S=S, m=m, n=n, a=a, b=b, alpha=alpha, beta=beta), log_estimate_v, method='trust-ncg', tol=1e-6)

        return np.exp(log_answer)
