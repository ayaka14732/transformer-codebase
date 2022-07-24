# transformer-codebase

Some useful code I wrote during my experiments in implementing the Transformer architecture, model pre-training, distributed training and performance modelling

This repository is inspired by [scaling experiments](https://github.com/sholtodouglas/scalingExperiments).

## Setup

```sh
python -m venv venv
. venv/bin/activate
pip install -U pip
pip install -U wheel
pip install "jax[tpu]==0.3.14" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
pip install -r requirements.txt
```

## Contents

- [x] [English Wikipedia](enwiki/): Split English Wikipedia into sentences.
- [ ] [BART model](bart_model/): An implementation of the BART model in JAX.
- [ ] [Model parallelism](model_parallelism/): An implementation of model parallelism of the self-attention layer
