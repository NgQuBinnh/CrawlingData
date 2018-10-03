from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem
class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["http://vbpl.vn"]
    start_urls = [
        "http://vbpl.vn/TW/Pages/vbpq-toanvan.aspx?ItemID=130179",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//*[@class="toanvancontent"]/p')
        print("Question Len = " , len(questions))
        result_string = ""
        for question in questions:
            item = StackItem()
            # item['textContent'] = question.xpath(u'//em/text()').extract().encode('utf-8').strip()
            # item['textContent'] = unicode(str(question.xpath(u'//em/text()').extract()), "utf-8")

            print(len(question.xpath('./text()').extract()))
            print(len(question.xpath('./em/text()').extract()))
            print(len(question.xpath('./strong/text()').extract()))

            for sentence in question.xpath('.//strong/text()').extract():
                print(str(sentence.encode('utf-8').strip()))
                result_string += str(sentence.encode('utf-8').strip())

            for sentence in question.xpath('.//em/text()').extract():
                print(str(sentence.encode('utf-8').strip()))
                result_string += str(sentence.encode('utf-8').strip())

            for sentence in question.xpath('.//text()').extract():
                print(str(sentence.encode('utf-8').strip()))
                result_string += str(sentence.encode('utf-8').strip())
            # print(result_string)
            print("---------------------")
            # print(question)
        item['textContent'] = result_string
        yield item