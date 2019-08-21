#!/bin/bash
for i in {1951..1952}:
do
python 'check_data.py' $1 $i
sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r8i2p1r1_$i --mem=1G --output=r8i2p1r1.log merge.sh r8i2p1r1 $i
done
