# -*- coding: utf-8 -*-
import scrapy
import json
from migupachong.items import MigupachongItem, BOOKItem

# catParentIds = ["5862","5880","5867","5864","5866","5855","5857","5861","5865","5869","5856","5860","5898","5868","5863","5858"]



class MIGUPACHONGSpider(scrapy.Spider):
    # 爬虫的名称
    name = 'migupachong_spider'
    # 爬虫允许抓取的域名
    allowed_domains = ['cmread.com']
    # 爬虫抓取数据地址,给调度器
    urls = ['http://migubookstore.cmread.com:8000/store-api/?method=core.biz.homepage.getCategoryListByType.query',"http://migubookstore.cmread.com:8000/store-api/?method=core.biz.homepage.getMoreListByHotwordsId.query"]

   
    def start_requests(self):
        headers = {
            'Content-Type': 'application/json;charset=utf-8',
            'Connection': 'Keep-Alive'    
        }
        data =  {
                "cateType":"2"
            }
                   
            # yield scrapy.FormRequest(url, method = 'POST', headers = headers, body=json.dumps(data), callback = self.parse_list, dont_filter = True)
        yield scrapy.Request(self.urls[0], method = 'POST', headers = headers, body=json.dumps(data), callback = self.category)

    
    def category(self, response):
        delimiter  = 500

        headers = {
            "hight": 548,
            "width": 320,
            "Content-Type": "application/json"
        }
        print ("获取分类列表和书目总数")
        # item = MigupachongItem() 
        res_json= json.loads(response.body.decode('utf-8'))
        res_data = res_json.get('result')
        print (len(res_data))


        for j in res_data:
            # item['areaId'] = j.get('areaId')
            # item['catId'] = j.get('catId')
            # item['catName'] = j.get('catName')
            # item['cateHref'] = j.get('cateHref')
            # item['catePath'] = j.get('catePath')
            # item['count'] = j.get('count')
            # item['createTime'] = j.get('createTime')
            # item['publicTime'] = j.get('publicTime')
            # item['sort'] = j.get('sort')
            # item['type'] = j.get('type')
            # item['updateTime'] = j.get('updateTime')
            # item['userId'] = j.get('userId')
            # yield item
            print (j)
            catId = j.get('catId')
            count = j.get('count')

            for i in range(0,int(count),int(delimiter)):
                data = {
                    "catParentId": catId,
                    "start": i,
                    "limit": delimiter,
                    # "brandId": "",
                    "sortByKey": "goodsSaleCount",
                    "sortType": "desc",
                    # "pageNum": ""
                } 

            # data = {
            #     "catParentId": "5880",
            #     "start": 200,
            #     "limit": "200",
            #     "brandId": 2402,
            #     "sortByKey": "goodsSaleCount",
            #     "sortType": "desc",
            #     "pageNum": ""
            # }
                print (data)
                # yield scrapy.FormRequest(url, method = 'POST', headers = headers, body=json.dumps(data), callback = self.parse_list, dont_filter = True)
                print ("------------------------------------------开始----------------------------------")
                yield scrapy.Request(self.urls[1], method = 'POST', headers = headers, body=json.dumps(data), callback = self.parse)

    
    def parse(self, response):
        print ("解析。。。。。。。。")
        print (response)
        res_json= json.loads(response.body.decode('utf-8'))
        print (res_json)
        item = BOOKItem()
        res = res_json.get('result')
        goodslist = res.get('goodsList')
        print (goodslist)
        if (goodslist==None):
            return
        print (len(goodslist))
        for i in goodslist:
            item['authorName'] = i.get('authorName')
            item['brandId'] = i.get('brandId')
            item['brandName'] = i.get('brandName')
            item['brandNickName'] = i.get('brandNickName')
            item['catId'] = i.get('catId')
            item['defaultInfo'] = i.get('defaultInfo')
            item['goodsId'] = i.get('goodsId')
            item['goodsImg'] = i.get('goodsImg')

            goodsInfo= i.get('goodsInfo')
            # goodsInfodetail = goodsInfo
            
            item['g_goodsId'] = goodsInfo[0].get('goodsInfoId')
            item['g_goodsInfoId'] = goodsInfo[0].get('goodsInfoId')
            item['g_goodsInfoNo'] = goodsInfo[0].get('goodsInfoNo')
            item['g_marketPrice'] = goodsInfo[0].get('marketPrice')
            item['g_originalPrice'] = goodsInfo[0].get('originalPrice')
            item['g_tagPrice'] = goodsInfo[0].get('tagPrice')
            item['g_wareStock'] = goodsInfo[0].get('wareStock')

            item['goodsName'] = i.get('goodsName')
            item['goodsStock'] = i.get('goodsStock')
            item['goodsSubTitle'] = i.get('goodsSubTitle')
            item['goodsTypeId'] = i.get('goodsTypeId')
            item['goodsTypeName'] = i.get('goodsTypeName')
            item['goodsTypeNickName'] = i.get('goodsTypeNickName')
            item['highValue'] = i.get('highValue')
            item['image'] = i.get('image')
            item['images'] = i.get('images')

            item['keywords'] = i.get('keywords')
            item['marketPrice'] = i.get('marketPrice')
            item['marketingId'] = i.get('marketingId')
            item['onShelfStatus'] = i.get('onShelfStatus')
            item['pictureProviderList'] = i.get('pictureProviderList')
            item['sort'] = i.get('sort')
            item['tagPrice'] = i.get('tagPrice')
            item['tagPrice'] = i.get('tagPrice')
            yield item