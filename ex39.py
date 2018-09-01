#create a mapping of state to abbreviation
states = {
'Oregon': 'OR',
'California' : 'CA',
'New York' : 'NY',
'Michigan' :'MI',
'India' : 'DL',

}
#create a basic set of states and some cities in them
cities = {
'CA': 'San Francisco',
'MI':'Detroit',
'FL':'Jacksonville',
'DL' : 'Delhi',

}
#add some more cities
cities['NY']= 'New york'
cities['OR']= 'Portland'
#pritn out some cities
print '_'*10
print "NY State has:",cities['NY']
print "OR State has:",cities['OR']
#print some states
print '_'*10
print "Michigan's abbreviation is :",states['Michigan']
print "India's abbreviation is :",states['India']

#do it by using the state then cities dicts
print '_'*10
print "Michigan has : ", cities[states['Michigan']]
print "India has : ", cities[states['India']]
#print every state abbreviation
print '_'*10
for state,abbrev in states.items():
    print "%s is abbreviated %s" %(state,abbrev)

#print every city in states
print '_'*10
for abbrev,city in cities.items():
    print "%s has the city %s" %(abbrev,city)

#now do both at the same time
print '_'*10
for state,abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])


print '_'*10
#safely get an abbreviation by state that might not be There
state = states.get('Texas',None)

if not state:
    print "Sorry, no Texas."

#get a city with a default value
city=cities.get('TX','Does Not Exist')
print "The city for the state 'TX' is : %s" % city
