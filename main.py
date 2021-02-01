import csv
import json
import os
import os.path

if __name__ == '__main__':

    def unique(in_data):
        output = []
        for x in in_data:
            if x not in output:
                output.append(x)
        return output


    my_cars = []
    header = ()
    cars_data = []
    print(os.getcwd())
    input_file = os.getcwd() + r'\homework_example.csv'

    with open(f'{input_file}') as csv_file:
        my_data = csv.reader(csv_file)

        for index, data in enumerate(my_data):
            if index == 0:
                header = (['index'] + data)
            else:
                cars_data.append([index] + data)

    my_cars = [{key: value for key, value in zip(header, element)} for element in cars_data]

    slow_cars = [x for x in my_cars if int(x.get(' hp', 0)) < 120]
    fast_cars = [x for x in my_cars if int(x.get(' hp', 0)) in range(120, 180)]
    sport_cars = [x for x in my_cars if int(x.get(' hp', 0)) >= 180]

    cheap_cars = [x for x in my_cars if int(x.get(' price', 0)) < 1000]
    medium_cars = [x for x in my_cars if int(x.get(' price', 0)) in range(1000, 5000)]
    expensive_cars = [x for x in my_cars if int(x.get(' price', 0)) >= 5000]

    out_names = ['slow_cars.json', 'fast_cars.json', 'sport_cars.json', 'cheap_cars.json', 'medium_cars.json',
                 'expensive_cars.json']
    out_data = [slow_cars, fast_cars, sport_cars, cheap_cars, medium_cars, expensive_cars]

    for y, f in zip(out_names, out_data):
        with open(y, 'w') as json_file:
            json_object = json.dumps(f)
            json_file.write(json_object)

    brands = []
    for car in my_cars:
        brands.append(car.get('brand', None))
        brands = unique(brands)
        brands.sort()

    brands_files = []
    os.makedirs(name='cars', exist_ok=True)
    old_path = os.getcwd()
    path = old_path + r'\cars'
    os.chdir(path)

    for x, z in zip(brands, my_cars):
        #z = [y for y in my_cars if y.get('brand', 0) == x]
        name = x + '.json'
        z = [k for k in my_cars if k.get('brand') == x]
        brands_files.append(name)
        print(x, z)
        with open(name, 'w') as json_file:
            json_object = json.dumps(z)
            json_file.write(json_object)

    for f in os.listdir():
        if f not in brands_files:
            os.remove(f)

    os.chdir(old_path)
