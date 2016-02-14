# Osu-Rank-Scraper

Note: This project is for educational purposes. Please don't actually use it without the permission of Dean Herbert (admin of osu.ppy.sh)

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
 Do the same thing with href=" and href="http://osu.ppy.sh  

Pasting Output Information to template.html
====================

Copy and paste everything in output.txt below the line that says  
"<!--PASTE OUTPUT INFORMATION HERE-->"  

Spacing does not matter. Save the html document and open it up with a web browser.

---

Created using Beautiful Soup http://www.crummy.com/software/BeautifulSoup/
