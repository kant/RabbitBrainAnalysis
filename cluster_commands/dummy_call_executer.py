import argparse
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(dir_path))

import main_pipeline.A0_main.main_executer as ma

parser = argparse.ArgumentParser()
parser.add_argument('-i', dest='str_input', type=str, required=True)
args = parser.parse_args()


f = open('../output_{}.txt'.format(args.str_input), 'w+')
f.writelines(args.str_input + '\n')
# f.writelines(root_study_rabbits + '\n')
f.writelines(ma.__file__ + '\n')
f.close()
