import importlib
import sys
import os

packages = [
	('torch', 'torch'),
	('IPython', 'IPython'),
	('chattts-fork', 'ChatTTS'),
	('toml', 'toml'),
	('flask', 'flask'),
	('modelscope', 'modelscope')
]

def test_requirements():
	for package_name, import_name in packages:
		try:
			importlib.import_module(import_name)
			print(f"Exist Dependece `{package_name}`")
		except:
			print(f'Missing Important Dependence `{package_name}`\nTrying to Install for You...')
			os.system(f'"{sys.executable}" -m pip install "{package_name}"')
