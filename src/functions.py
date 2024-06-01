import os
from IPython.display import Audio, display

audio_rate = 24000
audio_save_dir = './dist'

def get_audios(wavs):
	audios = []
	for wav in wavs:
		audios.append(Audio(wav, rate=audio_rate, autoplay=True))
	return audios

def display_audio(audios, texts = None):
	for i in range(len(audios)):
		if texts: print("\n" + texts[i])
		display(audios[i])

def save_audios(audios):
	for i in range(len(audios)):
		with open(os.path.join(audio_save_dir, f'part{i+1}.wav'), 'wb') as f:
			f.write(audios[i].data)

def solve_texts(texts):
	t = []
	for text in texts:
		t.append(text
			.replace('“', ', ')
			.replace('”', ', ')
			.replace('！', '. ')
			.replace('？', ' . ')
			.replace('?', '. ')
			.replace('!', '. ')
		)
	return t
