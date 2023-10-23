import tiktoken

# ----- token counter-----
def num_tokens_from_string(string, encoding_name):
    """Returns the number of tokens in a text string."""
    encoding_name = "cl100k_base"
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
