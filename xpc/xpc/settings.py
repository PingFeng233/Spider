# -*- coding: utf-8 -*-

# Scrapy settings for xpc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xpc'

SPIDER_MODULES = ['xpc.spiders']
NEWSPIDER_MODULE = 'xpc.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_TIMEOUT = 10
PROXIES = [
 'http://140.143.191.23:8888',
 'http://119.29.232.28:8888',
 'http://47.94.224.142:8888',
 'http://114.115.177.177:8888',
 'http://120.78.87.54:8888',
 'http://39.106.221.44:8888',
 'http://47.93.46.116:8888',
 'http://47.106.122.223:8888',
 'http://47.98.145.32:7758',
 'http://119.23.202.213:8888',
 'http://39.106.188.152:8888',
 'http://101.200.41.219:8888',
 'http://120.78.83.72:8888',
 'http://119.23.14.126:8888',
 'http://47.98.154.208:8888 ',
 'http://39.105.1.144:8888',
 'http://39.107.237.192:8888',
 'http://47.98.137.76:8888',
 'http://101.201.239.150:8888',
 'http://47.106.107.122:8888',
 'http://47.98.101.162:8888',
 'http://120.78.83.168:8888',
 'http://47.106.119.52:8888',
 'http://39.106.149.13:8888',
 'http://47.106.107.93:8888',
 'http://39.108.114.12:8888',
 'http://39.105.0.112:8888',
]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'DNT': "1",
    'Host': "www.xinpianchang.com",
    'Upgrade-Insecure-Requests': "1",
    'Postman-Token': "382a0081-c800-9da9-54c7-0b887820f774"
    }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xpc.middlewares.XpcSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'xpc.middlewares.RandomProxyMiddleware': 749,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'xpc.pipelines.MysqlPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
