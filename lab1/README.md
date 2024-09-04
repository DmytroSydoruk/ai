### 1. Що таке дерево простору станів?

**Дерево простору станів** — це абстрактна структура, яка використовується для моделювання процесу розв'язування задачі шляхом пошуку. Воно складається з вузлів (вершин) і ребер. Кожен вузол представляє стан системи, а ребра — можливі дії або переходи між станами. Кореневий вузол дерева відповідає початковому стану задачі, а листяні вузли можуть представляти кінцеві (цільові) стани.

### 2. Опишіть особливості рішення логічних задач методом пошуку в просторі станів.

Метод пошуку в просторі станів полягає у розгляді всіх можливих послідовностей дій, які можуть призвести від початкового до цільового стану. Основні особливості цього підходу:

- **Визначення станів**: Кожен стан — це окремий вузол дерева, який представляє конкретну ситуацію або конфігурацію системи.
- **Визначення дій**: Кожна дія переводить систему з одного стану в інший.
- **Цільовий стан**: Процес пошуку завершується, коли досягається вузол, що відповідає цільовому стану.
- **Алгоритм пошуку**: Може бути різним — від неінформативного (наприклад, пошук в ширину або в глибину) до інформативного (наприклад, A\* або пошук за евристиками).

### 3. Які види неінформативного пошуку ви знаєте? Охарактеризуйте їх.

**Неінформативний пошук** (також відомий як сліпий пошук) не використовує додаткової інформації про простір станів. Основні види:

- **Пошук в ширину (Breadth-First Search, BFS)**:

  - Перевіряє всі можливі стани на одному рівні перед переходом на наступний рівень.
  - Гарантує знаходження оптимального рішення (найкоротшого шляху), якщо таке існує.
  - Недолік: потребує багато пам'яті.

- **Пошук в глибину (Depth-First Search, DFS)**:

  - Поглиблюється у кожну гілку дерева до досягнення кінцевого стану або тупика, після чого повертається до останнього розгалуження.
  - Перевага: потребує менше пам'яті.
  - Недолік: не гарантує знаходження оптимального рішення і може застрягнути в нескінченних гілках.

- **Ітеративне поглиблення (Iterative Deepening Depth-First Search, IDDFS)**:

  - Комбінує підходи пошуку в ширину та глибину: виконує пошук в глибину з обмеженням на глибину, поступово збільшуючи це обмеження.
  - Перевага: знаходить оптимальний шлях і потребує менше пам'яті, ніж BFS.

- **Пошук за рівнем вартості (Uniform-Cost Search, UCS)**:
  - Подібний до BFS, але враховує вартість переходу між станами, віддаючи перевагу шляхам з меншою сумарною вартістю.

### 4. Що таке інформативний пошук? Які задачі ним вирішуються?

**Інформативний пошук** (також відомий як евристичний пошук) використовує додаткову інформацію про простір станів, щоб спрямувати пошук у напрямку цільового стану. Інформативний пошук вирішує задачі, де потрібно знайти оптимальний шлях або мінімізувати кількість кроків до цільового стану.

**Задачі, які ним вирішуються:**

- Оптимізаційні задачі, де потрібно знайти найкоротший шлях, наприклад, задача комівояжера.
- Задачі, де необхідно враховувати вартість кроків або часові обмеження, наприклад, пошук шляху в графі з урахуванням ваги ребер.

### 5. Які алгоритми інформативного пошуку ви знаєте?

Основні алгоритми інформативного пошуку:

- **Пошук A\***:

  - Використовує евристичну функцію для оцінки відстані від поточного стану до цільового і функцію вартості для оцінки вже пройденого шляху.
  - Гарантує знаходження оптимального рішення, якщо евристика є допустимою (не переоцінює відстань до цілі).

- **Пошук з найменшими витратами (Greedy Best-First Search)**:

  - Використовує тільки евристичну функцію для вибору наступного стану, що може призвести до швидшого знаходження рішення, але не гарантує його оптимальності.

- **Алгоритм пошуку ітеративного поглиблення з евристикою (IDA\*)**:
  - Комбінує підхід ітеративного поглиблення з евристичною оцінкою, що дозволяє ефективніше знаходити рішення з обмеженими ресурсами.

### 6. Що таке пошук в умовах протидії?

**Пошук в умовах протидії** використовується в ситуаціях, де присутні кілька сторін (наприклад, два гравці в грі), які мають протилежні цілі. У таких умовах кожна сторона намагається максимізувати свій результат, одночасно мінімізуючи результат опонента. Цей тип пошуку часто використовується в ігрових задачах, таких як шахи або шашки.

### 7. Опишіть алгоритм «мінімакса» та його модифікацію – альфа-бета відсікання.

- **Алгоритм «мінімакса»**:

  - Використовується для ігор з нульовою сумою, де один гравець намагається максимізувати свій виграш (Max), а інший — мінімізувати виграш опонента (Min).
  - Дерево гри розглядається, починаючи з поточного стану, і кожен можливий хід оцінюється з точки зору найгіршого для опонента (мінімакса).

- **Альфа-бета відсікання**:
  - Це оптимізація алгоритму «мінімакса», що дозволяє відсікати певні гілки дерева гри, які не впливають на кінцеве рішення.
  - Використовуються дві змінні: альфа (максимальне значення для Max) і бета (мінімальне значення для Min). Якщо під час перегляду гілки виявляється, що певна гілка не може покращити поточне рішення, вона відсікається.

### 8. Дослідіть та охарактеризуйте реалізацію програм для гри в шахи.

Програми для гри в шахи, як правило, використовують комбінацію наступних методів:

- **Пошук в просторі станів**: Визначається можливий набір ходів для кожного гравця та генерується дерево можливих ходів.
- **Алгоритм «мінімакса»**: Використовується для оцінки кожного можливого ходу.
- **Альфа-бета відсікання**: Дозволяє значно зменшити кількість перевірених ходів, що покращує ефективність.
- **Евристики**: Використовуються для оцінки проміжних позицій, що дозволяє приймати рішення навіть без повного аналізу дерева можливостей.
- **Таблиці заготовлених кінцівок**: Містять попередньо прораховані оптимальні стратегії для певних кінцевих позицій.

### 9. Чи можна скласти кубик Рубика методом пошуку в просторі станів? Якщо так, то поясніть яким чином. Якщо ні – чому?

Так, кубик Рубика можна скласти методом пошуку в просторі станів. Кожна конфігурація кубика Рубика — це окремий стан, а кожне обертання — дія, яка переводить кубик у новий стан. Цільовий стан — це конфігурація, де всі грані кубика одноколірні.

**Як це працює:**

- **Пошук в ширину (BFS)**: Гарантує знаходження оптимального рішення, але через величезний простір станів (кожне обертання може призводити до 43 трильйонів можливих конфігура

цій) потребує великих ресурсів.

- **Пошук A\***: Може бути більш ефективним, якщо використовується хороша евристика, яка оцінює, наскільки поточний стан близький до цільового.

**Виклики:**

- Великий простір станів робить традиційний пошук неефективним для реального часу, тому використовуються оптимізовані алгоритми, такі як метод Фрідріха, що дозволяє швидше досягати цільового стану з мінімальною кількістю ходів.