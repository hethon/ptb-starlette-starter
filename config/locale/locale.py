from .am import am
from .en import en
from .fr import fr


class Locale:
    data = {
        "en": en, 
        "am": am, 
        "fr": fr
    }

    @staticmethod
    def get(key, lang="en", **kwargs):
        text = Locale.data[lang][key].format(**kwargs)
        return text
