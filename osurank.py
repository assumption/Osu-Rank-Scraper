import requests
from bs4 import BeautifulSoup

output = open("output.txt", 'w')
index = 0
row = 1

for x in range(1, 201):
	print("Working on Page ", x)
	# paste the first page in between quotes and change the 'page=' to 'page=%d' at the end
	# for US players: https://osu.ppy.sh/p/pp/?c=US&m=0&s=3&o=1&f=&page=%d
	# for all players: https://osu.ppy.sh/p/pp/?m=0&s=3&o=1&f=&page=%d
	# you get the idea...
	site = requests.get("https://osu.ppy.sh/p/pp/?m=0&s=3&o=1&f=&page=%d" % x)
	soup = BeautifulSoup(site.content)

	soup.prettify()

	table = soup.find('table')

	links = table.findAll('a')

	tr = soup.findAll('tr')

	i = 0
	
	for link in links:
		i += 1
		print("Processing rank ", i)
		user = requests.get("https://osu.ppy.sh" + str(link['href']))
		soup2 = BeautifulSoup(user.content)
		mouse = soup2.findAll("div", { "class" : "playstyle mouse using" })
		tablet = soup2.findAll("div", { "class" : "playstyle tablet using" })
		keyboard = soup2.findAll("div", { "class" : "playstyle keyboard using" })
		touch = soup2.findAll("div", { "class" : "playstyle touch using" })
		# 'len(PLAY_STYLE) > 0' means search for this
		# 'len(PLAY_STYLE) == 0' means exclude this
		# for instance the following means search for mouse and keyboard, but exclude touch and tablet
		if len(mouse) > 0 and len(tablet) == 0 and len(keyboard) > 0 and len(touch) == 0:
			index += 1
			tds = tr[i].findAll("td")
			output.write("<tr class='row%dp'" % (row) + ">\n")
			if row == 1:
				row = 2
			else:
				row = 1
			output.write("<td>%d</td>\n" % (index))
			for td in tds:
				output.write(str(td) + "\n")
			output.write("</tr>\n")