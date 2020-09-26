# Spider file 
#Authur : Harvey Imama
# Implements Scrapy Spider. Defines a crawler for nigeria.opendataforafrica.org
#


from scrapy import Spider
from scrapyProject.items import ScrapyprojectItem
from scrapy.http.request import Request

class scrapyProjectSpider(Spider):
    
    name = 'scrapy_project_spider'
    allowed_domains = ['nigeria.opendataforafrica.org']
    start_urls = ['https://nigeria.opendataforafrica.org']
    
    #Implementation of the parse method from scarpy Spider
    # Returns a request to a defined callback
    # Reeives an Xpath from the defined start_urls paramter of thsi class
    
    def parse(self, response):
        
        return_urls = []
        
        rows = response.xpath('//*[@class="governance"]/text()').extract()
        
        i=0
        
        for row in rows[1:]:
            return_urls.append('https://nigeria.opendataforafrica.org/apps/atlas/'+row.replace('FCT','Abuja').replace(' ','-'))
            i=i+1
       
        for nextUrl in return_urls:
            try:
                print('crawling '+nextUrl)
                yield Request(url=nextUrl, callback=self.parse_result_page)
            except Error:
                raise Error("Error Crawling url "+url )
     
    # callback listening for requests from teh parse method
    # Returns an Item to be written to file based on configuration 
    # Recives an xpath from initaing method
    def parse_result_page(self, response):

        try:
           
            gdp = response.xpath('//*[@class="facts"]/ul[1]/li[6]/text()').extract()
            gdp_per_capital = response.xpath('//*[@class="facts"]/ul[1]/li[7]/text()').extract()
            unemployment = response.xpath('//*[@class="facts"]/ul[1]/li[8]/text()').extract()
            dollar_per_day = response.xpath('//*[@class="facts"]/ul[1]/li[9]/text()').extract()
            land_area = response.xpath('//*[@class="facts"]/ul[2]/li[1]/text()').extract()
            population = response.xpath('//*[@class="facts"]/ul[2]/li[2]/text()').extract()
            population_density = response.xpath('//*[@class="facts"]/ul[2]/li[3]/text()').extract()
            literacy_rate = response.xpath('//*[@class="facts"]/ul[2]/li[4]/text()').extract()
            early_marraige = response.xpath('//*[@class="facts"]/ul[2]/li[5]/text()').extract()
        except Error:
            raise Error("Error finding Xpath " )
        
        try:
            item = ScrapyprojectItem()
            item['gdp'] = gdp[1].rstrip()
            item['gdp_per_capital'] = gdp_per_capital[1].rstrip()
            item['unemployment_rate'] = unemployment[1].rstrip()
            item['dollar_per_day'] = dollar_per_day[1].rstrip()
            item['population'] = population[1].rstrip()
            item['population_density'] = population_density[1].rstrip()
            item['land_area'] = land_area[1].rstrip()
            item['early_marriages'] = early_marraige[1].rstrip()
            item['literacy_rate'] = literacy_rate[1].rstrip()
        except:
            raise Error("Error loading patameters")
       
        yield item