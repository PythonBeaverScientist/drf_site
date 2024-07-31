from pathlib import Path
from logging import config, getLogger

import yaml

from django_site.settings import LOGGING_CONF_FILE


with Path(LOGGING_CONF_FILE).open() as file:
    logger_config = yaml.safe_load(file)

config.dictConfig(logger_config)
log = getLogger(__name__)
