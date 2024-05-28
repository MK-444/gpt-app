import re
from app.schemas.models import PokemonInfo


def extract_pokemon_info(text):
    pattern = re.compile(r"Name:\s*(.*?)\s*Type:\s*(.*?)\s*Description:\s*(.*)")
    match = pattern.search(text)

    if not match:
        raise ValueError("The text does not have the required information")

    name, ptype, description = match.groups()
    return PokemonInfo(
        name=name.strip(), type=ptype.strip(), description=description.strip()
    )
