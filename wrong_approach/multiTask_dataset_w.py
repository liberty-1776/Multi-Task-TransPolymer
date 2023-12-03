import torch
from torch.utils.data import Dataset
import numpy as np

class MultiTask_Dataset_w(Dataset):
    def __init__(self, dataset):
        self.dataset = dataset
        

    def __len__(self):
        self.len = len(self.dataset)
        return self.len

    def __getitem__(self, i):
        data_row = self.dataset.iloc[i]

        Eea_fingerprints = data_row[5].replace('\n', '').replace('[', '').replace(']', '')
        Eea_fingerprints = Eea_fingerprints.split()
        Eea_fingerprints = np.array(Eea_fingerprints, dtype=np.float64)
        Eea_fingerprints = torch.tensor(Eea_fingerprints)

        Egb_fingerprints = data_row[6].replace('\n', '').replace('[', '').replace(']', '')
        Egb_fingerprints = Egb_fingerprints.split()
        Egb_fingerprints = np.array(Egb_fingerprints, dtype=np.float64)
        Egb_fingerprints = torch.tensor(Egb_fingerprints)

        Egc_fingerprints = data_row[7].replace('\n', '').replace('[', '').replace(']', '')
        Egc_fingerprints = Egc_fingerprints.split()
        Egc_fingerprints = np.array(Egc_fingerprints, dtype=np.float64)
        Egc_fingerprints = torch.tensor(Egc_fingerprints)

        Ei_fingerprints = data_row[8].replace('\n', '').replace('[', '').replace(']', '')
        Ei_fingerprints = Ei_fingerprints.split()
        Ei_fingerprints = np.array(Ei_fingerprints, dtype=np.float64)
        Ei_fingerprints = torch.tensor(Ei_fingerprints)

        props = []
        loss_mask = []

        for i in range(1,5):
            props.append(data_row[i])
            if(data_row[i]==-99):
                loss_mask.append(0)
            else:
                loss_mask.append(1)

        props = torch.tensor(props)
        loss_mask = torch.tensor(loss_mask)

        return dict(
            Eea_fingerprints = Eea_fingerprints,
            Egb_fingerprints = Egb_fingerprints,
            Egc_fingerprints = Egc_fingerprints,
            Ei_fingerprints = Ei_fingerprints,
            props=props,
            loss_mask = loss_mask
        )