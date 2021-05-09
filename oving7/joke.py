class Joke:

    def __init__(self, file, original_id, ordered_id, category, content, score):
        self.file = file
        self.original_id = original_id
        self.ordered_id = ordered_id
        self.category = category
        self.content = content
        self.score = score

    def __str__(self):
        return f'File: {self.file}\n' \
               f'ID(original: {self.original_id}, ordered: {self.ordered_id})\n' \
               f'Category: {self.category}\n' \
               f'Score: {self.score}\n\n' \
               f'{self.content}'
