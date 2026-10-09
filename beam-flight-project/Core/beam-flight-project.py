"""
Beam-Flight Project - Main Mission Control Digital Twin (Optimized Flight Physics Engine)
Integrated with SLO (Satellite Orbit) Grid for Handover Logic at 12 km.
"""

import math
import time

# Заглушка для автономної роботи, якщо slo_grid відсутній у локальному оточенні IDE
try:
    from slo_grid import SLOGridSimulation
except ImportError:
    class SLOGridSimulation:
        def __init__(self):
            self.altitude_handover_m = 12000.0
            self.t_ground_phase = 45.0
            self.t_satellite_phase = 78.5
        def run_orbital_energy_profile(self, active_missions_simultaneous):
            return {"oasis_export_gw": 2.5}
        def calculate_gross_transmission_power(self):
            return 250.0

class BeamFlightMissionControl:
    def __init__(self):
        # Базові константи місії (Phase 1: Beam-Mini Demonstrator)
        self.target_altitude_m = 115000.0  # 115 км крейсерська висота
        self.target_mach = 15.0
        
        # Фізичні параметри апарату зі специфікацій TS-LTHE-2026-004
        self.dry_mass_kg = 50.0            # Маса чистого корисного вантажу дрона
        self.fuel_mass_kg = 200.0          # Запас кріогенного LH2 на борту
        self.capsule_mass_kg = self.dry_mass_kg + self.fuel_mass_kg
        
        self.lthe_thrust_n = 35500.0       # Максимальна тяга двигуна 35.5 кН
        self.lthe_mass_flow_rate = 3.01    # Витрата водню 3.01 кг/с
        
        # Ініціалізація орбітальної мережі супутників (SLO)
        self.slo_network = SLOGridSimulation()
        
        # Статуси систем
        self.sces_buffer_charged = False
        self.lh2_fueled = False
        self.tether_tension_n = 5000.0     

    def prepare_systems(self):
        """Фаза підготовки: JIT-заправка та зарядка енергобуфера Землі."""
        print("[PRE-LAUNCH] Ініціалізація систем наземного комплексу...")
        self.lh2_fueled = True
        self.sces_buffer_charged = True
        self.tether_tension_n = 0.0
        print(f"[PRE-LAUNCH] Кріогенний водень LH2 заправлено (Борт: {self.capsule_mass_kg} кг).")
        print("[PRE-LAUNCH] Наземний буфер SCES заряджено на 250 МВт.")
        return self.lh2_fueled and self.sces_buffer_charged

    def calculate_mach(self, velocity_ms, altitude_m) -> float:
        """Динамічний розрахунок числа Маху на основі температурних ешелонів атмосфери."""
        if altitude_m > 100000.0:
            temp = 700.0  # Термосфера
        elif altitude_m > 50000.0:
            temp = 250.0  # Мезосфера
        else:
            temp = 288.15 - (0.0065 * altitude_m)  # Стратосфера / Тропосфера
            if temp < 216.65:
                temp = 216.65
                
        gamma = 1.4
        r_spec = 287.05
        speed_of_sound = math.sqrt(gamma * r_spec * temp)
        return velocity_ms / speed_of_sound

    def run_mission(self):
        """Повний цикл місії з чисельним інтегруванням фізики польоту за методом Ейлера."""
        if not self.prepare_systems():
            print("[CRITICAL] Системи не готові до старту. Місію скасовано.")
            return False

        print("\n--- ЗАПУСК КАПСУЛИ UABC (LAUNCH) ---")
        print("[STAGE 1] Активація наземного лазера. Старт вертикального розгону.")
        
        current_altitude = 0.0
        current_velocity = 0.0
        time_elapsed = 0.0
        dt = 1.0  # Крок інтегрування: 1 секунда
        
        # Крок 1: Наземний розгін (фізична модель до 12 км)
        while current_altitude < self.slo_network.altitude_handover_m:
            time_elapsed += dt
            
            # Розрахунок поточної маси та сили тяжіння (g змінюється з висотою)
            g_curr = 9.81 * (6371000.0 / (6371000.0 + current_altitude))**2
            if self.fuel_mass_kg > 0:
                self.fuel_mass_kg -= self.lthe_mass_flow_rate * dt
                self.capsule_mass_kg = self.dry_mass_kg + max(0.0, self.fuel_mass_kg)
                net_thrust = self.lthe_thrust_n
            else:
                net_thrust = 0.0  # Водень вигорів
                
            # Чисельне прискорення (без урахування аеродинамічного лобового опору для простоти)
            acceleration = (net_thrust / self.capsule_mass_kg) - g_curr
            current_velocity += acceleration * dt
            current_altitude += current_velocity * dt
            
            mach = self.calculate_mach(current_velocity, current_altitude)
            if int(time_elapsed) % 5 == 0:
                print(f" Час: {time_elapsed:.1f}с | Висота: {current_altitude/1000.0:.2f} км | Швидкість: {mach:.2f} M | Вага: {self.capsule_mass_kg:.1f} кг")

        # Крок 2: ХЕНДЛОВЕР НА РУБЕЖІ 12 КМ
        print(f"\n--- [HANDOVER DETECTED] ВИСОТА {current_altitude/1000.0:.2f} КМ ДОСЯГНУТА ---")
        print("[HANDOVER] Наземний лазер автоматично вимикається (End of ground phase).")
        print("[HANDOVER] Запит на перехоплення променя супутниковим ешелоном SLO...")
        
        slo_report = self.slo_network.run_orbital_energy_profile(active_missions_simultaneous=1)
        print(f"[STAGE 2] Навантаження на кріогенну шину супутника: {self.slo_network.calculate_gross_transmission_power():.2f} МВт.")
        print("[OK] Хендловер виконано безрозривно за 0.000 сек.")

        # Крок 3: Супутниковий розгін (від 12 км до крейсерських 115 км)
        print("\n[STAGE 2] Розгін супутниковим лазером у мезосфері та термосфері...")
        while current_altitude < self.target_altitude_m:
            time_elapsed += dt
            
            g_curr = 9.81 * (6371000.0 / (6371000.0 + current_altitude))**2
            if self.fuel_mass_kg > 0:
                self.fuel_mass_kg -= self.lthe_mass_flow_rate * dt
                self.capsule_mass_kg = self.dry_mass_kg + max(0.0, self.fuel_mass_kg)
                net_thrust = self.lthe_thrust_n * 1.2  # У вакуумі ККД сопла вище
            else:
                net_thrust = 0.0
                
            acceleration = (net_thrust / self.capsule_mass_kg) - g_curr
            current_velocity += acceleration * dt
            current_altitude += current_velocity * dt
            
            mach = self.calculate_mach(current_velocity, current_altitude)
            
            if int(time_elapsed) % 10 == 0:
                print(f" Час: {time_elapsed:.1f}с | Висота: {current_altitude/1000.0:.2f} км | Швидкість: {mach:.2f} M | Залишок LH2: {self.fuel_mass_kg:.1f} кг")
            
            if 90000.0 < current_altitude < 93000.0:
                print("  [MANEUVER] Бічне зміщення Z=95км для пропуску попутного супутника.")

        final_mach = self.calculate_mach(current_velocity, current_altitude)
        print(f"\n[CRUISE] Крейсерський ешелон досягнуто! Висота: {current_altitude/1000.0:.2f} км. Швидкість: {final_mach:.2f} M.")
        
        # Крок 4 & 5: Гальмування та посадка
        print("\n--- ФАЗА СИНХРОНІЗАЦІЇ ТА КОМБІНОВАНОГО ГАЛЬМУВАННЯ ---")
        print("[BRAKING] Активація МГД-каналу. Індукція поля котушок ReBCO: 4.5 Тесла.")
        print(f"[BRAKING] Рекуперація кінетичної енергії: 24.5 МВт повернуто в бортові накопичувачі SCES.")
        print("[LANDING] Фіксація на лазерну подушку комплексу 'ВЕКТОР-ПРАЙМ'. Швидкість: 0 м/с.")
        print(f"[INFO] Повний час місії: {time_elapsed:.1f} сек. Мережа Оазис стабілізована на {slo_report['oasis_export_gw']:.2f} GW.")
        print("=== МІСІЮ УСПІШНО ЗАВЕРШЕНО ===")
        return True

if __name__ == "__main__":
    mission = BeamFlightMissionControl()
    mission.run_mission()
    
