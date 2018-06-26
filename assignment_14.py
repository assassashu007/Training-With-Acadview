print("Q1.Extract the user id, domain name and suffix from the following email addresses.")
print('   emails = zuck26@facebook.com  ,  page33@google.com  &  jeff42@amazon.com \n')


import re
emails = """zuck26@facebook.com page33@google.com jeff42@amazon.com"""
print(re.findall(r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})', emails, flags=re.IGNORECASE))






print("\n\nQ2.Retrieve all the words starting with ‘b’ or ‘B’ from the following text: ")
print("   Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.\n")


import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(re.findall(r"\bB\w+", text, flags=re.IGNORECASE))







print("\n\nQ3. Split the irregular sentence into words only sentence")
print("    sentence :  A, very very; irregular_sentence\n")


import re
sentence = "A, very very; irregular_sentence"
output = " ".join(re.split('[;,\s_]+', sentence))
print(output)







print("\n\nQ4. Clean up the following tweet so that it contains only the user’s message")
print("    i.e. remove all URLs, hashtags, mentions, punctuations, RTs and CCs.\n")


import re
tweet = "Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
tweet = re.sub('(http\S+\s*)|(RT|cc)|(#\S+)|(@\S+)',' ',tweet)
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
tweet = re.sub('\s+', ' ', tweet)
print(tweet)



