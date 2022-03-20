# practicum_airflow
1) Скачать репозиторий в папку, из которой будет запускаться контейнер

2) Создать в этой папке директории для монтирования к airflow
mkdir -p ./dags ./logs ./plugins

3) Задать переменную окружения и сохранить в файл .env
echo -e "AIRFLOW_UID=$(id -u)" > .env

4) Скопировать скрипты для DAG-а в примантированную папку
cp ./exchange_dag_v2.py ./insert_to_t_pairs_value_hist_v2.sql ./dags

5) Инициализируем БД
docker-compose up airflow-init

6) Запускаем контейнеры в демоне
docker-compose up -d

7) Убедиться, что все работает (по умолчанию DAG is_paused_upon_creation=False т.е. сразу запустится при старте airflow)
	a) можно залогинившись в UI airflow по адресу <http://host-ip:8080> login:airflow password:airflow
	И(ИЛИ)
	b) сделав запрос к БД
	docker exec ${PWD##*/}_postgres_1 psql -U airflow -c "select * from dev_aae.t_pairs_value_hist;"

8) Чтобы все выключить выполнить команду
docker-compose down --volumes --remove-orphans