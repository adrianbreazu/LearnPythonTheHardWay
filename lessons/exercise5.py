my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

height_m = my_height * 0.0254  #convert to meters
weight_kg = my_weight * 0.453594  # convert to kilogram

print ("Let's talk about %s.", my_name)
print ("He's %d meters tall." % height_m)
print ("He's %d kg heavy." % weight_kg)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (
    my_age, height_m, weight_kg, my_age + height_m + weight_kg))