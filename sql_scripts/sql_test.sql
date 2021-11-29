1.How many total messages are being sent every day?
Sol:
select convert(date,createdAt) as createdAt,count(*) as cnt from  message
group by convert(date,createdAt);

2.Are there any users that did not receive any message?
Sol:
select distinct case when id is not null then 'Yes' else 'No' end as users_did_not_receive_any_message
from (select distinct u.id from users u left join message m
on u.id = m.receiverId
where m.receiverId is not null) a;

3.How many active subscriptions do we have today?
Sol:
SELECT count(distinct id ) as Active_Subscriptions
FROM subscription
WHERE enddate > CURRENT_TIMESTAMP and status = 'Active';

4.How much is the average price ticket (sum amount subscriptions / count 
subscriptions) breakdown by year/month (format YYYY-MM)?
Sol:
SELECT CONCAT(year(enddate),'-',month(enddate) ) as YYYY_MM ,sum(amount)/count(Id) as average_price_ticket
FROM subscription 
group by CONCAT(year(enddate),'-',month(enddate) ) ;
