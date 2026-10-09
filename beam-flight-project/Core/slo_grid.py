"""
Beam-Flight Project - Satellite Orbit (SLO) Grid Simulation (Optimized Energy Engine)
Models the two-stage propulsion profile, SCES-O buffer depletion, and Oasis Protocol.
"""

import math

class SLOGridSimulation:
    def __init__(self):
        # Конфігурація супутникового угруповання (90 апаратів Alpha/Master)
        self.total_satellites = 90
        self.sat_continuous_generation_mw = 60.0  # Безперервна генерація GaAs панелей (МВт)
        self.capsule_required_power_mw = 250.0   # Корисна потужність на приймачі капсули
        self.laser_efficiency = 0.45             # ККД волоконного лазера OPA (45%)
        self.mirror_loss = 0.05                  # Втрати на джиттер дзеркал ADAOS (5%)
        
        # Бортовий енергобуфер супутника типу SCES-O (зі специфікацій)
        self.sat_buffer_max_energy_gj = 150.0    # Максимальна ємність накопичувача одного супутника
        self.sat_buffer_current_energy_gj = self.sat_buffer_max_energy_gj
        
        # Константи польотного профілю
        self.t_ground_phase = 45.0               
        self.t_satellite_phase = 78.5            # Тривалість супутникового розгону (с)
        self.altitude_handover_m = 12000.0       
        self.altitude_cruise_m = 110000.0        
        
    def calculate_gross_transmission_power(self, altitude_m=12000.0) -> float:
        """Розрахунок повної електричної потужності шини супутника з урахуванням висотного згасання."""
        # Атмосферне згасання променя падає експоненціально з висотою (модель Бугера-Ламберта)
        atmosphere_attenuation = 0.08 * math.exp(-altitude_m / 8500.0)
        net_efficiency = self.laser_efficiency * (1.0 - self.mirror_loss) * (1.0 - atmosphere_attenuation)
        net_efficiency = max(0.30, net_efficiency)  # Нижня фізична межа ККД
        return self.capsule_required_power_mw / net_efficiency

    def run_orbital_energy_profile(self, active_missions_simultaneous: int = 1):
        """Динамічна симуляція стану енергомережі та накопичувачів під час розгону капсул."""
        # Сумарна миттєва генерація всього кільця супутників у ГВт
        total_harvested_power_gw = (self.total_satellites * self.sat_continuous_generation_mw) / 1000.0
        
        # Середня споживана потужність одного супутника супроводу (на середній висоті розгону ~60 км)
        avg_gross_sat_demand_mw = self.calculate_gross_transmission_power(altitude_m=61000.0)
        total_sat_drain_gw = (active_missions_simultaneous * avg_gross_sat_demand_mw) / 1000.0
        
        # Обчислення витрати реальної енергії в Гігаджоулях за час вікна розгону (78.5 сек)
        # Енергія = Потужність (МВт) * Час (сек) / 1000
        total_energy_spent_gj = (avg_gross_sat_demand_mw * self.t_satellite_phase) / 1000.0
        
        # Стан буфера лідируючого супутника після виконання місії
        self.sat_buffer_current_energy_gj = max(0.0, self.sat_buffer_max_energy_gj - total_energy_spent_gj)
        buffer_percentage = (self.sat_buffer_current_energy_gj / self.sat_buffer_max_energy_gj) * 100
        
        # Базовий експорт Протоколу Оазис на Землю у моменти супроводу
        oasis_surplus_gw = max(0.0, total_harvested_power_gw - total_sat_drain_gw)
        
        print("=== BEAM-FLIGHT ORBITAL GRIDSYSTEMS (SLO) ENERGY AUDIT ===")
        print(f"Загальна генерація орбітального ешелону: {total_harvested_power_gw:.2f} ГВт")
        print(f"Межа хендловеру Земля-Супутник      : {self.altitude_handover_m / 1000.0:.1f} км")
        print(f"Вікно супутникового прискорення     : {self.t_satellite_phase:.1f} секунд")
        print(f"Пікова електрична потужність супутника : {avg_gross_sat_demand_mw:.2f} МВт (Шина HTS 100 кВ)")
        print(f"Сумарно спалено енергії за один пуск : {total_energy_spent_gj:.2f} ГДж")
        print(f"Залишок заряду буфера SCES-O лідера  : {self.sat_buffer_current_energy_gj:.1f} ГДж ({buffer_percentage:.1f}%)")
        print(f"Поточний базовий експорт 'Оазис'     : {oasis_surplus_gw:.2f} ГВт на частоті 5.8 ГГц")
        print("====================================================")
        
        # Автоматичний захист від перевантаження мережі
        if self.sat_buffer_current_energy_gj <= 20.0:
            print("[УВАГА] Критичне виснаження буфера супутника! Необхідна пауза 420с для сонячної регенерації.")
            
        return {
            "harvested_gw": total_harvested_power_gw,
            "sat_drain_gw": total_sat_drain_gw,
            "oasis_export_gw": oasis_surplus_gw,
            "leader_buffer_left_gj": self.sat_buffer_current_energy_gj
        }

if __name__ == "__main__":
    sim = SLOGridSimulation()
    # Симуляція стандартного сценарію пуску однієї капсули
    sim.run_orbital_energy_profile(active_missions_simultaneous=1)
    
