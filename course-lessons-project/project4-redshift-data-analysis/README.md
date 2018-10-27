# Creating a Redshift Cluster

1. Navigate to Redshift in the AWS console
2. Quick Launch a 1-node cluster
3. Install Postico
4. Install the [JDBC driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver)
5. Copy Redshift JDBC url. e.g. `redshift-cluster-1.ccmcujfidyml.us-east-1.redshift.amazonaws.com` port `5439` and `dev` database

# Compression in Redshift

Automatic compression analysis requires enough rows in the load data (at least 100,000 rows per slice) to generate a meaningful sample.

```sql
create table sales(
    salesid integer not null,
    listid integer not null distkey,
    sellerid integer not null,
    buyerid integer not null,
    eventid integer not null,
    dateid smallint not null sortkey,
    qtysold smallint not null,
    pricepaid decimal(8,2),
    commission decimal(8,2),
    saletime timestamp
);

copy sales from 's3://awssampledbuswest2/tickit/sales_tab.txt'
iam_role 'arn:aws:iam::123123123123:role/redshift-po'
delimiter '\t' timeformat 'MM/DD/YYYY HH:MI:SS' region 'us-west-2';

select "column", type, encoding, distkey, sortkey, "notnull" 
from pg_table_def
where tablename = 'sales';

select * from sales limit 10;

analyze compression sales;

drop table sales;
```

# Distribution Styles

```sql
create table adpubresults_all(
    _1 varchar(50),
    _2 date,
    _3 float
)
diststyle all;

create table adpubresults_datekey(
    _1 varchar(50),
    _2 date distkey,
    _3 float
);

select "column", type, encoding, distkey, sortkey, "notnull" 
from pg_table_def
where tablename = 'sales';

copy adpubresults
from 's3://penguin-outfitters-adpubdata/adPubResultsjson/'
iam_role 'arn:aws:iam::123123123123:role/redshift-po' 
dateformat as 'MM/DD/YYYY'
json 'auto';

select * from adpubresults limit 100;

select * from stl_load_errors limit 1;
```

# Sort Keys

```sql
create table iotstreamdata(
    station varchar(16),
    name varchar(50),
    latitude decimal,
    longitude decimal,
    elevation decimal, 
    date_measured distkey sortkey date,
    precipitation decimal,
    snowfall decimal, 
    snow_depth decimal,
    average_temperature int,
    max_temperature int,
    min_temperature int
)
-- compound sortkey(listid,sellerid);
-- interleaved sortkey (c_custkey, c_city, c_mktsegment);
;

copy iotstreamdata
from 's3://big-data-iot-2018-la/2018/'
iam_role 'arn:aws:iam::123123123123:role/redshift-po' 
dateformat as 'YYYY-MM-DD'
json 'auto';
```

Create a table in the cluster and use all these things

# Unload and Copy

```sql
unload ('
    select * from (
        select 
            date_measured,
            max_temperature
        from iotstreamdata 
        order by max_temperature desc
        limit 10
    )
')
to 's3://penguin-orders-export-2018/redshiftunloads/maxtemps_'
iam_role 'arn:aws:iam::123123123123:role/redshift-po';

unload ('
    select 
        date_measured,
        max_temperature
    from iotstreamdata 
    where date_measured between \'2018-04-01\' and \'2018-04-07\'
    order by date_measured
')
to 's3://penguin-orders-export-2018/redshiftunloads/aprilmaxtemp_'
iam_role 'arn:aws:iam::123123123123:role/redshift-po' 
```


