# Linkedin-AutoApply
A small code snippet that I made in order to get a job.
The scraper searches only for "easy apply" jobs in a radius of 10 miles (16 km).
It may fail sometimes since in LinkedIn this feature isn't homogeneous between all job offers.

Requirements : selenium, Chromedriver stable release, a resume uploaded on LinkedIn as default.

HOW TO : 

Firstly, download scrape_linkedin.py.
Then, open a jupyter notebook instance in the same folder as scrape_linkedin.py and write in a cell (or put in a script in the same folder) the following :

from scrape_linkedin import scraper
scraper(mail, password, job, location) #replace the arguments



PS : Use it at your own risk, I am not responsible for any account ban from LinkedIn (even if that's not illegal, of course).

