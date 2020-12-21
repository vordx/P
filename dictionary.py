import json, requests
from .. import loader, utils


def register(cb):
    cb(DictionaryMod())

class DictionaryMod(loader.Module):
    """Dictionary."""
    strings = {'name': 'Dictionary'}

    async def meancmd(self, message):
        """Using: .mean <word>."""
        args = utils.get_args_raw(message)
        if not args:
            return await message.edit("<b>Can't find anything</b>")
        await message.edit('<b>Findin...</b>')
        lang = None
        alphabet = {"а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
                    "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"}
        for char in args:
            if char in alphabet:
                lang = 'ru'
            else:
                lang = 'en'
        r = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/{lang}/{args}')
        js = json.loads(r.text)
        df = ''
        try:
            for i in js[0]["meanings"][0]["definitions"]:
                try:
                    df += (f'{i["definition"]} ')
                except:
                    return
        except:
            await message.edit(f'◆ <b>{args}</b> - <i>Word not found.</i>')
            return
        ex = ''
        count = 0
        mess = (f'<b>{js[0]["word"]}</b>, <i>{js[0]["meanings"][0]["partOfSpeech"]}</i>.\n\n'
                f'◆ <b>Meaning:</b> <i>{df}</i>\n')
        try:
            for i in js[0]["meanings"][0]["definitions"]:
                count += 1
                ex += f'\n<b>{count})</b> <i>{i["example"]}</i>'
                alert = ''.join(ex)
        except:
           await message.edit(mess)
           return
        await message.edit(f'{mess}◆ <b>Examples:</b> {alert}')
