
def calculate_total_sales():
    total_land = 80
    segments = 5
    land_per_segment = total_land / segments
   
    # Yields per acre (tonnes)
    tomato_yield_30 = 10
    tomato_yield_70 = 12
    potato_yield = 10
    cabbage_yield = 14
    sunflower_yield = 0.7
    sugarcane_yield = 45
   
    # Prices per kg (Rs.)
    tomato_price = 7
    potato_price = 20
    cabbage_price = 24
    sunflower_price = 200
    sugarcane_price = 4000  # Per tonne
   
    # Tomato calculations
    tomato_land = land_per_segment
    tomato_sales = ((0.3 * tomato_land * tomato_yield_30) + (0.7 * tomato_land * tomato_yield_70)) * 1000 * tomato_price
   
    # Other crops
    potato_sales = land_per_segment * potato_yield * 1000 * potato_price
    cabbage_sales = land_per_segment * cabbage_yield * 1000 * cabbage_price
    sunflower_sales = land_per_segment * sunflower_yield * 1000 * sunflower_price
    sugarcane_sales = land_per_segment * sugarcane_yield * sugarcane_price
   
    total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
    return total_sales, tomato_sales + potato_sales + cabbage_sales + sunflower_sales

def main():
    total_sales, chemical_free_sales = calculate_total_sales()
    print(f"Total sales from 80 acres: Rs. {total_sales:.2f}")
    print(f"Sales from chemical-free farming at 11 months: Rs. {chemical_free_sales:.2f}")