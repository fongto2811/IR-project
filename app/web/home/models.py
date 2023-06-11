class SearchResult:
    def __init__(self, product):
        self.title = product['title']
        self.asin = product['asin']
        self.brand = product['brand']
        self.stars = float(product['stars'])
        self.reviewsCount = product['reviewsCount']
        self.thumbnailImage = product['thumbnailImage']
        self.breadCrumbs = product['breadCrumbs']
        self.description = product['description']
        self.price = product['price']
        self.url = product['url']

    def get_price(self):
        return self.price['value']

    def get_stars(self):
        return self.stars

# Create your models here.
