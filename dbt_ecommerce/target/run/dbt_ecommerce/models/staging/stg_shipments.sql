
  
    

create or replace transient table ecommerce_db.analysis.stg_shipments
    
    
    
    as (SELECT *
FROM raw.shipments
    )
;


  