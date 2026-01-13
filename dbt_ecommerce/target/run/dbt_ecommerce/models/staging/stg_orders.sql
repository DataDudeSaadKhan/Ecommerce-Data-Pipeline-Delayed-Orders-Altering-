
  
    

create or replace transient table ecommerce_db.analysis.stg_orders
    
    
    
    as (SELECT *
FROM raw.orders
    )
;


  