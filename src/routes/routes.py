from src.controllers.controller import *

routes = {
    "index_route":"/","indexcontroller":IndexController.as_view("index"),    
    "delete_route":"/delete/produtos/<int:codigo>","delete_controller":DeleteProdutoController.as_view("delete"),    
    "update_route":"/update/produtos/<int:codigo>","update_controller":UpdateProdutoController.as_view("update"),    
    "categories_route":"/create/categorias","categories_controller":CategoriesController.as_view("categories"),    
    
}