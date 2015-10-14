import scrapy

class AWSServiceHealth(scrapy.Spider):
    name = "aws"
    allowed_domains = ["status.aws.amazon.com"]
    start_urls = ["http://status.aws.amazon.com/#NA_block"]

#class AWSServiceHealth(scrapy.Spider):
#    name = "aws"
#    allowed_domains = ["status.aws.amazon.com"]
#    start_urls = [
#        "http://status.aws.amazon.com/rss/ec2-us-west-1.rss/",
#        "http://status.aws.amazon.com/"
#    ]


    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

