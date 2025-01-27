import re
import mkdocs
import logging
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files


# ------------------------
# Plugin
# ------------------------

class PlantUmlFilePlugin(BasePlugin):
    """
    Plugin that allows to embed PlantUML files into your markdown documents.
    Must be placed before plugin mkdocs_puml
    """
    config_scheme = (   
        (
            "file_extension",
            mkdocs.config.config_options.Type(str, default=".puml"),
        ),
    )

    def __init__(self):
        self.log = logging.getLogger(f"mkdocs.plugins.{__name__}")

    def on_page_markdown( self, markdown: str, page: Page, config: MkDocsConfig, files: Files ):
        search_pattern = r"!\[.*?\]\((.*?.puml)\)"

        for file in files.media_files():
            self.log.debug("PUML_FILE --------- " + file.src_path + " - " + file.abs_src_path + " --- " + file.src_uri)

        iterator = re.finditer(search_pattern, markdown)
        for occurence in reversed(list(iterator)):
            filename = occurence.group(1)
            puml_file_content = next((f.content_string for f in files.media_files() if (f.src_uri == filename)), "###")
            if puml_file_content == "###":
                self.log.warning("Plugin PUML_FILE: File %s not found.", filename)
                puml_file_content = "--- file not found ---"

            if len(puml_file_content) == 0:
                self.log.warning("Plugin PUML_FILE: File %s has no contents.", filename)

            puml_file_content = f"```puml\n{puml_file_content}\n```\n"
            markdown = markdown[:occurence.start()] + puml_file_content + markdown[occurence.end():]
        self.log.debug(markdown)
        return markdown
