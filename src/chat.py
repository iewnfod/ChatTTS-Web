import ChatTTS
from src.functions import *
import torch
from src.config import chat_config
import os
import uuid

class MyChat:
	def __init__(self):
		self._init_torch()

		self.timbres = ["Random"]
		self.timbre_type = chat_config.timbre_type
		self.chat = ChatTTS.Chat()
		chat.load_models(
			source = "local",
			local_path = os.path.join(chat_config.model_save_path, 'ChatTTS'),
			compile = True,
			device = self.device
		)

	def _init_torch(self):
		print(f"Torch Version {torch.__version__}")

		std, mean = torch.load('./models/ChatTTS/asset/spk_stat.pt').chunk(2)

		# 空字符串为随机，将会保存在 rand.pt 中
		# 否则调用预设
		spk_emb_type = ""
		spk_emb_save_dir = './models/spk_emb'

		if len(spk_emb_type) == 0 or spk_emb_type == "rand":
			rand_spk_emb = torch.randn(768) * std + mean
			spk_emb = rand_spk_emb
			torch.save(spk_emb, os.path.join(spk_emb_save_dir, 'rand.pt')) # save in tmp
			print(f'Speaker: Random')
		else:
			spk_emb_save_file_path = os.path.join(spk_emb_save_dir, f'{spk_emb_type}.pt')
			if os.path.exists(spk_emb_save_file_path):
				spk_emb = torch.load(spk_emb_save_file_path) # load speaker embedding
				print(f'Speaker: {spk_emb_type}')
			else:
				print(f"No such speaker: {spk_emb_type}")

		self.params_infer_code = {
			'spk_emb': spk_emb, # add sampled speaker
			'temperature': .3, # using custom temperature
			'top_P': 0.7, # top P decode
			'top_K': 20, # top K decode
		}

		self.params_refine_text = {
			'prompt': '[oral_2][laugh_0][break_6]'
		}

		self.device = "cpu"
		# if torch.backends.mps.is_available() and torch.backends.mps.is_built():
		# 	self.device = "mps"

		print(f"Device: {self.device}")

	def new_chat(self, text: str) -> str:
		wavs = self.chat.infer(
			solve_texts([text]),
			params_refine_text=self.params_refine_text,
			params_infer_code=self.params_infer_code
		)

		uid = uuid.uuid4()
		save_audios(audios=get_audios(wavs))

chat = MyChat()
