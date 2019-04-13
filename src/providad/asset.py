# Base class for all assets
class BaseAsset:
	def __init__(self):
		pass

class aImage(BaseAsset):
    def __init__(self, url=""):
        self.url = url

class aText(BaseAsset):
	def __init__(self, value=""):
		self.value=value