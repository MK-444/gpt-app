from fastapi import FastAPI, HTTPException
from g4f.client import Client

from app.schemas.models import ChatRequest, ChatResponse
from app.api.logic import extract_pokemon_info

import asyncio
import logging


app = FastAPI()
client = Client()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": f"Information about a Pokémon in English in the following format: Name: <name>, Type: <type>, Description: <description>. Here is the query: {request.content}",
                    }
                ],
            ),
        )
        ai_response = response.choices[0].message.content
        logger.info(f"AI Response: {ai_response}")
        structured_data = extract_pokemon_info(ai_response)
        return ChatResponse(response=structured_data)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

