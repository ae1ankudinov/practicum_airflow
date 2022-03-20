# practicum_airflow
1) Скачать репозиторий в папку, из которой будет запускаться контейнер<br>
```git clone https://github.com/ae1ankudinov/practicum_airflow.git```

2) Создать в этой папке директории для монтирования к airflow<br>
```mkdir -p ./dags ./logs ./plugins```

3) Задать переменную окружения и сохранить в файл .env<br>
```echo -e "AIRFLOW_UID=$(id -u)" > .env```

4) Скопировать скрипты для DAG-а в примантированную папку<br>
```cp ./exchange_dag_v2.py ./insert_to_t_pairs_value_hist_v2.sql ./dags```

5) Инициализируем БД<br>
```docker-compose up airflow-init```

6) Запускаем контейнеры в демоне<br>
```docker-compose up -d```

7) Убедиться, что все работает (по умолчанию DAG is_paused_upon_creation=False т.е. сразу запустится при старте airflow)<br>
	- можно залогинившись в UI airflow по адресу <http://host-ip:8080> login:airflow password:airflow<br>
	И(ИЛИ)<br>
	- сделав запрос к БД<br>
	```docker exec ${PWD##*/}_postgres_1 psql -U airflow -c "select * from dev_aae.t_pairs_value_hist;"```

8) Чтобы все выключить выполнить команду<br>
```docker-compose down --volumes --remove-orphans```
