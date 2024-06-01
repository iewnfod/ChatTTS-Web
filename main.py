from src.check_dependence import test_requirements

test_requirements()

from src.app import app
from src.config import basic_config

app.run(host=basic_config.host, port=basic_config.port)
