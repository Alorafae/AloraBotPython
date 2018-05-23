__module_name__ = "AloraBot"
__module_version__ = "0.2"
__module_description__ = "stop fucking breaking python"

import hexchat
import string

#twitchnotify username just subscribed!
#twitchontify username subscribed to channelname for x months in a row

#cdtimer = hexchat.hook_timer(15000)

def love2(word, word_eol, userdata):
	if word[1] == "!love" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		currchan.command("say nataH pteroHeart kylerLove niciL tiffsHnK")

def love(word, word_eol, userdata):
	hexchat.command("say nataH niciL pteroHeart kylerLove tkaoLUV sintLove hayliLove justcmeDonut potterLove beniLove cathRaver harveyLove relyksCreep fl0mHeart geersH sh0tsLove shroudH")

#hexchat.hook_command("love", love)
#hexchat.hook_print("Your Message", love2)
#hexchat.hook_print("Channel Message", love2)

#---------------------------
#
#BEGIN nata

def nata(word, word_eol, userdata):
	if word[1] == "!nata" and word[0] != "mhunt95":
		hexchat.command("me MAN nataDab DOES nataDab IT nataDab FEEL nataDab GOOD nataDab TO nataDab BE nataDab A nataDab NATAWHEE nataDab SUB")

hexchat.hook_print("Your Message", nata)
hexchat.hook_print("Channel Message", nata)

#END nata
#
#---------------------------

#---------------------------
#
#BEGIN nata

def ptero(word, word_eol, userdata):
	if word[1] == "!ptero" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#pterodactylsftw":
			currchan.command("me KNEES DACTYLS HEARTS pteroKnee pteroKnee pteroKnee pteroKnee pteroKnee pteroKnee pteroDactyl pteroDactyl pteroDactyl pteroDactyl pteroDactyl pteroDactyl pteroHeart pteroHeart pteroHeart pteroHeart pteroHeart pteroHeart")

hexchat.hook_print("Your Message", ptero)
hexchat.hook_print("Channel Message", ptero)

#END nata
#
#---------------------------

#---------------------------
#
#BEGIN nata sub

def natasub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#natawhee":
			currchan.command("me MAN nataWut DOES nataWut IT nataWut FEEL nataWut GOOD nataWut TO nataWut BE nataWut A nataWut NATAWHEE nataWut SUB")

#hexchat.hook_print("Channel Message", natasub)

#END nata sub
#
#---------------------------

#---------------------------
#
#BEGIN sh0ts channel sub

def sh0tssub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#sh0ts_tv":
			currchan.command("say Thanks for subscribing! Welcome to Sh0ts Dinomites! sh0tsLove sh0tsLove sh0tsLove sh0tsLove sh0tsLove sh0tsSellout sh0tsSellout sh0tsSellout sh0tsSellout sh0tsSellout")

#hexchat.hook_print("Channel Message", sh0tssub)

#END sh0ts channel sub
#
#---------------------------

#---------------------------
#
#BEGIN sykoyo channel sub TESTING FUNCTION

def sykosub(word, word_eol, userdata):
	if word[1].find("shroud") != -1:
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#sykoyo":
			currchan.command("say pteroGame pteroGame pteroGame")

hexchat.hook_print("Channel Message", sykosub)
hexchat.hook_print("Your Message", sykosub)

#END sykoyo channel sub
#
#---------------------------

#---------------------------
#
#BEGIN kyler channel sub

def kylersub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#kylerelizabeth":
			parsed = word[1].split()
			if word[1].find("months") != -1:
				currchan.command("me kylerLove kylerSteve kylerLove Thanks for subscribing for {0} months in a row, {1}! Welcome back to Kyler's pengiuns! kylerLove kylerSteve kylerLove".format(parsed[3], parsed[0]))
			else:
				currchan.command("me kylerLove kylerSteve kylerLove Thanks for subscribing {0}! Welcome to Kyler's pengiuns! kylerLove kylerSteve kylerLove".format(parsed[0]))

#hexchat.hook_print("Channel Message", kylersub)

#END kyler channel sub
#
#---------------------------


#---------------------------
#
#BEGIN cariboob

def caribou(word, word_eol, userdata):
	if word[1] == "!caribou" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		currchan.command("say caribou? caributt? cariboob? CARIBOOOOOOOOOOB")

hexchat.hook_print("Channel Message", caribou)
hexchat.hook_print("Your Message", caribou)

