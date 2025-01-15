## Start
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HpULUEvMX9avJoM9e7nZlo-rp9qRMne9#scrollTo=jygMdHK6DgN3)

To start the project, use the following command:

```bash
docker-compose up --build
```

## Credits for Grafana

- Datasource: Postgres
- Host URL: postgres:5432
- Database name: benchmark
- Username: admin
- Password: admin
- TLS/SSL Mode: disable

## Dashboard

dashboard.json

## Отчет по выполнению проекта
1. Сбор данных:

    - Ручной ввод данных в Google Sheets. 
    - Остальные данные собирались по частям в разные периоды времени. Для каждого периода был создан отдельный Jupyter Notebook, который может быть предоставлен по запросу.

2. Предобработка данных:

    На этапе обработки данных выполнены следующие действия:
    - Удаление пропусков и выбросов.

    Описание колонок: 

    - prompt:

        Тип: строка.

        Общее количество символов: 107.32k.

        Описание: Исходные запросы, отправляемые в модель.

    - prompt_label:

        Тип: категориальная.

        Количество значений: 2 (например, injection, safe).

        Описание: Метка, характеризующая запрос (например, безопасный или потенциально вредоносный).

    - response:

        Тип: строка.
        
        Общее количество символов: 165.61k.
        
        Описание: Ответы, сгенерированные моделью на запросы.
    
    - response_label:

        Тип: категориальная.
        
        Количество значений: 2 (например, harm, safe).
        
        Описание: Метка, определяющая характер ответа модели (например, вредоносный или безопасный).

    - response_refusal_label:

        Тип: категориальная.
        
        Количество значений: 2 (например, refusal, compliance).
        
        Описание: Метка, характеризующая ответ модели как отказ или выполнение запроса.

    - model:

        Тип: категориальная.
        
        Количество значений: 3.
        
        Описание: Используемая модель (например, разные версии LLM или алгоритмов).
    
    - language:

        Тип: категориальная.
        
        Количество значений: 2.
        
        Описание: Язык запроса и ответа (например, EN, RU).
    
    - source:

        Тип: категориальная.
        
        Количество значений: 10.
        
        Описание: Источник запросов (например, разные наборы данных или сценарии использования).
    
    - prompt_length:

        Тип: целое число (uint32).
        
        Средняя длина: 1014.5k.
        
        Описание: Длина запроса в символах.
    
    - response_length:

        Тип: целое число (uint32).
        
        Средняя длина: 1610.3k.
        
        Описание: Длина ответа в символах.

3. Исследовательский анализ данных (EDA):

    - Проведены базовые визуализации и анализ корреляций.
    - На основе анализа выявлены основные зависимости, которые представлены в виде графиков.

    - Определение и обоснование метрик качества данных
        - Поскольку задача бенчмарка оценить качество моделей для задачи классификации вредоносных промптов и ответов, а также дополнительно повелась ли LLM на этот ответ (что является дополнительным, но не обязательным лейблом), были выбраны стандартные и общепринятые метрики для задачи классификации :  Precision, Recall и F1-score, с уклоном в сторону взвешенной оценки.

        - Использовались метрики, релевантные задаче оценки качества входных данных и ML моделей.

4. Разработка базы данных для хранения данных:

    - Данные сохраняются в базе данных PostgreSQL. Для автоматизации процесса написан скрипт, обеспечивающий их загрузку и управление.

5. Оформление пунктов 1, 2 и 4 в отдельный пайплайн для автоматизации:

    - Создан Python-скрипт для автоматизированной обработки данных, доступный на GitHub. Скрипт включает:
        - Сбор данных из различных источников.
        - Предобработки данных.
        - Вычисление метрик качества данных (Precision, Recall и F1-score).

6. Оформление дашбордов:
    
    Дашборды разработаны на основе Grafana и PostgreSQL для мониторинга и анализа работы моделей машинного обучения (LLM). Основное внимание уделено распределению меток, анализу длины запросов и ответов, а также ключевым метрикам качества моделей.

    Основные элементы дашбордов:

        1. Label Distributions: визуальное представление распределения ключевых категорий меток.
        
        Включает три графика в виде круговых диаграмм:
        
            - Injection/Safe Labels: Отображает количество меток, классифицирующих запросы как безопасные или содержащие потенциальные инъекции.
            
            - Harm/Safe Labels: Показывает распределение меток, связанных с безопасностью ответов (вредные или безопасные).
            
            - Refusal/Compliance Labels: Демонстрирует количество ответов, соответствующих отказу или соблюдению запроса.
            

        2. Метрики качества моделей: оценка производительности моделей по основным метрикам

        Таблица, отображающая значения Precision, Recall и F1-score для различных меток:
            
            - prompt_label: Метки для запросов (например, "injection" или "safe").
            
            - response_label: Метки для ответов (например, "harm" или "safe").
            
            - refusal_label: Метки на соответствие отказа или выполнения запроса.

        
        3. Анализ длины запросов и ответов: анализ сложности запросов и объемов ответов для оптимизации модели

            - Prompt Length Distribution: Гистограмма, отображающая распределение длины запросов.
            
            - Response Length Distribution: Гистограмма, показывающая распределение длины ответов.

        
        4. Данные мониторинга: возможность детального анализа данных и их верификации

            - Таблица с сырыми данными из базы benchmark_llm_monitoring.
            - Содержит: ID, запросы, ответы, метки и другие атрибуты.

    Технические детали:
        
        - Данные: Используется PostgreSQL как источник данных, с таблицей benchmark_llm_monitoring.
        
        - Автоматизация: Дашборды обновляются в режиме реального времени.
        
        - Ценность: Дашборды позволяют оперативно отслеживать ключевые показатели качества работы моделей, идентифицировать возможные проблемы (например, несбалансированные данные), а также предоставляют информацию для улучшения ML пайплайнов.

## Бизнес ценность 

Провели оценку качества моделей Х на созданном бенчмарке и получили следующие результаты:

- **Для prompt**:
  - weighted: Precision: 0.94, Recall: 0.92, F1-Score: 0.92    
- **Для llm_response**:
  - weighted: Precision: 0.93, Recall: 0.92, F1-Score: 0.92

Эти показатели демонстрируют высокую эффективность моделей. Однако, в процессе оценки возникли ограничения, связанные с функциональностью судьи, что могло повлиять на корректность некоторых результатов. 

Бизнес-ценность проведённого исследования заключается в предоставлении инструмента для точной и быстрой оценки ML пайплайнов для задач AI Security/Safety. Это позволяет эффективно выявлять сильные и слабые стороны систем, а также принимать обоснованные решения для их дальнейшей оптимизации и внедрения. Такой подход минимизирует риски, связанные с эксплуатацией моделей в критически важных бизнес-процессах, и улучшает их соответствие поставленным целям.

В особенности данный бенчмарк обращает внимание на такую проблему, как data drift, когда модель выходит на инференс с данными, которые отличаются от тех, что использовались при обучении. Таким образом можно оценить её способность к обобщению и работе с новыми данными.
