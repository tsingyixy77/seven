#!/bin/python
import os
import time
xml = open('gnome-shell-theme.gresource.xml','w')
xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
xml.write('<gresources>\n')
xml.write('\t<gresource prefix="/org/gnome/shell/theme">\n')
for _r, _p, names in os.walk('./'):
    for _n in names:
        if _n.endswith('.svg') or _n.endswith('.css') or _n.endswith('.jpg') or _n.endswith('.png'):
            #print('collecting assets {}'.format((_r+'/'+_n)))
            if _r == './':
                xml.write('\t\t<file>{}</file>\n'.format((_r+'/'+_n)[3:]))
            elif _r == './assets':
                xml.write('\t\t<file>{}</file>\n'.format((_r+'/'+_n)[2:]))

xml.write('\t</gresource>\n')
xml.write('</gresources>\n')
xml.close()
os.system('glib-compile-resources gnome-shell-theme.gresource.xml')
os.system('sudo cp /usr/share/gnome-shell/gnome-shell-theme.gresource /usr/share/gnome-shell/gnome-shell-theme.gresource.bak')
os.system('sudo cp ./gnome-shell-theme.gresource /usr/share/gnome-shell -rf')
os.system('rm -rf ./gnome-shell-theme.gresource ./gnome-shell-theme.gresource.xml')
print('done...')
