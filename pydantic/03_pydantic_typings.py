from pydantic import BaseModel
from typing import List, Dict, Optional

class ProductInfo(BaseModel):
    sku_id: Dict[str, int]
    quantity: int
    products: List[str]
    product_image: Optional[str] = None
   
product_info = ProductInfo(sku_id={'101':111,'102':112},quantity=3,products=['iPhone','Samsung Galaxy'])