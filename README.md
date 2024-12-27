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

---

GPTZero is an AI model with some mathematical formulation to determine if a particular text fed to it is written by AI or a human being.

## The motivation for it

Recently, GPTZero gotten a lot of hype/traction from media to be able to determine whether a set of sentences are generated from ChatGPT. It was indeed a great initative for Education Institutes. However, the implementation is closed-source. We tried to construct identical solutioning and voila!! :tada: our implementation gets the exact same results mostly lol. :joy: :joy: :joy:

## Note
Our implementation produces 100% same results as <a href="https://gptzero.me">gptzero.me</a>. We've compared extensively on a large corpus of text to compare our values with them, and surprisingly got the same results.

## Acknowledgement
1. This repository is built based on the hugging face
https://huggingface.co/docs/transformers/perplexity

2. Liu, Yinhan, et al. "Roberta: A robustly optimized bert pretraining approach." arXiv preprint arXiv:1907.11692 (2019).
