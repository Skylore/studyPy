def one():
    global glob
    glob = 'afsdfa'

    loc = 'local'

    print(locals()['loc'])



one()

# varname = 'glob'
# print(globals()[varname])
#

print(locals()['loc'])