# economics/cost_model.py
def calculate_flight_economics(capsule_mass_kg):
    g = 9.81
    electricity_cost_per_kwh = 0.16  # Промисловий тариф у $
    # Гігаватний імпульс (250 МВт) на 45 сек = ~3125 кВт-год
    energy_consumed_kwh = 3125 
    
    infra_amortization = 10000  # Розподілена вартість пуску на конвеєрі
    consumables_cost = 1500     # LH2 + Гелій/Водень для гасіння плазми
    energy_cost = energy_consumed_kwh * electricity_cost_per_kwh
    
    total_launch_cost = infra_amortization + consumables_cost + energy_cost
    cost_per_kg = total_launch_cost / capsule_mass_kg
    
    print(f"=== РОЗРАХУНОК ЕКОНОМІКИ BEAM-FLIGHT ДЛЯ МАСИ {capsule_mass_kg} КГ ===")
    print(f" Собівартість енергії на пуск: ${energy_cost:.2f}")
    print(f" Загальна вартість одного пуску: ${total_launch_cost:.2f}")
    print(f" ВАРТІСТЬ ДОСТАВКИ ЗА 1 КГ: ${cost_per_kg:.2f} / кг")
    return cost_per_kg

if __name__ == "__main__":
    calculate_flight_economics(capsule_mass_kg=50) # Тест для Beam-Mini
