# transformer-codebase

Some useful code I wrote during my experiments in implementing the Transformer architecture, model pre-training, distributed training and performance models.

This repository is inspired by [scaling experiments](https://github.com/sholtodouglas/scalingExperiments).

## Contents

**[English Wikipedia](enwiki/)**

Extract Wikipedia dump by WikiExtractor, then use Bling Fire to split articles into sentences.

```sh
aria2c -x16 -s16 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
python -m wikiextractor.WikiExtractor enwiki-latest-pages-articles.xml.bz2 --json -o dump
```

**[BART](bart/)**

A BART implementation in JAX. Its correctness is attested in the following ways:

1. The model output is the same as the implementation in Flax
1. The model can generate proper sentences
