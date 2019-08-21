#!/bin/bash 
for i in {2004..2100}
    do
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r8i2p1r1_$i --mem=1G --output=r8i2p1r1.log --open-mode=append merge.sh r8i2p1r1 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r8i2p1r2_$i --mem=1G --output=r8i2p1r2.log --open-mode=append merge.sh r8i2p1r2 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r8i2p1r3_$i --mem=1G --output=r8i2p1r3.log --open-mode=append merge.sh r8i2p1r3 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r8i2p1r4_$i --mem=1G --output=r8i2p1r4.log --open-mode=append merge.sh r8i2p1r4 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r8i2p1r5_$i --mem=1G --output=r8i2p1r5.log --open-mode=append merge.sh r8i2p1r5 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r9i2p1r1_$i --mem=1G --output=r9i2p1r1.log --open-mode=append merge.sh r9i2p1r1 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r9i2p1r2_$i --mem=1G --output=r9i2p1r2.log --open-mode=append merge.sh r9i2p1r2 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r9i2p1r3_$i --mem=1G --output=r9i2p1r3.log --open-mode=append merge.sh r9i2p1r3 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r9i2p1r4_$i --mem=1G --output=r9i2p1r4.log --open-mode=append merge.sh r9i2p1r4 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r9i2p1r5_$i --mem=1G --output=r9i2p1r5.log --open-mode=append merge.sh r9i2p1r5 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r10i2p1r1_$i --mem=1G --output=r10i2p1r1.log --open-mode=append merge.sh r10i2p1r1 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r10i2p1r2_$i --mem=1G --output=r10i2p1r2.log --open-mode=append merge.sh r10i2p1r2 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r10i2p1r3_$i --mem=1G --output=r10i2p1r3.log --open-mode=append merge.sh r10i2p1r3 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r10i2p1r4_$i --mem=1G --output=r10i2p1r4.log --open-mode=append merge.sh r10i2p1r4 $i
        sbatch --account=rpp-hwheater --time=00:14:00 --job-name=merge_r10i2p1r5_$i --mem=1G --output=r10i2p1r5.log --open-mode=append merge.sh r10i2p1r5 $i
        sleep 840
    done
