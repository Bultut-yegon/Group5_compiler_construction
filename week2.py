import re

# Define token types and patterns for Zara language
TOKEN_SPECIFICATION = [
    ('KEYWORD',
     r'\b(if|else|do|while|for|int|float|string|array|stack)\b'),  # Keywords
    ('OPERATOR', r'[=+\-*/><]+|==|>=|<=|!='),  # Operators
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),  # Identifiers
    ('LITERAL',
     r'\b\d+(\.\d+)?\b|\"[^\"]*\"'),  # Integer, float, and string literals
    ('WHITESPACE', r'\s+'),  # Whitespace (optional to skip)
    ('COMMENT', r'//[^\n]*'),  # Single line comments
    ('UNKNOWN', r'.')  # Any other character (error handling)
]

# Compile all patterns into a single regex pattern
token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})'
                       for pair in TOKEN_SPECIFICATION)
token_re = re.compile(token_regex)


# Token class to represent the type and value of each token
class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'


# Lexical Analyzer to tokenize Zara code
def tokenize(code):
    tokens = []
    for match in token_re.finditer(code):
        token_type = match.lastgroup
        if token_type:  # Ensure token_type is not None
            token_value = match.group(token_type)
            # Skip whitespace tokens
            if token_type == 'WHITESPACE':
                continue

            # Add valid tokens to the list
            tokens.append(Token(token_type, token_value))

    return tokens


# Test the lexical analyzer with Zara-like sample code
def default():
    code = """
    int a = 10;
    float b = 3.14;
    string msg = "Hello, World!";
    if (a > b) {
        do {
            a = a + 1;
        } while (a < 20);
    }
    // This is a comment
    """

    # Tokenize the Zara code
    tokens = tokenize(code)

    # Print the tokens
    for token in tokens:
        print(token)


if __name__ == "__main__":
    default()
