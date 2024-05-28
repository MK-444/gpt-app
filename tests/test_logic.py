import pytest
from app.schemas.models import PokemonInfo
from app.api.logic import extract_pokemon_info


def test_extract_pokemon_info_correct_input():
    text = (
        "Name: Pikachu Type: Electric Description: Pikachu is an Electric-type Pokémon."
    )
    expected = PokemonInfo(
        name="Pikachu",
        type="Electric",
        description="Pikachu is an Electric-type Pokémon.",
    )
    assert extract_pokemon_info(text) == expected

def test_extract_pokemon_info_missing_name():
    text = "Type: Electric Description: Pikachu is an Electric-type Pokémon."
    with pytest.raises(ValueError, match="The text does not have the required information"):
        extract_pokemon_info(text)

def test_extract_pokemon_info_missing_type():
    text = "Name: Pikachu Description: Pikachu is an Electric-type Pokémon."
    with pytest.raises(ValueError, match="The text does not have the required information"):
        extract_pokemon_info(text)

def test_extract_pokemon_info_missing_description():
    text = "Name: Pikachu Type: Electric"
    with pytest.raises(ValueError, match="The text does not have the required information"):
        extract_pokemon_info(text)

def test_extract_pokemon_info_varied_format():
    text = """
    Name: Pikachu
    Type: Electric
    Description: Pikachu is an Electric-type Pokémon.
    """
    expected = PokemonInfo(
        name="Pikachu",
        type="Electric",
        description="Pikachu is an Electric-type Pokémon.",
    )
    assert extract_pokemon_info(text) == expected

def test_extract_pokemon_info_extra_whitespace():
    text = "Name:   Pikachu    Type:   Electric    Description:  Pikachu is an Electric-type Pokémon.  "
    expected = PokemonInfo(
        name="Pikachu",
        type="Electric",
        description="Pikachu is an Electric-type Pokémon.",
    )
    assert extract_pokemon_info(text) == expected

def test_extract_pokemon_info_newlines():
    text = "Name: Pikachu\nType: Electric\nDescription: Pikachu is an Electric-type Pokémon."
    expected = PokemonInfo(
        name="Pikachu",
        type="Electric",
        description="Pikachu is an Electric-type Pokémon.",
    )
    assert extract_pokemon_info(text) == expected

def test_extract_pokemon_info_partial_description():
    text = "Name: Pikachu Type: Electric Description: Pikachu"
    expected = PokemonInfo(name="Pikachu", type="Electric", description="Pikachu")
    assert extract_pokemon_info(text) == expected
