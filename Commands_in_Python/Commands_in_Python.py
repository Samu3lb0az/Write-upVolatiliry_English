vol -f /Scenarios/Investigations/Investigation-1.vmem windows.info

vol -f /Scenarios/Investigations/Investigation-1.vmem windows.pslist

vol -f /Scenarios/Investigations/Investigation-1.vmem windows.memmap --pid 1640 --dump

strings *.dmp | grep -i "user-agent"

vol -f /Scenarios/Investigations/Investigation-2.raw windows.pslist

vol -f /Scenarios/Investigations/Investigation-2.raw windows.dlllist | grep 740