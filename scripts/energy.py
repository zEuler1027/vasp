from pymatgen.io.vasp.outputs import Outcar
import pandas as pd
import os

def main(dir):
    all_energies = []
    for folder in os.listdir(dir):
        try:
            folder_path = os.path.join(dir, folder)
            outcar_path = os.path.join(folder_path, 'OUTCAR')
            if os.path.isfile(outcar_path):
                outcar = Outcar(outcar_path)
                energy = outcar.final_energy
                all_energies.append([folder, energy])
        except Exception as e:
            print(folder, e)
    df = pd.DataFrame(all_energies, columns=['Folder', 'E'])
    df.to_csv('energy.csv', index=False)

if __name__ == "__main__":
    directory = '.'
    main(directory)
