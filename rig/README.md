+-------------+   +---------------+   +---------+
|    CPU      |<->|  Motherboard  |<->|   RAM   |
| (Threadripper|   | (ASUS WS C621E|   | (Corsair|
|     3990X)  |   |      SAGE)    |   | Vengeance|
+-------------+   +-------^-------+   +----^----+
      |                     |                |
+-----v------+   +----------v----------+   +--v---+
|   GPU1     |<->|   P2P NVMe SSD1    |<->| Long-|
| (NVIDIA    |   | (Samsung 980 PRO)  |   | Term |
|  A100)     |   +----------^----------+   |Storage|
+-----^------+              |              +-------+
      |            +-------v-------+
+-----v------+     |   P2P NVMe SSD2    |
|   GPU2     |<->| (Western Digital   |
| (NVIDIA    |   |  SN850)            |
|  A100)     |   +-------^-------+
+-----^------+           |
      |                 |
+-----v------+     +----v----+
|   GPU3     |<->|   GPU4    |
| (NVIDIA    |   | (NVIDIA   |
|  A100)     |   |  A100)    |
+-------------+   +----------+
      |
+-----v------+
|Power Supply|
| (EVGA      |
| SuperNOVA  |
|  1600 T2)  |
+-------------+
      |
+-----v------+
| Cooling    |
| System     |
| (Submer     |
| SmartPodX)  |
+-----^------+
      |
+-----v------+
|  Chassis   |
| (Rosewill 4U|
| Server     |
| Chassis)   |
+-------------+


1. **CPUs**: High-end CPUs like the AMD Ryzen Threadripper or Intel Xeon are popular choices.
   - AMD Ryzen Threadripper 3990X: 64-Core, 128-Thread, 2.9 GHz Base Clock, 4.3 GHz Max Boost Clock.
   - Intel Xeon W-2295: 18-Core, 36-Thread, 3.0 GHz Base Clock, 4.8 GHz Turbo Boost Clock.

2. **Motherboard**: The motherboard should have enough PCIe slots to accommodate at least four GPUs.
   - ASUS WS C621E SAGE: Supports dual Xeon processors, 7 PCIe x16 slots, up to 768GB ECC DDR4 2666MHz RAM.

3. **GPUs**: High-end GPUs such as NVIDIA's A100, RTX 3090, or RTX 3080.
   - NVIDIA A100: 6912 CUDA Cores, 40 GB or 80 GB HBM2e memory.
   - NVIDIA RTX 3090: 10496 CUDA Cores, 24GB GDDR6X memory.
   - NVIDIA RTX 3080: 8704 CUDA Cores, 10GB GDDR6X memory.

4. **RAM**: Depending on the size of your datasets, you may need a lot of RAM.
   - Corsair Vengeance LPX 128GB (4 x 32GB) DDR4 3200: CAS Latency 16, Voltage 1.35V.

5. **Primary Storage (NVMe with DMA)**: NVMe SSDs with PCIe Gen 4.0 interface would be ideal for high-speed data transfer.
   - Samsung 980 PRO: Up to 7,000 MB/s Read and 5,000 MB/s Write, PCIe 4.0 NVMe M.2 form factor.
   - WD Black SN850: Up to 7,000 MB/s Read and 5,300 MB/s Write, PCIe 4.0 NVMe M.2 form factor.

6. **Secondary Storage (High Volume Long Term Storage)**: For larger, less frequently accessed datasets, you could add a high-capacity HDD or SSD.
   - Seagate IronWolf 16TB: 7200 RPM, SATA 6Gb/s, 256MB cache.
   - Samsung 860 EVO 4TB: SATA III SSD, Up to 550 MB/s Read and 520 MB/s Write.

7. **Cooling System**: For immersion cooling, you would need a specially designed tank and coolant.
   - Submer SmartPodX: Supports up to 50 kW, Uses SmartCoolant (Dielectric Fluid).
   - Green Revolution Cooling CarnotJet System: Rack-based, uses ElectroSafe coolant (Dielectric Fluid).

8. **Power Supply**: With four GPUs and other high-end components, you'll need a powerful PSU.
   - EVGA SuperNOVA 1600 T2: 1600W, 80 PLUS Titanium efficiency, Fully Modular.
   - Corsair AX1600i: 1600W, 80 PLUS Titanium efficiency, Fully Modular.

9. **Chassis/Case**: The case should be big enough to fit all components, including the four GPUs.
   - Rosewill 4U Server Chassis: Supports up to 15 internal 3.5" drives, 7 expansion slots.

10. **Operating System and Software**:
    - Ubuntu 20.04 LTS: Free and open-source, wide support for deep learning libraries.
    - NVIDIA CUDA Toolkit: For GPU acceleration of

   - NVIDIA CUDA Toolkit 12.1.1: The latest version as of April 2023, essential for enabling GPU acceleration for deep learning workloads【8†source】.

11. **Other Software**:
    - Docker: Useful for creating reproducible environments.
    - Python 3.x: Most ML/DL libraries are written in Python.
    - PyTorch, TensorFlow, etc.: Choose depending on your specific requirements.

I see a few topology options, given:
1x 64 core epyc cpu
7x host pcie slots

option 1:
1x infiniband card
6x pcie switches
5+1 (5 gpus, 1 nvme) on 6 switches

option 2:
1x infiniband card
6x pcie switches
nvme is all on the first switch
6+0 gpus on the other 5 switches

option 3:
7x pcie switches
5+1 (5 gpus, 1 infiniband) on 6 switches
nvme all on the last switch (or you just jam all of your nvme into 16 lanes with bifurcation and don't use a switch for it)

option 4:
7x pcie switches
4+1+1 (4 gpus, 1 infiniband, nvme) on all switches
(this one is only 28 gpus)
you can also put the nvme on the network and add like 6 more gpus to each box instead