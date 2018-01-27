# Homework 1 (due 'til 02. Feb. 2018)
This is the content of the set_simulation.py file:

```python
numbers = [1,2,3]
shapes = ['oval','rect','saussice',]
fillings = ['striped','empty','full']
colours = ['green','red','purple']

card_one = {'number':1,
            'shape':'oval',
            'filling':'striped',
            'colour':'green'}

card_two = {'number':2,
            'shape':'oval',
            'filling':'striped',
            'colour':'green'}

card_three = {'number':3,
            'shape':'oval',
            'filling':'striped',
            'colour':'green'}


def is_set(card_one,card_two, card_three):
    return is_equal_or_different(card_one, card_two, card_three, 'number') and is_equal_or_different(card_one, card_two, card_three, 'shape') and is_equal_or_different(card_one, card_two, card_three, 'filling') and is_equal_or_different(card_one, card_two, card_three, 'colour')

def is_equal_or_different(card_one,card_two,card_three,feature):
    test_features_equal = card_one[feature] == card_two[feature] and card_one[feature] == card_three[feature]
    test_features_diffrent = card_one[feature] != card_two[feature] and card_one[feature] != card_three[feature]  and card_two[feature] != card_three[feature]
    return test_features_equal or test_features_diffrent    

print(is_set(card_one, card_two, card_three))

```


The task is to create a function called `create_set(card_one, card_two)` that creates the complementary card in the set.


Make sure the outputs look as follows for the following commands:
```python
>>> import set_simulation as set
>>> card_one = {'number':1,
... 'shape':'oval',
... 'filling':'striped',
... 'colour':'green'}
>>> card_two = {'number':2,
... 'shape':'oval',
... 'filling':'striped',
... 'colour':'green'}
>>> set.create_set(card_one, card_two)
{'number': 3, 'shape': 'oval', 'filling': 'striped', 'colour': 'green'}
>>> set.create_set(card_two, card_one)
{'number': 3, 'shape': 'oval', 'filling': 'striped', 'colour': 'green'}
>>> card_one["shape"] = "rect"
>>> set.create_set(card_one, card_two)
{'number': 3, 'shape': 'saussice', 'filling': 'striped', 'colour': 'green'}
```
