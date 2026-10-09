"""
Beam-Flight Project - Integrated Mission Simulator (Counter-Laser & Oasis Architecture)
Models real-time Gaussian beam jitter, dynamic plasma counter-laser mitigation,
and Oasis Terrestrial Complex Agro-Voltaic microclimate specifications.
"""

import math
import random
import time

class BeamFlightIntegratedSimulator:
    def __init__(self, capsule_mass_kg=50, target_power_mw=250):
        # Базові константи та початковий стан
        self.capsule_mass = capsule_mass_kg
        self.g = 9.81
        self.target_power_mw = target_power_mw
        self.altitude_m = 0.0
        self.velocity_ms = 0.0
        
        # Параметри зустрічного лазерного контуру капсули (Counter-Laser Weapon-Grade Unit)
        self.capsule_counter_laser_power_mw = 1.5   # 1.5 МВт для іонізації та розрізання плазмового фронту
        self.plasma_mitigation_success = False
        
        # Енергетична матриця та базова оптика
        self.base_efficiency = 0.942        # Максимальний ККД матриць "Спина" / "Брюхо"
        self.total_spent_energy_mjs = 0.0   # Сумарно спожита системою енергія з накопичувачів
        
        # Параметри наземного агровольтаїчного комплексу ОАЗИС
        self.oasis_mast_height_m = 40.0     # Щогли підняті на 40 метрів для проходу с/г техніки
        self.oasis_shade_efficiency = 0.25  # Навіс затримує 25% сонячного світла (напівтінь, -12..-15°C піску)
        self.oasis_light_transmission = 0.75 # 75% сонячного світла проходить для фотосинтезу та озеленення
        self.downlink_frequency_ghz = 5.8   # Передача енергії на Землю строго через МІКРОХВИЛІ 5.8 ГГц
        
        # Телеметричні статуси
        self.active_source = "НАЗЕМНИЙ ЛАЗЕРНИЙ КОМПЛЕКС"
        self.active_controller = "ЛІДЕР"
        self.trajectory_mode = "ВЕРТИКАЛЬНИЙ СТАРТ (0-12 км)"

    def run_full_simulation(self):
        print("=== ЗАПУСК ОНОВЛЕНОГО СИМУЛЯТОРА МІСІЇ: КОНТУР ЗУСТРІЧНОГО ЛАЗЕРА ТА ОАЗИС ===")
        print(f"[КОНФІГУРАЦІЯ ОАЗИС] Висота щогл ректен: {self.oasis_mast_height_m} м | Пропуск світла для агросектору: {self.oasis_light_transmission*100}%")
        print(f"[ЕНЕРГЕТИКА] Цільова потужність на приймачі капсули: {self.target_power_mw} МВт (Даунлінк Оазис: Мікрохвилі {self.downlink_frequency_ghz} ГГц)")
        print("-" * 100)
        
        current_time = 0.0
        dt = 1.0  
        total_duration = 125.0  # Сумарний час активного розгону (45с земля + 80с космос)
        
        while current_time < total_duration:
            current_time += dt
            
            # Етап 1: Перемикання джерела (Хендловер) строго на 45-й секунді польоту (висота 12 км)
            if current_time > 45.0 and self.active_source == "НАЗЕМНИЙ ЛАЗЕРНИЙ КОМПЛЕКС":
                self.active_source = "ОРБІТАЛЬНИЙ ЕШЕЛОН (SLO RING)"
                self.trajectory_mode = "КРУЇЗНИЙ КУТОВИЙ РОЗГІН"
                print(f"\n[T={current_time:.1f}s] --- АВТОМАТИЧНИЙ ХЕНДЛОВЕР 0.000с: Перемикання на лазер супутника {self.active_controller} ---")
            
            # Етап 2: Динамічний профіль ешелонів
            if current_time <= 45.0:
                self.altitude_m += (12000.0 / 45.0) * dt
                self.velocity_ms += (1200.0 / 45.0) * dt
            else:
                self.altitude_m += ((115000.0 - 12000.0) / 80.0) * dt
                self.velocity_ms += ((5150.0 - 1200.0) / 80.0) * dt

            # Етап 3: Фізика плазмового удару та АКТИВАЦІЯ ЗУСТРІЧНОГО ЛАЗЕРА-МАЯКА КАПСУЛИ
            # На швидкостях понад Мах 5 (після 45-ї сек) повітря стискається в плазму
            if self.velocity_ms > 1500.0:
                self.plasma_mitigation_success = True
                plasma_attenuation_offset = 0.01  # Зустрічний лазер 1.5 МВт успішно пробив оптичне вікно в плазмі!
                if int(current_time) % 20 == 0:
                    print(f"  [🗲 PLASMA SHIELD] Т={current_time:.1f}с: Капсула випускає зустрічний лазер-маяк {self.capsule_counter_laser_power_mw} МВт. Плазмовий удар гаситься. Оптичний контур замикання стабільний.")
            else:
                self.plasma_mitigation_success = False
                plasma_attenuation_offset = 0.0
            
            # Етап 4: Математичне моделювання затухання та Гауссових шумів дзеркал
            atmospheric_attenuation = 0.06 * (math.exp(-self.altitude_m / 8500.0)) if current_time <= 45.0 else 0.0
            beam_jitter_loss = abs(random.normalvariate(0.015, 0.01))  # Випадкове мікротремтіння дзеркал ADAOS
            
            # Підрахунок фінального динамічного ККД променя
            current_efficiency = self.base_efficiency - atmospheric_attenuation - beam_jitter_loss + plasma_attenuation_offset
            current_efficiency = max(0.40, min(0.95, current_efficiency))
            
            # Визначення брутто-потужності випромінювача для утримання 250 МВт корисного навантаження
            required_source_power_mw = self.target_power_mw / current_efficiency
            self.total_spent_energy_mjs += required_source_power_mw * dt
            
            # Вивід телеметрії кожні 20 секунд польоту
            if int(current_time) % 20 == 0 or current_time == total_duration:
                print(f"Т={current_time:3.1f}с | Висота: {self.altitude_m/1000.0:6.2f} км | Швидкість: {self.velocity_ms:6.1f} м/с | ККД контуру: {current_efficiency*100:.2f}% | Випромінювання: {required_source_power_mw:.1f} МВт")

        # Фінальні результати
        print("\n--- СИМУЛЯЦІЮ ІНТЕГРОВАНОГО КОНТУРУ МІСІЇ УСПІШНО ЗАВЕРШЕНО ---")
        print(f"[РЕЗУЛЬТАТ] Крейсерська висота термосфери: {self.altitude_m/1000.0:.2f} км | Швидкість польоту: {self.velocity_ms:.1f} м/с (Mach {self.velocity_ms / 340.0:.1f})")
        print(f"[РЕЗУЛЬТАТ] Сумарно спожито з енергомережі системи: {self.total_spent_energy_mjs/1e3:.2f} ГДж енергії.")
        print("[РЕЗУЛЬТАТ] По завершенню місії SLO-кільце автоматично повернулося до трансляції БЕЗПЕЧНИХ МІКРОХВИЛЬ 5.8 ГГц на комплекс Оазис.")
        
        self.trajectory_mode = "МІСІЯ УСПІШНО ЗАВЕРШЕНА"
        return True

if __name__ == "__main__":
    simulator = BeamFlightIntegratedSimulator(capsule_mass_kg=50, target_power_mw=250)
    simulator.run_full_simulation()
    
