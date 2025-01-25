# utils for pmp script
import shutil, os, csv, copy

"""
Saves latest content from the export directory to the backup directory.
Just copies the whole content fromt one directory to the other.
"""
def backup_latest_export():
    if os.path.isdir('backup') and os.path.isdir('export'):
        shutil.copytree('export', 'backup', dirs_exist_ok=True)

"""
Clears the backup directory.
"""
def remove_latest_backup():
    if os.path.isdir('backup'):
        shutil.rmtree('backup')

"""
Takes the result variable, add a header row
"""
def create_result_csv(result):
    # make a deep copy the the list to avoid call by reference issues
    export_result = copy.deepcopy(result)
    # add a header row for the csv file export
    export_result.insert(0, ("train function", "best fitting function"))
    # save the list as csv file to the export directory
    with open('export/result.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(export_result)