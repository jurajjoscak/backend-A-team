import providad.assetsCollection
import providad.asset
import providad.asset_effects_Letters
import providad.asset_effects_Text
import providad.asset_effects_img
import random

class videoBase:
	def __init__(self, width, height, fps):
		self.width=width
		self.height=height
		self.fps=fps
		self.effects=list()
		self.assetsCollection=dict()

	def addAssetsCollection(self, assetsCollection):
		self.assetsCollection = assetsCollection

	def getHeader(self):
		return tuple(((self.width, self.height), 0, self.fps))

	def getDeclarations(self):
		declarations=list()
		assets = self.assetsCollection.getAssets()
		for actAsset in assets:
			declarations.append(tuple((actAsset,assets[actAsset])))

		return declarations

	def getEffects(self):
		return self.effects

	def generateDefaultEffects(self):

		#self.effects=list()
		#imageEffectArray=["imgFadeInOut", "imgSlide", "imgZoom", "imgSpiral"]
                                            #fontSize=60, txtcolor='red', bgcolor='transparent', font='Amiri-Bold'
		self.appendEffect(0.5, 2, "mainText", providad.asset_effects_Letters.LetterCascadeFromTop(5.0, bgcolor='transparent', txtcolor="black"))
		self.appendEffect(1, 1, "mainImage", providad.asset_effects_img.imgFadeInOut(4.0, 2.5))
		

		self.appendEffect(5, 2, "simpleText" + str(1), providad.asset_effects_Letters.LetterVortexIn(3.0, bgcolor='transparent', fontSize=50, percentageFromLeft=20, percentageFromTop=20))
		self.appendEffect(8, 2, "simpleText" + str(2), providad.asset_effects_Letters.LetterArriveFromBottom(4.0, bgcolor='transparent'))
		self.appendEffect(12, 2, "simpleText" + str(3), providad.asset_effects_Text.TextMove_From_RD_To_LU(4.0,100,100,bgcolor='transparent', txtcolor="green", font="Amiri-Bold"))
		self.appendEffect(16, 2, "simpleText" + str(4), providad.asset_effects_Letters.LetterCascadeFromRight(3.0, bgcolor='transparent',fontSize=100))
		self.appendEffect(24, 2, "simpleText" + str(5), providad.asset_effects_Text.TextsShowWords(5, bgcolor='transparent', fontSize=80))

		self.appendEffect(5, 1, "simpleImage" + str(1), providad.asset_effects_img.imgSlide(500,400))
		self.appendEffect(7, 1, "simpleImage" + str(2), providad.asset_effects_img.imgZoom(5,1.5))
		self.appendEffect(12, 1, "simpleImage" + str(3), providad.asset_effects_img.imgSpiral(4,10))
		self.appendEffect(16, 1, "simpleImage" + str(4), providad.asset_effects_img.imgSlide(300,300))
		self.appendEffect(19, 1, "simpleImage" + str(5), providad.asset_effects_img.imgZoom(4,2))

		#for i in range(self.assetsCollection.nSimpleTexts):
		#	self.appendEffect(0.5, 1, "simpleText" + str(i), "konktretnyEfekt")

	def appendEffect(self, time, zIndex, assetId, effect):
		self.effects.append((time, zIndex, assetId, effect));

	def deleteEffect(self, index):
		del self.effects[index]

	def editEffect(self, index, tupleIndex, value):
		myTuple = self.effects[index]
		myList = list(myTuple)
		myList[tupleIndex] = value
		myList[tupleIndex] = value
		t = tuple(myList)
		self.effects[index] = t

	def appendAsset(self, assetType, assetValue):
		if assetType == "mainImage" or assetType == "simpleImage":
			assetToInsert = providad.asset.aImage(assetValue)
		elif assetType == "mainText" or assetType == "description" or assetType == "simpleText" or assetType == "price" or assetType == "category":
			assetToInsert = providad.asset.aText(assetValue)
		else:
			return 0	

		self.assetsCollection.addAsset(assetType, assetValue)

	def deleteAsset(self, assetId):
		self.assetsCollection.deleteAsset(assetId)