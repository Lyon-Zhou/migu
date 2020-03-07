# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MigupachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    areaId = scrapy.Field()
    catId = scrapy.Field()
    catName = scrapy.Field()
    cateHref = scrapy.Field()
    catePath = scrapy.Field()
    count = scrapy.Field()
    createTime = scrapy.Field()
    publicTime = scrapy.Field()
    sort = scrapy.Field()
    type = scrapy.Field()
    updateTime = scrapy.Field()
    userId = scrapy.Field()

class BOOKItem(scrapy.Item):
    authorName = scrapy.Field()
    brandId = scrapy.Field()
    brandName = scrapy.Field()
    brandNickName = scrapy.Field()
    catId = scrapy.Field()
    defaultInfo = scrapy.Field()
    goodsId = scrapy.Field()
    goodsImg = scrapy.Field()

    # goodsInfo = scrapy.Field()
    g_goodsId = scrapy.Field()
    g_goodsInfoId = scrapy.Field()
    g_goodsInfoNo = scrapy.Field()
    g_marketPrice = scrapy.Field()
    g_originalPrice = scrapy.Field()
    g_tagPrice = scrapy.Field()
    g_wareStock = scrapy.Field()
    
    goodsName = scrapy.Field()
    goodsStock = scrapy.Field()
    goodsSubTitle = scrapy.Field()
    goodsTypeId = scrapy.Field()   
    goodsTypeName = scrapy.Field()
    goodsTypeNickName = scrapy.Field()
    highValue = scrapy.Field()
    image = scrapy.Field()
    images = scrapy.Field()

    keywords = scrapy.Field()
    marketPrice = scrapy.Field()
    marketingId = scrapy.Field()
    onShelfStatus = scrapy.Field()   
    pictureProviderList = scrapy.Field()
    sort = scrapy.Field()
    tagPrice = scrapy.Field()

