# GPTZero

Based on [BurhanUlT's repo](https://github.com/BurhanUlTayyab/GPTZero)

https://github.com/user-attachments/assets/e883444b-46e9-4594-b251-b196ee8a8bc0

Still very much a work in progress.

- [x] Line-by-line analysis of text
- [x] Make UI more user-friendly
- [ ] Add PDF support
- [ ] Update the model to support longer context window.
- [ ] Add more explaination to what is happening. (eh)
- [ ] Add cool animations (eh)

## How to run

1. Clone the repo

2. Navigate to the directory
```bash
$ cd GPTZeroWeb
...
$ docker compose build
...
```
Building would take around 7 minutes, because spaCy does not have a pre-bult wheel.

3. Run the container
```bash
$ docker compose up
```

4. Navigate to `localhost:8000` in your browser.

## To alter this project.
Aside from having docker and everything ready, you would want to install all the requirements in your python environment, and install the `en_core_web_sm` model for spaCy.
```bash
$ pip install -r requirements.txt
...
$ python -m spacy download en_core_web_sm
...
```

---

Copied from the [original README](https://github.com/BurhanUlTayyab/GPTZero):

GPTZero is an AI model with some mathematical formulation to determine if a particular text fed to it is written by AI or a human being.

## Note
This implementation produces 100% same results as <a href="https://gptzero.me">gptzero.me</a>. We've compared extensively on a large corpus of text to compare our values with them, and surprisingly got the same results.

## Acknowledgement
1. This repository is built based on the hugging face
https://huggingface.co/docs/transformers/perplexity

2. Liu, Yinhan, et al. "Roberta: A robustly optimized bert pretraining approach." arXiv preprint arXiv:1907.11692 (2019).

3. [BurhanUlT's repo](https://github.com/BurhanUlTayyab/GPTZero)
