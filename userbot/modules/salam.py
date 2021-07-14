from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Assalamu'alaikum wr. wb.`")


@register(outgoing=True, pattern='^.hy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝘩𝘺 𝘮𝘢𝘯𝘪𝘴𝘬𝘶")


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝘈𝘴𝘴𝘢𝘭𝘢𝘮𝘶'𝘢𝘭𝘢𝘪𝘬𝘶𝘮 𝘴𝘢𝘺𝘢𝘯𝘨")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝘞𝘢𝘢𝘭𝘢𝘪𝘬𝘶𝘮𝘴𝘢𝘭𝘢𝘮 𝘣𝘳𝘢𝘥𝘴")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝘞𝘢𝘭𝘢𝘪𝘬𝘶𝘮𝘴𝘢𝘭𝘢𝘮 𝘮𝘢𝘯𝘪𝘴")


CMD_HELP.update({
    "salam":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.P` | `P` | `.hy` \
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.L` `L`\
\n↳ : Untuk Menjawab Salam."
})
