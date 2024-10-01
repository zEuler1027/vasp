import os
import pandas as pd

def extract_forces_from_outcar(outcar_path):
    forces = []
    with open(outcar_path, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if 'POSITION' in line and 'TOTAL-FORCE' in line:
                for force_line in lines[i+2:]:
                    if force_line.strip() == '':
                        break
                    force_data = force_line.split()[3:6]
                    forces.append([float(f) for f in force_data])
                break
    return forces

def main(directory):
    all_forces = []
    for folder in os.listdir(directory):
        try:
            folder_path = os.path.join(directory, folder)
            outcar_path = os.path.join(folder_path, 'OUTCAR')
            if os.path.isfile(outcar_path):
                forces = extract_forces_from_outcar(outcar_path)
                for i, force in enumerate(forces[:-2]):
                    all_forces.append([folder, i] + force)
        except Exception as e:
            print(folder, e)

    df = pd.DataFrame(all_forces, columns=['Folder', 'Atom_Index', 'Force_X', 'Force_Y', 'Force_Z'])
    df.to_csv('force.csv', index=False)

if __name__ == "__main__":
    directory = '.'  # 设定当前目录为起始目录
    main(directory)
