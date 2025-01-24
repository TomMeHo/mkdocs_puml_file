import re
import mkdocs
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
    """
    config_scheme = (   
        (
            "file_extension",
            mkdocs.config.config_options.Type(str, default=".puml"),
        ),
    )

    def __init__(self):
        pass
        #self.log = logging.getLogger("mkdocs.plugins.diagrams")
        #self.pool = None


    def on_pre_page( self, page: Page, /, *, config: MkDocsConfig, files: Files ):
        search_pattern = r"!\[(.*?)\]\((.*?.puml)\)"
        replacement_pattern = r"```puml\n<$2.puml>\n```"

        page.markdown = re.sub( search_pattern, replacement_pattern, page.markdown )
        return page