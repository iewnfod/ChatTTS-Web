import toml

config_path = "config.toml"

def save_config():
	with open(config_path, 'w') as f:
		f.write(toml.dumps({
			"basic": vars(basic_config),
			"chat": vars(chat_config)
		}))

class BasicConfig:
	def __init__(self, config):
		self.host = config['host']
		self.port = config['port']
		self.model_save_dir = config['model_save_dir']

	def update(self, config):
		self.__dict__ = BasicConfig(config).__dict__
		save_config()

class ChatConfig:
	def __init__(self, config):
		self.timbre_type = config['timbre_type']
		self.prompt = config['prompt']

	def update(self, config):
		self.__dict__ = ChatConfig(config).__dict__
		save_config()


config = toml.load(config_path)

basic_config = BasicConfig(config['basic'])
chat_config = ChatConfig(config['chat'])
