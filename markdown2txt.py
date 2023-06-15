

import mistune

in_file = "./api_docs/aiRecognize.md"
with open(in_file, "r") as md_file:
    markdown_text = md_file.read()

markdown_parser = mistune.create_markdown()
plain_text = markdown_parser(markdown_text)

out_file = "./api_docs/aiRecognize.txt"
with open(out_file, "w") as txt_file:
    txt_file.write(plain_text)