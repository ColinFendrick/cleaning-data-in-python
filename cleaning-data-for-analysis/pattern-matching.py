import re

pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{4}', string='123-456-7890'))
print(pattern1)

pattern2 = bool(re.match(pattern='^\$\d*\.\d{2}$', string='$123.45'))
print(pattern2)

pattern3 = bool(re.match(pattern='\w*', string='Australia'))
print(pattern3)
