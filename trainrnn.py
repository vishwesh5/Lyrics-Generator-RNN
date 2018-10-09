from textgenrnn import textgenrnn
#textgen = textgenrnn(name="lyrics")
textgen = textgenrnn(weights_path='lyrics_weights.hdf5',
vocab_path='lyrics_vocab.json',
config_path='lyrics_config.json')
#textgen.reset()
textgen.train_from_largetext_file("lyrics.txt",new_model=False,num_epochs=80,word_level=True,max_gen_length=10,max_words=5000,max_length=10)
generated_texts = textgen.generate(10,return_as_list=True)
with open("lyrics_out.txt",'w') as f:
	f.write("\n".join(generated_texts))
