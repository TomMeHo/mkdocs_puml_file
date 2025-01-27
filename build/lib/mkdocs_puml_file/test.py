import re

def test():
    search_pattern = r"!\[.*?\]\((.*?.puml)\)"

    with open("example/docs/index.md", "r") as f:
        mkdocs = f.read()

    # mkdocs = "This is a string."

    iterator = re.finditer(search_pattern, mkdocs)
    for occurence in reversed(list(iterator)):
        puml_file_content = ''
        try:
            puml_file_name = occurence.group(1)
            with open(puml_file_name, "r") as puml_file:
                puml_file_content = f"```puml\n{puml_file.read()}\n```\n" 
        except IOError:
            puml_file_content = f'! File not found: { puml_file_name }'

        print(occurence.group(1))
        mkdocs = mkdocs[:occurence.start()] + puml_file_content + mkdocs[occurence.end():]

    print(mkdocs)

test()