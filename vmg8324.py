# Default ESSID is ZyxelXXXXXX
# Zyxel VMG8324-B10A (long and short version)
import hashlib
import argparse

def vmg8324(serial, lng):

	junk = 'agnahaakeaksalmaltalvandanearmaskaspattbagbakbiebilbitblableblib'\
	'lyboabodbokbolbomborbrabrobrubudbuedaldamdegderdetdindisdraduedu'\
	'kdundypeggeieeikelgelvemueneengennertesseteettfeifemfilfinflofly'\
	'forfotfrafrifusfyrgengirglagregrogrygulhaihamhanhavheihelherhith'\
	'ivhoshovhuehukhunhushvaideildileinnionisejagjegjetjodjusjuvkaika'\
	'mkankarkleklikloknaknekokkorkrokrykulkunkurladlaglamlavletlimlin'\
	'livlomloslovluelunlurlutlydlynlyrlysmaimalmatmedmegmelmenmermilm'\
	'inmotmurmyemykmyrnamnednesnoknyenysoboobsoddodeoppordormoseospos'\
	'sostovnpaiparpekpenpepperpippopradrakramrarrasremrenrevrikrimrir'\
	'risrivromroprorrosrovrursagsaksalsausegseiselsensessilsinsivsjus'\
	'jyskiskoskysmisnesnusolsomsotspastistosumsussydsylsynsyvtaktalta'\
	'mtautidtietiltjatogtomtretuetunturukeullulvungurourtutevarvedveg'\
	'veivelvevvidvikvisvriyreyte'

	md5 = hashlib.md5()
	md5.update(serial.encode())

	p = ""
	summ = 0
	for b in md5.digest():
		d1 = hex(b)[2:].upper()
		if len(d1) == 1:
			d1 += d1
		p += d1
	summ = sum([ord(char) for char in p])
	i = summ % 265
	if summ & 1:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:]
	else:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:].upper()
	s2 = "%s%s%s%s%s%s%s" % (p[0], s1[0:2], p[1:3], s1[2:4], p[3:6], s1[4:6], p[6:])

	md52 = hashlib.md5()
	md52.update(s2.encode())
	hex_digest = ""
	for b in md52.digest():
		d2 = hex(b)[2:].upper()
		if len(d2) == 1:
			d2 += d2
		hex_digest += d2
	if lng:
		key = hex_digest[14:26]
	else:
		key = hex_digest[18:26]
	print(key)


parser = argparse.ArgumentParser(description='Zyxel VMG1312-B30B Keygen')
parser.add_argument('serial', help='Serial Number')
parser.add_argument("-long", help='Generates the long version of the password. Without this flag the script generates the short version.', required=False, action='store_true')
args = parser.parse_args()

vmg8324(args.serial, args.long)
