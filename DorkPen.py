import googlesearch
import sys
import argparse

class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser()
parser.add_argument('--url',
                    help='The URL to test (ex: google.com)', required=True)
parser.add_argument('--resultcount',
                    help='The maximum amount of results to try. Higher numbers will impact performance', type=int, required=True)
parser.add_argument('--wait',
                    help='The time to wait (in seconds) between requests. Use higher numbers to avoid 429 timeouts.', type=int, required=True)
parser.add_argument('--verbose', action='store_true',
                    help='Verbose testing')
results = parser.parse_args()
print(colours.OKCYAN + "DorkPen v0.1 by ejedev\n" + colours.ENDC)

dorkDict = {"Exposed Documents": "ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv",
            "Directory Listing": "intitle:index.of",
            "Exposed Configuration File": "ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env | ext:htaccess",
            "Exposed Database File": "ext:sql | ext:dbf | ext:mdb",
            "Exposed Log File": "ext:log",
            "Backups": "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
            "Login page": " inurl:login | inurl:signin | intitle:Login | intitle:'sign in' | inurl:auth",
            "SQL Issues": "intext:'sql syntax near' | intext:'syntax error has occurred' | intext:'incorrect syntax near' | intext:'unexpected end of SQL command' | intext:'Warning: mysql_connect()' | intext:'Warning: mysql_query()' | intext:'Warning: pg_connect()'",
            "PHP Issues": "'PHP Parse error' | 'PHP Warning' | 'PHP Error'",
            "ID =": "inurl:'id='",
            "Exposed Repository - Domain": "inurl:git | inurl:svn | inurl:gitlab"",
            "Exposed Repository - File": "ext:git | ext:svn",
            }

highSeverity = ['.conf', '.cnf', '.cfg', '.env', '.sql', '.dbf', '.mdb', '.log', '.bak', '.htaccess']

mediumSeverity = ['.txt', '.csv', 'admin', 'git', 'svn', 'ini']

testingUrl = str(results.url)
resultsnumber = int(results.resultcount)
verbose = results.verbose
waitTime = results.wait

print("Searching....\n")
try:
    for dork in dorkDict:
        if verbose == True:
            print("[Testing " + dork + "]")
        results = []
        finishedDork = "site:" + testingUrl + " " + dorkDict[dork]
        for x in googlesearch.search(finishedDork, lang='en', num=resultsnumber, start=0, stop=resultsnumber, pause=waitTime, user_agent=googlesearch.get_random_user_agent()):
            results.append(x)
        if len(results) > 0:
            print(colours.OKGREEN + "[" + dork + "]" + colours.ENDC)
            for x in results:
                if bool([ele for ele in highSeverity if(ele in x)]):
                    print(colours.FAIL + x + colours.ENDC)
                elif bool([ele for ele in mediumSeverity if(ele in x)]):
                    print(colours.WARNING + x + colours.ENDC)
                else:
                    print(x)
except Exception as e:
    print(e)
