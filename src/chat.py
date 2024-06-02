import ChatTTS
from src.functions import *
import torch
from src.config import chat_config, basic_config
import os
import uuid

class MyChat:
	def __init__(self):
		self._init_torch()

		self.chat = ChatTTS.Chat()
		self.chat.load_models(
			source = "local",
			local_path = os.path.join(basic_config.model_save_dir, 'ChatTTS'),
			compile = True,
			device = self.device
		)

	def _init_torch(self):
		print(f"Torch Version {torch.__version__}")

		std, mean = torch.load(os.path.join(basic_config.model_save_dir, 'ChatTTS', 'asset', 'spk_stat.pt')).chunk(2)

		# 空字符串为随机，将会保存在 rand.pt 中
		# 否则调用预设
		spk_emb_save_dir = os.path.join(basic_config.model_save_dir, 'spk_emb')

		if len(chat_config.timbre_type) == 0 or chat_config.timbre_type == "random":
			rand_spk_emb = torch.randn(768) * std + mean
			spk_emb = rand_spk_emb
			torch.save(spk_emb, os.path.join(spk_emb_save_dir, 'rand.pt')) # save in tmp
			print(f'Speaker: Random')
		else:
			spk_emb_save_file_path = os.path.join(spk_emb_save_dir, f'{chat_config.timbre_type}.pt')
			if os.path.exists(spk_emb_save_file_path):
				spk_emb = torch.load(spk_emb_save_file_path) # load speaker embedding
				print(f'Speaker: {chat_config.timbre_type}')
			else:
				print(f"No such speaker: {chat_config.timbre_type}")

		self.params_infer_code = {
			'spk_emb': spk_emb, # add sampled speaker
			'temperature': .3, # using custom temperature
			'top_P': 0.7, # top P decode
			'top_K': 20, # top K decode
		}

		self.params_refine_text = {
			'prompt': chat_config.prompt
		}

		self.device = "cpu"
		# if torch.backends.mps.is_available() and torch.backends.mps.is_built():
		# 	self.device = "mps"

		print(f"Device: {self.device}")

	def new_chat(self, text: str, new_chat_config) -> str:
		chat_config.update(new_chat_config)
		self._init_torch()

		wavs = self.chat.infer(
			solve_texts([text]),
			params_refine_text=self.params_refine_text,
			params_infer_code=self.params_infer_code
		)

		uid = uuid.uuid4()
		save_audio(audio=get_audios(wavs)[0], text=text, name=uid)
		return uid

	def remove_chat(self, uid: str):
		remove_audio(uid)
		return uid

chat = MyChat()
