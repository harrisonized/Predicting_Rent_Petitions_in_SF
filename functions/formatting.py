# Objects included in this file:

# Functions included in this file:
# # title_to_snake_case


def title_to_snake_case(text):
    """Converts "Column Title" to column_title
    """
    return text.lower().replace(' ', '_').replace('-', '_')


def replace_char_with_space(text, chars):
    """From StackOverflow
    See: https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string
    """
    for char in chars:
        text = text.replace(char, ' ')
    return text
