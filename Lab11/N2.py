import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Налаштування стилю графіків
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# Завантаження даних
print("=" * 80)
print("АНАЛІЗ ВИКОРИСТАННЯ ВЕЛОДОРІЖОК У 2017 РОЦІ (МОНРЕАЛЬ)")
print("=" * 80)

df = pd.read_csv('comptagevelo2017.csv', sep=',', encoding='utf-8')

# 1. Основні характеристики датафрейму
print("\n1. ПЕРШІ 3 РЯДКИ ДАТАФРЕЙМУ:")
print(df.head(3))

print("\n2. ІНФОРМАЦІЯ ПРО ДАТАФРЕЙМ:")
print(df.info())

print("\n3. ОПИСОВА СТАТИСТИКА:")
print(df.describe())

# Обробка даних
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
df = df.dropna(subset=['Date'])
df = df.sort_values('Date')
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.day_name()

# Визначення числових стовпців (велодоріжки)
counter_cols = df.select_dtypes(include=['number']).columns.tolist()
if 'Month' in counter_cols:
    counter_cols.remove('Month')

# Видалення NaN значень для розрахунків
df_clean = df[counter_cols].fillna(0)

print("\n" + "=" * 80)
print("АНАЛІЗ ВЕЛОДОРІЖОК")
print("=" * 80)

print(f"\nКількість велодоріжок: {len(counter_cols)}")
print(f"\nВелодоріжки:")
for i, site in enumerate(counter_cols, 1):
    print(f"  {i}. {site}")

# 2. Загальна кількість велосипедистів за рік (усі велодоріжки)
print("\n" + "=" * 80)
print("ЗАГАЛЬНА СТАТИСТИКА")
print("=" * 80)

total_year_all_sites = df_clean.sum().sum()
print(f"\n✓ Загальна кількість велосипедистів за рік (ВСІ велодоріжки):")
print(f"  {total_year_all_sites:,.0f} велосипедистів")

# 3. Загальна кількість велосипедистів за рік на кожній велодоріжці
print("\n✓ ТОП-10 ВЕЛОДОРІЖОК ПО ПОПУЛЯРНОСТІ:")
print("-" * 80)

total_year_per_site = df_clean.sum().sort_values(ascending=False)
print(f"{'№':<3} {'Велодоріжка':<35} {'Кількість':<20}")
print("-" * 80)
for i, (site, count) in enumerate(total_year_per_site.head(10).items(), 1):
    print(f"{i:<3} {site:<35} {count:>15,.0f}")

# 4. Вибір трьох найпопулярніших велодоріжок
chosen_sites = total_year_per_site.head(3).index.tolist()
print(f"\n✓ ОБРАНІ ДЛЯ АНАЛІЗУ (ТОП-3):")
for i, site in enumerate(chosen_sites, 1):
    print(f"  {i}. {site}: {total_year_per_site[site]:,.0f}")

# 5. Найпопулярніший місяць для кожної з трьох велодоріжок
print("\n" + "=" * 80)
print("НАЙПОПУЛЯРНІШІ МІСЯЦІ (ТОП-3 ВЕЛОДОРІЖОК)")
print("=" * 80)

month_names = {
    1: 'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень',
    5: 'Травень', 6: 'Червень', 7: 'Липень', 8: 'Серпень',
    9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12: 'Грудень'
}

for site in chosen_sites:
    monthly = df.groupby('Month')[site].sum().fillna(0)
    best_month = monthly.idxmax()
    best_value = monthly.max()
    
    print(f"\n✓ Велодоріжка: {site}")
    print(f"  Найпопулярніший місяць: {month_names[best_month]} (місяць {best_month})")
    print(f"  Кількість велосипедистів: {best_value:,.0f}")
    
    # Розгорнута таблиця всіх місяців для цієї велодоріжки
    print(f"\n  Розподіл по місяцях:")
    print(f"  {'Місяць':<15} {'Кількість':<20} {'% від річного':<15}")
    print(f"  {'-'*50}")
    for month in range(1, 13):
        count = monthly[month] if month in monthly.index else 0
        percentage = (count / total_year_per_site[site] * 100) if total_year_per_site[site] > 0 else 0
        print(f"  {month_names[month]:<15} {count:>15,.0f}    {percentage:>6.2f}%")

