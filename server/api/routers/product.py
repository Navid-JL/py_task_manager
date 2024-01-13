from api.models.product_schema import Product, DisplayProduct
from api.models.product_model import Product as ProductContext
from api.database import get_db
from fastapi import Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/")
async def create_product(request: Product, response: Response, db: Session = Depends(get_db)):
    new_product = ProductContext(
        name=request.name,
        description=request.description,
        price=request.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    response.status_code = status.HTTP_201_CREATED
    return request


@router.get("/", response_model=list[DisplayProduct])
async def get_products(db: Session = Depends(get_db)):
    products = db.query(ProductContext).all()
    if not products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Products not found")
    return products


@router.get("/{id}", response_model=DisplayProduct)
async def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(ProductContext).filter(ProductContext.id == id).first()
    return product


@router.put("/{id}")
async def update_product(id: int, request: Product, db: Session = Depends(get_db)):
    product = db.query(ProductContext).filter(ProductContext.id == id)
    if not product.first():
        pass
    else:
        product.update(request.model_dump())
        db.commit()
        return {"Product successfully updated"}


@router.delete("/{id}")
async def delete_product(id: int, db: Session = Depends(get_db)):
    product = db.query(ProductContext).filter(
        ProductContext.id == id).delete(synchronize_session=False)
    db.commit()
    return {"Entry deleted"}
