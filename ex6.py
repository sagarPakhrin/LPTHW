#strings and text
#this line will print There are 10 types of people
x = "There are %d types of people." %10
binary = "binary"
do_not ="don't"
#Those who know binary and those who don't
y = "Those who know %s and those who %s" %(binary,do_not)

#There are 10 types of people.
print x
#Those who know binary and those who don't
print y


#%r will enclose the value within a '' 
# I said: 'There are 10 types of people.'
print "I said: %r" %x
#I also said: 'Those who understand binary and those who don't
print "I also said: '%s'." %y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r" 

print joke_evaluation % hilarious

w = "This is the left side of....."
e = "a string with a right side"
print w + e
