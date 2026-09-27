import math
import time
import random
import matplotlib.pyplot as plt

class UniversalCoreSafetyController:
    def __init__(self, capsule_mass_kg=15000, is_passenger_mission=True):
        self.mass = capsule_mass_kg
        self.g = 9.81
        self.target_g = 3.0          
        self.is_passenger = is_passenger_mission
        
        # Початкові умови (Круїз у термосфері перед аварійним тестом)
        self.altitude_z_m = 110000.0   # 110 км
        self.velocity_ms = 5150.0      # Mach 15
        self.cabin_temperature_c = 21.0
        
        # Списки для збереження телеметрії (для побудови графіків)
        self.timeline = []
        self.altitudes = []
        self.velocities_mach = []
        self.g_forces = []

    def calculate_mach(self, altitude, velocity):
        """Розрахунок точного числа Маху залежно від висотного шару"""
        if altitude > 100000:
            temp_k = 700.0  # Розігрів термосфери
        elif altitude > 50000:
            temp_k = 250.0
        else:
            temp_k = max(210.0, 288.15 - 0.0065 * altitude)
        speed_of_sound = math.sqrt(1.4 * 287.05 * temp_k)
        return velocity / speed_of_sound

    def run_visual_emergency_mission(self):
        print("=== ЗАПУСК ГРАФІЧНОГО СИМУЛЯТОРА BEAM-MAX УНІВЕРСАЛЬНОГО ЯДРА ===")
        
        current_time = 0
        # Імітуємо 2 секунди нормального круїзу на ешелоні
        for sec in range(2):
            mach = self.calculate_mach(self.altitude_z_m, self.velocity_ms)
            self.timeline.append(current_time)
            self.altitudes.append(self.altitude_z_m / 1000.0) # в км
            self.velocities_mach.append(mach)
            self.g_forces.append(1.0) # Стабільний політ без прискорення
            current_time += 1

        print(f"\n🚨 [CRITICAL ALERT]: Фіксується відмова лазерного утримання на 110 км!")
        print("[ПРОТОКОЛ ЕВАКУАЦІЇ] -> Відстріл універсального ядра безпеки.")
        
        # Фаза автономного порятунку від 110 км до поверхні Землі
        while self.altitude_z_m > 0:
            mach = self.calculate_mach(self.altitude_z_m, self.velocity_ms)
            
            # Набір даних для графіків
            self.timeline.append(current_time)
            self.altitudes.append(self.altitude_z_m / 1000.0)
            self.velocities_mach.append(mach)
            
            # Фізика сил залежно від щільності атмосфери та систем утримання
            if self.altitude_z_m > 40000.0:
                # Робота вакуумних мікродвигунів RCS
                current_deceleration = 1.8 * self.g
                self.g_forces.append(1.8)
            elif self.altitude_z_m <= 15000.0:
                # Робота гальмівних парашутів у щільних шарах
                current_deceleration = 4.2 * self.g
                self.g_forces.append(4.2)
            else:
                # Чисте аеродинамічне гальмування обтічника
                current_deceleration = 2.8 * self.g
                self.g_forces.append(2.8)
                
            # Перерахунок динаміки польоту ядра на один крок
            self.velocity_ms = max(5.0, self.velocity_ms - current_deceleration * 2.5)
            self.altitude_z_m = max(0.0, self.altitude_z_m - 10000.0)
            current_time += 1
            time.sleep(0.1)

        print("🌍 [УСПІХ]: Капсула на Землі. Генерація графіків телеметрії для інвесторів...")
        self.generate_plots()

    def generate_plots(self):
        """Побудова трьох графіків у професійному інженерному стилі"""
        plt.style.use('dark_background') # Темний космічний стиль графіків
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))
        fig.suptitle('BEAM-FLIGHT: EMERGENCY CORE EJECTION TELEMETRY (PHASE 2)', fontsize=14, color='cyan')

        # 1. Графік висоти
        ax1.plot(self.timeline, self.altitudes, color='#ff3333', linewidth=2.5, label='Висота ядра (Z)')
        ax1.set_ylabel('Висота (км)', color='white')
        ax1.grid(True, linestyle='--', alpha=0.5)
        ax1.axvline(x=2, color='yellow', linestyle=':', label='Точка відстрілу (110 км)')
        ax1.legend(loc='upper right')

        # 2. Графік швидкості Маху
        ax2.plot(self.timeline, self.velocities_mach, color='#33cc33', linewidth=2.5, label='Швидкість (Mach)')
        ax2.set_ylabel('Число Маху', color='white')
        ax2.grid(True, linestyle='--', alpha=0.5)
        ax2.legend(loc='upper right')

        # 3. Графік перевантажень (G-Force)
        ax3.plot(self.timeline, self.g_forces, color='#3399ff', linewidth=2.5, label='Навантаження (G-Force)')
        ax3.set_xlabel('Польотний час (секунди симуляції)', color='white')
        ax3.set_ylabel('Перевантаження (G)', color='white')
        ax3.axhline(y=4.0, color='red', linestyle='--', label='Пасажирська межа безпеки')
        ax3.grid(True, linestyle='--', alpha=0.5)
        ax3.legend(loc='upper right')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Запуск візуального контролера порятунку вантажно-пасажирського ядра
    controller = UniversalCoreSafetyController(capsule_mass_kg=15000, is_passenger_mission=True)
    controller.run_visual_emergency_mission()
