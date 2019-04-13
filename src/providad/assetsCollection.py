
#mainText, #mainImage, #description, #price, #category, #simpleText
class AssetsCollection:
	def __init__(self):
		self.nSimpleImages=0
		self.nSimpleTexts=0
		self.assets = dict()

	def addAsset(self, aType, asset):
		name = aType
		if aType == "simpleText" :
			self.nSimpleTexts += 1
			name = name + str(self.nSimpleTexts)
		if aType == "simpleImage" :
			self.nSimpleImages += 1
			name = name + str(self.nSimpleImages)

		self.assets[name] = asset

	def getAssets(self):
		return self.assets

	def getAsset(self, index):
		return self.assets[index]

	def deleteAsset(self, assetId):
		del self.assets[assetId]