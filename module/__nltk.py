import nltk
from nltk import corpus

# from numpy import *
# from nltk import book

# similar 查找相似单词
# w1-w-w2, 找打所有满足w1-w'-w2的w'
words = ['今天', '天气', '很', '热', ',', '今天', '气温', '很', '高']
text = nltk.Text(words)
_ = text.similar('天气')
# 气温

# common_contexts 研究共用两个以上词汇的上下文
_ = text.common_contexts(['天气', '气温'])
# 今天_很

# concordance 搜索词语出现的位置，显示附近文本
_ = text.concordance('天气')
# 今天 天气 很 热 , 今天 气温 很 高

# 固定数量的邻近单次组合
nltk.ngrams(words, 3)
# [('今天', '天气', '很'), ..., ('气温', '很', '高')]

# print(nltk.corpus.sinica_treebank.tagged_words())

# from nltk.corpus import brown
# brown_tagged_sents = brown.tagged_sents(categories='news')

# cfd = nltk.ConditionalFreqDist(((x[1], y[1], z[0]), z[1]) for sent in
# brown_tagged_sents for x, y,
# z in nltk.trigrams(sent))

# for c in cfd.conditions():
#     if len(cfd[c]) > 1:
#         print(c)
# brown_sents = brown.sents(categories='news')
#
# cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
#
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents[:1000])
# unigram_tagger.evaluate(brown_tagged_sents[-100:])

from nltk.corpus import movie_reviews


############################################################
###  RegexpParser 分块/加缝
############################################################
def _():
    sentence = [('小', 'JJ'), ('黄', 'JJ'), ('狗', 'NN'), ('躲', 'VB'), ('在', 'IN'),
                ('小', 'JJ'), ('猫', 'NN'), ('的', 'NO'), ('后面', 'VBD')]
    root_tree = nltk.tree.Tree('root', sentence)
    root_tree.draw()

    grammar = 'NP: {<JJ>*<NN>}'
    cp = nltk.RegexpParser(grammar)
    # 解析树构造新分块树
    new_tree = cp.parse(root_tree)
    # (S (NP 小/JJ 黄/JJ 狗/NN) 躲/VB 在/IN (NP 小/JJ 猫/NN) 的/NO 后面/VBD)
    new_tree.draw()

    # 提取块
    _ = [subtree for subtree in new_tree.subtrees() if
             subtree.label() == 'NP']
    # [Tree('NP', [('小', 'JJ'), ('黄', 'JJ'), ('狗', 'NN')]),
    #  Tree('NP', [('小', 'JJ'), ('猫', 'NN')])]

    # 评估分块器
    str(cp.evaluate((new_tree,)))
    # 'ChunkParse score:\n    IOB Accuracy: 100.0%%\n    Precision:    100.0%%\n
    # Recall:       100.0%%\n    F-Measure:    100.0%%'

    grammar = """
        NP:
         {<.*>+}
         }<VB.*|IN|NO>+{
    """
    new_tree = nltk.RegexpParser(grammar).parse(root_tree)
    # (S (NP 小/JJ 黄/JJ 狗/NN) 躲/VB 在/IN (NP 小/JJ 猫/NN) 的/NO 后面/VBD)
    new_tree.draw()

    text = 'he PRP B-NP\n' \
           'accepted VBD B-VP\n' \
           'the DT B-NP\n' \
           'position NN I-NP\n' \
           'of IN B-PP\n' \
           'vice NN B-PP\n' \
           'chairman NN I-NP\n' \
           'of IN B-PP\n' \
           'Carlyle NNP B-NP\n' \
           'Group NNP I-NP'
    nltk.chunk.conllstr2tree(text, chunk_types=('NP',)).draw()
    # LazyMap包含树的列表
    train_sents = nltk.corpus.conll2000.chunked_sents('train.txt',
                                                     chunk_types='NP')
    # 列表单个元素为一句中各词的词性及分块元组组成的列表
    train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)]
                  for sent in train_sents]

    # 一维标签器
    tagger = nltk.UnigramTagger(train_data)

