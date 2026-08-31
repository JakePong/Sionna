import torch
print("PyTorch Version:", torch.__version__)
if torch.cuda.is_available():
    print("Compute Platform: CUDA/ROCm (GPU)")
    print("CUDA Version built with PyTorch:", torch.version.cuda)
    print("Device Name:", torch.cuda.get_device_name(0))
elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
    print("Compute Platform: MPS (Apple Silicon GPU)")
else:
    print("Compute Platform: CPU")