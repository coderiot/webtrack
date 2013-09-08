#!/usr/bin/env python
# encoding: utf-8

from abc import ABCMeta, abstractmethod

import lxml.etree


class Guesser(object):
    __metaclass__ = ABCMeta
    NO_LINK = "http://"

    @abstractmethod
    def guess_title(self, elem):
        """@todo: Docstring for guess_title

        :elem: @todo
        :returns: @todo

        """
        pass

    @abstractmethod
    def guess_link(self, elem):
        """@todo: Docstring for guess_link

        :elem: @todo
        :returns: @todo

        """
        pass

    @abstractmethod
    def guess_guid(self, elem):
        """@todo: Docstring for guess_guid

        :elem: @todo
        :returns: @todo

        """
        pass

    @abstractmethod
    def guess_description(self, elem):
        """@todo: Docstring for guess_descritpio

        :elem: @todo
        :returns: @todo

        """
        pass


class SimpleGuesser(Guesser):
    def guess_title(self, elem):
        return elem.text_content().strip()[0:50]


    def guess_link(self, elem):
        try:
            # get first link of element as rss link
            links = [e for e, _, u, _ in elem.iterlinks()]
            link = links[0]
            item_link = link.attrib['href']
        except:
            item_link = Guesser.NO_LINK

        return item_link


    def guess_guid(self, elem):
        item_link = self.guess_link(elem)
        item_title = self.guess_title(elem)

        if item_link is not Guesser.NO_LINK:
            item_guid = item_link
        else:
            item_guid = item_title[0:25]

        return item_guid


    def guess_description(self, elem):
        return lxml.etree.tostring(elem)
