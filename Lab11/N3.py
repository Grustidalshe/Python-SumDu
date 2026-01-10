import nltk
from nltk.corpus import gutenberg, stopwords
from nltk import FreqDist
import string
import matplotlib.pyplot as plt

# Налаштування шрифту для кращого відображення
plt.rcParams['font.size'] = 10

# Завантаження необхідних ресурсів NLTK
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

print("=" * 80)
print("АНАЛІЗ ТЕКСТУ 'BRYANT-STORIES.TXT' (Project Gutenberg)")
print("=" * 80)

# 1. Завантаження тексту та визначення кількості слів
words = gutenberg.words('bryant-stories.txt')
total_words = len(words)
print(f"\n1. ЗАГАЛЬНА КІЛЬКІСТЬ СЛІВ У ТЕКСТІ: {total_words:,}")

# 2. Топ-10 найбільш вживаних слів (усі слова)
print("\n" + "=" * 80)
print("2. ТОП-10 НАЙБІЛЬШ ВЖИВАНИХ СЛІВ (ВСІ СЛОВА)")
print("=" * 80)

fdist_all = FreqDist(words)
top10_all = fdist_all.most_common(10)

print(f"\n{'№':<3} {'Слово':<20} {'Кількість':<15}")
print("-" * 40)
for i, (word, count) in enumerate(top10_all, 1):
    print(f"{i:<3} {word:<20} {count:<15}")

# Побудова діаграми для всіх слів
fig, ax = plt.subplots(figsize=(14, 7))
words_all, counts_all = zip(*top10_all)

# Екранування спецсимволів для відображення
words_display = [f"'{w}'" if w in string.punctuation else w for w in words_all]

bars = ax.bar(range(len(words_all)), counts_all, color='steelblue', alpha=0.8, edgecolor='navy')
ax.set_title('ТОП-10 найбільш вживаних слів (усі слова)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Слово', fontsize=13, fontweight='bold')
ax.set_ylabel('Кількість входжень', fontsize=13, fontweight='bold')
ax.set_xticks(range(len(words_all)))
ax.set_xticklabels(words_display, rotation=45, ha='right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Додати значення на стовпцях
for i, (word, count) in enumerate(top10_all):
    ax.text(i, count, f'{count:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('top10_all_words.png', dpi=150, bbox_inches='tight')
print("\n✓ Діаграма збережена як 'top10_all_words.png'")
plt.show()

# 3. Очищення: видалення стоп-слів та пунктуації
print("\n" + "=" * 80)
print("3. ОЧИЩЕННЯ ТЕКСТУ (видалення стоп-слів та пунктуації)")
print("=" * 80)

stop_words = set(stopwords.words('english'))

# Фільтрація: тільки алфавітні слова, без стоп-слів, у нижньому регістрі
filtered_words = [w.lower() for w in words if w.isalpha() and w.lower() not in stop_words]
filtered_count = len(filtered_words)

print(f"\nКількість слів після очищення: {filtered_count:,}")
print(f"Видалено стоп-слів та пунктуації: {total_words - filtered_count:,}")

# 4. Топ-10 після очищення
print("\n" + "=" * 80)
print("4. ТОП-10 НАЙБІЛЬШ ВЖИВАНИХ СЛІВ (ПІСЛЯ ОЧИЩЕННЯ)")
print("=" * 80)

fdist_filtered = FreqDist(filtered_words)
top10_filtered = fdist_filtered.most_common(10)

print(f"\n{'№':<3} {'Слово':<20} {'Кількість':<15}")
print("-" * 40)
for i, (word, count) in enumerate(top10_filtered, 1):
    print(f"{i:<3} {word:<20} {count:<15}")

# Побудова діаграми для очищених слів
fig, ax = plt.subplots(figsize=(14, 7))
words_filtered, counts_filtered = zip(*top10_filtered)

bars = ax.bar(range(len(words_filtered)), counts_filtered, color='darkgreen', alpha=0.8, edgecolor='darkblue')
ax.set_title('ТОП-10 найбільш вживаних слів (після очищення)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Слово', fontsize=13, fontweight='bold')
ax.set_ylabel('Кількість входжень', fontsize=13, fontweight='bold')
ax.set_xticks(range(len(words_filtered)))
ax.set_xticklabels(words_filtered, rotation=45, ha='right', fontsize=11)
ax.grid(True, alpha=0.3, axis='y')

# Додати значення на стовпцях
for i, (word, count) in enumerate(top10_filtered):
    ax.text(i, count, f'{count:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('top10_filtered_words.png', dpi=150, bbox_inches='tight')
print("\n✓ Діаграма збережена як 'top10_filtered_words.png'")
plt.show()

# 5. Порівняльна статистика
print("\n" + "=" * 80)
print("ПІДСУМКОВА СТАТИСТИКА")
print("=" * 80)
print(f"\nЗагальна кількість слів: {total_words:,}")
print(f"Після очищення: {filtered_count:,}")
print(f"Унікальних слів (всіх): {len(fdist_all):,}")
print(f"Унікальних слів (очищених): {len(fdist_filtered):,}")
print(f"\nЗгенеровані файли:")
print(f"  • top10_all_words.png")
print(f"  • top10_filtered_words.png")
print("=" * 80)