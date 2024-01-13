import torch
def check_device():
    if torch.cuda.is_available():
        return "cuda"
    else:
        return "cpu"

