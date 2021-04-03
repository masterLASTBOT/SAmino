from .Local import LocalClient
from .Global import GlobalClient
from .lib import objects, pack
from requests import get
from json import loads


try:
    __version__ = '1.1.3'
    __newest__ = loads(get("https://pypi.python.org/pypi/SAmino/json").text)["info"]["version"]
    if __version__ != __newest__:
        print(f"SAmino New Version!: {__newest__} (Your Using {__version__})")
except:
    pass
