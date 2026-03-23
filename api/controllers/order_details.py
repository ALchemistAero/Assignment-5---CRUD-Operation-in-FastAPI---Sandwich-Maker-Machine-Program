from sqlalchemy.orm import Session
from fastapi import status, Response
from ..models import models, schemas


def create(db: Session, order_details: schemas.OrderDetailCreate):
    db_order_details = models.OrderDetail(
        order_id=order_details.order_id,
        sandwich_id=order_details.sandwich_id,
        amount=order_details.amount
    )
    db.add(db_order_details)
    db.commit()
    db.refresh(db_order_details)
    return db_order_details


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_details_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id).first()


def update(db: Session, order_details_id: int, order_details: schemas.OrderDetailUpdate):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id).first()
    if db_order_details is None:
        return None

    update_data = order_details.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_order_details, key, value)

    db.commit()
    db.refresh(db_order_details)
    return db_order_details


def delete(db: Session, order_details_id: int):
    db_order_details = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_details_id).first()
    if db_order_details is None:
        return None

    db.delete(db_order_details)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
