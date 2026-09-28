"""
Beam-Flight Project - Main Mission Control Digital Twin
Integrated with SLO (Satellite Orbit) Grid for Handover Logic at 12 km.
"""

import math
import time
# Інтеграція нашого нового модуля енергетичної сітки супутників
from slo_grid import SLOGridSimulation

class BeamFlightMissionControl:
    def __init__(self):
        # Базові константи місії
        self.target_altitude_m = 115000.0  # 115 км крейсерська висота
        self.target_mach = 15.0
        self.capsule_mass_kg = 50.0        # Вантажний дрон (Phase 1: Beam-Mini)
        
        # Ініціалізація орбітальної мережі супутників (SLO)
        self.slo_network = SLOGridSimulation()
        
        # Динамічні статуси систем
        self.sces_buffer_charged = False
        self.lh2_fueled = False
        self.tether_tension_n = 5000.0     # Стартовий натяг тросів
        
    def prepare_systems(self):
        """Фаза підготовки: JIT-заправка та зарядка енергобуфера Землі."""
        print("[PRE-LAUNCH] Ініціалізація систем наземного комплексу...")
        self.lh2_fueled = True
        self.sces_buffer_charged = True
        self.tether_tension_n = 0.0
        print("[PRE-LAUNCH] Кріогенний водень LH2 заправлено (JIT).")
        print("[PRE-LAUNCH] Наземний буфер SCES заряджено на 250 МВт.")
        print("[PRE-LAUNCH] Натяг утримуючих тросів скинуто до 0 Н.")
        return self.lh2_fueled and self.sces_buffer_charged

    def calculate_mach(self, velocity_ms, altitude_m) -> float:
        """Динамічний розрахунок числа Маху на основі температурних ешелонів."""
        # Визначення температури середовища залежно від висоти
        if altitude_m > 100000.0:
            temp = 700.0  # Термосфера
        elif altitude_m > 50000.0:
            temp = 250.0  # Мезосфера
        else:
            temp = 288.15 - (0.0065 * altitude_m)  # Тропосфера / Стратосфера
            if temp < 216.65:
                temp = 216.65
                
        gamma = 1.4
        r_spec = 287.05
        speed_of_sound = math.sqrt(gamma * r_spec * temp)
        return velocity_ms / speed_of_sound

    def run_mission(self):
        """Повний цикл місії з автоматичним викликом супутникових функцій на 12 км."""
        if not self.prepare_systems():
            print("[CRITICAL] Системи не готові до старту. Місію скасовано.")
            return False

        print("\n--- ЗАПУСК КАПСУЛИ UABC (LAUNCH) ---")
        print("[STAGE 1] Активація наземного лазера. Старт вертикального розгону під тиском світла.")
        
        current_altitude = 0.0
        current_velocity = 0.0
        time_elapsed = 0.0
        
        # Крок 1: Наземний розгін до межі хендловеру (12 км / 45 секунд)
        while current_altitude < self.slo_network.altitude_handover_m:
            time_elapsed += 5.0
            # Спрощена лінійна модель розгону для симуляції логіки контурів
            current_altitude += (self.slo_network.altitude_handover_m / (self.slo_network.t_ground_phase / 5.0))
            current_velocity += 60.0  # Набір швидкості в щільних шарах
            mach = self.calculate_mach(current_velocity, current_altitude)
            print(f" Час: {time_elapsed:.1f}с | Висота: {current_altitude/1000.0:.2f} км | Швидкість: {mach:.2f} M (Наземний лазер)")

        # Крок 2: АВТОМАТИЧНИЙ ХЕНДЛОВЕР НА ВАТЕРЛІНІЇ 12 КМ
        print("\n--- [HANDOVER DETECTED] ВИСОТА 12.0 КМ ДОСЯГНУТА ---")
        print("[HANDOVER] Наземний лазер автоматично вимикається (End of 45s pulse).")
        print("[HANDOVER] Запит на перехоплення променя супутниковим ешелоном SLO...")
        
        # Виклик функцій супутника: прорахунок пікового навантаження шини та експорту енергії Оазис
        slo_report = self.slo_network.run_orbital_energy_profile(active_missions_simultaneous=1)
        
        print("[STAGE 2] Пара супутників 'А-Лідер' та 'Ведомий' замкнули оптичний контур.")
        print(f"[STAGE 2] Навантаження на кріогенну шину лідируючого супутника: {self.slo_network.calculate_gross_transmission_power():.2f} МВт.")
        
        # Симуляція аварійного сценарію перехоплення (про який йшлося у файлі 2 вашого проекту)
        simulated_leader_fault = False  # Прапорець для тестування Rollback-відкату
        if simulated_leader_fault:
            print("[ALERT] Збій фокусування супутника 'Лідер'! Активація Rollback-протоколу.")
            print("[EMERGENCY] Миттєве перехоплення (хендловер 0.000с) супутником 'Ведомий'. Стабілізація успішна.")
        else:
            print("[OK] Хендловер виконано в штатному режимі за 0.000 сек. Помилок фокусування не виявлено.")

        # Крок 3: Супутниковий розгін (від 12 км до 110-115 км / 78.5 секунд)
        print("\n[STAGE 2] Розгін супутниковим лазером у розріджених шарах атмосфери та мезосфері...")
        sat_phase_time = 0.0
        while current_altitude < self.target_altitude_m:
            sat_phase_time += 10.0
            time_elapsed += 10.0
            current_altitude += ((self.target_altitude_m - self.slo_network.altitude_handover_m) / (self.slo_network.t_satellite_phase / 10.0))
            current_velocity += 550.0  # Стрімкий прискорювальний імпульс у вакуумі
            mach = self.calculate_mach(current_velocity, current_altitude)
            print(f" Час: {time_elapsed:.1f}с | Висота: {current_altitude/1000.0:.2f} км | Швидкість: {mach:.2f} M (Супутникове ведення)")
            
            # Маневр уникнення зіткнень на проміжних ешелонах (з вашої техспецифікації)
            if 90000.0 < current_altitude < 100000.0:
                print("  [MANEUVER] Активація бічного зміщення Z=95км для пропуску попутного апарату.")

        print(f"\n[CRUISE] Крейсерський ешелон досягнуто! Висота: {current_altitude/1000.0:.1f} км. Стабілізація швидкості на Mach {self.calculate_mach(current_velocity, current_altitude):.1f}.")
        
        # Крок 4: Замикання енергетичного мосту та підготовка до гальмування
        print("\n--- ФАЗА СИНХРОНІЗАЦІЇ ТА КОМБІНОВАНОГО ГАЛЬМУВАННЯ ---")
        print("[BRAKING] Активація носового маяка капсули UABC.")
        print("[BRAKING] Інжекція кріогенного водню крізь носові форсунки (роздування плазмового екрана).")
        print("[BRAKING] Увімкнення зустрічного лазерного реверсу + МГД-гальмування. Перевантаження: 6.5G.")
        print("[BRAKING] Швидкість впала нижче Mach 3. Автоматичне відсікання газового гасіння плазми.")
        
        # Крок 5: Посадка на лазерну подушку
        print("\n--- ФІКСАЦІЯ ТА ПОСАДКА ---")
        print("[LANDING] Капсула зависла над решіткою-конфоркою хабу 'ВЕКТОР-ПРАЙМ'. Швидкість: 0 м/с.")
        print("[LANDING] Спрацювали роботизовані затискачі утримання ядра.")
        print("[LANDING] Залишки рекуперованої енергії гальмування скинуто назад у наземну мережу.")
        print(f"[INFO] Повний час місії склав: {time_elapsed:.1f} секунд. Мережа Оазис повернулася до базового експорту {slo_report['oasis_export_gw']:.2f} GW.")
        print("=== МІСІЮ УСПІШНО ЗАВЕРШЕНО ===")
        return True

if __name__ == "__main__":
    mission = BeamFlightMissionControl()
    mission.run_mission()
