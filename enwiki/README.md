# English Wikipedia

1. Download the English Wikipedia data
1. Extract the data by WikiExtractor
1. Split the articles into sentences by Bling Fire

```sh
aria2c -x16 -s16 https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
python -m wikiextractor.WikiExtractor enwiki-latest-pages-articles.xml.bz2 --json -o dump
python main.py
```

The processed sentences are stored in `dump2/` directory.
