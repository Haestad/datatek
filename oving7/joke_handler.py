""" This module contains classes handling the jokes """

import json

import IPython
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score

from oving7.joke import Joke


class JokeHandler:
    """ This class loads the given jokes into a list,
      and is able to search for the top 3 jokes. """

    jokes = []
    ord_id = 0

    def add_jokes(self, file):
        """ Adds the jokes from the file to the internal list. """
        with open(file, "r") as data_file:
            data = json.load(data_file)
        for joke in data:
            self.jokes.append(self.decode_data(joke, self.ord_id, file))
            self.ord_id += 1

    @staticmethod
    def decode_data(dct, ordered_id, file):
        """ Decodes the given data and returns a joke object. """
        original_id = dct["id"]

        if "category" in dct:
            category = dct["category"]
        else:
            category = None

        if "title" in dct:
            content = dct["title"] + "\n" + dct["body"]
        else:
            content = dct["body"]

        if "score" in dct:
            score = dct["score"]
        else:
            score = None

        return Joke(file, original_id, ordered_id, category, content, score)

    @staticmethod
    def joke_content(data):
        """ Returns a list of the content of the given jokes. """
        content = []
        for joke in data:
            content.append(joke.content)
        return content

    def get_joke(self, index):
        """ Returns the joke at the given index. """
        return self.jokes[index]

    vectorizer = TfidfVectorizer(use_idf=True)

    def vectorize_jokes(self, data):
        """ Vectorizes the given jokes. """
        return self.vectorizer.fit_transform(data)

    def top_three_jokes(self, query):
        """ Finds the top three jokes that matches the given query. """
        vectors = self.vectorize_jokes(self.joke_content(self.jokes))
        query = self.vectorizer.transform([query])

        distances = []
        for count, row in enumerate(vectors):
            distances.append([cosine_similarity(row, query)[0][0], count])
            if not count % 10000:
                print(f'Jokes processed: {count}')

        distances.sort(key=lambda x: x[0])
        top = [x[1] for x in distances[-3:]]

        for index in top:
            print(self.get_joke(index))


class ClfRegr:

    testing_jokes = []
    training_jokes = []

    vectorizer = TfidfVectorizer(use_idf=True)
    clf = RandomForestClassifier()
    regr = RandomForestRegressor()

    def __init__(self, files):
        self.unique_categories = set()
        self.joke_handler = JokeHandler()
        for file in files:
            self.joke_handler.add_jokes(file)

        if len(self.joke_handler.jokes) % 2:
            del self.joke_handler.jokes[-1]
        for joke in self.joke_handler.jokes:
            if joke.ordered_id % 2:
                self.testing_jokes.append(joke)
            else:
                self.training_jokes.append(joke)
            self.unique_categories.add(joke.category)

        self.unique_categories = list(self.unique_categories)
        self.vectorizer.fit(self.joke_handler.joke_content(self.joke_handler.jokes))

    def get_category_ids(self, jokes):
        """ Returns a list with the ID of categories for the given jokes. """
        category_ids = []
        for joke in jokes:
            category_ids.append(self.unique_categories.index(joke.category))
        return category_ids

    @staticmethod
    def get_scores(jokes):
        """ Returns a list of the scores for the given jokes. """
        scores = []
        for joke in jokes:
            scores.append(joke.score)
        return scores

    def clf_fit(self):
        """ Fits the random forest classifier with the training jokes. """
        training_vectors = self.vectorizer.transform(self.joke_handler.joke_content(self.training_jokes))
        training_categories = self.get_category_ids(self.training_jokes)

        self.clf.fit(training_vectors, training_categories)

    def clf_predict(self):
        """ Predicts the categories of the testing jokes. """
        testing_vectors = self.vectorizer.transform(self.joke_handler.joke_content(self.testing_jokes))
        testing_categories = self.get_category_ids(self.testing_jokes)

        tested_categories = self.clf.predict(testing_vectors)

        return accuracy_score(testing_categories, tested_categories)

    def regr_fit(self):
        """ Fits the random forest regression with the training jokes. """
        training_vectors = self.vectorizer.transform(self.joke_handler.joke_content(self.training_jokes))
        training_scores = ClfRegr.get_scores(self.training_jokes)

        self.regr.fit(training_vectors, training_scores)

    def regr_predict(self):
        """ Predicts the scores of the testing jokes. """
        testing_vectors = self.vectorizer.transform(self.joke_handler.joke_content(self.testing_jokes))
        testing_scores = ClfRegr.get_scores(self.testing_jokes)

        tested_scores = self.regr.predict(testing_vectors)
        return accuracy_score(testing_scores, tested_scores)


"""
cl = ClfRegr(["stupidstuff.json", "wocka.json"])
cl.clf_fit()
print(f'Classification accuracy score: {cl.clf_predict()}')
"""

regr = ClfRegr(["reddit_jokes.json"])
regr.regr_fit()
print("Jokes fitted")
print(f'Regression accuracy score: {regr.regr_predict()}')

IPython.embed()
