# Engineering Specification: "Oasis" Ground Energy Grid & Adaptive Mast Architecture

## 1. Grid Infrastructure & Spatial Adaptability
The "Oasis" ground-based complex is a decentralized, high-capacity electrical distribution network that powers the laser phased arrays. The core innovation of the Oasis protocol lies in its highly modular and dynamically adaptive geometric configuration.

*   **Dynamic Telescopic Masts:** The emitter stations are mounted on high-load, multi-stage hydraulic telescopic mast assemblies. Unlike static setups, these structures can alter their vertical elevation and horizontal deployment area based on operational needs.
*   **Operational Topology Tuning:** The layout changes to compensate for seasonal atmospheric density fluctuations, cloud ceiling levels, and specific orbital inclination requirements of the payload target.
*   **Power Distribution Backplane:** Grid power is supplemented by a 5.8 GHz wireless power transmission (WPT) microwave link system to feed distant phase-locking control nodes without relying on heavy copper ground cabling.

## 2. Dynamic Mast Control & Geometry Protocol
*   **Vertical Height Range ($H_z$):** 15 meters (retracted/storm-safe state) to 75 meters (maximum operating extension to clear ground mist layer).
*   **Horizontal Footprint Expansion ($A_{xy}$):** Scalable from a compact $10 \times 10$ m base up to an expanded $45 \times 45$ m stabilizing footprint via automated outriggers for high-wind scenarios.
*   **Mast Positioning Latency:** Full actuation and reconfiguration completed in $\le 180 \text{ seconds}$.
*   **Structural Load Rating:** Capable of stabilizing an 8.5-ton ADAOS mirror/laser optical assembly at full extension under wind speeds up to 45 m/s.
*   **Grid Coupling Frequency:** Synchronized multi-phase power distribution with sub-nanosecond phase-locking between separated emitter nodes.

---

# Інженерна специфікація: Наземний енергокомплекс «Оазис» та архітектура адаптивних щогл

## 1. Інфраструктура мережі та просторова адаптивність
Наземний комплекс «Оазис» являє собою децентралізовану високопотужну мережу розподілу електроенергії, яка живить лазерні фазовані решітки. Головна інновація протоколу «Оазис» полягає в його модульності та динамічно адаптивній геометричній конфігурації.

*   **Динамічні телескопічні щогли:** Станції випромінювачів змонтовані на високовантажних багаторівневих гідравлічних телескопічних щоглах. На відміну від статичних споруд, ці конструкції здатні змінювати свою вертикальну висоту та горизонтальну площу розгортання залежно від поточних потреб системи.
*   **Юстирування операційної топології:** Зміна геометрії комплексу дозволяє компенсувати сезонні коливання щільності атмосфери, висоту нижньої межі хмар та специфічні вимоги до нахилу орбіти цільового корисного вантажу.
*   **Енергетична розподільча шина:** Живлення від провідної мережі доповнюється системою бездротової передачі енергії (WPT) на частоті 5.8 ГГц для живлення віддалених вузлів фазової синхронізації без прокладання важких наземних кабелів.

## 2. Протокол керування та геометрія адаптивних щогл
*   **Діапазон вертикальної висоти ($H_z$):** від 15 метрів (складений/штормовий стан) до 75 метрів (максимальне робоче висування для виходу вище рівня приземного туману).
*   **Горизонтальне розширення площі ($A_{xy}$):** Масштабується від компактної бази $10 \times 10$ м до розширеної опорної площі $45 \times 45$ м за допомогою автоматичних виносних опор (аутригерів) для роботи в умовах сильного вітру.
*   **Швидкість реконфігурації щогли:** Повна зміна висоти та фіксація геометрії займає $\le 180$ секунд.
*   **Граничне структурне навантаження:** Надійна стабілізація 8.5-тонного оптичного блоку лазера/ADAOS на максимальній висоті при швидкості вітру до 45 м/с.
*   **Фазова синхронізація вузлів:** Суб-наносекундне узгодження фаз розподіленої генерації між просторово рознесеними щоглами випромінювачів.
