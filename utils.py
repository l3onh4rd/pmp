# utils for pmp script
import shutil, os

# copies content of export folder to backup folder
def backup_latest_export():
    shutil.copytree('export', 'backup', dirs_exist_ok=True)

# removes content of the backup folder if it exists
def remove_latest_backup():
    if os.path.isdir('backup'):
        shutil.rmtree('backup')
