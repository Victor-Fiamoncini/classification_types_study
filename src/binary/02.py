from csv import reader
from os import getcwd
from typing import List, Union
from sklearn.naive_bayes import MultinomialNB

def load_data() -> Union[List[int], List[int]]:
  cwd = getcwd()

  x = []
  y = []

  try:
    file = open(cwd + '/src/binary/data/users_access.csv', 'rt')
    buffer = reader(file)

    buffer.__next__()

    for home, how_it_works, contact, bought in buffer:
      x.append([int(home), int(how_it_works), int(contact)])
      y.append(int(bought))

    return x, y
  except:
    raise

def train_test_data(x, y) -> None:
  x_train = x[:90]
  y_train = y[:90]

  x_test = x[-9:]
  y_test = y[-9:]

  model = MultinomialNB()

  try:
    model.fit(x_train,  y_train)

    predictions = model.predict(x_test)
    differences = predictions - y_test

    hits = [d for d in differences if d == 0]
    hit_rate = (100 * len(hits)) / len(x_test)

    print('Hit rate: ', hit_rate)
    print('Number of tested elements: ', len(x_test))
  except:
    raise

x, y = load_data()

train_test_data(x=x, y=y)
