term_colors = {
    'blue': '\033[94m',
    'red': '\033[91m',
    "yellow": '\033[93m',
    "green": '\033[92m',
    'clear': '\033[0m',
    "bold": '\033[1m',
    "underline": '\033[4m'
}


def color(key: str, text: str) -> str:
    return term_colors[key] + text + term_colors['clear']
