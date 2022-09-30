# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

import os, sys


def new_dir(out_dir):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

def progress(i, N, text = None):
    '''
    Update progress in the same line
    :param i: current progress
    :param N: total count
    :param text: description text
    :return:
    '''
    sys.stdout.write('/r')
    if text is None:
        sys.stdout.write('Frame {0}/{1} added to video'.format(i, N))
    else:
        sys.stdout.write(text + '{0}/{1}'.format(i, N))
    sys.stdout.flush()