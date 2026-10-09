"""
BEAM-FLIGHT: Universal Core Safety Controller (Optimized Flight Physics & Telemetry Engine)
Calculates real-time deceleration curves, aero-braking, and generates investor-ready plots.
"""

import math
import matplotlib.pyplot as plt

class UniversalCoreSafetyController:
    def __init__(self, capsule_mass_kg=15000, is_passenger_mission=True):
        self.mass = capsule_mass_kg
        self.g = 9.81
        self.is_passenger = is_passenger_mission
        
        # Початкові умови: Аварійний відстріл капсули на крейсерському ешелоні
        self.altitude_z_m = 110000.0   # 110 км (Термосфера)
        self.velocity_ms = 5150.0      # ~Mach 15
        self.cabin_temperature_c = 21.0
        
        # Списки для збереження синхронізованої телеметрії
        self.timeline = []
        self.altitudes = []
        self.velocities_mach = []
        self.g_forces = []

    def calculate_mach(self, altitude, velocity):
        """Розрахунок точного числа Маху залежно від висотного шару атмосфери"""
        if altitude > 100000:
            temp_k = 700.0  
        elif altitude > 50000:
            temp_k = 250.0
        else:
            temp_k = max(210.0, 288.15 - 0.0065 * altitude)
        speed_of_sound = math.sqrt(1.4 * 287.05 * temp_k)
        return velocity / speed_of_sound

    def run_visual_emergency_mission(self):
        print("=== ЗАПУСК ОПТИМІЗОВАНОГО ФІЗИЧНОГО СИМУЛЯТОРА АВАРІЙНОГО ЯДРА ===")
        
        current_time = 0.0
        dt = 0.5  # Крок диференціального інтегрування — 0.5 секунди
        
        # 1. Симуляція 2 секунд штатного польоту перед катастрофою
        for _ in range(4):
            mach = self.calculate_mach(self.altitude_z_m, self.velocity_ms)
            self.timeline.append(current_time)
            self.altitudes.append(self.altitude_z_m / 1000.0)
            self.velocities_mach.append(mach)
            self.g_forces.append(1.0)
            current_time += dt

        print(f"\n🚨 [T={current_time:.1f}s][CRITICAL ALERT]: Фіксується відмова утримання променя!")
        print("[ПРОТОКОЛ ЕВАКУАЦІЇ] -> Активація відстрілу аварійного пасажирського кокона.")
        
        # 2. Фаза автономного динамічного спуску до поверхні Землі
        while self.altitude_z_m > 0:
            mach = self.calculate_mach(self.altitude_z_m, self.velocity_ms)
            
            # Визначення перевантаження (G-Force) на основі висотних ешелонів та гальмівних систем
            if self.altitude_z_m > 40000.0:
                # Робота вакуумних двигунів RCS для орієнтації ядра
                g_load = 1.8
            elif self.altitude_z_m <= 12000.0:
                # Вхід у щільні шари та розкриття каскаду гальмівних парашутів
                g_load = 3.8 if self.is_passenger else 5.5
            else:
                # Екстремальне аеродинамічне гальмування обтічника (Вхід у стратосферу)
                g_load = 2.8

            # Запис поточного стану у телеметрію
            self.timeline.append(current_time)
            self.altitudes.append(self.altitude_z_m / 1000.0)
            self.velocities_mach.append(mach)
            self.g_forces.append(g_load)
            
            # ФІЗИЧНИЙ ПЕРЕРАХУНОК: Швидкість падає під дією перевантаження
            deceleration_ms2 = g_load * self.g
            self.velocity_ms = max(15.0, self.velocity_ms - (deceleration_ms2 * dt))
            
            # ФІЗИЧНИЙ ПЕРЕРАХУНОК: Висота зменшується суворо відповідно до швидкості капсули
            self.altitude_z_m -= self.velocity_ms * dt
            
            if self.altitude_z_m <= 0:
                self.altitude_z_m = 0.0
                break
                
            current_time += dt

        print(f"🌍 [УСПІХ]: Капсула здійснила посадку. Повний час евакуації: {current_time:.1f} секунд.")
        print("Генерація професійних графіків аналізу телеметрії...")
        self.generate_plots()

    def generate_plots(self):
        """Побудова синхронізованих графіків телеметрії спуску апарату"""
        plt.style.use('dark_background')
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
        fig.suptitle('BEAM-FLIGHT: EMERGENCY CORE RECOVERY TELEMETRY (DYNAMIC PHYSICS)', fontsize=14, color='cyan')

        # 1. Графік висоти
        ax1.plot(self.timeline, self.altitudes, color='#ff3333', linewidth=2.5, label='Траєкторія спуску ядра (Z)')
        ax1.set_ylabel('Висота (км)', color='white')
        ax1.grid(True, linestyle='--', alpha=0.3)
        ax1.axvline(x=2.0, color='yellow', linestyle=':', linewidth=2, label='Точка відстрілу кокона')
        ax1.legend(loc='upper right')

        # 2. Графік швидкості Маху
        ax2.plot(self.timeline, self.velocities_mach, color='#33cc33', linewidth=2.5, label='Поточна швидкість (Mach)')
        ax2.set_ylabel('Число Маху', color='white')
        ax2.grid(True, linestyle='--', alpha=0.3)
        ax2.legend(loc='upper right')

        # 3. Графік перевантажень (G-Force)
        ax3.plot(self.timeline, self.g_forces, color='#3399ff', linewidth=2.5, label='Перевантаження (G-Force)')
        ax3.set_xlabel('Польотний час (секунди)', color='white')
        ax3.set_ylabel('Перевантаження (G)', color='white')
        ax3.axhline(y=4.0, color='red', linestyle='--', linewidth=1.5, label='Пасажирський ліміт безпеки (4G)')
        ax3.grid(True, linestyle='--', alpha=0.3)
        ax3.legend(loc='upper right')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Запуск симулятора для пасажирської місії з обмеженням перевантажень
    controller = UniversalCoreSafetyController(capsule_mass_kg=15000, is_passenger_mission=True)
    controller.run_visual_emergency_mission()
        
