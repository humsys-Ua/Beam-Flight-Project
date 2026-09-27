import matplotlib.pyplot as plt

class BeamFlightROIModel:
    def __init__(self):
        self.initial_capex = 15000000.0  # Капітальні інвестиції ($15 млн)
        
        # ОНОВЛЕНІ ПАРАМЕТРИ ЗА ВАШОЮ ПОРАДОЮ
        self.price_per_kg = 500.0        # Комерційна ціна підвищена до $500/кг
        self.capsule_payload_kg = 50.0   # Маса вантажу однієї капсули
        self.cost_per_launch = 19600.0   # Жорстка собівартість пуску (з урахуванням ККД 45%)
        
        self.monthly_opex = 120000.0     # Постійні витрати компанії на місяць
        self.discount_rate = 0.10        # Ставка дисконтування для VC (10%)
        
        # Розрахунок маржинальності з одного пуску
        self.revenue_per_launch = self.price_per_kg * self.capsule_payload_kg  # $25,000
        self.profit_per_launch = self.revenue_per_launch - self.cost_per_launch  # $5,400 чистими
        
    def generate_roi_chart(self, total_months=24, launches_per_month=500):
        months = []
        cumulative_npv = []
        
        current_npv = -self.initial_capex
        
        for month in range(0, total_months + 1):
            months.append(month)
            
            if month == 0:
                cumulative_npv.append(current_npv / 1e6)
                continue
                
            # За вашою порадою: 500 пусків на місяць (16 запусків на день)
            monthly_launch_profit = launches_per_month * self.profit_per_launch # $2,700,000
            monthly_net_cash_flow = monthly_launch_profit - self.monthly_opex   # $2,580,000 чистими!
            
            # Дисконтування (Формула NPV)
            discount_factor = (1 + self.discount_rate) ** (month / 12.0)
            discounted_cash_flow = monthly_net_cash_flow / discount_factor
            
            current_npv += discounted_cash_flow
            cumulative_npv.append(current_npv / 1e6)
            
        self.plot_finance(months, cumulative_npv, launches_per_month)

    def plot_finance(self, months, cumulative_npv, launches_per_month):
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        
        plt.plot(months, cumulative_npv, color='#33cc33', linewidth=3, label='Дисконтований чистий дохід (NPV)')
        plt.axhline(y=-self.initial_capex/1e6, color='#ff3333', linestyle=':', label=f'Стартовий CapEx (${self.initial_capex/1e6:.1f}M)')
        plt.axhline(y=0, color='white', linestyle='--', alpha=0.6, label='Точка беззбитковості (NPV = 0)')
        
        # Пошук місяця окупності
        breakeven_month = None
        for i, val in enumerate(cumulative_npv):
            if val >= 0:
                breakeven_month = months[i]
                break
                
        if breakeven_month:
            plt.axvline(x=breakeven_month, color='yellow', linestyle='-.', label=f'Окупність на {breakeven_month}-й місяць польотів')
            
        plt.title('BEAM-FLIGHT: OPTIMIZED VC-GRADE NPV CURVE (PRICE: $500/KG | 500 LAUNCHES/MO)', fontsize=11, color='cyan', pad=15)
        plt.xlabel(f'Місяці експлуатації магістралі ({launches_per_month} пусків/місяць — ~16 запусків/день)', color='white')
        plt.ylabel('Чиста приведена вартість проєкту (Мільйони USD)', color='white')
        
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend(loc='lower right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    roi_model = BeamFlightROIModel()
    # Запускаємо оптимізовану модель на 24 місяці з 500 пусками на місяць
    roi_model.generate_roi_chart(total_months=24, launches_per_month=500)
