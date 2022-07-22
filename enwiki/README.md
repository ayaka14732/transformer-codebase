# English Wikipedia

1. Download the English Wikipedia data
1. Extract the data by WikiExtractor
1. Split the articles into sentences by Bling Fire
1. Distort the sentences
1. Tokenize the original and the distorted sentences
1. Save to file

```sh
aria2c -x16 -s16 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
python -m wikiextractor.WikiExtractor enwiki-latest-pages-articles.xml.bz2 --json -o dump
python main.py
```

The files are written in:

- `src.dat`
- `packed_mask_dec_1d.dat`
- `dst.dat`
- `packed_mask_enc_1d.dat`

Usage:

See `example.py`

```
src.dtype: int32
src.shape: (7630, 512)
mask_enc_1d.dtype: bool
mask_enc_1d.shape: (7630, 512)
dst.dtype: int32
dst.shape: (7630, 512)
mask_enc_1d.dtype: bool
mask_enc_1d.shape: (7630, 512)
```
