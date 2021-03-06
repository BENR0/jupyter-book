"""Execute all of the notebooks in a folder. This is helpful if you wish
to ensure that all of your notebooks run, and that the output
contained in the notebook files is up-to-date."""
from glob import glob
from subprocess import run
from tqdm import tqdm
import argparse
import os.path as op
import sys

DESCRIPTION = ("Execute all of the notebooks in a specified folder.")
parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("path_content",
                    help="The path to a folder with Jupyter Notebooks inside"
                         " that you'd like to run.")
parser.add_argument("--kernel-name", default="python3",
                    help="The name of the kernel used to run the notebook"
                         " code.")


def run_book():
    args = parser.parse_args(sys.argv[2:])
    path = args.path_content
    kernel_name = args.kernel_name

    print("Running all notebooks underneath {}".format(path))
    ipynb_files = glob(op.join(path, '**', '*.ipynb'), recursive=True)

    failed_files = []
    for ifile in tqdm(ipynb_files):
        call = 'jupyter nbconvert --inplace --ExecutePreprocessor.kernel_name={} --to notebook --execute {}'.format(
            kernel_name, ifile)
        try:
            run(call.split(), check=True)
        except Exception:
            failed_files.append(ifile)

    print('Failing files:')
    for ifile in failed_files:
        print(ifile)
