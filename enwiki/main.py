from glob import glob
from os import cpu_count
import subprocess
from tqdm import tqdm
from typing import Any, List

assert subprocess.check_output(['python', '-V'], shell=False).startswith(b'Python 3')

def make_chunks(lst: List[Any], n: int) -> List[List[Any]]:
    '''Yield successive n-sized chunks from lst.'''
    return [lst[i:i+n] for i in range(0, len(lst), n)]

n_cpu = cpu_count()
filepaths = glob('dump/*/*')

def process_chunk(chunk_filepaths: List[str]):
    processes = []

    for filepath in chunk_filepaths:
        _, dir_name, filename = filepath.split('/')
        f_in = filepath
        dir_out = f'dump2/{dir_name}'
        f_out = f'{dir_out}/{filename}'

        subprocess.call(['mkdir', '-p', dir_out], shell=False)

        p = subprocess.Popen(['python', 'process_one_file.py', f_in, f_out], shell=False)
        processes.append(p)

    for p in processes:
        p.wait()

if __name__ == '__main__':
    for chunk_filepaths in tqdm(make_chunks(filepaths, n_cpu)):
        process_chunk(chunk_filepaths)
