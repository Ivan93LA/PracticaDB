SELECT 
        sol.product_id,
        so.date AS sale_date,
        SUM(sol.price_subtotal) AS daily_sales
    FROM 
        sale_order_line sol
        JOIN sale_order so ON sol.order_id = so.id
    WHERE 
        so.date >= CURRENT_DATE - INTERVAL '60' DAY and  so.state = 'aprobado' and sol.state= 'aprobado'
    GROUP BY 
        sol.product_id, so.date;
       
        
      select * from sale_order
      where sale_order.state = 'aprobado';
      
      
      SELECT 
        sol.product_id,
        so.date AS sale_date,
        SUM(sol.price_subtotal) AS daily_sales
    FROM 
        sale_order_line sol
        JOIN sale_order so ON sol.order_id = so.id
    WHERE 
        so.date >= CURRENT_DATE - INTERVAL '60' DAY
    GROUP BY 
        sol.product_id, so.date;
        
        select * from sale_order_line