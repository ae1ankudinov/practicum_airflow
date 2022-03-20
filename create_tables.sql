--alter user airflow WITH PASSWORD '123';

create schema if not exists dev_aae;

create table if not exists dev_aae.t_pairs_value_hist (
	  pair_name varchar(50) check (pair_name in ('BTC/USD'))
	, calendar_dt date
	, exchange_rate decimal(18,6)
	, inserted_ttmp timestamp default current_timestamp
	, updated_ttmp timestamp default current_timestamp
	, constraint pk_t_pairs_value_hist primary key(pair_name, calendar_dt)
);
