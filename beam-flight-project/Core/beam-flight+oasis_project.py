import math

class GlobalSpaceEnergyRing:
    """
    ГЛОБАЛЬНЕ КОСМІЧНЕ ЕНЕРГОКІЛЬЦЕ (Орбітальна шина).
    Єдиний транзитний простір, через який взаємодіють об'єкти на різних континентах.
    """
    def __init__(self):
        self.ring_load_percent = 78.5  # Поточне навантаження кільця (%)
        self.orbital_buffer_mj = 1000000.0  # Енергія в космічних накопичувачах

    def inject_energy(self, energy_mj):
        """Прийом енергії від наземних хабів генерації."""
        self.orbital_buffer_mj += energy_mj
        # Зняття напруги з кільця, якщо воно перевантажене
        if self.ring_load_percent > 50:
            self.ring_load_percent -= (energy_mj / 50000.0)
        return self.ring_load_percent

    def extract_energy(self, energy_mj):
        """Запит енергії пусковими шахтами з орбіти."""
        if self.orbital_buffer_mj >= energy_mj:
            self.orbital_buffer_mj -= energy_mj
            return energy_mj, True
        return 0.0, False


class OasisAfricanHub:
    """
    ПРОЄКТ «ОАЗИС» (Локація: АФРИКА).
    Абсолютно автономний комерційний доп-варіант для інвесторів.
    Працює незалежно від шахт. Знімає напругу з кільця, накопичує і скидає гігавати в космос.
    """
    def __init__(self, global_ring_reference):
        self.location = "Africa (Sahara Sub-sector)"
        self.space_ring = global_ring_reference
        self.adaptive_masts_count = 120
        self.current_mast_height = 75.0  # Динамічні телескопічні щогли (м)
        self.local_generation_mw = 1200.0  # Потужність власної сонячно-термальної генерації

    def run_daily_balancing(self):
        """Оазис балансує космічне кільце: качає туди гігавати енергії, розвантажуючи мережу."""
        generated_energy_mj = self.local_generation_mw * 3600  # Енергія за умовну годину
        new_ring_load = self.space_ring.inject_energy(generated_energy_mj)
        
        print(f"\n[ПРОЄКТ ОАЗИС — {self.location.upper()}]")
        print(f"-> Адаптивні щогли виставлені на висоту {self.current_mast_height}м для пробиття приземного шару.")
        print(f"-> Згенеровано та закачано в орбітальне кільце: {generated_energy_mj/1e3:.1f} ГДж енергії.")
        print(f"-> Результат: Напругу з космічного кільця ЗНЯТО. Поточне навантаження: {new_ring_load:.2f}%")


class PacificLaunchShaft:
    """
    ПУСКОВА ШАХТА (Локація: ГАВАЇ / АВСТРАЛІЯ).
    Ізольований комплекс. Не знає про існування Оазису в Африці.
    Бере енергію суто з Космічного Кільця, над яким проходить лінія.
    """
    def __init__(self, global_ring_reference, location="Hawaii"):
        self.location = location
        self.space_ring = global_ring_reference
        self.TARGET_ALTITUDE = 12000.0  # 12 км
        self.capsule_mass = 1200.0  # кг
        self.bryukho_efficiency = 0.942

    def execute_launch(self):
        print(f"\n[ПУСКОВА ШАХТА — {self.location.upper()}] Иніціалізація пуску капсули UABC.")
        # Шахта просить 500 МДж енергії у космічного кільця
        energy_drawn, success = self.space_ring.extract_energy(500000.0)
        
        if not success:
            print("[ПОМИЛКА] В космічному кільці недостатньо енергії для пуску!")
            return

        print(f"-> Отримано {energy_drawn/1e3:.1f} ГДж енергії з орбітального кільця.")
        
        # Спрощений прорахунок фінішної точки зльоту (чиста фізика на шахті)
        rho_12km = 1.225 * math.exp(-self.TARGET_ALTITUDE / 8500.0)
        optics_at_peak = self.bryukho_efficiency * (1.0 - (0.15 * (rho_12km / 1.225)))
        
        print(f"-> [УСПІХ] Капсула вийшла на {self.TARGET_ALTITUDE/1000} км.")
        print(f"-> Оптична ефективність матриці «Брюхо» на піку: {optics_at_peak*100:.2f}%")


if __name__ == "__main__":
    print("=== ГЛОБАЛЬНА СИМУЛЯЦІЯ СЕТИ: Core/beam-flight+oasis_project.py ===")
    
    # 1. Створюємо єдине космічне енергетичне кільце
    cosmo_ring = GlobalSpaceEnergyRing()
    print(f"Початковий стан Космічного Кільця. Навантаження: {cosmo_ring.ring_load_percent}%, Буфер: {cosmo_ring.orbital_buffer_mj/1e3} ГДж")
    print("-" * 90)

    # 2. Оазис в Африці працює сам по собі (залучає спонсорів, генерує гроші та енергію, знімає напругу)
    oasis_africa = OasisAfricanHub(cosmo_ring)
    oasis_africa.run_daily_balancing()
    print("-" * 90)

    # 3. Пускова шахта на Гаваях працює сама по собі (виводить супутники, споживаючи з кільця)
    hawaii_shaft = PacificLaunchShaft(cosmo_ring, location="Hawaii")
    hawaii_shaft.execute_launch()
    print("-" * 90)
    
    print(f"Фінальний стан Космічного Кільця. Навантаження: {cosmo_ring.ring_load_percent:.2f}%, Буфер: {cosmo_ring.orbital_buffer_mj/1e3:.1f} ГДж")
