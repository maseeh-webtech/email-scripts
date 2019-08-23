from subprocess import Popen, PIPE, STDOUT, call

list_name = "maseeh6-freshmen"
#list_name = 'maseeh-2019-private'

cmd = 'blanche ' + list_name + ' -m'

# from https://www.saltycrane.com/blog/2008/09/how-get-stdout-and-stderr-using-python-subprocess-module

p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)

stdout, stderr = p.communicate()

members = stdout.split()

# is there a 'remove all members' flag for blanche?
for m in members:
    print('removing ' + m)
    call(['blanche', list_name, '-d', m])

