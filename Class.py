class Smartphone:
    def __init__(self, brand=None,model=None,storage=None,price=None):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}GB")
        print(f"Price: ${self.price}")

    def check_category(self):
        if self.price < 300:
            return "Budget Smartphone\n"
        elif self.price < 800:
            return "Mid-Range Smartphone\n"
        else:
            return "Premium Smartphone\n"

def main():
    smartphones = []
    n = int(input("Enter the number of smartphones: "))

    for i in range(n):
        print(f"\nEnter details for smartphone {i + 1}:")
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        storage = int(input("Enter storage capacity (in GB): "))
        price = float(input("Enter price (in $): "))

        phone = Smartphone(brand, model, storage, price)
        smartphones.append(phone)

    print("\nSmartphone Details: ")
    for phone in smartphones:
        phone.display_info()
        print(f"Category: {phone.check_category()}")

if __name__ == "__main__":
    main()
  
