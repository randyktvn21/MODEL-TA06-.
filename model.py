import numpy as np
import matplotlib.pyplot as plt

# Parameter berdasarkan perhitungan manual
T0 = 90      # suhu awal (°C)
Ta = 25      # suhu lingkungan (°C)
k = 0.05     # konstanta pendinginan (menit^-1)

# Waktu simulasi (0–60 menit)
t = np.linspace(0, 60, 200)

# Rumus teoritis Newton's Law of Cooling
T = Ta + (T0 - Ta) * np.exp(-k * t)

# Perhitungan manual untuk verifikasi (misal t=20)
t_manual = 20
T_manual = Ta + (T0 - Ta) * np.exp(-k * t_manual)
print(f"Suhu setelah 20 menit = {T_manual:.2f} °C")

# Plot hasil
plt.figure(figsize=(8,5))
plt.plot(t, T, 'b', linewidth=2, label='Simulasi Hukum Newton')
plt.axhline(y=Ta, color='r', linestyle='--', label='Suhu Lingkungan (25°C)')
plt.scatter([20], [T_manual], color='orange', label=f'T(20)= {T_manual:.1f}°C')

plt.title('Simulasi Pendinginan Air Panas Berdasarkan Hukum Newton')
plt.xlabel('Waktu (menit)')
plt.ylabel('Suhu Air (°C)')
plt.legend()
plt.grid(True)
plt.show()