#END cariboob
#
#---------------------------

#---------------------------
#
#BEGIN cariboob

def moistboys(word, word_eol, userdata):
	if word[1] == "!mb" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		currchan.command("say M O I S T B O I S")

hexchat.hook_print("Channel Message", moistboys)
hexchat.hook_print("Your Message", moistboys)

#END cariboob
#
#---------------------------

def tree(word, word_eol, userdata):
	if word[1].find("alora") != -1 or word[1].find("Alora") != -1 or word[1].find("ALORA") != -1:
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#pterodactylsftw":
			currchan.command("say I am a tree.")

#hexchat.hook_print("Channel Msg Hilight", tree)
#hexchat.hook_print("Your Message", tree)

#---------------------------
#
#BEGIN cariboob

def butts(word, word_eol, userdata):
	if word[1].find("butts?") != -1:
		currchan = hexchat.get_context()
		currchan.command("say mine?")

hexchat.hook_print("Channel Message", butts)
#hexchat.hook_print("Your Message", caribou)

#END cariboob
#
#---------------------------

#---------------------------
#
#BEGIN cariboob

def hugs(word, word_eol, userdata):
	if word[1].find("hugs?") != -1:
		currchan = hexchat.get_context()
		currchan.command("say Winnie wants one niciL")

hexchat.hook_print("Channel Message", hugs)
#hexchat.hook_print("Your Message", caribou)

#END cariboob
#
#---------------------------

#---------------------------
#
#BEGIN cariboob

def bobs(word, word_eol, userdata):
	if word[1].find("bobs?") != -1 or word[1].find("boobs?") != -1:
		currchan = hexchat.get_context()
		currchan.command("say sheilas pteroKnee ?")

hexchat.hook_print("Channel Message", bobs)
#hexchat.hook_print("Your Message", caribou)


#END cariboob
#
#---------------------------

#---------------------------
#
#BEGIN shroudew

def shroudew(word, word_eol, userdata):
	if word[1].find("shroudH") != -1:
		return
	elif word[1].find("shroud?") != -1 or word[1].find("Shroud?") != -1 or word[1].find("shroud ") != -1:
			currchan = hexchat.get_context()
			if currchan.get_info("channel") == "#natawhee":
				currchan.command("say pteroGame pteroGame pteroGame")

#hexchat.hook_print("Channel Message", shroudew)
#hexchat.hook_print("Your Message", caribou)

#END shroudew
#
#---------------------------

#---------------------------
#
#BEGIN smooched

def smooched(word, word_eol, userdata):
	if word[1].find("gave sykoyo") != -1:
		currchan = hexchat.get_context()
		currchan.command("say niciGasm")

hexchat.hook_print("Channel Msg Hilight", smooched)
#hexchat.hook_print("Your Message", smooched)

#END smooched
#
#--------------------------

#---------------------------
#
#BEGIN roosloth

def rooroosloth(word, word_eol, userdata):
	if word[1] == "!roosloth" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		currchan.command("me MAN OSsloth DOES OSsloth IT OSsloth FEEL OSsloth GOOD OSsloth TO OSsloth SLOTH OSsloth LIKE OSsloth ROOROO")

hexchat.hook_print("Channel Message", rooroosloth)
hexchat.hook_print("Your Message", rooroosloth)

#END roosloth
#
#--------------------------

#---------------------------
#
#BEGIN issykobot

def issykobot(word, word_eol, userdata):
	if (word[1].find("Sykoyo") != -1) and word[1].find("bot") != -1: #"!botkoyo":
		currchan = hexchat.get_context()
		currchan.command("say Negative, I am a meat popsicle.")

#hexchat.hook_print("Channel Message", issykobot)
#hexchat.hook_print("Channel Msg Hilight", issykobot)
#hexchat.hook_print("Your Message", issykobot)

#END issykobot
#
#--------------------------

#---------------------------
#
#BEGIN issykobot

def slap(word, word_eol, userdata):
	if word[1].find("!slap") != -1:
		currchan = hexchat.get_context()
		parsed = word[1].split()
		currchan.command("me slaps {0} around a bit with a pteroWoke !".format(parsed[1]))

hexchat.hook_print("Channel Message", slap)
hexchat.hook_print("Channel Msg Hilight", slap)
hexchat.hook_print("Your Message", slap)

#END issykobot
#
#--------------------------

#---------------------------
#
#BEGIN crumpet boy

