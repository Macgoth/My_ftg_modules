from .. import loader, utils

class ModuleMod(loader.Module):
    "Описание"
    strings = {"name": "ContiMod"}

    async def conticmd(self, message):
        """Описание скрипта"""
        reply = await message.get_reply_message()
        user= await message.client.get_entity(int(reply.text.split('@')[1]))
        await message.reply("На сколько заражал:")
        await message.respond(f"{user.first_name} {user.last_name if user.last_name else ''}")