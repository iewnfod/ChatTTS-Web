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

def save_audio(audio, text, name):
	if not os.path.exists(audio_save_dir):
		os.makedirs(audio_save_dir)

	with open(os.path.join(audio_save_dir, f'{name}.wav'), 'wb') as f:
		f.write(audio.data)
	with open(os.path.join(audio_save_dir, f'{name}.txt'), 'w') as f:
		f.write(text)

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

def get_text_from_uid(uid):
	with open(os.path.join(audio_save_dir, f'{uid}.txt'), 'r') as f:
		return f.read()

def remove_audio(uid):
	os.remove(os.path.join(audio_save_dir, f'{uid}.wav'))
	os.remove(os.path.join(audio_save_dir, f'{uid}.txt'))
