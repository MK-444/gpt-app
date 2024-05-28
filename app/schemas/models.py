from pydantic import BaseModel


class ChatRequest(BaseModel):
    content: str


class PokemonInfo(BaseModel):
    name: str
    type: str
    description: str


class ChatResponse(BaseModel):
    response: PokemonInfo
