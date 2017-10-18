#$ -l h_rt=12:00:00
#$ -l tmem=20G
#$ -l h_vmem=20G
#$ -N "Atlas_selected_T1_DWI_only"
#$ -S /bin/bash
#$ -cwd
#$ -t 1-8
#$ -e /cluster/project0/fetalsurgery/Data/MRI/KUL_preterm_rabbit_model/software/z_output
#$ -o /cluster/project0/fetalsurgery/Data/MRI/KUL_preterm_rabbit_model/software/z_output


date
hostname

SUBJECT=`sed -n ${SGE_TASK_ID}p subjects_atlas_only.txt`


export PATH=/share/apps/fsl-5.0.8/bin/:${PATH}
export PATH=/home/ferraris/software_lib/NiftyFit2/niftyfit-build/fit-apps/:${PATH}
export LD_LIBRARY_PATH=/share/apps/cmic/NiftyMIDAS/bin/:${LD_LIBRARY_PATH}

EXEC=/home/ferraris/py_venvs/v2/bin/python
CALLER=cluster_commands/call_executer.py

echo $EXEC $CALLER -i $SUBJECT

$EXEC $CALLER -i $SUBJECT
