# test002-1.py

# text1 = "I Wasted $1000 On A Tactical Stroller"

# def shorten(text):
#     if len(text) >= 41:
#         n = text[:-3]+"..."
#         print(n)
# shorten(text1)

text = "Dropping a Camera to the Bottom of Antarctica"

def ShortenTitle(title):
    if len(title) >= 41:
        short_text = title[0:30]+"..."
        return short_text
    else:
        return title

print(ShortenTitle(text))