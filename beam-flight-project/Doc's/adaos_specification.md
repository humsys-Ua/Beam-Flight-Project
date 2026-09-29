# Engineering Specification: ADAOS (Active Dynamic Adaptive Optics System)

## 1. System Architecture & Components
The ADAOS infrastructure is a closed-loop optoelectronic framework deployed at the ground-based launch matrices to actively neutralize atmospheric wavefront distortions and prevent thermal blooming.

*   **Wavefront Sensing Core:** A high-speed Shack-Hartmann sensor matrix operating in tandem with a reference green pilot laser ($\lambda = 532$ nm). It samples the atmospheric column distortion 5,000 times per second.
*   **Deformable Mirror Matrix (DMM):** A 6.5-meter primary mirror system backed by a matrix of 1,024 high-voltage, low-stroke piezoelectric actuators. The mirror substrate is made of low-expansion ultra-thin beryllium coated with high-reflectivity dielectric layers.
*   **Real-Time Compute Engine:** A dedicated FPGA/GPU tensor-core cluster that solves wavefront reconstruction equations with a processing latency of $\le 0.15$ ms.

## 2. Setup, Calibration, and Phase Alignment
The system utilizes a three-stage calibration protocol to guarantee optical line-of-sight stabilization:

*   **Static Interference Calibration:** Conducted daily in clean-air state using an internal laser interferometer to map and store the structural manufacturing imperfections of the mirror substrate.
*   **Atmospheric Reference Probe:** 2.0 seconds before launch, the 532 nm pilot laser fires along the projected capsule trajectory (Z-axis). The Shack-Hartmann sensor measures the atmospheric phase error matrix.
*   **Dynamic Closed-Loop Cross-Talk Tuning:** Active during flight. Actuators utilize differential coordinate maps to eliminate inter-actuator mechanical stress, ensuring clean, continuous surface adaptation.

## 3. Technical Specifications Matrix
*   **Actuator Type:** Multilayer Piezoelectric PZT (Lead Zirconate Titanate) Stack
*   **Total Actuator Count:** 1,024 units
*   **Adjustment Frequency:** 5.0 kHz (5,000 corrections per second)
*   **Actuator Stroke Range:** 0 to 15 µm
*   **Surface Flattening Precision:** $\le \lambda/20$ at 1.06 µm ($\approx 53$ nm)
*   **Target Beam Spot Jitter Limit:** $\le 0.01$ mm at 12 km altitude
*   **Maximum Incident Thermal Load:** 600 MW (pulsed, 45 seconds duration)
*   **Reflectivity Index:** 99.97% at $\lambda = 1.06$ µm

---

# Інженерна специфікація: ADAOS (Активна динамічна адаптивна оптична система)

## 1. Архітектура системи та компоненти
Інфраструктура ADAOS є оптоелектронною системою із замкнутим контуром керування, яка розгорнута на наземних пускових матрицях для активної нейтралізації спотворень хвильового фронту та запобігання тепловому лінзуванню атмосфери.

*   **Ядро зчитування хвильового фронту:** Високошвидкісна матриця датчиків Шака-Гартмана, яка працює в тандемі з еталонним зеленим пілот-лазером ($\lambda = 532$ нм). Система сканує спотворення атмосферного стовпа 5,000 разів на секунду.
*   **Матриця деформівних дзеркал (DMM):** Головна 6.5-метрова дзеркальна система, підтримувана матрицею з 1,024 високовольтних п'єзоелектричних приводів (актуаторів) з малим ходом. Підкладка дзеркала виготовлена з надтонкого берилію з низьким коефіцієнтом термічного розширення та покрита високовідбиваючими діелектричними шарами.
*   **Обчислювальний модуль реального часу:** Спеціалізований тензорний кластер FPGA/GPU, який розв'язує рівняння реконструкції хвильового фронту з латентністю обробки даних $\le 0.15$ мс.

## 2. Налаштування, калібрування та фазове узгодження
Система використовує триетапний протокол калібрування для гарантування стабілізації оптичної лінії прямої видимості:

*   **Статичне інтерференційне калібрування:** Проводиться щодня в умовах чистого повітря за допомогою внутрішнього лазерного інтерферометра для картографування та збереження в пам'яті структурних дефектів виготовлення дзеркальної підкладки.
*   **Атмосферне зондування:** За 2.0 секунди до старту пілотний лазер 532 нм робить постріл уздовж прогнозованої траєкторії капсули (вісь Z). Датчик Шака-Гартмана вимірює матрицю фазових помилок атмосфери.
*   **Динамічне налаштування перехресних перешкод:** Активне безпосередньо під час польоту. Актуатори використовують диференціальні координатні карти для усунення механічного напруження між сусідніми приводами, забезпечуючи чисту та плавну адаптацію поверхні.

## 3. Матриця технічних характеристик
*   **Тип актуатора:** Багатошаровий п'єзоелектричний пакет PZT (титанат-цирконат свинцю)
*   **Загальна кількість актуаторів:** 1,024 одиниці
*   **Частота юстирування:** 5.0 кГц (5,000 коригувань поверхні на секунду)
*   **Діапазон ходу актуатора:** від 0 до 15 мкм
*   **Точність вирівнювання поверхні:** $\le \lambda/20$ при 1.06 мкм ($\approx 53$ нм)
*   **Максимальний допуск зміщення плями променя:** $\le 0.01$ мм на висоті 12 км
*   **Максимальне падаюче теплове навантаження:** 600 МВт (імпульсне, тривалістю 45 секунд)
*   **Коефіцієнт відбиття дзеркала:** 99.97% при $\lambda = 1.06$ мкм
