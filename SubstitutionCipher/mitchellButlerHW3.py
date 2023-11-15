import sys
import os
englishAlphabetFrequency = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 'f': 0.02228, 
              'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
              'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929, 'q': 0.00095, 'r': 0.05987,
              's': 0.06327, 't': 0.09056, 'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
              'y': 0.01974, 'z': 0.00074}
sorted_english = list(dict(sorted(englishAlphabetFrequency.items(), key=lambda item: item[1], reverse=True)).keys())
# print(sorted_english)
cipherAlphabetFrequency = {'a': 0.0, 'b': 0.0, 'c': 0.0, 'd': 0.0, 'e': 0.0, 'f': 0.0, 
              'g': 0.0, 'h': 0.0, 'i': 0.0, 'j': 0.0, 'k': 0.0, 'l': 0.0,
              'm': 0.0, 'n': 0.0, 'o': 0.0, 'p': 0.0, 'q': 0.0, 'r': 0.0,
              's': 0.0, 't': 0.0, 'u': 0.0, 'v': 0.0, 'w': 0.0, 'x': 0.0,
              'y': 0.0, 'z': 0.0}
cipherKey = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 
              'g': '', 'h': '', 'i': '', 'j': '', 'k': '', 'l': '',
              'm': '', 'n': '', 'o': '', 'p': '', 'q': '', 'r': '',
              's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '',
              'y': '', 'z': ''}

keyInput = False
fileInput = False
print("Welcome to the Substitution Cipher Cracker!")
if len(sys.argv) == 2:
  fileInput = True
else:
  keyInput = True
if fileInput:
  fileName = sys.argv[1]
  with open(fileName) as file:
    cipherText = file.read().lower()
  file.close()
elif keyInput:
  print("Enter the text you would like to decrypt:")
  cipherText = input().lower()

# print("Enter the key you would like to use:")

totalChars = 0
for ch in cipherText:
  if ch.isalpha():
    totalChars += 1
    cipherAlphabetFrequency[ch] += 1
for key in cipherAlphabetFrequency:
  cipherAlphabetFrequency[key] = round((cipherAlphabetFrequency[key]/totalChars), 5)
sorted_cipher = list(dict(sorted(cipherAlphabetFrequency.items(), key=lambda item: item[1], reverse=True)).keys())
# print(sorted_cipher)

for i in range(0, len(sorted_english)):
  cipherKey[sorted_cipher[i]] = sorted_english[i]
# print(cipherKey)

while True:
  plainText = ""
  for letter in cipherText:
    if letter.isalpha():
      plainText += cipherKey[letter]
    else:
      plainText += letter
  print("-------–-----------------------------------")
  print(plainText)
  print("-------–-----------------------------------")
  print("--Enter the letter you would like to replace (or type 'exit' to quit):", end=" ")
  letter = input().lower()
  if letter == "exit" or letter == "quit":
    break
  elif len(letter) != 1 or not letter.isalpha():
    print("1 alphabetical character only")
    continue
  print("--Enter the letter you would like to replace it with:", end=" ")
  replacement = input().lower()
  if len(replacement) != 1 or not replacement.isalpha():
    print("1 alphabetical character only")
    continue
  for key, val in cipherKey.items():
    if val == letter:
      for key2, val2 in cipherKey.items():
        if val2 == replacement:
          cipherKey[key2] = letter
      cipherKey[key] = replacement
      break

plainText += "\n"
if fileInput:
  if not os.path.isfile(fileName + "_ANS"):
    open(fileName + "_ANS", 'w').close()
  with open(fileName + "_ANS", 'w') as file:
     file.write(plainText)
  file.close()
print("Thank you!")
print("-------–-----------------------------------")
