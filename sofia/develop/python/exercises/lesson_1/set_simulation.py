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

def create_set(card_one, card_two):
	card_three = {}
	card_three["number"] = create_feature(list(numbers), card_one["number"], card_two["number"])
	card_three["shape"] = create_feature(list(shapes), card_one["shape"], card_two["shape"])
	card_three["filling"] = create_feature(list(fillings), card_one["filling"], card_two["filling"])
	card_three["colour"] = create_feature(list(colours), card_one["colour"], card_two["colour"])
	return card_three


def create_feature(features, feature1, feature2):
	if feature1 == feature2:
		return feature1
	else:
		features.remove(feature1)
		features.remove(feature2)
		return features[0]

print(is_set(card_one, card_two, card_three))

