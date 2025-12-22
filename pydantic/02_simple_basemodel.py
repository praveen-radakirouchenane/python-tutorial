from pydantic import BaseModel

class ProductDetails(BaseModel):
    product_id: int
    product_name: str
    product_stock_availability: bool = True
    product_price: float


product_1 = ProductDetails(product_id=101, product_name="iPhone 12", product_stock_availability=True, product_price=1200)
product_2 = ProductDetails(product_id='102', product_name="iPhone 13", product_price=1000.00)