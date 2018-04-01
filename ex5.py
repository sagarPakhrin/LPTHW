name = "Sagar Lama"
age = 22
height = 5.1 #feet
weight = 48 #kg
eyes = 'Brown'
teeth = 'white'
hair = 'black'

print "Let's talk about %s" %name
print "He's %0.1f feet tall" %height
print "He's %d kg heavy" %weight
print "Actually that's not too heavy."
print "He's got %s eyes and %d hair." %(eyes, height)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age,height,weight, age+height+weight)
