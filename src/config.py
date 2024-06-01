import toml

class BasicConfig:
	def __init__(self, config):
		self.host = config['host']
		self.port = config['port']

	def update(self, config):
		self = BasicConfig(config)

class ChatConfig:
	def __init__(self, config):
		self.timbre_type = config['timbre_type']
		self.model_save_path = config['model_save_path']

	def update(self, config):
		self = ChatConfig(config)


config = toml.load("config.toml")

basic_config = BasicConfig(config['basic'])
chat_config = ChatConfig(config['chat'])
