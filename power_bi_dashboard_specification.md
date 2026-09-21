# Power BI Supply Chain & Delivery Performance Dashboard Specification

## 1. Data Model Setup
- **Source Table**: `Train.csv` (Renamed to `ecommerce_shipments`)
- **Primary Key**: `ID`
- **Fact Table Metrics**:
  - `Cost_of_the_Product` (Decimal / Currency)
  - `Discount_offered` (Decimal / Percentage / Currency)
  - `Weight_in_gms` (Whole Number)
  - `Customer_care_calls` (Whole Number)
  - `Customer_rating` (Whole Number)
  - `Prior_purchases` (Whole Number)
  - `Reached.on.Time_Y.N` (Binary Whole Number: 1 = On Time, 0 = Delayed)

---

## 2. Production DAX Measures
Create a dedicated measures table named `_Measures` and insert the following calculations:

```dax
-- Total Shipment Volume
Total Shipments = COUNTROWS('ecommerce_shipments')

-- On-Time Shipments Count
On Time Shipments = CALCULATE(
    COUNTROWS('ecommerce_shipments'),
    'ecommerce_shipments'[Reached.on.Time_Y.N] = 1
)

-- Delayed Shipments Count
Delayed Shipments = CALCULATE(
    COUNTROWS('ecommerce_shipments'),
    'ecommerce_shipments'[Reached.on.Time_Y.N] = 0
)

-- On-Time Delivery (OTD) Rate %
OTD Rate % = 
DIVIDE(
    [On Time Shipments],
    [Total Shipments],
    0
) * 100

-- Delay Rate %
Delay Rate % = 
DIVIDE(
    [Delayed Shipments],
    [Total Shipments],
    0
) * 100

-- Average Product Value
Avg Product Cost = AVERAGE('ecommerce_shipments'[Cost_of_the_Product])

-- Average Discount Offered
Avg Discount Offered = AVERAGE('ecommerce_shipments'[Discount_offered])

-- Average Package Weight (kg)
Avg Weight (kg) = DIVIDE(AVERAGE('ecommerce_shipments'[Weight_in_gms]), 1000, 0)
```

---

## 3. Dashboard Visual Layout (Single-Page Executive Report)

### Canvas Dimensions: 16:9 Standard (1280 x 720 px)

### A. Header & Executive KPI Cards (Top Banner, Y: 20px - 140px)
- **KPI Card 1**: Total Shipments (`[Total Shipments]` -> 10,999)
- **KPI Card 2**: On-Time Delivery Rate (`[OTD Rate %]` -> 59.67%)
- **KPI Card 3**: Average Package Weight (`[Avg Weight (kg)]` -> 3.63 kg)
- **KPI Card 4**: Average Product Cost (`[Avg Product Cost]` -> $210.20)
- **KPI Card 5**: Average Discount (`[Avg Discount Offered]` -> $13.37)

### B. Analytical Charts (Middle Section, Y: 160px - 450px)
- **Visual 1 (Donut Chart)**:
  - **Category**: `Mode_of_Shipment`
  - **Values**: `[Total Shipments]`
  - **Tooltip**: `[OTD Rate %]`
  - **Insight**: Ship accounts for ~68% of fulfillment volume; Flight and Road share the remaining equally.
- **Visual 2 (Clustered Bar Chart)**:
  - **Y-Axis**: `Warehouse_block` (A, B, C, D, F)
  - **X-Axis**: `[Delay Rate %]`
  - **Insight**: Highlights uniform delivery risk (~40%) across all fulfillment centers.
- **Visual 3 (Scatter Plot / Area Chart)**:
  - **X-Axis**: `Weight_in_gms`
  - **Y-Axis**: `Discount_offered`
  - **Legend**: `Reached.on.Time_Y.N`
  - **Insight**: Visualizes shipment clustering where discounts > 10% correlate with on-time delivery priority.

### C. Operational Granularity Matrix (Bottom Section, Y: 470px - 690px)
- **Rows**: `Product_importance` (low, medium, high)
- **Columns**: `Customer_rating` (1, 2, 3, 4, 5)
- **Values**: `[OTD Rate %]`, `[Avg Product Cost]`
- **Slicers (Interactive Filters)**:
  - Dropdown Slicer: `Mode_of_Shipment` (All, Flight, Ship, Road)
  - Radio Slicer: `Product_importance`
