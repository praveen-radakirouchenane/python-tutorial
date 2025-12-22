from pydantic import BaseModel,computed_field, Field

class ProductInfo(BaseModel):
    product_price: float
    product_quantity: int


    @computed_field
    @property
    def total_price(self) -> float:
        return self.product_price * self.product_quantity
    

class HotelBooking(BaseModel):
    room_id: int
    hotel_id: int
    rate_per_night: int
    no_of_days_booking: int = Field(
        ...,
        ge=1
    )    

    @computed_field
    @property  
    def total_booking_price(self) -> int:
        return self.rate_per_night * self.no_of_days_booking

product_info = ProductInfo(
    product_price=1.0,
    product_quantity=5
)
print(f"Total price {product_info.total_price}")

booking = HotelBooking(
    room_id=1,
    hotel_id=2,
    rate_per_night=100,
    no_of_days_booking=5
)

print(f"Total Booking price {booking.total_booking_price}")
print("Model dump",booking.model_dump())