import requests
from .. import loader, utils


def register(cb):
    cb(WeatherMod())
    
class WeatherMod(loader.Module):
    """Погода с сайта wttr.in"""
    strings = {'name': 'Weather'}
    
    async def pwcmd(self, message):
        """"Кидает погоду картинкой.\nИспользование: .pw <город>; ничего."""
        args = utils.get_args_raw(message).replace(' ', '+')
        await message.edit("Узнаем погоду...")
        city = requests.get(f"https://wttr.in/{args if args != None else ''}.png").content
        await message.client.send_file(message.to_id, city)
        await message.delete()


    async def weathercmd(self, message):
        """Throws weather ascii-artom.\reusing the art: .weather <City>; Nothing."""
        city = utils.get_args_raw(message)
        await message.edit("Finding weather...")
        r = requests.get(f"https://wttr.in/{city if city != None else ''}?0?q?T&lang=en")
        await message.edit(f"<code>City: {r.text}</code>")