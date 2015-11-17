from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_1,
            )#reducer=self.reducer_1)
        ]

    def mapper_1(self, key, line):
        e = line.split()
        yield e[0], e[1]

    def reducer_1(self, key, values):
        yield key, values

if __name__ == '__main__':
    MRWordCount.run()