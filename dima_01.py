import string
from collections import Counter


def words(paragraph):
  paragraph =paragraph.lower()
  paragraph=paragraph.translate(str.maketrans("","",string.punctuation))
  word_list=paragraph.split()
  counter=Counter(word_list)
  return counter


def main():
  paragraph = """ Elon Musk is a business magnate and investor. 
  He is the founder, CEO and chief engineer of SpaceX; 
  angel investor, CEO and product architect of Tesla, 
  Inc.; owner and CEO of Twitter, Inc.; founder of The Boring Company; 
  co-founder of Neuralink and OpenAI; and president of the philanthropic Musk Foundation.
   With an estimated net worth of around $196 billion as of February 15, 2023, primarily from
    his ownership stakes in Tesla and SpaceX,[4][5] Musk is the second-wealthiest person in the world, 
    according to both the Bloomberg Billionaires Index and Forbes's real-time billionaires list."""
  print(words(paragraph))

if __name__=="__main__":
    main()
