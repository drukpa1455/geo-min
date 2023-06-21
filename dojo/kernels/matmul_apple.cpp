void mmul_kernel<32u, 128u, 16u, 2u, 4u, 1u, 2u, 4u>(
    metal::array_ref<void MTLdevice*>, // Array reference of MTLdevice* pointers
    MPSNDArrayKernelParameters const MTLconstant*, // Constant pointer to MPSNDArrayKernelParameters
    float const MTLdevice*, // Constant pointer to float values stored in MTLdevice
    half const MTLdevice*, // Constant pointer to half values stored in MTLdevice
    short const MTLdevice*, // Constant pointer to short values stored in MTLdevice
    signed char const MTLdevice*, // Constant pointer to signed char values stored in MTLdevice
    float const, // Constant float value
    float const MTLdevice*, // Constant pointer to float values stored in MTLdevice
    half const MTLdevice, // Constant half value stored in MTLdevice
    short const, // Constant short value
    float MTLdevice*, // Pointer to float values stored in MTLdevice
    half MTLdevice*, // Pointer to half values stored in MTLdevice
    MPSMatrixBatchMulParameters const MTLconstant&, // Constant reference to MPSMatrixBatchMulParameters
    float MTLthreadgroup*, // Pointer to float values stored in MTLthreadgroup
    half MTLthreadgroup*, // Pointer to half values stored in MTLthreadgroup
    short MTLthreadgroup*, // Pointer to short values stored in MTLthreadgroup
    signed char MTLthreadgroup*, // Pointer to signed char values stored in MTLthreadgroup
    half MTLdevice*, // Pointer to half values stored in MTLdevice
    MPSMatrixBatchMulParameters const, // Constant MPSMatrixBatchMulParameters
    MPSMatrixBatchMulParameters const MTLconstant&, // Constant reference to MPSMatrixBatchMulParameters
    float MTLthreadgroup*, // Pointer to float values stored in MTLthreadgroup
    unsigned short __vector(3), // Vector of unsigned short values with 3 components
    unsigned short, // Unsigned short value
    unsigned short // Unsigned short value
)

/*
                                +-----------------------+
                                | mmul_kernel<32u,      |
                                | 128u, 16u, 2u, 4u,    |
                                | 1u, 2u, 4u>           |
                                +-----------+-----------+
                                            |
                                            |
                         +------------------+------------------+
                         |                                     |
                         |             +--------------+        |
                         |             | metal::array |        |
                         |             | _ref<void    |        |
                         |             | MTLdevice*>, |        |
                         |             +------+-------+        |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | MPSNDArrayKernelParameters    |           |                |
   | const MTLconstant*           |           |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | float             const MTLdevice*       |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | half              const MTLdevice*       |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | short             const MTLdevice*       |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | signed char       const MTLdevice*       |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | float             const                   |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | float             const MTLdevice*       |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | half              const MTLdevice        |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | short             const                   |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | float             MTLdevice*             |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | half              MTLdevice*             |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | MPSMatrixBatchMulParameters const         |                |
   | MTLconstant&                              |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | float             MTLthreadgroup*        |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | half              MTLthreadgroup*        |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | short             MTLthreadgroup*        |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | signed char       MTLthreadgroup*        |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | half              MTLdevice*             |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | MPSMatrixBatchMulParameters const         |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | MPSMatrixBatchMulParameters const         |                |
   | MTLconstant&                              |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | float             MTLthreadgroup*        |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | unsigned short __vector(3)               |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | unsigned short                            |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
   +---------------------+--------+           |                |
   | unsigned short                            |                |
   +---------------------+--------+           |                |
                         |                    |                |
                         |                    |                |
*/