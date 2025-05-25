from ARISHFA_MUSIC.core.bot import ARISHFA
from ARISHFA_MUSIC.core.dir import dirr
from ARISHFA_MUSIC.core.git import git
from ARISHFA_MUSIC.core.userbot import Userbot
from ARISHFA_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ARISHFA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
