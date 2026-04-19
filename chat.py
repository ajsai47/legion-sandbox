from hello import greet
from farewell import farewell


def chat(name: str) -> str:
    """Return a greeting and farewell for the given name."""
    return greet(name) + ' ' + farewell(name)
