
def write_data(data, path):
    f = open(path, "w")

    f.write("Label, EEG.Cz, EEG.Fz, EEG.Fp1, EEG.F7, EEG.F3, EEG.FC, EEG.C3, EEG.FC5, EEG.FT9, EEG.T7, EEG.CP5, EEG.CP1, EEG.P3, EEG.P7, EEG.PO9, EEG.O1, EEG.Pz, EEG.Oz, EEG.O2, EEG.PO10, EEG.P8, EEG.P4, EEG.CP2, EEG.CP6, EEG.T8, EEG.FT10, EEG.FC6, EEG.C4, EEG.FC2, EEG.F4, EEG.F8, EEG.Fp2,\n")
    for element in data:
        f.write(f"{element[1]}, ")
        for index, item in enumerate(element[0]):
            f.write(f"{item},")
        f.write("\n")
    f.close()
    