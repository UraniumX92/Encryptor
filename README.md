# **Encryptor v1.0**
## **About Encryptor :**
I made this Program which encrypts and decrypts a given text using 1 or 2 keys, Keys can be given just like the keys in polyalphabetic cipher

i.e : keys can have either integer numbers, or any alphabet in upper or lower case

Example : 

    1,2,3,4,a,b,c,d 

Similarly, you can encrypt the text in 2 layered keys, you have to enter 2 keys in the 'key' field, you have to separate the 2 keys using two hyphens '--'

make sure you don't have any spaces before or after hyphens

Valid Entry:

    1,2,3,a,b--4,5,c,d

Invalid Entries:

    1,2,3,a,b -- 4,5,c,d
    1,2,3,a,b --4,5,c,d
    1,2,3,a,b-- 4,5,c,d

> ***Note :*** Notice how a space on either side of hyphens will make the entry invalid

***
### **2 Layered Encryption/Decryption :**
The program Encrypts and Decrypts in 2 layers if 2 keys are provided

In Encryption, The input text will first get encrypted with the first key and then the encrypted text will get another layer of encryption using the 2nd key.
Well that is self explanatory.

But, In Decryption, The input text will first get decrypted with the 2nd key and then the decrypted text will get decrypted using first key.
This is to follow the order of Encryption.

So, **DO NOT** change the order of your keys if you are doing 2 layered Encryption/Decryption.
***
***
## **History :**
Previously I made a similar Cipher/Decipher program using `C++`
That program was just a console program, a polyalphabetic cipher with 2 layers of keys, which was still crackable without even knowing key (If used improperly)

If used properly, it was a little hard to crack without key (Requires hours of time,and really good computer machines.. I gues...)

So after some time of completing that program (those were my early days into coding), I thought:

**"Why make a cipher program which contains only alphabets? it is easier to crack because it only has alphabets, why not make an Encryptor which should have alphabets as well as other characters"**

That's when I Decided that I will make this type of Encryptor some time.
And I started this Project a couple of days ago, and I'm proud to say that this Encryption is not crackable without key.(if used good keys, because this is partially polyalphabetic cipher, but if you use keys smartly, it is uncrackable)

>---
I also made a Discord Bot using Python, If you want to check that out, [Here is the link for Discord Bot I made using python `(discord.py)`](https://github.com/UraniumX92/Discord-Bot-using-py "Link to Discord Bot using Python made by UraniumX92") 

(`discord.py` was maintained at that time)

Well that is pretty much it for this Project, I will continue to work on this project for few days, Maybe Look for bugs and fix it.

And after that I am gonna make an offline password manager, In which I am going to use this encryption to store passowrds in files.
***
    