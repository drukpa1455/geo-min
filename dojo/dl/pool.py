def _pool(self, k_:Tuple[int, ...], stride:Union[Tuple[int, ...], int]=1, dilation:Union[Tuple[int, ...], int]=1) -> Tensor:
    # Ensure tensor dimensions are compatible with the kernel size
    assert len(self.shape) >= len(k_), f"can't pool {self.shape} with {k_}"

    # Create stride and dilation pairs (ensure they match the kernel dimension)
    s_, d_ = make_pair(stride, len(k_)), make_pair(dilation, len(k_))
    assert len(k_) == len(s_) and len(k_) == len(d_), f"stride/dilation mismatch kernel:{k_} stride:{s_} dilation:{d_}"

    # Extract prefix dimensions (dims not involved in pooling)
    slc_prefix, prefix, i_ = [(0,x) for x in self.shape[0:-len(k_)]], self.shape[0:-len(k_)], self.shape[-len(k_):]

    # Check if stride is not equal to kernel size or dilation is not 1
    if any(k > s for k,s in zip(k_, s_)) or any(d != 1 for d in d_):
        # Calculate output shape after pooling and dilation size
        o_ = [(i - d * (k-1) - 1)//s + 1 for i,d,k,s in zip(i_, d_, k_, s_)]
        e_ = [math.ceil(k*(i+d) / i) for k,i,d in zip(k_, i_, d_)]  # expands such that we don't need padding

        # Reshape tensor for dilation and apply dilation
        xup = self.reshape(*prefix, *flatten((1,i) for i in i_)).expand(*prefix, *flatten((e,i) for e,i in zip(e_, i_))).reshape(*prefix, *[e*i for e,i in zip(e_, i_)])

        # Apply dilation by slicing
        xup = xup.slice(slc_prefix + [(0,k*(i+d)) for k,i,d in zip(k_, i_, d_)])
        xup = xup.reshape(*prefix, *flatten((k,i+d) for k,i,d in zip(k_, i_, d_)))
        xup = xup.slice(slc_prefix + flatten(((0,k), (0,o*s)) for k,o,s in zip(k_, o_, s_)))

        # Handle stride by reshaping and slicing
        xup = xup.reshape(*prefix, *flatten((k,o,s) for k,o,s in zip(k_, o_, s_)))
        xup = xup.slice(slc_prefix + flatten(((0,k), (0,o), (0,1)) for k,o in zip(k_, o_)))
        xup = xup.reshape(*prefix, *flatten((k,o) for k,o in zip(k_, o_)))

        # Permute to move reduce dimensions to the end
        return xup.permute(*range(len(prefix)), *[len(prefix)+i*2+1 for i in range(len(k_))], *[len(prefix)+i*2 for i in range(len(k_))])
    else:
        # Alternative implementation when stride equals the kernel size and dilation equals 1

        # Calculate output shape after pooling
        o_ = [(i+(s-k))//s for i,s,k in zip(i_, s_, k_)]
        xup = self.slice(slc_prefix + [(0,o*s) for o,s in zip(o_, s_)])
        xup = xup.reshape(*prefix, *flatten(((o, s) for o,s in zip(o_, s_))))
        xup = xup.slice(slc_prefix + flatten(((0,o), (0,k)) for o,k in zip(o_, k_)))

        # Permute to move reduce dimensions to the end
        return xup.permute(*range(len(prefix)), *[len(prefix)+i*2 for i in range(len(k_))], *[len(prefix)+i*2+1 for i in range(len(k_))])
