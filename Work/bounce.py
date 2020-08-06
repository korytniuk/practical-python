# bounce.py
#
# Exercise 1.5
height = 100
bounce = 0 
while bounce < 10:
    bounce += 1 
    height = height * (3/5)
    print(f'{ bounce } { round(height, 4) }') 
