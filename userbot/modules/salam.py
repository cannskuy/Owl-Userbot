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


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐍𝐀𝐉𝐈𝐒 𝐊𝐍𝐓𝐋")

@register(outgoing=True, pattern='^C(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐊𝐈𝐑𝐀𝐈𝐍 𝐌𝐔𝐊𝐀𝐍𝐘𝐀 𝐀𝐉𝐀 𝐘𝐀𝐍𝐆 𝐒𝐀𝐌𝐏𝐀𝐇, 𝐄𝐇 𝐓𝐄𝐑𝐍𝐘𝐀𝐓𝐀 𝐆𝐂 𝐍𝐘𝐀 𝐉𝐔𝐆𝐀")

@register(outgoing=True, pattern='^Y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐒𝐔𝐊𝐀 𝐁𝐄𝐑𝐄𝐍𝐀𝐍𝐆 𝐘𝐀, 𝐏𝐀𝐍𝐓𝐄𝐒 𝐁𝐀𝐍𝐘𝐀𝐊 𝐆𝐀𝐘𝐀")

@register(outgoing=True, pattern='^HAHA(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐘𝐀𝐇𝐀𝐇𝐀𝐇𝐀𝐇𝐀 𝐖𝐀𝐇𝐘𝐎𝐄𝐄𝐄𝐄𝐄")

@register(outgoing=True, pattern='^Z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐆𝐀 𝐔𝐒𝐀𝐇 𝐍𝐈𝐍𝐆𝐆𝐈 𝐃𝐄𝐏𝐀𝐍 𝐆𝐔𝐀 𝐁𝐆, 𝐋𝐔 𝐁𝐔𝐊𝐀𝐍 𝐒𝐈𝐀𝐏𝐀 𝐒𝐈𝐀𝐏𝐀 𝐃𝐈𝐌𝐀𝐓𝐀 𝐆𝐔𝐀")


@register(outgoing=True, pattern='^B(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐁𝐀𝐂𝐎𝐓𝐓 𝐀𝐍𝐉𝐈𝐍𝐆𝐆")


@register(outgoing=True, pattern='^X(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐏𝐏 𝐀𝐉𝐀 𝐆𝐀 𝐀𝐃𝐀, 𝐀𝐏𝐀 𝐋𝐀𝐆𝐈 𝐌𝐀𝐒𝐀 𝐃𝐄𝐏𝐀𝐍 𝐔𝐏𝐒")


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
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.p` | `P` |\
\n↳ : Untuk Memberi salam.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.hy`\
\n↳ : untuk memanggil seseorang\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `HAHA`\
\n↳ : WAHYOEEEE\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `X`\
\n↳ : untuk mengejek PP\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `C`\
\n↳ : Hina gc + Muka\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Y`\
\n↳ : banyak gaya\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `B`\
\n↳ : Bacot gblk\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Z`\
\n↳ : COBA SENDIRI\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `G`\
\n↳ : Najis\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.l` | `L`\
\n↳ : Untuk Menjawab Salam."
})
