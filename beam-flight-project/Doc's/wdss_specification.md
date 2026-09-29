# Engineering Specification: WDSS (Wavefront Distortion Scanning System)

## 1. Subsystem Architecture & Operational Principles
The WDSS serves as the primary diagnostic sensor layer for ADAOS, continuously analyzing the atmospheric optical path to calculate phase conjugations before the high-energy propulsion laser fires.

*   **Atmospheric Reference Probe (Rayleigh Rayleigh Lidar):** A high-frequency pulsed Nd:YAG green laser ($\lambda = 532$ nm) co-axial to the main power laser. It generates an artificial "guide star" or scattering column in the upper mesosphere (80 km), providing a stable phase reference.
*   **Microlens Hartmann Array:** A matrix of $64 \times 64$ high-grade fused silica square microlenses (4,096 sub-apertures total). Each microlens focuses its segment of the returning wavefront onto a localized zone of the sensor.
*   **Ultra-Fast CMOS Sensor Node:** A back-illuminated, high-quantum-efficiency photon sensor linked to the microlens array. It captures the localized focal spot displacements caused by atmospheric refractive index fluctuations ($C_n^2$).

## 2. Signal Processing & Actuator Feedback Loop
The processing pipeline converts optical deflection into mechanical mirror adjustments through a real-time matrix algorithm:

*   **Spot Centroid Detection:** The CMOS sensor maps the $(X, Y)$ coordinate shift of all 4,096 focal spots relative to their ideal calibration positions.
*   **Vector Gradient Computation:** Spot displacements are translated into local wavefront slope vectors $(\partial \phi / \partial x, \partial \phi / \partial y)$.
*   **Zernike Polynomial Reconstruction:** The compute cluster uses the vector gradients to reconstruct the complete phase error profile $\phi(x,y)$ using Zernike polynomial expansion up to the 55th radial order.
*   **Voltage Command Generation:** The phase profile is inverted and translated directly into 1,024 high-voltage control signals sent to the ADAOS piezo-actuators to flatten the wavefront.

## 3. Technical Specifications Matrix
*   **Wavefront Sensor Type:** Fused Silica Shack-Hartmann Microlens Array
*   **Sub-Aperture Grid Resolution:** $64 \times 64$ (4,096 sampling points)
*   **Sampling and Frame Rate:** 5.0 kHz (5,000 spatial profiles per second)
*   **Reference Laser Wavelength:** 532 nm (Pulsed, 120 mJ per pulse)
*   **Processing Latency (Sensor to FPGA Loop):** $\le 85$ microseconds ($\mu$s)
*   **Wavefront Phase Error Resolution:** $\le \lambda/50$ ($\approx 21$ nm)
*   **Dynamic Range of Distortion Tracking:** $\pm 18 \, \mu$rad
*   **Sensor Interface Architecture:** Direct PCIe Gen5 / Custom FPGA Fabric Interconnect

---

# Інженерна специфікація: WDSS (Система сканування спотворень хвильового фронту)

## 1. Архітектура підсистеми та принципи роботи
WDSS виконує роль головного діагностичного сенсорного шару для системи ADAOS, безперервно аналізуючи оптичний шлях в атмосфері для розрахунку фазових спряжень перед пострілом високоенергетичного силового лазера.

*   **Атмосферний еталонний зонд (Рейлеївський лідар):** Високочастотний імпульсний зелений лазер Nd:YAG ($\lambda = 532$ нм), встановлений коаксіально (на одній осі) з основним силовим лазером. Він створює штучну «гід-зірку» або стовп розсіювання у верхній мезосфері (80 км), забезпечуючи стабільну фазову опору.
*   **Мікролінзова матриця Гартмана:** Сітка з $64 \times 64$ високоякісних квадратних мікролінз із плавленого кварцу (всього 4,096 субапертур). Кожна мікролінза фокусує свій сегмент повернутого хвильового фронту на локалізовану зону сенсора.
*   **Надшвидкісний сенсорний вузол CMOS:** Зворотньо-освітлений фотосенсор із високою квантовою ефективністю, інтегрований з мікролінзовою матрицею. Він фіксує зміщення локальних фокальних плям, викликані флуктуаціями показника заломлення атмосфери ($C_n^2$).

## 2. Обробка сигналів та контур зворотного зв'язку
Програмно-апаратний контур перетворює оптичне відхилення променя на механічне коригування дзеркала за допомогою матричного алгоритму в реальному часі:

*   **Детекція центроїдів плям:** CMOS-сенсор визначає зсув координат $(X, Y)$ усіх 4,096 фокальних плям відносно їхніх ідеальних калібрувальних позицій у вакуумі.
*   **Розрахунок векторних градієнтів:** Зміщення плям транслюються у вектори локальних нахилів хвильового фронту $(\partial \phi / \partial x, \partial \phi / \partial y)$.
*   **Реконструкція поліномів Церніке:** Обчислювальний кластер використовує векторні градієнти для відновлення повного профілю фазової помилки $\phi(x,y)$ за допомогою розкладання в ряд за поліномами Церніке до 55-го радіального порядку.
*   **Генерація вольт-команд:** Отриманий профіль фази інвертується і перетворюється безпосередньо в 1,024 високовольтних сигнали керування, які надсилаються на п'єзоактуатори ADAOS для вирівнювання хвильового фронту.

## 3. Матриця технічних характеристик
*   **Тип датчика хвильового фронту:** Кварцова мікролінзова матриця Шака-Гартмана
*   **Роздільна здатність сітки субапертур:** $64 \times 64$ (4,096 точок дискретизації)
*   **Частота дискретизації та кадрів:** 5.0 кГц (5,000 просторових профілів на секунду)
*   **Довжина хвилі опорного лазера:** 532 нм (імпульсний, 120 мДж в імпульсі)
*   **Затримка обробки даних (цикл «сенсор-FPGA»):** $\le 85$ мікросекунд ($\mu$с)
*   **Точність визначення фазової помилки:** $\le \lambda/50$ ($\approx 21$ нм)
*   **Динамічний діапазон відстеження спотворень:** $\pm 18$ мкрад
*   **Архітектура інтерфейсу сенсора:** Пряме з'єднання PCIe Gen5 / Спеціалізована топологія шини FPGA
