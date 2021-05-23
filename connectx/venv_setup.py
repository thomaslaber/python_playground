conda create -n connectx python=3.7
# conda remove -n connectx -all
conda activate connectx
# conda deactivate

## install ipykernel
pip3 install --user ipykernel
python3 -m ipykernel install --user --name connectx --display-name "Python (connectx)"

pip3 install <package> 