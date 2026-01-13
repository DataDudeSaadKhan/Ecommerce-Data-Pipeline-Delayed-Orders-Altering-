
  
    

create or replace transient table ecommerce_db.analysis.stg_customers
    
    
    
    as (SELECT *
FROM raw.customers
    )
;


  