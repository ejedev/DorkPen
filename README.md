# DorkPen 
A simple pentesting tool to find information and exposed files on a target website using google dorks.

This tool tests a variety of dorks to try and find relevant information for bug bounties and pentesting. It will print out findings along the way as it searches.

## Usage

Basic use with no verbose logging.

`python3 DorkPen.py --url google.com --resultcount 10 --wait 5`

Use `Dorkpen.py -h` to view the options.

```
usage: DorkPen.py [-h] --url URL --resultcount RESULTCOUNT --wait WAIT
                  [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             The URL to test (ex: google.com)
  --resultcount RESULTCOUNT
                        The maximum amount of results to try. Higher numbers
                        will impact performance
  --wait WAIT           The time to wait (in seconds) between requests. Use
                        higher numbers to avoid 429 timeouts.
  --verbose             Verbose testing
```

## Requirements

Python 3.x

Libraries found in requirements.txt

## Known issues

429 timeout from too many requests. Solution is to wait a bit. There is the potential to add proxy support in the future. You can also mitigate this by doing some of the following:

* Use a VPN
* Change the resultcount to ~5
* Increase the wait time to around 30-50 seconds. This will be slow but is almost guarenteed to work.

## Custom/new dorks

If you want to add new dorks in feel free to make a PR! Otherwise you could just edit the file yourself to add some custom ones in.

## Current tests

* Exposed Documents (doc, docx. odt, rtf, sxw, psw, ppt, pptx, pps, csv)
* Directory listing (Index of)
* Exposed Configuration File (xml, conf, cnf, reg, inf, rdp, cfg, txt, ora, ini, env)
* Exposed Database File (sql, dbf, mdb)
* Exposed Log File
* Backup Files (bkf, bkp, bak, old, backup)
* Login Pages
* SQL Issues
* PHP Issues
* ID =
* Exposed Repository - Domain (git, svn, gitlab)
* Exposed Repository - File (git, svn)

<a href="https://www.buymeacoffee.com/ejedev" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
