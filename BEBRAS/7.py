'''ntroduction
Harriet loves to send messages encrypted using secret ciphers. She has invented a simple cipher where every letter of her message is separated by a rogue letter. For example, the message:

MEET ME AT SIX

Could be encrypted as:

MGEREQTA YMCEL HAPTX ASUINXM

To decrypt the message you simply look at every other character of the message (including the spaces).

          MGEREQTA  YMCEL  HAPTX  ASUINXM

Task
Write a program that, given a string holding an encrypted message, prints out the secret message.

Input format
A single line holding the encrypted message.

Output format
A single line displaying the unencrypted message.

Example:
Input:
MGEREQTA YMCEL HAPTX ASUINXM
Output:
MEET ME AT SIX
'''





encrypted = input()
encrypt = []


decrypted = ''
for i in encrypted:
  if i // 2 != 0:
    decrypted += encrypted[i]

print(decrypted)



















