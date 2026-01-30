from wikibot import scrape

def test_weke():
    assert "Microsoft" in scrape("Microsoft")