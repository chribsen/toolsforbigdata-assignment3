from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_1,
                   reducer=self.reducer_1),
            MRStep(reducer=self.reducer_2),
            MRStep(reducer=self.reducer_3)
        ]

    def mapper_1(self, key, line):
        e = line.split()
        yield e[0], 1
        yield e[1], 1

    def reducer_1(self, key, values):
        yield key, sum(values)

    def reducer_2(self, key, values):
        yield 'Euler graph?', values.next() % 2 == 0

    def reducer_3(self, key, values):
        yield 'Euler graph?', not False in list(values)

if __name__ == '__main__':
    MRWordCount.run()