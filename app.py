import os
from dotenv import load_dotenv
import tweepy
import time

from textgenrnn import textgenrnn
textgen = textgenrnn('colaboratory_weights1.hdf5', vocab_path='colaboratory_vocab1.json',
config_path='colaboratory_config1.json')
load_dotenv()
#textgen = textgenrnn()
#textgen.train_from_file('bktestform3.csv', num_epochs=5, new_model=True)
# textgen.generate(max_gen_length=150)

c_k = os.getenv("API_key")
c_s = os.getenv("API_secret_key")
a_k = os.getenv("Access_token")
a_s = os.getenv("access_token_secret")
auth = tweepy.OAuthHandler(c_k, c_s)
auth.set_access_token(a_k, a_s)
api = tweepy.API(auth)
def tweety():
    api.update_status(textgen.generate(max_gen_length=150, temperature=0.2, return_as_list=True)[0])


    time.sleep(1800)
    tweety()


tweety()
