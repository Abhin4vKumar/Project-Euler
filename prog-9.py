# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# LOGIC
#------------
# a + b + c = 1000
# a^2 + b^2 = c^2
# a^2 +b^2 = (1000 - (a+b))^2
# simplifying....we get
# a = 1000(500-b)/(1000 - b)
# given that a < b < c ......... and a b c are natural numbers
# hence b < 500
# so for 499 values we brute force the final equation to get a
# then, we will calculate a*b*c as (1000 - (a + b) )* a * b



# CODE
# --------------
for b in range(1,500):
    a = 1000 * (500 - b) / (1000 - b)
    if float(int(a)) == float(a):
        print(int(a * b * (1000 - (a + b))))
        break
