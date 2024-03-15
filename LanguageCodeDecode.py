import random
import string

alphabets = list(string.ascii_letters)
random_string = random.sample(alphabets, 3)

r1 = ''.join(random_string)
r1 = r1[::-1]
r2 = ''.join(random_string)


st = input("Enter message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding=="1") else False

# Coding
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      stnew = r1+ word[1:] + word[0] + r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))

# Decoding
else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))