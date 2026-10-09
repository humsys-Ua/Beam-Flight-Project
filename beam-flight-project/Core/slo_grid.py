"""
Beam-Flight Project - Satellite Orbit (SLO) Grid Simulation (Verifiable Physics Engine)
Models the satellite propulsion window (110km to 12km) and ground magnetic grid handover.
"""

import math

class SLOGridSimulation:
    def __init__(self):
        # Конфігурація супутникового угруповання (90 апаратів Master)
        self.total_satellites = 90
        self.sat_continuous_generation_mw = 60.0  # Генерація GaAs панелей одного супутника
        self.capsule_required_power_mw = 250.0   # Потужність на приймачі капсули
        self.laser_efficiency = 0.45             # ККД лазера OPA (45%)
        self.mirror_loss = 0.05                  # Втрати на джиттер дзеркал ADAOS (5%)
        
        # ІСТИННІ КОНСТАНТИ ВАШОЇ БАЛІСТИКИ
        self.altitude_cruise_m = 110000.0        # Старт гальмування супутниками (110 км)
        self.altitude_handover_m = 12000.0       # Межа відключення супутників і увімкнення ШАХТИ (12 км)
        self.t_satellite_phase = 78.5            # Тривалість супутникового супроводу (сек)
        
        # Параметри підземного МГД-комплексу (Ешелон 12км - 0)
        self.ground_magnetic_field_tesla = 4.5    # Вертикальний потік шахти
        self.ground_mhd_recovery_power_mw = 24.5 # Потужність рекуперації в землю

    def calculate_gross_transmission_power(self, altitude_m) -> float:
        """Розрахунок повної потужності лазера супутника в залежності від висоти."""
        # Атмосферне затухання діє лише ближче до 12 км
        atmosphere_attenuation = 0.08 * math.exp(-altitude_m / 8500.0) if altitude_m < 50000.0 else 0.0
        net_efficiency = self.laser_efficiency * (1.0 - self.mirror_loss) * (1.0 - atmosphere_attenuation)
        return self.capsule_required_power_mw / net_efficiency

    def run_orbital_energy_profile(self, active_missions_simultaneous: int = 1):
        """Симуляція супутникової мережі у вікні від 110 км до 12 км."""
        total_harvested_power_gw = (self.total_satellites * self.sat_continuous_generation_mw) / 1000.0
        
        # Середня потужність супутника під час гальмування у мезосфері
        avg_sat_demand_mw = self.calculate_gross_transmission_power(altitude_m=61000.0)
        total_sat_drain_gw = (active_missions_simultaneous * avg_sat_demand_mw) / 1000.0
        
        # Експорт Оазис під час активного супутникового контуру
        oasis_surplus_gw = total_harvested_power_gw - total_sat_drain_gw
        
        print("=== BEAM-FLIGHT ORBITAL GRIDSYSTEMS (SLO) AUDIT ===")
        print(f"Загальна генерація орбітального Кільця : {total_harvested_power_gw:.2f} ГВт")
        print(f"Зона роботи супутникового реверсу     : від {self.altitude_cruise_m/1000.0:.1f} км до {self.altitude_handover_m/1000.0:.1f} км")
        print(f"Час супутникового гальмування          : {self.t_satellite_phase:.1f} секунд")
        print(f"Споживання лазера лідируючого супутника: {avg_sat_demand_mw:.2f} МВт")
        print(f"Базовий експорт Протоколу Оазис        : {oasis_surplus_gw:.2f} ГВт")
        print("----------------------------------------------------")
        print(f"🔮 [РУБІЖ 12 КМ ДОСЯГНУТО]: Супутники вимикають реверс променя.")
        print(f"⚡ [ПІДЗЕМНА АКТИВАЦІЯ]: Шахта вмикає вертикальний магнітний потік {self.ground_magnetic_field_tesla} Тл.")
        print(f"🌍 [МГД-ПОСАДКА 12км-0]: {self.ground_mhd_recovery_power_mw} МВт енергії гальмування стікає в наземні SCES.")
        print("====================================================")
        
        return {"oasis_export_gw": oasis_surplus_gw}

if __name__ == "__main__":
    sim = SLOGridSimulation()
    sim.run_orbital_energy_profile(active_missions_simultaneous=1)
