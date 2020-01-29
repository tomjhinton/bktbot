
from textgenrnn import textgenrnn
textgen = textgenrnn('colaboratory_weights1.hdf5',vocab_path='colaboratory_vocab1.json',
config_path='colaboratory_config1.json')

#textgen = textgenrnn()
#textgen.train_from_file('bktestform3.csv', num_epochs=5, new_model=True)
textgen.generate(max_gen_length=150)
