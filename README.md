# transformer-codebase

Some useful code I wrote during my experiments in implementing the Transformer architecture, model pre-training, distributed training and performance models.

This repository is inspired by [scaling experiments](https://github.com/sholtodouglas/scalingExperiments).

- [English Wikipedia](enwiki/)
- [BART](bart/)

Setup:

```sh
python -m venv venv
. venv/bin/activate
pip install -U pip
pip install -U wheel
pip install "jax[tpu]==0.3.14" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
pip install -r requirements.txt
```
