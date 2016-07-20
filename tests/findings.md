# Original .text section
Text segment has a fairly high entropy of around 0.8 for the most part where the instructions are located. Which makes sense as it is simply binary data. In some sections however it does drop quite low.

# AES 256 in ECB mode
Mostly the entropy value for this mode is around 0.99 however it is correlated to parts where original entropy drops. Due to the way ECB mode leaks information about the clear text.

# AES 256 in CBC mode
CBC mode does not leak information in the way that ECB does hence its entropy is around 0.99 constantly, CBC is considered a better encryption mode and is used for this property over ECB.
I expect other modes such as CTR, XTS, GCM behave in similar way as they utilize tweaking values in the same way CBC uses crypt text from previous block to encrypt the next. Hence their entropy should be high.
