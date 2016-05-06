#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/5/1 下午7:42
# @Author  : ZHZ
import nltk
from nltk.collocations import *
from nltk.metrics import TrigramAssocMeasures, spearman_correlation, ranks_from_scores, BigramAssocMeasures
from nltk.corpus import stopwords, webtext

text = "hello world I love you hello world hello world I"

#
# scorer = BigramAssocMeasures.likelihood_ratio
# compare_scorer = BigramAssocMeasures.raw_freq
#
# while True:
#     words = "hello world I love you hello world hello world I"
#     cf = BigramCollocationFinder.from_words(words)
#     cf.apply_freq_filter(3)
#
#     corr = spearman_correlation(ranks_from_scores(cf.score_ngrams(scorer)),
#                                 ranks_from_scores(cf.score_ngrams(compare_scorer)))
#     print(file)
#     print('\t', [' '.join(tup) for tup in cf.nbest(scorer, 15)])
#     print('\t Correlation to %s: %0.4f' % (compare_scorer.__name__,
#                                            corr))  # text= "Everyone has their own dreams, I am the same. But my dream is not a lawyer, not a doctor, not actors, not even an industry. Perhaps my dream big people will find it ridiculous, but this has been my pursuit! My dream is to want to have a folk life! I want it to become a beautiful painting, it is not only sharp colors, but also the colors are bleak, I do not rule out the painting is part of the black, but I will treasure these bleak colors! Not yet, how about, a colorful painting, if not bleak, add color, how can it more prominent American? Life is like painting, painting the bright red color represents life beautiful happy moments. Painting a bleak color represents life difficult, unpleasant time. You may find a flat with a beautiful road is not very good yet, but I do not think it will. If a person lives flat then what is the point? Life is only a short few decades, I want it to go Finally, Each memory is a solid."
#     break
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = TrigramCollocationFinder.from_words(text.split())
print finder.nbest(trigram_measures.chi_sq, 2)
print finder.score_ngrams(TrigramAssocMeasures.mi_like)

#
# bigram_measures = nltk.collocations.BigramAssocMeasures()
# finder = BigramCollocationFinder.from_words(text.split())
# print finder.nbest(bigram_measures.student_t, 2)
# print finder.score_ngrams(BigramAssocMeasures.mi_like)
