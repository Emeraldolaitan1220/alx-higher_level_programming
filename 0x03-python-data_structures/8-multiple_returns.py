#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sen_len = len(sentence)
    else:
        sen_len = 0
    return (sen_len, sentence[:1] if sentence else None)