#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod

import lxml.etree


class Guesser(object):
    """Class for guessing the parts of an RSS item from
       an given HTML element."""
    __metaclass__ = ABCMeta

    NO_LINK = "http://"

    @abstractmethod
    def guess_title(self, elem):
        pass

    @abstractmethod
    def guess_link(self, elem):
        pass

    @abstractmethod
    def guess_guid(self, elem):
        pass

    @abstractmethod
    def guess_description(self, elem):
        pass


class SimpleGuesser(Guesser):
    def guess_title(self, elem):
        """ Simply guess the first few characters from text content
            of the html element as title.

        :elem: etree element that should be an rss item
        :returns: title for the rss item

        """
        return elem.text_content().strip()[0:50]

    def guess_link(self, elem):
        """ Simply the first link in the html element.

        :elem: etree element that should be an rss item
        :returns: link for the rss item, if no link exitst return
                  a empty link: 'http://'

        """
        try:
            # get first link of element as rss link
            links = [e for e, _, u, _ in elem.iterlinks()]
            link = links[0]
            item_link = link.attrib['href']
        except:
            item_link = Guesser.NO_LINK

        return item_link

    def guess_guid(self, elem):
        """ The default guid is the link from guess_link(...).
            If no link exists the first few characters of the title
            represents the guid.

        :elem: etree element that should be an rss item
        :returns: link if exitst, else the prefix of the title

        """
        item_link = self.guess_link(elem)
        item_title = self.guess_title(elem)

        if item_link is not Guesser.NO_LINK:
            item_guid = item_link
        else:
            item_guid = item_title[0:25]

        return item_guid

    def guess_description(self, elem):
        """The whole element is the description.

        :elem: etree element that should be an rss item
        :returns: the whole etree element as a string

        """
        return lxml.etree.tostring(elem)
