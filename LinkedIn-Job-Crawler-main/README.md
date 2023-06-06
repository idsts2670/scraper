# LinkedIn-Job-Crawler
Selenium and Beautiful Soup Crawler for LinkedIn Jobs

1. (*Recommend*) create and run the virtual environment first
```
$conda create -n python39(any name for virtual env) python=3.9

For MacOS
$conda activate python39
For Windows
C:(**)>activate python39

For MacOS
$conda deactivate python39
For Windows
C:(**)>deactivate python39

```

2. Run
might need to do this
https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/
``` 
pip3 install -r requirement.txt
python3 -m pip install --user --upgrade --no-cache selenium
```

3. Enter the Linkedin Credentials in Config.yaml

4. Paste the LinkedIn Job Search URL and run the script. 
eg: https://www.linkedin.com/jobs/search/?currentJobId=3601815902&f_E=2%2C3&f_JT=F&f_SB2=2&f_T=340%2C370%2C29&f_WT=1%2C3&geoId=103644278&keywords=data%20analyst&location=United%20States&refresh=true&sortBy=R
eg: https://www.linkedin.com/jobs/search/?currentJobId=3354980118&f_E=2%2C3&f_JT=F&f_SB2=2&f_T=370%2C340%2C29%2C252%2C2625%2C26610%2C30217&f_WT=1%2C3&geoId=103644278&keywords=data%20analyst&location=United%20States&refresh=true&sortBy=R
eg: https://www.linkedin.com/jobs/search/?currentJobId=3606354915&f_E=2%2C3&f_I=6%2C96%2C3231&f_JT=F&f_SB2=3&f_WT=1%2C3&geoId=103644278&keywords=data%20scientist&location=United%20States&refresh=true&sortBy=R
```
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3569702242&f_TPR=r86400&geoId=103644278&keywords=software%20engineer&location=United%20States&refresh=true")
```


5. You can change the number of page to crawl in 

```
links = []
print('Links collecting now.')
try:
    for page in tqdm(range(2, 10)): 
```

6. At last
```
Python3 crawler.py
```

It takes around an hour to crawl through 700 unique job links 