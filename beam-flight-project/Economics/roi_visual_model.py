import matplotlib.pyplot as plt

class BeamFlightROIModel:
    def __init__(self):
        # Первинні фінансові параметри (Венчурний масштаб)
        self.initial_capex = 15000000.0  # Капітальні інвестиції на Фазу 1.5/2 ($15 млн)
        self.price_per_kg = 400.0        # Комерційна ціна доставки для клієнтів за 1 кг
        self.capsule_payload_kg = 50.0   # Маса вантажу однієї капсули Beam-Mini
        self.cost_per_launch = 12000.0   # Собівартість пуску з нашої технічної cost_model.py
        
        # Розрахунок маржинальності
        self.revenue_per_launch = self.price_per_kg * self.capsule_payload_kg
        self.profit_per_launch = self.revenue_per_launch - self.cost_per_launch
        
    def generate_roi_chart(self, max_launches=3000):
        launches = []
        net_financial_position = []
        
        # Прораховуємо фінансовий стан стартапу з кожним новим запуском
        for current_launch in range(0, max_launches + 1, 50):
            launches.append(current_launch)
            # Позиція = (Кількість пусків * Прибуток з пуску) - Стартові інвестиції
            current_position = (current_launch * self.profit_per_launch) - self.initial_capex
            net_financial_position.append(current_position / 1e6) # Переводимо в Мільйони $
            
        self.plot_finance(launches, net_financial_position)

    def plot_finance(self, launches, net_financial_position):
        """Побудова професійного фінансового графіка окупності для Pitch Deck"""
        plt.style.use('dark_background')
        plt.figure(figsize=(10, 6))
        
        # Будуємо криву накопиченого прибутку
        plt.plot(launches, net_financial_position, color='#33cc33', linewidth=3, label='Чистий баланс проєкту (Net Profit)')
        
        # Лінія початкових інвестицій (червона зона збитків)
        plt.axhline(y=-self.initial_capex/1e6, color='#ff3333', linestyle=':', label=f'Стартовий капітал (CapEx: ${self.initial_capex/1e6:.1f}M)')
        
        # Лінія беззбитковості (Нульовий баланс)
        plt.axhline(y=0, color='white', linestyle='--', alpha=0.6, label='Точка беззбитковості (Break-even)')
        
        # Математичний пошук точної точки окупності
        exact_breakeven_launches = int(self.initial_capex / self.profit_per_launch)
        plt.axvline(x=exact_breakeven_launches, color='yellow', linestyle='-.', 
                    label=f'Окупність: {exact_breakeven_launches} пусків конвеєра')
        
        # Оформлення графіка
        plt.title('BEAM-FLIGHT: FINANCIAL ROI & INVESTMENT RECOVERY CURVE', fontsize=12, color='cyan', pad=15)
        plt.xlabel('Кількість комерційних запусків капсул UABC (Конвеєрний потік)', color='white')
        plt.ylabel('Фінансовий результат (Мільйони USD)', color='white')
        
        # Додаткові текстові блоки для інвесторів
        plt.text(100, -self.initial_capex/1e6 + 0.5, '🔴 ЗОНА РИЗИКУ (CapEx)', color='#ff6666', fontsize=10)
        plt.text(exact_breakeven_launches + 100, 2.0, '🟢 ЧИСТИЙ ПРИБУТОК (ROI)', color='#66ff66', fontsize=10)
        
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.legend(loc='lower right')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    roi_model = BeamFlightROIModel()
    # Будуємо фінансовий графік на перші 3000 запусків
    roi_model.generate_roi_chart(max_launches=3000)
