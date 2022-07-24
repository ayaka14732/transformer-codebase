import blingfire
import json
from typing import List
import sys

def article_to_sentences(text: str) -> List[str]:
    '''
    ```python
    >>> article_to_sentences('A cat. The mouse.')
    ['A cat.', 'The mouse.']
    >>> article_to_sentences('A long line\nwith wrapping. The mouse.')
    ['A long line with wrapping.', 'The mouse.']
    >>> article_to_sentences('\n    ')
    []
    ```
    '''
    if not text.strip():
        return []
    return blingfire.text_to_sentences(text).split('\n')

def process(filename_in: str, filename_out: str) -> List[str]:
    all_sentence = []
    with open(filename_in, encoding='utf-8') as f:
        for line in f:
            obj = json.loads(line)
            text = obj['text']
            sentences = article_to_sentences(text)
            all_sentence.extend(sentences)
    with open(filename_out, 'w', encoding='utf-8') as f:
        for sentence in all_sentence:
            assert '\n' not in sentence
            print(sentence, file=f)

if __name__ == '__main__':
    filename_in = sys.argv[1]
    filename_out = sys.argv[2]
    process(filename_in, filename_out)
