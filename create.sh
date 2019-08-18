#!/bin/bash

ensemble=''

for i in {1951..2100}
  do
    python 'create_'$ensemble'.py' $i
  done
