#!/bin/bash
for i in {1951..2100}
  do
    python 'merge_nc.py' $1 $i
  done