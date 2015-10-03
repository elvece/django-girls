if 3 > 2:
  print ('3 is greater than 2')
else:
  print ('3 is not greater than 2')

name = 'Lucy'
if (name == 'Sonja'):
  print ('Hello Sonja')
elif (name == 'Lucy'):
  print ('Hello Lucy')
else:
  print ('Hey you')

score = 90
if (0 <= score <= 40):
  print ('You Failed!')
elif (41 <= score <= 60):
  print ('You passed with a below average score')
elif (61 <= score <= 80):
  print ('You passed!')
else:
  print ('You passed with an above average score')

def hi(name):
  print ('Hi ' + name + '!')
hi('john')

girls = ['sandra', 'sarah', 'allie', 'lucy']

# for name in girls:
#   hi(name)
#   print ('NEXT')

for test in girls:
  hi(test)
  print ('---')
