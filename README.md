# hackathon
hackathon- backend for parsing video

**Install**
* moviepy
* ImageMagic
* scipy
* numpy
* pyhon3

**Arguments**
* -file = Path to XML
* -e = edit
* -width = horizontal resolution
* -height = vertical resolution
* -outputDir = output dir
* -fps = fps
* -music = Path to music file

**Video edit**
Start with argument -e. Commands: 
* info
* quit
* deleteEntity entityId
* addEntity entityId value
* addEffect startTime zIndex entityId effectType duration
* deleteEffect effectId

**Run Example**
* go to src folder
* python3 Main.py -file=../presentation/iphonex.xml

**Sources**
* Source: bit.ly/unit-sources
# XML:
```
<channel>
	<item>		
		<description>Popis produktu</description>
		<image_link>Odkaz na hlavný obrázok(url/lokálne)</image_link>
		
		<image_alt>Ďalší obrázok</image_alt>
		n*
		
		<simple_text>Zopár viet o produkte</simple_text>
		n*
		
		<title>Názov produktu</title>
		<price>Cena</price>
		<category1>Kategória</category1>
		
		.
		.
		.
		
	</item>
	n*

</channel>
```
# JOZO CODE:
```
[Header]  - ( (Rozlisenie_sirka, Rozlisenie_vyska), Duration, FPS, )
[Assets]  - ( ("img1", asset.Image("img/02.jpg")), .... )
[Effects] - ( (Start_Time, Z-index, "ID", Effect_Fnce(params)), ... )
```