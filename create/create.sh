#!/bin/bash
for i in {1951..2100}
  do
    python 'create_'$1'.py' $i
  done
