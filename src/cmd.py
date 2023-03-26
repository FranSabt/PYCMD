import subprocess


def cmd(commando):
    x = subprocess.run(commando, shell=True, capture_output=True, text=True)
    return x.stdout

z = cmd('ping 8.8.8.8 ')

# print("----")

print('print:', z)