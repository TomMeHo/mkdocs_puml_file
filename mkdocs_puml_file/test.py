import re

def test():
    search_pattern = r"!\[.*?\]\((.*?.puml)\)"
    replacement_pattern = r"```puml\n'$2.puml'\n```"

    with open("../example/docs/index.md", "r") as f:
        input = f.read()

    output = re.sub( search_pattern, replacement_pattern, input )

    for occurence in re.finditer(search_pattern, input):
        print(occurence.groups(1))
        # loop backwards
        # https://stackoverflow.com/questions/869885/loop-backwards-using-indices

    print(output)

test()