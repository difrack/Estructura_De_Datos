from metodos_ordenamiento import (
    burbuja,
    heapsort,
    insercion,
    quicksort,
    radix,
    seleccion,
    shellsort
)

arr = [ 40, 65, 84, 2, 87, 75, 22, 69]

print("\nOrdenamiento")
print(f"Original: {arr}")

print(f" burbuja: { burbuja(arr.copy())}")  
print(f"Inserción: {insercion(arr.copy())}")  
print(f"Selección: {seleccion(arr.copy())}") 
print(f"ShellSort: {shellsort(arr.copy())}")
print(f"Quicksort: {quicksort(arr.copy())}")  
print(f"Heapsort:  {heapsort(arr.copy())}") 
print(f"Radix:     {radix(arr.copy())}")      