from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from elasticsearch import Elasticsearch

from . import models

HOST = "https://localhost:9200"
ELASTIC_USER = "elastic"
# The password for the 'elastic' user generated by Elasticsearch
ELASTIC_PASSWORD = "4n=KTc8mxoKwp=UCKfw_"
# The path of ca certificates
CA_CERTS = r"D:/4T/cuoiky/elasticsearch-8.6.2/config/certs/http_ca.crt"
index_name = "product"
type_name = "_doc"
path = r"D:/4T/cuoiky/documents/"

# Create the client instance
es = Elasticsearch(
    hosts=HOST,
    ca_certs=CA_CERTS,
    http_auth=(ELASTIC_USER, ELASTIC_PASSWORD),
)

if not es.ping():
    raise ValueError("Connection failed")


def getProductsFilter(req, products):
    category = req.GET.get('category')
    min_price = req.GET.get('min_price')
    max_price = req.GET.get('max_price')
    stars = req.GET.get('stars')  # New line

    filtered_items = []

    if category:
        body = {
            "query": {
                "multi_match": {
                    "query": category,
                    "fields": "breadCrumbs",
                }
            }
        }
        filtered_items = [models.SearchResult(p['_source']) for p in
                          es.search(index=index_name, body=body)["hits"]["hits"]]
    else:
        filtered_items = products

    if min_price and max_price:
        filtered_items = [item for item in filtered_items if
                          float(min_price) <= float(item.get_price()) <= float(max_price)]
    elif min_price:
        filtered_items = [item for item in filtered_items if float(item.get_price()) >= float(min_price)]
    elif max_price:
        filtered_items = [item for item in filtered_items if float(item.get_price()) <= float(max_price)]

    # if search_query:
    #     filtered_items = [item for item in filtered_items if search_query.lower() in item['title'].lower()]

    if stars:  # New lines
        filtered_items = [item for item in filtered_items if float(item.get_stars()) <= float(stars)]

    return filtered_items


# def getProductsFilter(req, products):
#     category = req.GET.get('category')
#     filtered_items = []
#     print(category)
#     if category:
#         for item in products["products"]:
#             print(item['Category']+"1")
#             if item['Category'] == category:
#                 filtered_items.append(item)
#         return filtered_items
#     return products["products"]
def home(request):
    search_query = request.GET.get('search')
    if search_query:
        body = {
            "query": {
                "multi_match": {
                    "query": search_query,
                    "fields": ["brand", "title"],
                    "operator": "and"
                }
            }
        }
    else:
        body = {
            "query": {
                "match_all": {}
            }
        }
    products = [models.SearchResult(p['_source']) for p in es.search(index=index_name, body=body)["hits"]["hits"]]
    productsFilter = getProductsFilter(request, products)
    pagination = Paginator(productsFilter, 4)
    page_number = request.GET.get("page")

    try:
        productsList = pagination.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        productsList = pagination.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        productsList = pagination.page(pagination.num_pages)

    count = len(productsFilter)

    return render(request, 'home.html',
                  {"countProducts": count, "products": productsFilter, "productsList": productsList})
