# -*- coding:UTF-8 -*-
import url_manager
import html_downloader
import html_outputer
import html_parser
class SpiderMain(object):
    count = 1
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count ==100:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/link?url=iYGd6RePOS1xkyTpV0OoSrZ96YRjaPmaxxLgEH4yQFlepo11sn5g4E0oi6cu1hihq651LtUSr9ZVjIY4ePnPla'
    # root_url是百度百科python页面的链接
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
