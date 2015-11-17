from mrjob.job import MRJob
from nltk.tokenize import RegexpTokenizer

r = RegexpTokenizer(u'\w+|[^\w\s\ufeff]+')

class MRWordCount(MRJob):
    def mapper(self, key, line):
        for word in r.tokenize(line):
            yield word.lower(), 1

    def combiner(self, word, c):
        yield word, sum(c)

    def reducer(self, key, vals):
        yield key, sum(vals)

if __name__ == '__main__':
    MRWordCount.run()