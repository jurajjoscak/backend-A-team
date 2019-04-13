import providad
import providad.asset
import providad.AssetsGenerator
import providad.assetsCollection
import providad.parse_XML
import providad.videoBase
import providad.video_generator
import argparse
import sys
#Spustanie: python Main.py --file=../presentation/iphonex.xml

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("-file", help="XML file", required="true")
	parser.add_argument("-e", help="edit", action='store_true')
	parser.add_argument("-width", help="Video width", default="800")
	parser.add_argument("-height", help="Video height", default="600")
	parser.add_argument("-outputDir", help="output dictionary for example: ../video/", default="../video/")
	parser.add_argument("-fps", help="Video fps", default="30")
	parser.add_argument("-music", help="Music for video", default="music_1.mp3")

	args = parser.parse_args()

	xmlParser = providad.parse_XML.XmlProductParser(args.file);
	entities = xmlParser.parse_xml()

	for actEntity in entities:
		myAssetsGenerator = providad.AssetsGenerator.AssetsGenerator()
		assetsCollection = myAssetsGenerator.generateAssetsCollection(actEntity)

		videoBaseObj = providad.videoBase.videoBase(int(args.width), int(args.height), int(args.fps))

		videoBaseObj.addAssetsCollection(assetsCollection)
		videoBaseObj.generateDefaultEffects()

		#zatial bez osetrenia neplatnych vstupov
		if args.e:
			print ("Entity a efekty boli vygenerované")
			printActState(videoBaseObj)
			while True:
				x = input()
				if(x == "quit"):
					break

				commands = x.split(" ");
				if(commands[0] == "deleteEntity"):
					videoBaseObj.deleteAsset(commands[1])
					print("Entity was deleted")
				elif(commands[0] == "addEntity"):
					videoBaseObj.appendAsset(commands[1], commands[2])
					print("Entity was created")
				elif(commands[0] == "addEffect"):
					if(commands[4] == "TextMoveLeft"):
						videoBaseObj.appendEffect(float(commands[1]), int(commands[2]), commands[3], providad.asset_effects_Text.TextMoveLeftTest(commands[5]))
						print("Effect was created")
					else:
						print("Wrong effect. Available effects: TextMoveLeft")
				elif(commands[0] == "deleteEffect"):
					videoBaseObj.deleteEffect(int(commands[1]))
					print("Effect was deleted")
				#edit effect sa dorobi
				elif(commands[0] == "info"):
					printActState(videoBaseObj)


		providad.video_generator.create_video(videoBaseObj.getHeader(), videoBaseObj.getDeclarations(), videoBaseObj.getEffects(), args.outputDir + videoBaseObj.assetsCollection.getAsset("mainText").value.replace(" ", "_") + ".mp4", music=args.music)


def printActState(videoBaseObj):
	print("Zoznam entít: ")
	entities = videoBaseObj.assetsCollection.getAssets()
	for actEntity in entities:
		print(actEntity)
	print("Zoznam efektov: ")
	effects = videoBaseObj.getEffects()
	i=0
	for actEffect in effects:
		print(str(i) + ": " + actEffect[2] + ": začiatok-> " + str(actEffect[0]) + "s, zIndex-> " + str(actEffect[1]) + ", efekt-> " + actEffect[3].name())
		i = i+1
main()