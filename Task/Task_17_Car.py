def make_car(manufacturer, model, **car_info):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in car_info.items():
        car[key] = value
    return car

def main():
    car = make_car('Ford', 'Outback', color='Blue', tow_package=True)
    print(car)

if __name__ == "__main__":
    main()
