import os

os.system('cls' if os.name == 'nt' else 'clear')

from .domainfronting import domainfronting, domainfronting_handler
from .proxyrotator import proxyrotator
from .important import *
from .redsocks import *
from .psiphon import *
from .config import *
from .log import *

print(colors(''.join(open(real_path('/data/.0000001')).readlines())))