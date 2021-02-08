import csv
import json
import os
import os.path

if __name__ == '__main__':

    my_cars = []
    header = ()
    cars_data = []

    with open('homework_example.csv') as csv_file:
        my_data = csv.reader(csv_file)
        for index, data in enumerate(my_data):
            if index == 0:
                data = [x.strip() for x in data]
                header = (['index'] + data)
            else:
                cars_data.append([index] + data)

    my_cars = [{key: value for key, value in zip(header, element)} for element in cars_data]

    if 'output_data' not in os.listdir():
        os.mkdir('output_data')

    slow_cars = [x for x in my_cars if int(x.get('hp', 0)) < 120]
    fast_cars = [x for x in my_cars if int(x.get('hp', 0)) in range(120, 180)]
    sport_cars = [x for x in my_cars if int(x.get('hp', 0)) >= 180]

    cheap_cars = [x for x in my_cars if int(x.get('price', 0)) < 1000]
    medium_cars = [x for x in my_cars if int(x.get('price', 0)) in range(1000, 5000)]
    expensive_cars = [x for x in my_cars if int(x.get('price', 0)) >= 5000]

    out_names = ['slow_cars.json', 'fast_cars.json', 'sport_cars.json', 'cheap_cars.json', 'medium_cars.json',
                 'expensive_cars.json']
    out_data = [slow_cars, fast_cars, sport_cars, cheap_cars, medium_cars, expensive_cars]

    for f in os.listdir('output_data'):
        if str(f).endswith('.json'):
            os.remove(os.path.join('output_data', f))

    for y, f in zip(out_names, out_data):
        with open(os.path.join('output_data', y), 'w') as json_file:
            json_object = json.dumps(f)
            json_file.write(json_object)

    brands = []
    for car in my_cars:
        brands.append(car.get('brand', None))
        brands_s = {x for x in brands if x is not None}
        brands_files = []

        for x, z in zip(brands_s, my_cars):
            name = x + '.json'
            b_n = [k for k in my_cars if k.get('brand') == x]
            brands_files.append(name)

            with open(os.path.join('output_data', name), 'w') as json_file:
                json_object = json.dumps(b_n)
                json_file.write(json_object)
