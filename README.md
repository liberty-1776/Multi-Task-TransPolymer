## Multi-Task TransPolymer ##

#### Adapted from TransPolymer </br>

#### npj Computational Materials [[Paper]](https://www.nature.com/articles/s41524-023-01016-5) [[arXiv]](https://arxiv.org/abs/2209.01307) [[PDF]](https://www.nature.com/articles/s41524-023-01016-5.pdf) </br>

[GitHub-Link for TransPolymer](https://github.com/ChangwenXu98/TransPolymer)


### Installation

Set up conda environment and clone the github repo

```
# create a new environment
$ conda create --name TransPolymer python=3.9
$ conda activate TransPolymer

# install requirements
$ conda install pytorch==1.12.0 torchvision torchaudio cudatoolkit=11.3 -c pytorch
$ pip install transformers==4.20.1
$ pip install PyYAML==6.0
$ pip install fairscale==0.4.6
$ conda install -c conda-forge rdkit=2022.3.4
$ conda install -c conda-forge scikit-learn==0.24.2
$ conda install -c conda-forge tensorboard==2.9.1
$ conda install -c conda-forge torchmetrics==0.9.2
$ conda install -c conda-forge packaging==21.0
$ conda install -c conda-forge seaborn==0.11.2
$ conda install -c conda-forge opentsne==0.6.2

# clone the source code of TransPolymer
$ git clone https://github.com/ChangwenXu98/TransPolymer.git
$ cd TransPolymer
```



