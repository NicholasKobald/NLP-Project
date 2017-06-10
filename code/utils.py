#The code based on baseline provided by the FNC organization,
#under the the Apache License
#https://github.com/FakeNewsChallenge/fnc-1-baseline
#and modified to run on Python2.7
#
# N. Kobald 2017-06-09

from csv import DictReader


class DataSet():

    def __init__(self, path="../data_sets"):
        self.path = path

        print("Reading dataset")
        bodies = "train_bodies.csv"
        stances = "train_stances.csv"

        self.stances = self.read(stances)
        articles = self.read(bodies)

        for s in self.stances:
            s['Body ID'] = int(s['Body ID'])

        self.articles = dict()
        for article in articles:
            self.articles[int(article['Body ID'])] = article['articleBody']

    def read(self, filename):
        rows = []
        with open(self.path + "/" + filename, "r") as table:
            r = DictReader(table)
            for line in r:
                rows.append(line)

        return rows

    def print_stances(self, print_limit=10):
        print "First", print_limit, "stances"
        for i in range(print_limit):
            print self.stances[i]

    def print_articles(self, print_limit=10):
        print "First", print_limit, "articles"
        for i in range(print_limit):
            print self.articles[self.stances[i]['Body ID']]

    def get_stance_counts(self):
        counts = dict(unrelated=0, discuss=0,
            agree=0, disagree=0
        )
        for s in self.stances:
            counts[s['Stance']] += 1

        return counts