# 6. Побудова графіків
print("\n" + "=" * 80)
print("ПОБУДОВА ГРАФІКІВ")
print("=" * 80)

# Графік 1: Завантаженість першої велодоріжки по місяцях
site = chosen_sites[0]
monthly_counts = df.groupby('Month')[site].sum().fillna(0)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(monthly_counts.index, monthly_counts.values, color='steelblue', alpha=0.8, edgecolor='navy')
ax.set_title(f'Завантаженість велодоріжки "{site}" по місяцях, 2017', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Місяць', fontsize=12, fontweight='bold')
ax.set_ylabel('Кількість велосипедистів', fontsize=12, fontweight='bold')
ax.set_xticks(range(1, 13))
ax.set_xticklabels([month_names[i] for i in range(1, 13)], rotation=45, ha='right')
ax.grid(True, alpha=0.3, axis='y')

# Додати значення на стовпцях
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,.0f}',
            ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('bike_path_monthly.png', dpi=150, bbox_inches='tight')
print(f"\n✓ Графік 1: Завантаженість '{site}' по місяцях")
print(f"  Збережено як 'bike_path_monthly.png'")
plt.show()

# Графік 2: Порівняння топ-3 велодоріжок
fig, ax = plt.subplots(figsize=(14, 7))

for site in chosen_sites:
    monthly = df.groupby('Month')[site].sum().fillna(0)
    ax.plot(monthly.index, monthly.values, marker='o', label=site, 
            linewidth=2.5, markersize=8)

ax.set_title('Завантаженість ТОП-3 велодоріжок по місяцях, 2017', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Місяць', fontsize=12, fontweight='bold')
ax.set_ylabel('Кількість велосипедистів', fontsize=12, fontweight='bold')
ax.set_xticks(range(1, 13))
ax.set_xticklabels([month_names[i] for i in range(1, 13)], rotation=45, ha='right')
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('bike_paths_comparison.png', dpi=150, bbox_inches='tight')
print(f"\n✓ Графік 2: Порівняння ТОП-3 велодоріжок")
print(f"  Збережено як 'bike_paths_comparison.png'")
plt.show()

# Графік 3: Загальна динаміка всіх велодоріжок
fig, ax = plt.subplots(figsize=(16, 8))

df_plot = df.set_index('Date')[counter_cols].fillna(0)
df_plot.plot(figsize=(16, 8), alpha=0.6, ax=ax)

ax.set_title('Використання УСІХ велодоріжок протягом року 2017 (щодня)', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Дата', fontsize=12, fontweight='bold')
ax.set_ylabel('Кількість велосипедистів', fontsize=12, fontweight='bold')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8, ncol=1)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('all_bike_paths.png', dpi=150, bbox_inches='tight')
print(f"\n✓ Графік 3: Динаміка всіх велодоріжок (щодня)")
print(f"  Збережено як 'all_bike_paths.png'")
plt.show()

# Графік 4: Щомісячна динаміка ТОП-3
fig, ax = plt.subplots(figsize=(14, 7))

monthly_data = []
months_range = range(1, 13)

for site in chosen_sites:
    monthly = df.groupby('Month')[site].sum().fillna(0)
    monthly_data.append([monthly.get(m, 0) for m in months_range])

x = np.arange(len(months_range))
width = 0.25

for i, (site, data) in enumerate(zip(chosen_sites, monthly_data)):
    ax.bar(x + i*width, data, width, label=site, alpha=0.8)

ax.set_title('Щомісячне порівняння ТОП-3 велодоріжок, 2017', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Місяць', fontsize=12, fontweight='bold')
ax.set_ylabel('Кількість велосипедистів', fontsize=12, fontweight='bold')
ax.set_xticks(x + width)
ax.set_xticklabels([month_names[i] for i in months_range], rotation=45, ha='right')
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('monthly_comparison.png', dpi=150, bbox_inches='tight')
print(f"\n✓ Графік 4: Щомісячне порівняння (столбиковий)")
print(f"  Збережено як 'monthly_comparison.png'")
plt.show()

print("\n" + "=" * 80)
print("АНАЛІЗ УСПІШНО ЗАВЕРШЕНО")
print("=" * 80)
print(f"\nГенеровані файли:")
print(f"  • bike_path_monthly.png")
print(f"  • bike_paths_comparison.png")
print(f"  • all_bike_paths.png")
print(f"  • monthly_comparison.png")
print("=" * 80)