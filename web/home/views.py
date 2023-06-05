from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

products = {"products":[
    {
        "id": "1",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Industrial",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "2",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Industrial",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "3",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Industrial",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "4",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Industrial",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "5",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Industrial",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "5",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Baby",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "5",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Baby",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
    {
        "id": "5",
        "title": "Amazon Basics 2-Ply Paper Towels, Flex-Sheets, 150 Sheets per Roll, 12 Rolls (2 Packs of 6), White (Previously Solimo)",
        "asin": "B09BWFX1L6",
        "brand": "Amazon Basics",
        "stars": "4.2",
        "reviewCount": "42,115",
        "thumbnailImage": "https://m.media-amazon.com/images/I/61POocZniqL.__AC_SX300_SY300_QL70_FMwebp_.jpg",
        "Category": "Baby",
        "description": " Amazon Basics paper towels include 12 rolls with 150 2-ply sheets per roll, 1,800 total sheets Amazon Basics Towels lint less making them great for cleaning hard surfaces like mirrors, glass, and countertops",
        "price": {
            "value": "29.44",
            "currency": "USD",
        },
        "url": "admin",
},
]}

def getProductsFilter(req, products):
    category = req.GET.get('category')
    filtered_items = []
    print(category)
    if category:
        for item in products["products"]:
            print(item['Category']+"1")
            if item['Category'] == category:
                filtered_items.append(item)
        return filtered_items
    return products["products"]

def home(request):
    productsFilter = getProductsFilter(request, products)
    pagination = Paginator(productsFilter,4)
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
    return render(request, 'home.html', {"countProducts": count, "products":productsFilter, "productsList": productsList})
