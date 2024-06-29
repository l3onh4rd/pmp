'''
Utils file for basic scripts for the program
'''

import shutil, os

def backup_latest_export():
    shutil.copytree('export', 'backup', dirs_exist_ok=True)

def remove_latest_backup():
    if os.path.isdir('backup'):
        shutil.rmtree('backup')