from .en import en

class Locale:
	data = {
		"en": en
	}

	@staticmethod
	def get(key, lang="en", **kwargs):
		text = Locale.data[lang][key].format(**kwargs)
		return text
