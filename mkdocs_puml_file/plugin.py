import re
import mkdocs
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files


# ------------------------
# Plugin
# ------------------------

SEARCH_PATTERN = r'!\[(.*?)\]\((.*?.puml)\)'
REPLACEMENT_PATTERN = r'```puml\n<$2.puml>\n```'

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
        page.markdown = re.sub( SEARCH_PATTERN, REPLACEMENT_PATTERN, page.markdown )
        return page