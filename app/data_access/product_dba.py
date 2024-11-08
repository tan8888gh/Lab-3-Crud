# import the model class
from app.models.product import Product
from starlette.config import Config
import httpx


# Load environment variables from .env
config = Config(".env")

# A dictionary for products
products_data = {}

# initialise with data from dummyjson
def dataInitDB() :

    # use global var
    global products_data

    # data already exists
    if (products_data) :
        return True

    # Get data
    response = httpx.get(config("PRODUCT_DATA_URL"))
    data = response.json()
    products_data = data['products']

    #print("data initialised: ", products_data)
    return True

# get all products
def dataGetProducts():
    global products_data
    # force init if first time
    check_data: bool = dataInitDB()
    return products_data

# get product by id
def dataGetProduct(id):
    return products_data[id-1]


def dataAddProduct(title,description,stock,price,thumbnail):
    global products_data

    new_id=len(products_data)+1
    new_product=Product(
        id=new_id,
        title=title,
        description= description,
        category= "",
        price= price,
        rating= 1.0,
        stock= stock,
        brand= "",
        sku= "",
        thumbnail= thumbnail
    )
    products_data.append(new_product)
    return new_product


def dataUpdateProduct(id, title, description,stock,price):
    for product in products_data:
        if product["id"] == id:
            old_thumbnail= product["thumbnail"]

    new_product=Product(
        id=id,
        title=title,
        description= description,
        category= "",
        price= price,
        rating= 1.0,
        stock= stock,
        brand= "",
        sku= "",
        thumbnail=old_thumbnail
    )
    products_data[id-1]=new_product
    return new_product

def dataDeleteTodo(id:int):
    for p in products_data:
        if p["id"] == id:
            products_data.remove(p)