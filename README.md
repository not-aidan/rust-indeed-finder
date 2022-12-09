# Indeed.com Rust Job Finder
It is difficult to filter through 1000+ jobs (most of which aren't rust-related) when searching through Indeed.com even when using rust keywords.

This project webscrapes Indeed.com using selenium and analyzes which ones has rust keywords with beautiful soup.

I was considering using rust for this project but wanted to tap into python's ecosystem and didn't require complicated code.

## Usage
Commands:
`python3 scrape.py` scape data from Indeed.com.
`python3 analyze.py` extract and filter scraped job postings.

Scrape and export data into a file:
`python3 scrape.py && python3 analyze.py >> output.txt'
