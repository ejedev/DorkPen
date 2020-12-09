# DorkPen
A simple pentesting tool to find information and exposed files on a target website using google dorks.

This tool tests a variety of dorks to try and find relevant information for bug bounties and pentesting.

## Usage

Basic use with no verbose logging.

`python3 DorkPen.py --url google.com --resultcount 10`

Use `Dorkpen.py -h` to view the options.

```
usage: DorkPen.py [-h] --url URL --resultcount RESULTCOUNT [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             The URL to test (ex: google.com)
  --resultcount RESULTCOUNT
                        The maximum amount of results to try. Higher numbers
                        will impact performance
  --verbose             Verbose testing
```

## Requirements

Python 3.x
Libraries found in requirements.txt

## Known issues

429 timeout from too many requests. Solution is to wait a bit. There is the potential to add proxy support in the future.

## Custom/new dorks

If you want to add new dorks in feel free to make a PR! Otherwise you could just edit the file yourself to add some custom ones in.
