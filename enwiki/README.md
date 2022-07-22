# English Wikipedia

Extract Wikipedia dump by WikiExtractor, then use Bling Fire to split articles into sentences.

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
