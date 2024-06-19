from datetime import datetime

def read_dates_from_file(file_path):
    dates = []
    with open(file_path, 'r') as file:
        for line in file:
            dates.append(line.strip())
    return dates

def compare_dates(dates):
    result = []
    for date_str in dates:
        # Parse the date
        date = datetime.strptime(date_str, "%Y,%m,%d")
        # Create the comparison date (July 1st of the same year)
        comparison_date = datetime(date.year, 7, 1)
        # Compare the dates
        if date < comparison_date:
            result.append("Antigüedad Enero")
        else:
            result.append("Antigüedad Julio")
    return result

def write_results_to_file(results, output_file_path):
    with open(output_file_path, 'w') as file:
        for result in results:
            file.write(result + '\n')

# Ejemplo de uso
input_file_path = r'C:\PRUEBAS\cv\fechas.txt'
output_file_path = r'C:\PRUEBAS\cv\resultados.txt'

# Leer las fechas del archivo
dates = read_dates_from_file(input_file_path)

# Comparar las fechas
comparisons = compare_dates(dates)

# Escribir los resultados en un nuevo archivo
write_results_to_file(comparisons, output_file_path)

print(f'Resultados escritos en {output_file_path}')
