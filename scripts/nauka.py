import requests

import lxml.html

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]


print(new_releases)

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')

print(titles)

prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

print(prices)

tags = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
total_tags = []
for tag in tags:
    total_tags.append(tag.text_content())

platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)