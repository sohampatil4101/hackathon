import re

# Token types
TOKEN_TYPES = {
    'KEYWORD': r'int|float|if|else|while|for|return',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*',
    'OPERATOR': r'\+|\-|\*|\/|\=\=|\!\=|\<|\>|\<\=|\>\=|\=|\+\+|\-\-|\&\&|\|\|',
    'LITERAL': r'\d+(\.\d+)?',
    'SEPARATOR': r'\;|\,|\(|\)|\{|\}',
    'COMMENT': r'\/\/.*|\/\*[\s\S]*?\*\/',
    'HEADER': r'\#include\s+<([a-zA-Z0-9_]+\.h)>'
}

# Function to tokenize the input C code
def tokenize_c_code(code):
    tokens = []
    code = re.sub(r'\s+', ' ', code)  # Remove extra whitespaces
    pattern = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_TYPES.items())
    for match in re.finditer(pattern, code):
        for name, value in match.groupdict().items():
            if value is not None and name != 'COMMENT':
                tokens.append((name, value))
    return tokens

# Function to read C code from file
def read_c_file(filename):
    with open(filename, 'r') as file:
        c_code = file.read()
    return c_code

# Example usage
filename = 'lex_example.c'
c_code = read_c_file(filename)
tokens = tokenize_c_code(c_code)

header_files = set()
for token_type, token_value in tokens:
    if token_type == 'HEADER':
        header_files.add(token_value)
    print(token_type, token_value)
