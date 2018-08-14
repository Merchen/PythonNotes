import nltk
from nltk import corpus
from nltk.corpus import movie_reviews, conll2000

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


############################################################
###  FreqDist/ConditionalFreqDist
############################################################
def _():

    """FreqDist"""
    words = nltk.corpus.brown.words('cp15')
    # ['``', 'They', 'make', 'us', 'conformists', 'look', ...]
    fd = nltk.FreqDist(words)
    # FreqDist({',': 171, '.': 129, 'the': 80, ...})
    fd.max()
    # ','
    fd.most_common(2)
    # [(',', 171), ('.', 129)]
    fd.N()
    # 2524 = len(words)
    _ = fd['the']
    # 80

    tagged_words = nltk.corpus.brown.tagged_words()
    # [('The', 'AT'), ('Fulton', 'NP-TL'), ...]
    cfd = nltk.ConditionalFreqDist(tagged_words)
    _ = cfd['the']
    # FreqDist({'AT': 62288, 'AT-TL': 223, 'AT-HL': 172, 'AT-NC': 26, 'NIL': 3, 'AT-TL-HL': 1})
    _.most_common(2)
    # [('AT', 62288), ('AT-TL', 223)]
    _.max()
    # 'AT'
    cfd.conditions()
    # ['``', 'They', 'make', ...] = cfd.keys()



############################################################
###  RegexpParser 分块/加缝
############################################################
def _():
    sentence = [('小', 'JJ'), ('黄', 'JJ'), ('狗', 'NN'), ('躲', 'VB'), ('在', 'IN'),
                ('小', 'JJ'), ('猫', 'NN'), ('的', 'NO'), ('后面', 'VBD')]
    root_tree = nltk.tree.Tree('root', sentence)
    cp = nltk.RegexpParser('NP: {<JJ>*<NN>}')
    # 解析树构造新分块树
    new_tree = cp.parse(root_tree)
    # (S (NP 小/JJ 黄/JJ 狗/NN) 躲/VB 在/IN (NP 小/JJ 猫/NN) 的/NO 后面/VBD)
    new_tree.draw()

    # 提取块
    _ = [subtree for subtree in new_tree.subtrees() if subtree.label() == 'NP']
    # [Tree('NP', [('小', 'JJ'), ('黄', 'JJ'), ('狗', 'NN')]),
    #  Tree('NP', [('小', 'JJ'), ('猫', 'NN')])]

    # 评估分块器
    str(cp.evaluate((new_tree,)))
    # 'ChunkParse score:\n    IOB Accuracy: 100.0%%\n    Precision: 100.0%%\n
    # Recall: 100.0%%\n    F-Measure: 100.0%%'
    str(cp.evaluate(conll2000.chunked_sents('test.txt', chunk_types=['NP'])))
    # 'ChunkParse score:\n    IOB Accuracy: 49.5%%\n    Precision: 15.2%%\n
    # Recall: 8.1%%\n    F-Measure: 10.6%%'

    grammar = """
        NP:
         {<.*>+}
         }<VB.*|IN|NO>+{
    """
    new_tree = nltk.RegexpParser(grammar).parse(root_tree)
    # (S (NP 小/JJ 黄/JJ 狗/NN) 躲/VB 在/IN (NP 小/JJ 猫/NN) 的/NO 后面/VBD)
    new_tree.draw()

    nltk.tree2conlltags(new_tree)
    # [('小', 'JJ', 'B-NP'),
    #  ('黄', 'JJ', 'I-NP'),
    #  ('狗', 'NN', 'I-NP'),
    #  ('躲', 'VB', 'O'),
    #  ('在', 'IN', 'O'),
    #  ('小', 'JJ', 'B-NP'),
    #  ('猫', 'NN', 'I-NP'),
    #  ('的', 'NO', 'O'),
    #  ('后面', 'VBD', 'O')]

    class UnigramChunker(nltk.ChunkParserI):
        def __init__(self, train_sents):
            # [[('NN', 'B-NP'), ('IN', 'O'),...],...]
            train_data = [[(t, c) for w, t, c in nltk.chunk.tree2conlltags(sent)]
                          for sent in train_sents]
            self.tagger = nltk.UnigramTagger(train_data)

        def parse(self, sentence):
            tagged_pos_tags = self.tagger.tag([pos for word, pos in sentence])
            conlltags = [(s[0], s[1], t[1]) for s,t in zip(sentence, tagged_pos_tags)]
            return nltk.chunk.conlltags2tree(conlltags)

    # nltk.collections.LazyMap, 包含树的列表
    train_sents = conll2000.chunked_sents('train.txt',chunk_types=['NP'])
    test_sents = conll2000.chunked_sents('test.txt',chunk_types=['NP'])

    unigram_chunker = UnigramChunker(train_sents)
    unigram_chunker.tagger.tag(['JJ', 'IN'])
    # [('JJ', 'I-NP'), ('IN', 'O')]
    str(unigram_chunker.evaluate(test_sents))
    # 'ChunkParse score:\n    IOB Accuracy: 92.9%%\n    Precision: 79.9%%\n
    # Recall: 86.8%%\n    F-Measure: 83.2%%'


############################################################
###  线性分块
############################################################
def npchunk_feature(sentence, i, history):
    word, pos = sentence[i]
    return {'pos':pos}

class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            # [('Confidence', 'NN'), ('in', 'IN'), ...]
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_feature(untagged_sent, i, history)
                # ({'pos': 'JJ'}, 'I-NP')
                train_set.append((featureset, tag))
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train(train_set, trace=0)

    def tag(self, sentence):
        history = []
        for i in range(len(sentence)):
            featureset = npchunk_feature(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)


train_sents = conll2000.chunked_sents('train.txt',chunk_types=['NP'])
# [Tree('S', [...]), Tree(...)], 一句一树
tagged_sents = [[((w, t), c) for w, t, c in nltk.chunk.tree2conlltags(sent)] for sent
              in train_sents]
# [[(('Confidence', 'NN'), 'B-NP'),...], ...], 一句一列表
list(ConsecutiveNPChunkTagger(tagged_sents[:2]).tag([('my', 'JJ')]))
# [(('my', 'JJ'), 'I-NP')]