The goal of MD5 development was to create a function/algorithm that quickly and without much computational power creates a unique digest for each unique string (message). From this digest, it must not be possible (without using brute force or rainbow tables) to reconstruct the original message backwards. The MD5 hash is 128 bits long and is represented by 32 characters.

However, already a year after its publication, it became clear that this function does not work properly and a situation can occur where the function produces the same digest for two different strings. This flaw is fundamental and makes the MD5 function completely unusable for cryptography, as it leads to a number of security holes. The use of the MD5 function has been strongly discouraged for many years.

Nevertheless, the MD5 function continues to be widely used to authenticate strings (most commonly probably passwords) or to verify data integrity in simple and non-critical applications where a brute force attack is not expected. To make it more difficult to attempt to decrypt digests created with MD5, a so-called salt, which is an arbitrary secret key known only to the author of the application, is added to the beginning or end of the text to be encrypted.

Recommendation: if you are creating your own application and need to create a digest of some text, consider using other encryption functions that have not been found to have any security flaws.

