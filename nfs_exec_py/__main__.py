
# Parses CLI arguments to allow remote machines to:
#  - run some arbitrary executables on this machine,
#  - append data to an arbitrary file on this machine,
#  - read data from an arbitrary file on this machine,
#  - Monitor a network directory & dump execution metadata

from nfs_exec_py import NFSExec

e = NFSExec()
# e.spawn_state_thread()

while True:
  e.perform_state_check()


