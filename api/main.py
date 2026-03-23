from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import order_details as order_details_controller
from .controllers import orders, recipes, resources, sandwiches
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order_db = orders.read_one(db=db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_db


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.update(db=db, order_id=order_id, order=order)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order_db


@app.delete("/orders/{order_id}", tags=["Orders"], status_code=204)
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order_db = orders.read_one(db=db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="Order not found")
    orders.delete(db=db, order_id=order_id)


@app.post("/resources/", response_model=schemas.Resource, tags=["resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Resource], tags=["resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db=db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource_db


@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.update(db=db, resource_id=resource_id, resource=resource)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource_db


@app.delete("/resources/{resource_id}", tags=["resources"], status_code=204)
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db=db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete(db=db, resource_id=resource_id)


@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db=db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich_db


@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["sandwiches"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.update(db=db, sandwich_id=sandwich_id, sandwich=sandwich)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich_db


@app.delete("/sandwiches/{sandwich_id}", tags=["sandwiches"], status_code=204)
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db=db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)


@app.post("/recipes/", response_model=schemas.Recipe, tags=["recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)


@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db=db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe_db


@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["recipes"])
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.update(db=db, recipe_id=recipe_id, recipe=recipe)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe_db


@app.delete("/recipes/{recipe_id}", tags=["recipes"], status_code=204)
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db=db, recipe_id=recipe_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.delete(db=db, recipe_id=recipe_id)


@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["order_details"])
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details_controller.create(db=db, order_details=order_detail)


@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["order_details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details_controller.read_all(db)


@app.get("/order_details/{order_details_id}", response_model=schemas.OrderDetail, tags=["order_details"])
def read_one_order_detail(order_details_id: int, db: Session = Depends(get_db)):
    order_detail_db = order_details_controller.read_one(db=db, order_details_id=order_details_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_detail_db


@app.put("/order_details/{order_details_id}", response_model=schemas.OrderDetail, tags=["order_details"])
def update_one_order_detail(order_details_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    order_detail_db = order_details_controller.update(
        db=db,
        order_details_id=order_details_id,
        order_details=order_detail
    )
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_detail_db


@app.delete("/order_details/{order_details_id}", tags=["order_details"], status_code=204)
def delete_one_order_detail(order_details_id: int, db: Session = Depends(get_db)):
    order_detail_db = order_details_controller.read_one(db=db, order_details_id=order_details_id)
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return order_details_controller.delete(db=db, order_details_id=order_details_id)



