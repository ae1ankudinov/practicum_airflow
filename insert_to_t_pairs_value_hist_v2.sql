--insert to t_pairs_value_hist
insert into dev_aae.t_pairs_value_hist
(pair_name, calendar_dt, exchange_rate)
values
(%(pair_name)s, %(calendar_dt)s, '{{ ti.xcom_pull(task_ids="get_data", key="return_value") }}')
on conflict(pair_name, calendar_dt)
do update 
    set exchange_rate = '{{ ti.xcom_pull(task_ids="get_data", key="return_value") }}', updated_ttmp = current_timestamp;