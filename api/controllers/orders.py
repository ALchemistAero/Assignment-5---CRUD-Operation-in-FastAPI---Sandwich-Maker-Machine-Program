from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas


def create(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(
        customer_name=order.customer_name,
        description=order.description
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def read_all(db: Session):
    return db.query(models.Order).all()


def read_one(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def update(db: Session, order_id: int, order: schemas.OrderUpdate):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order is None:
        return None

    update_data = order.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order, key, value)

    db.commit()
    db.refresh(db_order)
    return db_order


def delete(db: Session, order_id: int):
    db_order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if db_order is None:
        return None

    db.delete(db_order)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
