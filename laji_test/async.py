"""
@Time: 2023/11/24 16:19
@Author: WQ
@File: async.py
@Des:
"""

import asyncio
import httpx


async def main():
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'

    async with httpx.AsyncClient() as client:

        resp = await client.get(pokemon_url)

        pokemon = resp.json()
        print(pokemon['name'])

asyncio.run(main())
