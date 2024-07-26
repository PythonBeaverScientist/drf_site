from pathlib import Path
from logging import config, getLogger

import yaml

from global_settings import settings


with Path(settings.LOGGING_CONF_FILE).open() as file:
    logger_config = yaml.safe_load(file)

config.dictConfig(logger_config)
log = getLogger(__name__)
