# BunnyHop: Async Video Uploader for Bunny CDN (bunny.net)

A minimalist Python utility for asynchronously uploading videos to Bunny CDN using the Bunny Stream API. Leverages `httpx` and `aiofiles` for non-blocking HTTP requests and file I/O.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Batch Example](#batch-example)
- [License](#license)

---

## Features

- **Async-first**: Uses `httpx.AsyncClient` and `aiofiles` for fully asynchronous uploads.
- **Simple API**: Wraps Bunny CDN video creation and upload in a single callable class.
- **Error Handling**: Raises on non-2xx responses to fail fast.

---

## Prerequisites

- Python 3.8 or higher (3.12 recommended)
- Bunny CDN Video Library credentials (API key and Library ID)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/siliconsociety/BunnyHop.git
   cd BunnyHop
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```

3. Install dependencies:
    ```bash
    ./install.sh
    ```
    Alternatively:
    ```bash
    pip install -r requirements.txt
    ```
---

## Configuration

Create a `.env` file in the project root with your Bunny CDN credentials:

```env
BUNNY_API_KEY=your_bunny_api_key_here
BUNNY_LIB_ID=your_bunny_library_id_here
```

The script will load these automatically via `python-dotenv`.

---

## Usage

Import and use the `BunnyHop` class for uploading videos:

```python
import asyncio
from main import BunnyHop

async def main():
    bunny = BunnyHop()
    video_id = await bunny(
        title="My Test Video",
        filepath="videos/movie.mp4"
    )
    print(f"Video uploaded, ID: {video_id}")

asyncio.run(main())
```

---

## Batch Example

Upload multiple files concurrently:

```python
import asyncio
from main import BunnyHop

async def batch_upload():
    bunny = BunnyHop()
    tasks = [
        bunny(title=f"Video {i}", filepath=f"videos/movie_{i}.mp4")
        for i in range(5)
    ]
    results = await asyncio.gather(*tasks)
    print("Uploaded video IDs:", results)

asyncio.run(batch_upload())
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
