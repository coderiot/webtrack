#!/usr/bin/env python
# encoding: utf-8

import lxml.etree
from lxml.builder import E

def build_rss(title, link, items):
    """ Create Simple RSS feed from a list of items.

    :items: list of items. An item is a dictionary with
            three attributes: title, link and description
    :returns: string that contains the rss feed

    """

    root = lxml.etree.Element('rss', version="2.0")
    channel = lxml.etree.SubElement(root, 'channel')
    channel.append(E.title(title))
    channel.append(E.link(link))

    for i in items:
        item = E.item(E.title(i['title']),
                      E.guid(i['guid']),
                      E.link(i['link']),
                      E.description(i['description']))
        channel.append(item)

    return root
