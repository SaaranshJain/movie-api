from dotenv import get_key
from typing import Literal

api_key = get_key("./.env", "KEY")


def make_url_by_title(i: str = None,
             t: str = None,
             type: Literal["movie", "series", "episode"] = None,
             y: int = None,
             plot: Literal["short", "full"] = None,
             r: Literal["json", "xml"] = None,
             callback: str = None,
             v: int = None) -> str:

    args = {"i": i, "t": t, "type": type, "y": y,
            "plot": plot, "r": r, "callback": callback, "v": v}

    url = f"http://www.omdbapi.com/?apikey={api_key}"

    for arg, val in args.items():
        if val:
            url += f"&{arg}={val}"

    return url

def make_url_by_search(s: str = None,
             page: int = None,
             type: Literal["movie", "series", "episode"] = None,
             y: int = None,
             plot: Literal["short", "full"] = None,
             r: Literal["json", "xml"] = None,
             callback: str = None,
             v: int = None) -> str:

    args = {"s": s, "page": page, "type": type, "y": y,
            "plot": plot, "r": r, "callback": callback, "v": v}

    url = f"http://www.omdbapi.com/?apikey={api_key}"

    for arg, val in args.items():
        if val:
            url += f"&{arg}={val}"

    return url
