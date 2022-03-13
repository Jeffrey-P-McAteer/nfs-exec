#!/bin/bash

req_programs=(
  gcc
)

for p in "${req_programs[@]}" ; do
  if ! command -v $p &> /dev/null ; then
    echo "the tool '$p' is required for building nfs-exec-c but was not found, please install and try again."
    exit 1
  fi
done


# todo

