"""
Beam-Flight Project - Integrated Mission & Energy Loss Simulator
Calculates real-time Gaussian beam jitter and dynamic atmospheric attenuation.
"""

import math
import random
import time

class BeamFlightIntegratedSimulator:
    def __init__(self, capsule_mass_kg=50, target_power_mw=250):
        # Базові константи
        self.capsule_mass = capsule_mass_kg
        self.g = 9.81
        self.target_power_mw = target_power_mw
        
        # Динамічні параметри польоту
        self.altitude_m = 0.0
        self.velocity_ms = 0.0
        
        # Енергетична матриця та оптичні втрати
        self.base_efficiency = 0.942        # Максимальний ККД матриці "Брюхо"
        self.total_spent_energy_mjs = 0.0   # Накопичена витрачена енергія в МДж
        
        # Системні телеметричні статуси
        self.active_source = "НАЗЕМНИЙ ЛАЗЕРНИЙ КОМПЛЕКС"
        self.satellite_pair_active = "ПАРА А (Орбітальний Ешелон 1)"
        self.active_controller = "ЛІДЕР"
        self.trajectory_mode = "ВЕРТИКАЛЬНИЙ СТАРТ"

    def run_full_simulation(self):
        print("=== ЗАПУСК ІНТЕГРОВАНОГО СИМУЛЯТОРА МІСІЇ (ПОСЕКУНДНИЙ ПРОРАХУНОК) ===")
        print(f"Цільова корисна потужність променя на приймачі дрона: {self.target_power_mw} МВт")
        
        current_time = 0.0
        dt = 1.0  # Крок симуляції — 1 секунда
        total_duration = 125.0  # Сумарний час активного розгону до крейсерського ешелону (45с земля + 80с космос)
        
        while current_time < total_duration:
            current_time += dt
            
            # Етап 1: Перемикання джерела (Хендловер) строго на 45-й секунді польоту (12 км)
            if current_time > 45.0 and self.active_source == "НАЗЕМНИЙ ЛАЗЕРНИЙ КОМПЛЕКС":
                self.active_source = "ОРБІТАЛЬНИЙ ЕШЕЛОН (SLO RING)"
                self.trajectory_mode = "КРУЇЗНИЙ КУТОВИЙ РОЗГІН"
                print(f"\n[T={current_time:.1f}s] --- АВТОМАТИЧНИЙ ХЕНДЛОВЕР 0.000с: Перемикання на лазер супутника {self.active_controller} ---")
            
            # Етап 2: Моделювання висоти та швидкості (Динамічний профіль)
            if current_time <= 45.0:
                self.altitude_m += (12000.0 / 45.0) * dt
                self.velocity_ms += (1200.0 / 45.0) * dt
            else:
                self.altitude_m += ((115000.0 - 12000.0) / 80.0) * dt
                self.velocity_ms += ((5150.0 - 1200.0) / 80.0) * dt

            # Етап 3: Фізичне моделювання втрат оптичного наведення (Гауссівський шум мікрокутів)
            # У нижніх шарах атмосфери додається затухання через щільність повітря (Атмосферне згасання)
            atmospheric_attenuation = 0.05 * (math.exp(-self.altitude_m / 8500.0)) if current_time <= 45.0 else 0.0
            
            # Флуктуації наведення дзеркал ADAOS (випадкове тремтіння променя)
            beam_jitter_loss = abs(random.normalvariate(0.02, 0.015))  
            
            # Разом чистий ККД на поточній секунді польоту
            current_efficiency = self.base_efficiency - atmospheric_attenuation - beam_jitter_loss
            current_efficiency = max(0.50, min(0.95, current_efficiency))  # Обмежувачі фізичного ліміту
            
            # Розрахунок необхідної потужності випромінювача для утримання 250 МВт на капсулі
            required_source_power_mw = self.target_power_mw / current_efficiency
            self.total_spent_energy_mjs += required_source_power_mw * dt
            
            # Вивід телеметрії кожні 15 секунд польоту
            if int(current_time) % 15 == 0 or current_time == total_duration:
                print(f"Т={current_time:3.1f}с | Висота: {self.altitude_m/1000.4:.1f} км | Швидкість: {self.velocity_ms:.1f} м/с | ККД променя: {current_efficiency*100:.2f}% | Джерело Потужності: {required_source_power_mw:.1f} МВт")

        # Результати місії
        print("\n--- СИМУЛЯЦІЮ МІСІЇ УСПІШНО ЗАВЕРШЕНО ---")
        print(f"[ТЕЛЕМЕТРІЯ] Кінцева висота: {self.altitude_m/1000.0:.2f} км (Ціль: 115.0 км).")
        print(f"[ТЕЛЕМЕТРІЯ] Кінцева швидкість: {self.velocity_ms:.1f} м/с (Mach {self.velocity_ms / 340.0:.2f}).")
        print(f"[ЕНЕРГЕТИКА] Сумарно витрачено з накопичувачів системи: {self.total_spent_energy_mjs/1e3:.2f} ГДж енергії з урахуванням динамічних втрат оптики.")
        
        self.trajectory_mode = "МІСІЯ УСПІШНО ЗАВЕРШЕНА"
        return True

if __name__ == "__main__":
    simulator = BeamFlightIntegratedSimulator(capsule_mass_kg=50, target_power_mw=250)
    simulator.run_full_simulation()
    