def lxa(word, word_eol, userdata):
	if word[1] == "!lxa":
		currchan = hexchat.get_context()
		currchan.command("say TheLxa the crumpet boyyyyyyyyyyyyyyyyy LxaCrumpet")

hexchat.hook_print("Channel Message", lxa)
hexchat.hook_print("Your Message", lxa)

#END crumpet boy
#
#---------------------------

#---------------------------
#
#BEGIN crumpet boy

def nomm(word, word_eol, userdata):
	if word[1] == "!nomm":
		currchan = hexchat.get_context()
		currchan.command("say nomm is a cutie c:")

hexchat.hook_print("Channel Message", nomm)
hexchat.hook_print("Your Message", nomm)

#END crumpet boy
#
#---------------------------

def battlewhisk(word, word_eol, userdata):
	if word[1] == "!battlewhisk":
		currchan = hexchat.get_context()
		currchan.command("say battlewhisk has a tiny penis kylerCreep")

hexchat.hook_print("Channel Message", battlewhisk)
hexchat.hook_print("Your Message", battlewhisk)

#battlewhisk

def totem(word, word_eol, userdata):
	if word[1] == "!totem":
		currchan = hexchat.get_context()
		currchan.command("say http://i.imgur.com/QnZ708J.png")

#hexchat.hook_print("Channel Message", totem)
#hexchat.hook_print("Your Message", totem)

def ears(word, word_eol, userdata):
	if word[1] == "!ears":
		currchan = hexchat.get_context()
		currchan.command("say pteroEw )))) NotLikeThis (((( pteroGame")

hexchat.hook_print("Channel Message", ears)
hexchat.hook_print("Your Message", ears)

#---------------------------
#
#BEGIN crumpet boy

def steve(word, word_eol, userdata):
	if word[1] == "!steve":
		currchan = hexchat.get_context()
		currchan.command("say 'Steve, finish' - Alora 2016")

hexchat.hook_print("Channel Message", steve)
hexchat.hook_print("Your Message", steve)

#END crumpet boy
#
#---------------------------

#---------------------------
#
#BEGIN crumpet boy

def bunnehsteve(word, word_eol, userdata):
	if word[1].find("kylerSteve") != -1 and word[0] == "bunnehhh":
		currchan = hexchat.get_context()
		currchan.command("say kylerSteve kylerSteve")

hexchat.hook_print("Channel Message", bunnehsteve)

#END crumpet boy
#
#---------------------------

#---------------------------
#
#BEGIN tiff channel sub

def tkaosub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#tkao94":
			parsed = word[1].split()
			if word[1].find("months") != -1:
				currchan.command("me tiffsLove tiffsGasm tiffsHey Thanks for subscribing for {0} months in a row, {1}! Welcome back to Tiffany's stream! tiffsHey tiffsGasm tiffsLove".format(parsed[3], parsed[0]))
			else:
				currchan.command("me tiffsLove tiffsGasm tiffsHey Thanks for subscribing {0}! Welcome to Tiffany's stream! tiffsHey tiffsGasm tiffsLove".format(parsed[0]))

hexchat.hook_print("Channel Message", tkaosub)

#END tiff channel sub
#
#---------------------------

#---------------------------
#
#BEGIN fl0m channel sub

def fl0msub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#fl0m":
			parsed = word[1].split()
			if word[1].find("months") != -1:
				currchan.command("me fl0mHeart fl0mHype fl0mFlock fl0mNoble Thanks for subscribing for {0} months in a row, {1}! Welcome back to fl0m's flock! fl0mNoble fl0mFlock fl0mHype fl0mHeart".format(parsed[3], parsed[0]))
			else:
				currchan.command("me fl0mHeart fl0mHype fl0mFlock fl0mNoble Thanks for subscribing {0}! Welcome to fl0m's flock! fl0mNoble fl0mFlock fl0mHype fl0mHeart".format(parsed[0]))

#hexchat.hook_print("Channel Message", fl0msub)

#END fl0m channel sub
#
#---------------------------

#---------------------------
#
#BEGIN shroud channel sub

def shroudsub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#shroud":
			parsed = word[1].split()
			if word[1].find("months") != -1:
				currchan.command("me shroudKenz shroudH shroudSellout shroudPigeon Thanks for subscribing for {0} months in a row, {1}! Welcome back to shroud's pigeons! shroudPigeon shroudSellout shroudH shroudKenz".format(parsed[3], parsed[0]))
			else:
				currchan.command("me shroudKenz shroudH shroudSellout shroudPigeon Thanks for subscribing {0}! Welcome to shroud's pigeons! shroudPigeon shroudSellout shroudH shroudKenz".format(parsed[0]))

