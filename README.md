# Osu-Rank-Scraper

Python Version: 3

Script defaults to scraping Mouse + Keyboard users in the top 10,000 globally.  
Instructions on how to change what playstyle to look for and what country to scrape in is included in the script.  
This process will take anywhere from 1-3 hours since you're parsing html from 10,200 different webpages.  
You can stop the script early if you want once the script reaches your profile (as indicated by the current page and current user output in the command line interface)

Formatting Output Information
====================

(makes the final result more visually appealing)

Open up the output file (default is output.txt) with a text editor (notepad++, sublime text, etc.)  
Press Ctrl+f and replace all src=" with src="http:  
This is shown here: http://puu.sh/gmWPC/818ad277ab.png  
Do the same thing with href=" and href="http://osu.ppy.sh  
This is shown here: http://puu.sh/gmWZS/3c7c19bceb.png

Pasting Output Information to template.html
====================

Copy and paste everything in output.txt below the line that says  
"<!--PASTE OUTPUT INFORMATION HERE-->"  

Spacing does not matter. Save the html document and open it up with a web browser.

---

Created using Beautiful Soup http://www.crummy.com/software/BeautifulSoup/
