import asyncio
from main import BunnyHop


# Typical Usage
async def main():
    bunny = BunnyHop()
    video_id = await bunny(
        title="My Test Video",
        filepath="videos/movie.mp4"
    )
    print(f"Video uploaded, ID: {video_id}")


asyncio.run(main())


# Concurrent Batching
async def batch_upload():
    bunny = BunnyHop()
    tasks = (
        bunny(title=f"Video {i}", filepath=f"videos/movie_{i}.mp4")
        for i in range(5)
    )
    results = await asyncio.gather(*tasks)
    print("Uploaded video IDs:", results)

asyncio.run(batch_upload())
