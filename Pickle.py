import pickle

file = open('super.txt', 'wb')

data = {}
data['super'] = "Man"

ha = pickle.dumps(data)
# print "-------------"
# print ha
# print "-------------"
# print pickle.loads(ha)
