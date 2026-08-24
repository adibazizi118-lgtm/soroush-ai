from splusthon import SoroushClient, events

client = SoroushClient("soroush_assistant")


@client.on(events.NewMessage)
async def handler(event):
    text = event.raw_text.strip()

    if text == "/start":
        await event.reply(
            "سلام 👋\n"
            "به دستیار سروش خوش آمدی!\n\n"
            "/help - راهنما"
        )

    elif text == "/help":
        await event.reply(
            "📚 راهنما\n\n"
            "/start - شروع ربات\n"
            "/help - نمایش راهنما\n"
            "سلام - پاسخ سلام"
        )

    elif text == "سلام":
        await event.reply("سلام 👋 خوش اومدی!")


client.start()
client.run_until_disconnected()
