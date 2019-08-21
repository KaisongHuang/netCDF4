#!/bin/bash
for i in {1951..1952}
  do
    python 'create_'$1'.py' $i
  done
