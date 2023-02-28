import subprocess

files = [
    'fig_GOE_example-scale',
    'fig_GOE_example',
    'fig_GOE_kN',
    'fig_MP_solve',
    'legend',
]

for file in files:
    subprocess.run(f'jupyter nbconvert --execute --to notebook --inplace --allow-errors --ExecutePreprocessor.timeout=-1 {file}.ipynb',shell=True)

