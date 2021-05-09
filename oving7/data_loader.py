import json

from oving7.joke import Joke


class DataLoader:

    jokes = []
    ord_id = 0

    def add_jokes(self, file):
        with open(file, "r") as data_file:
            data = json.load(data_file)
        for joke in data:
            self.jokes.append(self.decode_data(joke, self.ord_id, file))
            self.ord_id += 1

    @staticmethod
    def decode_data(dct, ordered_id, file):
        original_id = dct["id"]

        if "category" in dct:
            category = dct["category"]
        else:
            category = None

        if "title" in dct:
            content = dct["title"] + " " + dct["body"]
        else:
            content = dct["body"]

        if "score" in dct:
            score = dct["score"]
        else:
            score = None

        return Joke(file, original_id, ordered_id, category, content, score)
