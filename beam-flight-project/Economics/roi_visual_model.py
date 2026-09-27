import matplotlib.pyplot as plt

class BeamFlightROIModel:
    def __init__(self):
        self.initial_capex = 15000000.0  # $15 млн
        self.price_per_kg = 400.0        
        self.capsule_payload_kg = 50.0   
        self.cost_per_launch = 19600.0   # Оновлена собівартість пуску (з урахуванням ККД)
        
        # БІЗНЕС-МЕТРИКИ
        self.monthly_opex = 120000.0     # Постійні витрати компанії на місяць (зарплати, оренда)
        self.discount_rate = 0.10        # Ставка дисконтування для VC (10% річних)
        
        self.revenue_per_launch = self.price_per_kg * self.capsule_payload_kg
        self.profit_per_launch = self.revenue_per_launch - self.cost_per_launch
        
    def generate_roi_chart(self, total_months=24, launches_per_month=150):
        months = []
        cumulative_npv = []
        
        current_npv = -self.initial_capex
        
        for month in range(0, total_months + 1):
            months.append(month)
            
            if month == 0:
                cumulative_npv.append(current_npv / 1e6)
                continue
                
            # Операційний прибуток за місяць
            monthly_launch_profit = launches_per_month * self.profit_per_launch
            monthly_net_cash_flow = monthly_launch_profit - self.monthly_opex
            
            # Математика дисконтування (Формула NPV для венчурного аналізу)
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
        plt.axhline(y=0, color='white', linestyle='--', alpha=0.6, label='Точка окупності (NPV = 0)')
        
        # Пошук місяця окупності
        breakeven_month = None
        for i, val in enumerate(cumulative_npv):
            if val >= 0:
                breakeven_month = months[i]
                break
                
        if breakeven_month:
            plt.axvline(x=breakeven_month, color='yellow', linestyle='-.', label=f'Окупність на {breakeven_month}-й місяць')
            
        plt.title('BEAM-FLIGHT: VC-GRADE VENTURE ROI & NPV CURVE (WITH OPEX & DISCOUNTING)', fontsize=11, color='cyan', pad=15)
        plt.xlabel(f'Місяці експлуатації магістралі ({launches_per_month} пусків/місяць)', color='white')
        plt.ylabel('Чиста приведена вартість проєкту (Мільйони USD)', color='white')
        
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend(loc='lower right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    roi_model = BeamFlightROIModel()
    roi_model.generate_roi_chart(total_months=24, launches_per_month=200)
