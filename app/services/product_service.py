from fastapi import Request
from app.data_access.product_dba import dataGetProducts,dataGetProduct,dataAddProduct,dataUpdateProduct,dataDeleteTodo
from app.models.product import Product
import json

# get list of products from data
def getAllProducts() :
    products = dataGetProducts()
    return products

def getProduct(id) :
    return dataGetProduct(id)

def addProduct(title,description,stock,price,thumbnail):
    return dataAddProduct(title,description,stock,price,thumbnail)

def updateProduct(id, title, description,stock,price):
    updated = dataUpdateProduct(id, title, description,stock,price)
    return updated

def deleteProduct(id:int):
    dataDeleteTodo(id)
