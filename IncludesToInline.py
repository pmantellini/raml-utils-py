import sys
import re

# Constants
include_regex = "^(\s*)(.*) \!include (.*)"
include_inline_separator = ' |\n'
spaces_indent = '  '
raml_input = ''
raml_inline_output = ''

# Functions
def appendInclude(file_in_line, include_path, parent_indent):
    with open(include_path, "r") as include_file:
        for include_line in include_file:
            file_in_line.write(parent_indent + spaces_indent + include_line)

def execute():
    with open(raml_input, 'r') as file_with_includes: 
        with open(raml_inline_output, 'w+') as file_in_line:
            for src_line in file_with_includes:
                match_include_line = re.match(include_regex, src_line)
                if match_include_line:
                    file_in_line.write(match_include_line.group(1) + match_include_line.group(2) + include_inline_separator)
                    appendInclude(file_in_line, match_include_line.group(3), match_include_line.group(1))
                else:
                    file_in_line.write(src_line)

# Entry point

if len(sys.argv) != 3:
    sys.exit('Usage: python IncludesToInline.py raml_input raml_inline_output')

raml_input = sys.argv[1]
raml_inline_output = sys.argv[2]

execute()