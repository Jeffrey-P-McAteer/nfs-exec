
# NFS Exec

A python/c utility to execute foreign functions using nothing more than a shared network folder.

## Usage

TODO write it first

## Building

### nfs_exec_py

It's a python module;

```bash
PYTHONPATH=$PYTHONPATH;$(realpath ./nfs_exec_py/)
python <<<EOF
import nfs_exec_py
# Whatever
EOF
```

### nfs-exec-c

```bash

cd nfs-exec-c
./build.sh
# Link nfs-exec-c.so / nfs-exec-c.a using symbols in nfs-exec-c.h
# to whichever frontend code you're calling it from.

```

