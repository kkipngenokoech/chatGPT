# Supervised Machine learning

f(x) => y

## types of language learning models

1. Base Language Model - predicts next word based on text training data
2. Instruction tuned Language learning models - tries to follow instructions

## Getting a BASE LM to ILLM

train a Base LM on a lot of data.

further train the model by fine-tuning it with examples where output follow input instructions.

obtain human ratings of different LLM ratings

tune the LLM to provide higher quality ratings using reinforcement learning from human feedback (RLHF)

## TOKENS

tokens rep one word that are commonly occuring sequences in the english word.

so for a word like prompting -`prom` is the first token, `pti` another and finally `ing`

for an english language input, 1 token is around 4 characters

## Token limit

different models have different limits on the number tokens in the input `context` + output completion.