import providad
import providad.asset
import providad.assetsCollection

class AssetsGenerator:
	def __init__(self):
		pass

	def generateAssetsCollection(self, entity):
		assetsCollection = providad.assetsCollection.AssetsCollection()
		for actAsset in entity:
			if actAsset['type'] == "mainImage" or actAsset['type'] == "simpleImage":
				assetToInsert = providad.asset.aImage(actAsset['url'])
			elif actAsset['type'] == "mainText" or actAsset['type'] == "description" or actAsset['type'] == "simpleText" or actAsset['type'] == "price" or actAsset['type'] == "category":
				assetToInsert = providad.asset.aText(actAsset['value'])
			else:
				continue	

			assetsCollection.addAsset(actAsset['type'], assetToInsert)

		return assetsCollection