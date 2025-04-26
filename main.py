import os

import httpx
import aiofiles
from dotenv import load_dotenv


class BunnyHop:
    load_dotenv()
    api_key = os.getenv("BUNNY_API_KEY")
    lib_id = os.getenv("BUNNY_LIB_ID")
    base_url = f"https://video.bunnycdn.com/library/{lib_id}/videos"
    headers = {"accept": "application/json", "AccessKey": api_key}

    async def __call__(self, title: str, filepath: str):
        async with httpx.AsyncClient() as client:
            resp = await client.post(self.base_url, headers=self.headers, json={"title": title})
            resp.raise_for_status()
            vid_id = resp.json()["guid"]
            upload_url = f"{self.base_url}/{vid_id}"
            async with aiofiles.open(filepath, "rb") as f:
                data = await f.read()
            resp = await client.put(upload_url, headers=self.headers, content=data)
            resp.raise_for_status()
            return vid_id
