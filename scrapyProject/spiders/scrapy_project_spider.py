# Spider file 
#


from scrapy import Spider
from scrapyProject.items import ScrapyprojectItem

class scrapyProjectSpider(Spider):
    
    name = 'scrapy_project_spider'
    allowed_domains = ['https://nigeria.opendataforafrica.org/']
    start_urls = ['https://nigeria.opendataforafrica.org/']
    
    def parse(self, response):
        
        return_url = []
        
        rows = response.xpath('//*[@class="governance"]/text()').extract()
        
        i=0
        
        for row in rows[1:]:
            return_urls.append('https://nigeria.opendataforafrica.org/apps/atlas/'+row)
            i=i+1
            
        for url in result_urls[:2]:
            yield Request(url=url, callback=self.parse_result_page)
            
     
    def parse_result_page(self, response):

        gdp = response.xpath('//*[@class="facts"]/ul[1]/li[6]/text()').extract()
        gdp_per_capital = response.xpath('//*[@class="facts"]/ul[1]/li[7]/text()').extract()
        unemployment = response.xpath('//*[@class="facts"]/ul[1]/li[8]/text()').extract()
        dollar_per_day = response.xpath('//*[@class="facts"]/ul[1]/li[9]/text()').extract()
        land_area = response.xpath('//*[@class="facts"]/ul[2]/li[1]/text()').extract()
        population = response.xpath('//*[@class="facts"]/ul[2]/li[2]/text()').extract()
        population_density = response.xpath('//*[@class="facts"]/ul[2]/li[3]/text()').extract()
        literacy_rate = response.xpath('//*[@class="facts"]/ul[2]/li[4]/text()').extract()
        early_marraige = response.xpath('//*[@class="facts"]/ul[2]/li[5]/text()').extract()
        
        
        item['gdp'] = gdp[1].rstrip()
        item['gdp_per_capital'] = gdp_per_capital[1].rstrip()
        item['unemployment_rate'] = unemployment[1].rstrip()
        item['dollar_per_day'] = dollar_per_day[1].rstrip()
        item['population'] = population[1].rstrip()
        item['population_density'] = population_density[1].rstrip()
        item['land_area'] = land_area[1].rstrip()
        item['early_marriages'] = early_marraige[1].rstrip()
        item['literacy_rate'] = literacy_rate[1].rstrip()
       
        