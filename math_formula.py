# Even Odd
def even_odd(number):
 if number%2==0:
    print('even')
 else:
    print('odd')

# Positive Negative Zero
def num_pos_neg(number):
 if number>0:
    print('positive')
 elif number<0:
    print('negative')
 else:
  print('zero')

# list count(length)
def length(v_name):
 count=0
 for i in v_name:
  if i!=None:
   count+=1
 print(count)
 #return count