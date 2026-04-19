def titlecase(text: str) -> str:
    """Capitalize the first letter of each whitespace-separated word in ``text``."""
    return " ".join(word[:1].upper() + word[1:] for word in text.split(" "))


def snake_to_camel(text: str) -> str:
    """Convert a snake_case string to camelCase."""
    parts = text.split("_")
    if not parts:
        return ""
    first = parts[0]
    rest = (part[:1].upper() + part[1:] for part in parts[1:])
    return first + "".join(rest)
