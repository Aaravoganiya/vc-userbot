import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
SESSION = os.getenv("SESSION", "AQBsTDkATYi68eCqt2fa905pfWVR5YHUleIX0TgJSi1GLKazifn2o_h3Ur9pC1qPVomlGqXhYCmQszjWzQgXD-u7-c3K-Rj5U9oLWp35S8idgK-KKOaJ8eXz0lyN_Yf3ak_x5VU47rjW3uhydsHGU7o78_uqieoo3RYmtnjQI7zXERKvZAsEVrxFBE-y0aiYxBKVdNX3JxAqgG1Nsj012-cwgIrtitDmpVKCoMn_OHk7qUHeg5TQPMdvy8prDfwZd6u0VmWcDAoatNEqWLZt3EM7A4DImCjmZi8MMR5UiCj3IxzzFokyqufoBj_HhvtgtNI9X8pjAaEDSo5F-thB79r7I_U9IgAAAAEt6RM1AA") 
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="plugins"))
call_py = PyTgCalls(bot)
