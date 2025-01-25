# utils for pmp script
import shutil, os, csv, copy
from pathlib import Path

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
Checks for the existence of a backup and export folder. If they not exist, they are created.
"""
def check_for_dirs():

    backup_path = Path('backup')
    export_path = Path('export')
    export_ideal_plots_multiple = Path('export/ideal_plots_multiple')
    export_ideal_plots_single = Path('export/ideal_plots_single')
    export_test_plots_single = Path('export/test_plots_single')
    export_train_plots_single = Path('export/train_plots_single')

    if not os.path.isdir('backup'):
        backup_path.mkdir()
        print("\nLOG INFO: Created backup directory since it was not found")

    if not os.path.isdir('export'):
        export_path.mkdir('export')
        export_ideal_plots_multiple.mkdir('export/ideal_plots_multiple')
        export_ideal_plots_single.mkdir('export/ideal_plots_single')
        export_test_plots_single.mkdir('export/test_plots_single')
        export_train_plots_single.mkdir('export/train_plots_single')
        print("\nLOG INFO: Created export directories since they were not found")

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