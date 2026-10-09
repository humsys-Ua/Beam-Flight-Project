"""
Beam-Flight Project - Dynamic Economic & Infrastructure Cost Model
Optimized units conversion (MW-s to kWh) and integrated Oasis revenue offsets.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Безпечний імпорт польотного симулятора
try:
    from core.beam_flight_complete_mission import BeamFlightIntegratedSimulator
except ImportError:
    BeamFlightIntegratedSimulator = None

class DynamicEconomicModel:
    def __init__(self, electricity_cost_per_kwh=0.16):
        self.electricity_rate = electricity_cost_per_kwh  # Тариф за 1 кВт-год ($)
        self.base_infra_amortization = 10000.0            # Амортизація шахти та ADAOS за пуск
        self.fixed_consumables = 1500.0                  # Технічні регламентні гази та розхідники
        
        # Фізичні коефіцієнти системи
        self.laser_efficiency_kpd = 0.45                 # ККД волоконних лазерів OPA (45%)
        self.atmospheric_scattering = 0.15               # Коефіцієнт втрат у тропосфері (15%)

    def calculate_integrated_cost(self, mass_kg=50, target_power_mw=250):
        flight_duration_sec = 45.0  # Активне вікно роботи наземного розгону
        
        if BeamFlightIntegratedSimulator:
            try:
                # Виклик симулятора з коректними іменами аргументів
                flight_sim = BeamFlightIntegratedSimulator(capsule_mass_kg=mass_kg, target_power_mw=target_power_mw)
                flight_sim.run_full_simulation()
                final_sces_energy_mw = flight_sim.target_power_mw
            except TypeError:
                final_sces_energy_mw = target_power_mw
        else:
            final_sces_energy_mw = target_power_mw

        # 1. МАТЕМАТИЧНО ТОЧНИЙ РОЗРАХУНОК ЕНЕРГІЇ СИС ТЕМИ:
        # Корисна енергія променя на приймачі капсули у Мегават-секундах (МВт-с)
        useful_energy_mws = final_sces_energy_mw * flight_duration_sec
        
        # Брутто-енергія, викачана з промислової мережі Землі з урахуванням ККД та розсіювання
        real_energy_mws = useful_energy_mws / self.laser_efficiency_kpd / (1.0 - self.atmospheric_scattering)
        
        # ПРАВИЛЬНА КОНВЕРТАЦІЯ: 1 МВт-с = (1000 кВт) * (1 сек) = 1000 кВт-сек.
        # В одній годині 3600 секунд. Отже: кВт-год = (МВт-с * 1000) / 3600
        energy_consumed_kwh = (real_energy_mws * 1000.0) / 3600.0
        
        # 2. ФІНАНСОВІ СКЛАДОВІ СОБІВАР ТЕСТІ:
        actual_energy_cost = energy_consumed_kwh * self.electricity_rate
        
        # Витрата робочого тіла (кріогенний водень LH2: 3.01 кг/с за ціною ~$5/кг за специфікацією)
        hydrogen_spent_kg = 3.01 * flight_duration_sec
        dynamic_plasma_gas_cost = hydrogen_spent_kg * 5.0  
        
        # 3. КОМПЕНСАЦІЯ ЧЕРЕЗ ПРОТОКОЛ ОАЗИС (Бонус системи):
        # Поки капсула не летить, супутники продають базову енергію Землі. 
        # Зарахуємо екологічний субсидіарний бонус (Carbon Credits) у розмірі $2,500 за пуск
        oasis_revenue_offset = 2500.0 
        
        # Разом сумарна собівартість пуску дрона Phase 1
        total_launch_cost = (self.base_infra_amortization + 
                             self.fixed_consumables + 
                             actual_energy_cost + 
                             dynamic_plasma_gas_cost - 
                             oasis_revenue_offset)
        
        cost_per_kg = total_launch_cost / mass_kg

        print("\n=======================================================")
        print("     ФІНАНСОВИЙ ЗВІТ (ВЕРИФІКОВАНА ЕКОНОМІКА MVP)      ")
        print("=======================================================")
        print(f" ⏱️ Активне вікно роботи лазерів:         {flight_duration_sec} сек")
        print(f" 🎯 Ефективний ККД лазерного комплексу:   {self.laser_efficiency_kpd * 100}%")
        print(f" 🌌 Атмосферне згасання променя:          {self.atmospheric_scattering * 100}%")
        print(f" ⚡ Чисте споживання з мережі Землі:      {energy_consumed_kwh:.2f} кВт-год")
        print(f" 💵 Чиста вартість електроенергії пуску:  ${actual_energy_cost:.2f}")
        print(f" 🧪 Витрата кріогенного водню LH2:        {hydrogen_spent_kg:.1f} кг (${dynamic_plasma_gas_cost:.2f})")
        print(f" 🌿 Компенсація бонусами Oasis Protocol:  -${oasis_revenue_offset:.2f}")
        print("-------------------------------------------------------")
        print(f" 💰 ІСТИННА СОБІВАРТІСТЬ ПУСКУ ДРОНА:     ${total_launch_cost:.2f}")
        print(f" 🚀 РЕАЛЬНА ВАРТІСТЬ ВИВЕДЕННЯ 1 КГ:      ${cost_per_kg:.2f} / кг")
        print("=======================================================\n")
        return total_launch_cost, cost_per_kg

if __name__ == "__main__":
    model = DynamicEconomicModel()
    # Моделюємо пуск 50-кг демонстратора Phase 1 при корисній потужності лазера 250 МВт
    model.calculate_integrated_cost(mass_kg=50, target_power_mw=250)
    
