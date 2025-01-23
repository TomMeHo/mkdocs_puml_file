import os
import re
import string
import logging
import mkdocs
from mkdocs.plugins import BasePlugin


# ------------------------
# Plugin
# ------------------------

REPLACEMENT_PATTERN = r'!\[(.*?)\]\((.*?.puml)\)'

class PlantUmlFilePlugin(BasePlugin):
    """
    Plugin that allows to embed PlantUML files into your markdown documents.
    """
    config_scheme = (
        (
            "file_extension",
            mkdocs.config.config_options.Type(str, default=".puml"),
        ),
    )