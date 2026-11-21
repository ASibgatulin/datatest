import pandas as pd
import io

# загружаем datatest
df = pd.read_csv('dataset.csv')

def _print_both(msg, file_obj):
    print(msg)
    print(msg, file=file_obj)

def main():
    # Открываем файл report
    with open('report.txt', 'w', encoding='utf-8') as f:
        _print_both(f"Размер датасета: {df.shape}", f)

        buffer = io.StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        _print_both(info_str, f)

        null_counts = df.isnull().sum()
        _print_both("Пропуски по колонкам:", f)
        _print_both(null_counts.to_string(), f)

        categorical_cols = ['anaemia', 'diabetes', 'high bp']
        actual_categorical = [col for col in df.columns if col in categorical_cols]
        numeric_cols = [col for col in df.columns if col not in actual_categorical]

        _print_both("\nСтатистика для счётных колонок (среднее; медиана; std):", f)
        _print_both("Колонка> среднее; медиана; отклонение", f)
        for col in numeric_cols:
            mean_val = df[col].mean()
            median_val = df[col].median()
            std_val = df[col].std()
            _print_both(f"{col}> {mean_val:.2f}; {median_val:.2f}; {std_val:.2f}", f)

        _print_both("\nКатегориальные признаки:", f)
        for col in actual_categorical:
            _print_both(f"\n{col}:", f)
            _print_both(df[col].value_counts().to_string(), f)

if __name__ == '__main__':
    main()