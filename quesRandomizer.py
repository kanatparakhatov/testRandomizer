import random
import os

def clean_and_load_questions(input_path):
    """Читает, очищает и загружает вопросы с ответами из файла."""
    with open(input_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    # Объединяем строки в один текст и разделяем на блоки вопросов
    content = '\n'.join(lines)
    questions = content.split('+++++')

    parsed_questions = []
    for question_block in questions:
        lines = question_block.strip().split('\n')
        if len(lines) > 1:
            question = lines[0].strip()
            answers = [line.strip().lstrip('=') for line in lines[1:] if line.strip() and not line.startswith('====')]
            # Если ответов 5, первый — это продолжение вопроса
            if len(answers) == 5:
                question += f" {answers[0]}"
                answers = answers[1:]
            parsed_questions.append((question, answers))
    return parsed_questions

def create_test_variants(questions, num_questions, num_variants, output_dir, subject):
    """Создаёт файлы с уникальными вариантами тестов."""
    if len(questions) < num_questions:
        raise ValueError("Недостаточно вопросов в исходном файле для создания варианта.")

    for variant in range(1, num_variants + 1):
        variant_questions = random.sample(questions, num_questions)
        variant_content = (f"________ topar studenti ___________________________ \"{subject}\" páni ayırmashılıǵı boyinsha qadaǵalaw jumisi. \nVariant-{variant}\n\n" +
            "\n\n".join(
                f"{i+1}. {q}\n" + "\n".join(f"  {chr(97+j)}. {a}" for j, a in enumerate(ans))
                for i, (q, ans) in enumerate(variant_questions)
            )
        )

        output_path = f"{output_dir}/variant_{variant}.txt"
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(variant_content)
        print(f"Создан файл: {output_path}")

if __name__ == "__main__":
    # Пути к файлам
    input_path = "C:/asd/test/akk_qq.txt"
    output_directory = "c:/asd/finishedTest/akk_qq/"

    # Очищаем и загружаем вопросы
    print("Очистка и загрузка вопросов из файла...")
    questions_data = clean_and_load_questions(input_path)

    # Запрос параметров для генерации тестов
    subject = input("Введите предмет: ")
    num_questions = int(input("Введите количество вопросов в одном варианте: "))
    num_variants = int(input("Введите количество вариантов: "))

    # Создание тестовых вариантов
    os.makedirs(output_directory, exist_ok=True)
    create_test_variants(questions_data, num_questions, num_variants, output_directory, subject)
