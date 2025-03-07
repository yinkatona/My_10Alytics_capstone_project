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
