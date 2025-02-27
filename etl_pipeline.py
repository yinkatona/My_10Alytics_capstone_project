### Extraction Phase

# Importing Necessary Packages
import pandas as pd
import os
import io
from azure.storage.blob import BlobServiceClient, BlobClient
from dotenv import load_dotenv

# Reading the Data from the source
nycpayroll2020_df = pd.read_csv(r'Data\nycpayroll_2020.csv')

# Displaying the Data
nycpayroll2020_df.head()

 # Converting the FiscalYear to datetime
nycpayroll2020_df['FiscalYear'] = pd.to_datetime(nycpayroll2020_df['FiscalYear'], format='%Y') 

# Converting the AgencyStartDate to datetime
nycpayroll2020_df['AgencyStartDate'] = pd.to_datetime(nycpayroll2020_df['AgencyStartDate'], format='%m/%d/%Y')

# Creating Employee Table
employee = nycpayroll2020_df[['EmployeeID','LastName', 'FirstName', 'TitleDescription','AgencyName']].copy().drop_duplicates().reset_index(drop=True)

# Creating Agency Table
agency = nycpayroll2020_df[['AgencyID','AgencyName','AgencyStartDate','WorkLocationBorough']].copy().drop_duplicates().reset_index(drop=True)

# Creating Title Table
title = nycpayroll2020_df[['TitleCode', 'TitleDescription']].copy().drop_duplicates().reset_index(drop=True)

# Merging the DataFrames
payroll_fact = nycpayroll2020_df.merge(employee, on=['EmployeeID','LastName', 'FirstName', 'TitleDescription','AgencyName'], how='left') \
                                .merge(agency, on=['AgencyID','AgencyName','AgencyStartDate','WorkLocationBorough'], how='left') \
                                .merge(title, on=['TitleCode', 'TitleDescription'], how='left') \
                [['FiscalYear','PayrollNumber','AgencyID','EmployeeID','TitleCode','LeaveStatusasofJune30','BaseSalary','PayBasis','RegularHours','RegularGrossPaid','OTHours', 'TotalOTPaid', 'TotalOtherPay']] 

payroll_fact.index.name = 'PayrollFactID'
payroll_fact = payroll_fact.reset_index()

# saving the data to csv
employee.to_csv(r'rawdata\employee.csv', index=False)
agency.to_csv(r'rawdata\agency.csv', index=False)
title.to_csv(r'rawdata\title.csv', index=False)
payroll_fact.to_csv(r'rawdata\payroll_fact.csv', index=False)

print('Files has been loaded temporarrily to the local machine')


# Setting up Azure Blob Storage connection

load_dotenv()

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
container_client = blob_service_client.get_container_client(container_name)


# Create a function to upload files to the Azure Blob Storage
def upload_to_azure_blob(df, container_client, blob_name):
    buffer = io.BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(buffer, blob_type="BlockBlob", overwrite=True)
    print(f'{blob_name} uploaded to Azure Blob Storage')


# Uploading the Data to Azure Blob Storage
upload_to_azure_blob(employee, container_client, 'rawdata/employee.parquet')
upload_to_azure_blob(agency, container_client, 'rawdata/agency.parquet')
upload_to_azure_blob(title, container_client, 'rawdata/title.parquet')
upload_to_azure_blob(payroll_fact, container_client, 'rawdata/payroll_fact.parquet')  