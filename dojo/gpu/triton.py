# Import the necessary modules
import torch
import triton
import triton.language as tl

@triton.jit
def add_kernel(
    x_ptr,  # Pointer to first input vector.
    y_ptr,  # Pointer to second input vector.
    output_ptr,  # Pointer to output vector.
    n_elements,  # Size of the vector.
    BLOCK_SIZE: tl.constexpr,  # Number of elements each program should process.
):
    """
    Triton kernel for performing vector addition.

    Parameters:
    x_ptr (torch.Tensor): Pointer to first input vector.
    y_ptr (torch.Tensor): Pointer to second input vector.
    output_ptr (torch.Tensor): Pointer to output vector.
    n_elements (int): Size of the vector.
    BLOCK_SIZE (int): Number of elements each program should process.
    """
    # Programs in Triton are identified by their program id.
    pid = tl.program_id(axis=0)  # We use a 1D launch grid so axis is 0.
    
    # Compute the start index of the block of data this program will handle.
    block_start = pid * BLOCK_SIZE
    offsets = block_start + tl.arange(0, BLOCK_SIZE)
    
    # Create a mask to guard memory operations against out-of-bounds accesses.
    mask = offsets < n_elements
    
    # Load x and y from DRAM, masking out any extra elements in case the input is not a
    # multiple of the block size.
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    
    # Perform the addition.
    output = x + y
    
    # Write x + y back to DRAM.
    tl.store(output_ptr + offsets, output, mask=mask)

def add(x: torch.Tensor, y: torch.Tensor):
    """
    Function to perform vector addition using the Triton kernel.

    Parameters:
    x (torch.Tensor): First input tensor.
    y (torch.Tensor): Second input tensor.

    Returns:
    torch.Tensor: The result of the addition.
    """
    # Preallocate the output tensor.
    output = torch.empty_like(x)
    assert x.is_cuda and y.is_cuda and output.is_cuda
    
    # Compute the number of elements.
    n_elements = output.numel()
    
    # The SPMD launch grid denotes the number of kernel instances that run in parallel.
    # It is analogous to CUDA launch grids. In this case, we use a 1D grid where the size is the number of blocks.
    grid = lambda meta: (triton.cdiv(n_elements, meta['BLOCK_SIZE']),)
    
    # Call the Triton kernel.
    add_kernel[grid](x, y, output, n_elements, BLOCK_SIZE=1024)
    
    # Return the output tensor. Note that the kernel is still running asynchronously at this point until
    # torch.cuda.synchronize() is called.
    return output

# Test the function with some data.
torch.manual_seed(0)
size = 98432
x = torch.rand(size, device='cuda')
y = torch.rand(size, device='cuda')
output_torch = x + y
output_triton = add(x, y)
print(output_torch)
print(output_triton)
print(
    f'The maximum difference between torch and triton is '
    f'{torch.max(torch.abs(output_torch - output_triton))}'
)
