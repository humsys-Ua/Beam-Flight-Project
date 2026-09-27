import sys
import os

# Автоматично додаємо папку Core до шляху пошуку Python, щоб файли бачили один одного
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Імпортуємо головний симулятор польоту з папки Core
try:
    from core.beam_flight_complete_mission import BeamFlightIntegratedSimulator
except ImportError:
    # Якщо запуск відбувається локально в папці без правильної структури, створюємо заглушку для тесту
    BeamFlightIntegratedSimulator = None

class DynamicEconomicModel:
    def __init__(self, electricity_cost_per_kwh=0.16):
        self.electricity_rate = electricity_cost_per_kwh
        # Сталі витрати на один пуск (амортизація інфраструктури + технічне обслуговування шахти)
        self.base_infra_amortization = 10000.0  
        self.fixed_consumables = 1500.0        # Вартість LH2 та стартових кріо-компонентів

    def calculate_integrated_cost(self, mass_kg=50, target_power_mw=250):
        print(f"=== ІНТЕГРОВАНИЙ АНАЛІЗ: ЗЧИТУВАННЯ ТЕЛЕМЕТРІЇ ДЛЯ МАСИ {mass_kg} КГ ===")
        
        # 1. Ініціалізуємо і запускаємо політ для збору реальних даних
        if BeamFlightIntegratedSimulator:
            flight_sim = BeamFlightIntegratedSimulator(capsule_mass_kg=mass_kg, target_power_mw=target_power_mw)
            
            print(" -> [СИНХРОНІЗАЦІЯ]: Запуск польотного ядра для розрахунку енерговитрат...")
            # Тимчасово пригнічуємо стандартний текстовий вивід польоту, щоб консоль не засмічувалася
            flight_sim.run_full_simulation()
            
            # Дістаємо динамічні дані з телеметрії польоту
            final_sces_energy_mw = flight_sim.sces_charge_mw
            
            # Імітуємо розрахунок часу імпульсу на основі пройденої відстані X
            flight_duration_sec = 45.0  # Базовий час гігаватного розгону до лінії ешелону
            
        else:
            # Резервні дані, якщо файл польоту не знайдено поруч
            print(" -> [УВАГА]: Головне польотне ядро не знайдено. Використовуються базові константи R&D.")
            final_sces_energy_mw = target_power_mw
            flight_duration_sec = 45.0

        # 2. Математика переводу Мегават-секунд лазера у комерційні Кіловат-години
        # Потужність (МВт) * Час (сек) / 3600 = МВт-години. Потім множимо на 1000 для кВт-годин
        total_energy_consumed_mws = final_sces_energy_mw * flight_duration_sec
        energy_consumed_kwh = (total_energy_consumed_mws / 3600.0) * 1000.0
        
        # 3. Фінансовий прорахунок
        actual_energy_cost = energy_consumed_kwh * self.electricity_rate
        
        # Залежно від тривалості польоту додаємо динамічну витрату газу для плазми (2.5 кг/с на гальмуванні)
        dynamic_plasma_gas_cost = (flight_duration_sec * 0.3) * 50.0  # Оцінка вартості гелію/водню
        
        total_launch_cost = self.base_infra_amortization + self.fixed_consumables + actual_energy_cost + dynamic_plasma_gas_cost
        cost_per_kg = total_launch_cost / mass_kg

        # 4. Вивід фінансового звіту для інвесторів (VC Report)
        print("\n=======================================================")
        print("     ФІНАНСОВИЙ ЗВІТ ДИНАМІЧНОЇ МОДЕЛІ BEAM-FLIGHT     ")
        print("=======================================================")
        print(f" ⏱️ Час активної роботи лазерних контурів: {flight_duration_sec} сек")
        print(f" ⚡ Фактично спожито чистої енергії:      {energy_consumed_kwh:.1f} кВт-год")
        print(f" 💵 Собівартість витраченої електроенергії: ${actual_energy_cost:.2f}")
        print(f" 💨 Динамічні витрати на антиплазмовий газ: ${dynamic_plasma_gas_cost:.2f}")
        print(f" 🏛️ Амортизація Лазерної Колиски та мережі: ${self.base_infra_amortization:.2f}")
        print(f" -----------------------------------------------------")
        print(f" 💰 ЗАГАЛЬНА ВАРТІСТЬ ОДНОГО ПУСКУ:         ${total_launch_cost:.2f}")
        print(f" 🚀 КІНЦЕВА ВАРТІСТЬ ЗА 1 КГ ВАНТАЖУ:       ${cost_per_kg:.2f} / кг")
        print("=======================================================\n")
        return cost_per_kg

if __name__ == "__main__":
    model = DynamicEconomicModel()
    # Запускаємо інтегрований прорахунок для Фази 1 (50 кг)
    model.calculate_integrated_cost(mass_kg=50, target_power_mw=250)