#hexchat.hook_print("Channel Message", shroudsub)

#END shroud channel sub
#
#---------------------------

#---------------------------
#
#BEGIN emongg channel sub

def emonggsub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#emongg":
			parsed = word[1].split()
			if word[1].find("months") != -1:
				currchan.command("me emongHeart emongHeart emongHeart Thanks for subscribing for {0} months in a row, {1}! Welcome back to emongg's pugs! emongHeart emongHeart emongHeart".format(parsed[3], parsed[0]))
			else:
				currchan.command("me emongHeart emongHeart emongHeart Thanks for subscribing {0}! Welcome to emongg's pugs! emongHeart emongHeart emongHeart".format(parsed[0]))

#hexchat.hook_print("Channel Message", emonggsub)

#END emongg channel sub
#
#---------------------------

#---------------------------
#
#BEGIN virtus channel sub

def virtussub(word, word_eol, userdata):
	if word[1].find("subscribed") != -1 and word[0] == "twitchnotify":
		currchan = hexchat.get_context()
		if currchan.get_info("channel") == "#virtuslol":
			parsed = word[1].split()
			if word[1].find("months") != -1:
				currchan.command("me virtusGasm Thanks for subscribing for {0} months in a row, {1}! Welcome back to the Virty Virgins! virtusHype".format(parsed[3], parsed[0]))
			else:
				currchan.command("me virtusGasm Thanks for subscribing {0}! Welcome to the Virty Virgins! virtusHype".format(parsed[0]))

#hexchat.hook_print("Channel Message", virtussub)

#END virtus channel sub
#
#---------------------------

def banger(word, word_eol, userdata):
	if word[1] == "!banger" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		currchan.command("me ヽヽ༼༼ຈຈل͜ل͜ຈຈ༽༽ﾉﾉ SONG IS A mangoBANGER ヽヽ༼༼ຈຈل͜ل͜ຈຈ༽༽ﾉﾉ")

hexchat.hook_print("Your Message", banger)
hexchat.hook_print("Channel Message", banger)


#lets hope this fucking works LMAO

def bansexsite(word, word_eol, userdata):
	if word[1].find("SEX") != -1 and word[1].find("SITE") != -1 and word[1].find("►►►") != -1:
		currchan = hexchat.get_context()
		currchan.command("say .ban {0}".format(word[0]))

hexchat.hook_print("Channel Message", bansexsite)

def bansextest(word, word_eol, userdata):
	if word[1].find("BEST") != -1:
		currchan = hexchat.get_context()
		currchan.command("say .ban elena".format(word[0]))

#hexchat.hook_print("Channel Message", bansextest)
#hexchat.hook_print("Your Message", bansextest)

def doublept(word, word_eol, userdata):
	if word[1] == "!double" and word[0] != "mhunt95":
		currchan = hexchat.get_context()
		currchan.command("me Ｗａｎｎａ 　ｄｏｕｂｌｅ 　ｙｏｕｒ 　ｐｔｏｋｅｎｓ？  muhSmug")

hexchat.hook_print("Your Message", doublept)
hexchat.hook_print("Channel Message", doublept)

def hairpurge(word, word_eol, userdata):
	if word[1].find("chair") == -1 and word[1].find("hair") != -1 or word[1].find("HAIR") != -1 or word[1].find("Hair") != -1:
		currchan = hexchat.get_context()
		currchan.command("say .timeout {0} 1".format(word[0]))

#hexchat.hook_print("Channel Message", hairpurge)


def pterosmug(word, word_eol, userdata):
	if word[1] == "!smug":
		currchan = hexchat.get_context()
		currchan.command("say ptero1 ptero2")
		currchan.command("say ptero3 ptero4")

hexchat.hook_print("Channel Message", pterosmug)
hexchat.hook_print("Your Message", pterosmug)

def jakebest(word, word_eol, userdata):
	if word[1] == "!jake":
		currchan = hexchat.get_context()
		currchan.command("say He is Great Friend .. He is the funniest on twitch .. He is cute .. He his Faithfull .. He has a pretty GF .. He Must Be our Lord and Saviour Jake")

hexchat.hook_print("Channel Message", jakebest)
hexchat.hook_print("Your Message", jakebest)
