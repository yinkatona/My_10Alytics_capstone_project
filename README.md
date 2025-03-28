# Project: NYC Payroll Data Integration  

## Project Overview  

The City of New York is launching a project to integrate payroll data across all municipal agencies, aiming to develop a comprehensive Data Analytics platform. This platform will serve two key objectives:  

- **Financial Resource Allocation Analysis**: Evaluate how the City's financial resources are distributed, with a particular focus on the budget allocated to overtime pay.  
- **Transparency and Public Accessibility**: Provide public access to payroll data, ensuring transparency in how taxpayer money is spent on salaries and overtime for all City employees.  

This initiative is designed to enhance financial oversight and promote transparency in the City's budget allocation.  

## Tech Stack

- **Python**: Used for scripting data extraction, cleaning, and transformation processes.
- **SQL**: Employed for data manipulation and querying within the SQL database in Azure.
- **Azure Data Factory**: Utilized for building and orchestrating ETL pipelines.
- **Pandas**: A Python library for efficient data manipulation and analysis.
- **Azure Data Lake Storage**: Serves as the storage solution for processed data.
  
![python](https://github.com/user-attachments/assets/4829ff6f-1e54-4e20-9e28-a78490d7bdbb)
![Azure](https://github.com/user-attachments/assets/677f8b92-d0de-4b9b-ab9c-ebece1738511)
![SQL](https://github.com/user-attachments/assets/59da2c1e-3d3c-46aa-b053-11943096a6a5)
![ADF](https://github.com/user-attachments/assets/0936a912-949b-4ea6-93b7-6f7ffdc01b12)
![ADLS](https://github.com/user-attachments/assets/8b9e0a34-74f6-48bf-b565-ddadebb671fa)

## Why This Tech Stack?  

To build high-quality data pipelines that are **dynamic, automated, scalable, and efficiently monitored**, I have chosen **Azure Cloud** as the platform for development.  

- **Azure Data Factory** is used to orchestrate the end-to-end **ETL (Extract, Transform, Load) process**, ensuring seamless data integration and transformation across various sources.  
- **Azure SQL Database** provides a robust and scalable environment for efficient data storage, management, and querying.  
- **Python** and **Pandas** facilitate data processing, transformation, and automation, enhancing pipeline flexibility and performance.  
- **Azure Data Lake Storage** serves as a centralized repository for structured and unstructured data, supporting scalability and efficient data access.  

This stack ensures the pipeline is **cost-effective, highly available, and optimized for performance**, meeting the requirements of an enterprise-grade data integration solution. 

## NYC Payroll Integration Pipeline Architecture  

![capstone-project-architecture-new-Page-2](https://github.com/user-attachments/assets/1eec8b5c-79e4-42c7-86e9-278d97f263be)

The NYC Payroll Integration Pipeline is designed to efficiently process payroll data from ingestion to analysis using **Azure cloud services**. The architecture ensures **scalability, automation, and efficient data transformation** through a structured flow, as illustrated in the diagram.  

### **Pipeline Flow and Stages**  

1. **Data Source (CSV Files) Ingestion**  
   - Payroll data is collected from remotely stored CSV files and ingested into the pipeline for processing.  
   - Python was used for **data extraction, transformation, and cleaning**, ensuring the data is in the correct format before storage.  

2. **Storage in Azure Data Lake**  
   - The transformed data is loaded into **Azure Data Lake Storage**, which acts as a **centralized data repository** for structured and semi-structured data.  
   - This enables **scalable and cost-effective storage** while maintaining data integrity.  

3. **Data Warehousing – Staging Layer (SQL Database)**  
   - The ingested data is then moved to the **staging layer** in an Azure **SQL Database**.  
   - This step allows **data validation, deduplication, and further transformation** before proceeding to final storage.  

4. **Data Warehousing – Serving Layer (SQL Database)**  
   - After validation, the processed data is transferred to the **serving layer**, which serves as the final structured **data warehouse**.  
   - This optimized storage layer supports **efficient querying and reporting** for downstream analysis.  

5. **Data Orchestration with Azure Data Factory**  
   - The entire **ETL (Extract, Transform, Load) pipeline** is managed using **Azure Data Factory**, automating data movement and processing.  
   - This ensures a **seamless and scheduled data pipeline** with monitoring and logging capabilities.  

6. **Analysis & Reporting**  
   - The cleaned and processed data is now ready for **business intelligence (BI) and analytics**.  
   - The data can be integrated into **visualization tools like Power BI or Azure Synapse Analytics** for insights on payroll trends, overtime allocations, and budget transparency.  

### **Key Benefits of This Architecture**  
✅ **Scalability** – Easily handles growing payroll data across municipal agencies.  
✅ **Automation** – Ensures a streamlined and monitored ETL process.  
✅ **Efficiency** – Optimized for quick querying and business intelligence.  
✅ **Transparency** – Provides public access to payroll data for accountability.  

This architecture effectively enables the **City of New York** to enhance financial oversight and improve public transparency in budget allocations.  

## NYC Payroll Data Integration Schema  

The NYC Payroll Data Integration schema is designed using a **star schema** model to optimize **data retrieval, analytics, and reporting**. The schema consists of one **fact table** (`payroll_fact`) and three **dimension tables** (`employee_dim`, `agency_dim`, and `title_dim`).  

### **Schema Overview & Table Relationships**  

![capstone-project-Page-2 drawio](https://github.com/user-attachments/assets/662b9a91-7937-4e66-ac5f-89731a4ff32c)


1. **Fact Table: `payroll_fact`**  
   - This table serves as the **central repository** for payroll-related transactions.  
   - It contains detailed payroll records, including **base salary, overtime hours, total overtime paid, and other compensations**.  
   - The **primary key (`payroll_ID`)** uniquely identifies each payroll record.  
   - The table maintains a **foreign key (FK) relationship** with the following dimension tables:  
     - `AgencyID` → **Links to `agency_dim`** (to associate payroll data with the respective municipal agency).  
     - `EmployeeID` → **Links to `employee_dim`** (to associate payroll data with employees).  
     - `TitleCode` → **Links to `title_dim`** (to associate payroll data with job titles).  

2. **Dimension Table: `employee_dim`**  
   - This table contains detailed employee information, including **first name, last name, and associated agency**.  
   - The **primary key (`EmployeeID`)** uniquely identifies each employee.  
   - The table maintains relationships with:  
     - `payroll_fact` via **`EmployeeID`**.  
     - `title_dim` through **`TitleDescription`**, providing additional job classification details.  

3. **Dimension Table: `agency_dim`**  
   - Stores information about municipal agencies, such as **agency name, start date, and borough location**.  
   - The **primary key (`AgencyID`)** uniquely identifies each agency.  
   - This table is connected to **`payroll_fact`** via `AgencyID`, allowing payroll data to be grouped by agency.  

4. **Dimension Table: `title_dim`**  
   - Stores job title classifications, including **title codes and descriptions**.  
   - The **primary key (`TitleCode`)** uniquely identifies each job title.  
   - It connects to both **`payroll_fact`** (via `TitleCode`) and **`employee_dim`** (via `TitleDescription`), enabling analysis of salaries and payroll trends by job role.  

### **Key Features & Benefits**  

✅ **Optimized for Analytics** – The **star schema** design enhances query performance for payroll and budget analysis.  
✅ **Scalability** – Supports large datasets, making it ideal for city-wide payroll data integration.  
✅ **Data Integrity** – Uses **primary and foreign key constraints** to maintain referential integrity.  
✅ **Efficient Querying** – Allows quick insights into **payroll expenses, overtime trends, and financial distributions** across agencies and job titles.  

This schema enables **efficient financial analysis, transparency, and reporting**, supporting the City of New York’s goal of improving payroll data accessibility and accountability.  

