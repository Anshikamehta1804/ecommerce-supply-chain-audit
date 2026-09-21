-- ==============================================================================
-- E-Commerce Fulfillment & Delivery Performance SQL Queries
-- Database: MySQL / PostgreSQL Compatible
-- ==============================================================================

-- 1. Create Staging Table Schema
CREATE TABLE IF NOT EXISTS ecommerce_shipments (
    id INT PRIMARY KEY,
    warehouse_block VARCHAR(10),
    mode_of_shipment VARCHAR(50),
    customer_care_calls INT,
    customer_rating INT,
    cost_of_the_product DECIMAL(10,2),
    prior_purchases INT,
    product_importance VARCHAR(20),
    gender VARCHAR(5),
    discount_offered DECIMAL(10,2),
    weight_in_gms INT,
    reached_on_time INT
);

-- 2. Shipping Mode Efficiency Audit (On-Time Delivery Rate & Spend)
SELECT 
    mode_of_shipment,
    COUNT(id) AS total_shipments,
    SUM(CASE WHEN reached_on_time = 1 THEN 1 ELSE 0 END) AS on_time_shipments,
    ROUND(SUM(CASE WHEN reached_on_time = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS otd_percentage,
    ROUND(AVG(cost_of_the_product), 2) AS avg_product_cost
FROM ecommerce_shipments
GROUP BY mode_of_shipment
ORDER BY otd_percentage DESC;

-- 3. Warehouse Delay Risk & Weight Distribution
SELECT 
    warehouse_block,
    COUNT(id) AS total_orders,
    ROUND(SUM(CASE WHEN reached_on_time = 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS delay_rate_percentage,
    ROUND(AVG(weight_in_gms), 2) AS avg_weight_gms
FROM ecommerce_shipments
GROUP BY warehouse_block
ORDER BY delay_rate_percentage DESC;

-- 4. Customer Care Calls vs Delivery Failure Analysis
SELECT 
    customer_care_calls,
    COUNT(id) AS order_volume,
    ROUND(SUM(CASE WHEN reached_on_time = 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(id), 2) AS delay_percentage
FROM ecommerce_shipments
GROUP BY customer_care_calls
ORDER BY customer_care_calls ASC;
