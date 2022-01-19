from subprocess import run

PID = None

lsns = run(['sudo', 'lsns', '-l', '-t', 'mnt', '-o', 'PID,COMMAND'], capture_output=True, universal_newlines=True)
# grep = run(['grep', 'mininet:h3'], capture_output=True, text=True, stdin=lsns.stdout)

output = lsns.stdout.splitlines()[1:]
for line in output:
    line = line.split()
    if line[-1] == 'mininet:h3':
        PID = line[0]

# in case mininet is not on
if not PID:
    print('Error, no namespace')
    exit(-1)


ip_link = run(['sudo', 'ip', 'link', 'add', 'veth0', 'type', 'veth', 'peer', 'name', 'veth0', 'netns', PID])
print('setting up interface:', ip_link.args)
print('Code:', ip_link.returncode)
run(['sudo', 'ip', 'link', 'set', 'veth0', 'up'])
run(['sudo', 'ip', 'addr', 'add', '10.0.1.2/24', 'dev', 'veth0'])

print('sending process to namespace')
run(['sudo', 'nsenter', '-t', PID, '-n', 'sudo', 'ip', 'link', 'set', 'veth0', 'up'])
run(['sudo', 'nsenter', '-t', PID, '-n', 'sudo', 'ip', 'addr', 'add', '10.0.1.1/24', 'dev', 'veth0'])
print('Testing')
run(['ping', '-c', '4', '10.0.1.1'], text=True)
