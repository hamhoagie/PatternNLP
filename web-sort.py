from pattern.web import sort

results = sort(terms=[
    'sunset',
    'puppies',
    'kittens',
    'babies',
    'hedgehogs',
    'birthday',
    'bunnies'], context='joy', prefix=True)

for weight, term in results:
    print "%.2f" % (weight * 100) + '%', term
