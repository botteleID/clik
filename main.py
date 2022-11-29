import os
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
    CallbackQuery,
)
from pyrogram import Client, filters
from pyrogram.errors import MessageNotModified
from dotenv import load_dotenv
from pyromod import listen 

load_dotenv()


Bot = Client(
    name="confess",
    bot_token=os.environ.get("BOT_TOKEN", "5910290961:AAGScXmdRpYOhvvJW18IA3ybg7aEchnQNjU"),
    api_id=int(os.environ.get("API_ID", "14962060")),  # type: ignore
    api_hash=os.environ.get("API_HASH", "b726ce690552a5707dd80294907f39e1"),
)
KR=-1001782660352
Start_text = """<i>Hallo! [Menfess 4Me](https://t.me/Menfess4Me_bot) akan membantumu untuk mengirimkan pesan secara anonim ke Grup,Silakan Klik tombol <b>🔰 Menu 🔰</b> Untuk Melakunkan Menfes.

Sebelum menggunakan silakan baca rules terlebih dahulu ya🥰</i>

<b>Butuh bantuan? Hubungi</b> @Chat4Robot"""
KONTOL = "https://telegra.ph/file/abeae27723ac7d7be7807.jpg"
HOME_TEXT = """
<b>📪 Confess - Untuk Confess.
🗣 Kritik - Untuk mengkritik admin.</b>
<i>Klik tombol dibawah sesuai yang kamu mau</i>
"""

@Bot.on_message(filters.command(["start"]))
async def start(_, update: Message):
    await update.reply_photo(
        photo=KONTOL,
        caption=Start_text,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⛔️ Rules", callback_data="rules"),
                    InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan"),
                ],
                [
                    InlineKeyboardButton("🔰 Menu 🔰", callback_data="home_ban"),
                ],
            ]
        )
    )
    
RULES_TEXT = """📢 Peraturan Menfess 4Me

1. dilarang dm berisikan hal yg mengundang war (bersifat menjatuhkan suatu fandom, grup, agama, suku maupun ras)
2. dilarang mengirim menfess yang memuat data pribadi secara terang-terangan sekalipun data pribadi sendiri seperti nomor hp
3. dilarang berjualan barang apapun

📢 Owner/Admin tidak akan ikut campur dan tau menau tentang menfess yang masuk serta tidak akan membeberkan siapa si pengirim menfess terkecuali kalau pengirim melanggar RULES yang sudah dibuat diatas dan akan mendapatkan kosekuensinya

•PELANGGARAN RINGAN AKAN DITEGUR
•PELANGGARAN BERAT AKAN DI POST DAN DI BLOK PERMANEN"""

@Bot.on_callback_query(filters.regex("rules"))
async def rulescb(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=RULES_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🔙 Back", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )  
PENJELASAN_TEXT = """
<b>Apa Itu Menfess ?</b>
<b>•</b> Menfess adalah singkatan dalam bahasa Inggris dari "mention confess" yang memiliki makna kurang lebih "surat kaleng" atau "pesan anonim".

<b>Apa Itu Kritik ?</b>
<b>•</b> Kritik itu adalah kecaman atau tanggapan, kadang-kadang disertai uraian dan pertimbangan baik buruk terhadap suatu hasil karya, pendapat, dan sebagainya.
"""
@Bot.on_callback_query(filters.regex("penjelasan"))
async def penjelasan(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=PENJELASAN_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🔙 Back", callback_data="cbstart"),
                           ],
                         ]
                       ),
                      )  
    
@Bot.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=Start_text,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("⛔️ Rules", callback_data="rules"),
                             InlineKeyboardButton("Penjelasan 📝", callback_data="penjelasan"),
                           ],
                           [
                             InlineKeyboardButton("🔰 Menu 🔰", callback_data="home_ban"),
                           ],
                         ]
                       ),
                      )
    
@Bot.on_callback_query(filters.regex("home_ban"))
async def home_ban(_, query: CallbackQuery):
  await query.message.delete()
  await Bot.send_photo(query.message.chat.id,
                       photo=KONTOL,
                       caption=HOME_TEXT,
                       reply_markup=InlineKeyboardMarkup(
                         [
                           [
                             InlineKeyboardButton("🗣 Kritik", callback_data="cbkritik"),
                             InlineKeyboardButton("Confess 📪", callback_data="cbconfess"),
                           ]
                         ]
                       ),
                      ) 
PVA=-1001782660352    
@Bot.on_callback_query(filters.regex("cbkritik"))
async def cbkritik(client, query: CallbackQuery):
  await query.message.delete()  
  user_id = query.from_user.id
  Tujuan = await client.ask(user_id, '🗣 <b>Silakan ketik apa yang kamu ingin sampaikan kepada admin.</b>', filters=filters.text, timeout=30)
  if "/" in Tujuan.text:
    kri = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketikan apa yang kamu ingin katakan kepada admin__')
  else:
    kri = Tujuan
  await client.send_message(PVA, f"from {query.from_user.mention}\nisi : {kri.text}")
  await client.send_message(query.from_user.id, "Kritik kamu telah terkirim")
    
LOG=-1001874589177
ADM=-1001622611890

@Bot.on_callback_query(filters.regex("cbconfess"))
async def cbconfess(client, query: CallbackQuery):
    await query.message.delete()  
    user_id = query.from_user.id
    nama = await client.ask(user_id, '🗣 <b>Ketik Nama kamu</b>\n\n<b>Informasi :</b> __Pakai nama kamu,Jika ingin privasi nama silakan gunakan /secret saja__', filters=filters.text, timeout=30)
    if "/" in nama.text:
        nama = "secret"
    else:
        nama = nama.text
    tujuan = await client.ask(user_id, '🗣 <b>Ketik Nama Crush kamu</b>\n\n<b>Informasi :</b> __Wajib pakai username/nama__', filters=filters.text, timeout=30)
    if "/" in tujuan.text:
        to = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketik nama crush kamu__', filters=filters.text, timeout=30)
        if "/" in to.text:
            return await client.send_message(user_id, 'Sepertinya anda masih bodoh, silakan bertanya kepada @Chat4Robot')
        else:
            to = to
    else:
        to = tujuan
    isi = await client.ask(user_id, f"🗣 <b>Ketik apa yang ingin kamu sampaikan kepada {to.text}</b>", filters=filters.text, timeout=30)
    if "/" in isi.text:
        confesss = await client.ask(user_id, '<b>⚠️ Terjadi kesalahan.</b>\n__Ketik apa yang kamu ingin sampaikan kepada crush__', filters=filters.text, timeout=30)

    else:
        confesss = isi
    report = await client.send_message(ADM, f"<b>Id :</b> <pre>{query.from_user.id}</pre>\n<b>Pesan :</b> <i>{confesss.text}</i>")

        confesss = isi
    report = await client.send_message(LOG, f"<b>From :</b> <i>{nama}</i>\n<b>To :</b> <i>{to.text}</i>\n<b>Isi :</b> <i>{confesss.text}</i>", disable_web_page_preview=True)
    await client.send_message(user_id, f"Terima kasih telah menggunakan bot ini, pesan Anda akan segera dikirim.", 
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➡ Lihat Pesan", url=f"https://t.me/c/1874589177/{report.id}")]]),
                              disable_web_page_preview=True,
                             )
    
    
Bot.run()

