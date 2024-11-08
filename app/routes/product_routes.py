from fastapi import APIRouter,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services.product_service import getAllProducts,addProduct,updateProduct,getProduct,deleteProduct

router=APIRouter()

templates=Jinja2Templates(directory="app/view_templates")

@router.get("/product",response_class=HTMLResponse)
async def all_products(request:Request):
    return templates.TemplateResponse("product/products.html",{"request":request,"productList":getAllProducts()})

@router.get("/product/add-form",response_class=HTMLResponse)
async def get_add_form(request:Request):
    return templates.TemplateResponse("product/partials/product_add_form.html",{"request":request})

@router.post("/product/add",response_class=HTMLResponse)
async def add_product(request:Request,title:str=Form(...),
                      description:str=Form(...),
                      stock:int=Form(...),
                      price:int=Form(...),
                      thumbnail:str=Form(...)  
                      ):
    new_product=addProduct(title,description,stock,price,thumbnail)
    return templates.TemplateResponse("product/partials/product_tr.html",{"request":request,"product":new_product})

@router.get("/update/{id}", response_class=HTMLResponse)
async def product_byId(request: Request, id: int):
    return templates.TemplateResponse("product/partials/product_update_form.html", {"request": request, "product": getProduct(id) })

@router.put("/update/",response_class=HTMLResponse)
def update_item(request: Request, id: int=Form(...), 
                        title: str = Form(...),
                         description: str = Form(...),
                         stock: str = Form(...),
                         price: str = Form(...),
                         ):
    # get item value from the form POST data
    up_product = updateProduct(id, title, description,stock,price)
    return templates.TemplateResponse("product/partials/product_tr.html", {"request": request, "product": up_product})

@router.delete("/product/{id}")
def delete_item(request: Request, id: int):
    deleteProduct(id)
    return templates.TemplateResponse("product/partials/product_table.html", {"request": request, "productList": getAllProducts() })
