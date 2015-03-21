#!/usr/bin/env python
# encoding: utf-8

import argparse
import urllib.request

import lxml.html

import webtrack.guess as guess
import webtrack.rss as rss


def make(url, selector, guesser=guess.SimpleGuesser(), limit=0):
    """Creating a RSS feed of HTML elements of a website using CSS3
       selectors.

    :url: url of website
    :selector: css3 selector of an element to keep track of
    :guesser: guessing the elements of rss item from the element of the website. Default class is SimpleGuesser.
    :limit: limit the feed item. Default is 0 for all items.
    :returns: formatted rss 2.0 feed of selected elements.

    """
    doc = lxml.html.parse(urllib.request.urlopen(url))
    root = doc.getroot()
    root.make_links_absolute()

    # find title for feed
    feed_title = doc.find('.//title').text

    elements = root.cssselect(selector)

    if limit > 0:
        elements = elements[0:limit]

    items = []
    for elem in elements:
        item = {}

        item['title'] = guesser.guess_title(elem)
        item['guid'] = guesser.guess_guid(elem)
        item['link'] = guesser.guess_link(elem)
        item['description'] = guesser.guess_description(elem)

        items.append(item)

    # reverse list to get the newest first
    items.reverse()

    feed = rss.build_rss(feed_title, url, items)

    return lxml.etree.tostring(feed,
                               pretty_print=True,
                               xml_declaration=True,
                               encoding='utf-8')


def main():
    parser = argparse.ArgumentParser("Create a RSS feed from every website.")

    parser.add_argument('url',
                        help="Site to create a feed from.")

    parser.add_argument('selector',
                        help="CSS3 Selector for HTML elments that gets updated.")

    parser.add_argument('--limit',
                        '-l',
                        help="Limit for number of items in feed.",
                        type=int,
                        default=0)

    args = parser.parse_args()

    print(make(args.url,
               args.selector,
               limit=args.limit,
               ))


if __name__ == '__main__':
    main()
