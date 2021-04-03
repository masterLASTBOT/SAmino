from .Local import LocalClient
from .Global import GlobalClient
from .lib import objects, pack, headers
from requests import get
from json import loads


try:
    __version__ = '1.2.0'
    __newest__ = loads(get("https://pypi.python.org/pypi/SAmino/json").text)["info"]["version"]
    if __version__ != __newest__:
        print(f"\033[1;33mSAmino New Version!: {__newest__} (Your Using {__version__})\033[1;0m")
except:
    pass