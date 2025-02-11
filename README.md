# Automated Sales Data Pipeline: GCS & BigQuery Integration

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)  
![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)  
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)  

This project demonstrates a **Cloud Data Pipeline** that automates the process of uploading files to **Google Cloud Storage (GCS)** and loading the data into **Google BigQuery**. The pipeline is built using **Python**, **Flask**, and **Google Cloud SDK**.
 
---

## **Features**
- **File Upload**: Upload files to a Google Cloud Storage bucket using a Flask web interface.
- **BigQuery Integration**: Automatically load uploaded files into a BigQuery table.
- **Scalable**: Designed to handle large files efficiently.
- **Error Handling**: Robust error handling and logging for reliable operation.

---

## **Prerequisites**
Before running the code, ensure you have the following:

1. **Google Cloud Account**: A Google Cloud project with billing enabled.
2. **Google Cloud SDK**: Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
3. **Python 3.7+**: Install Python from [python.org](https://www.python.org/).
4. **Service Account Key**: Create a service account with the following roles:
   - **Storage Object Admin** (`roles/storage.objectAdmin`)
   - **BigQuery Data Editor** (`roles/bigquery.dataEditor`)
   - Download the JSON key file and set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
     ```

---


## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/cloud-pipeline.git
cd cloud-pipeline
```

### 2. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```
### 3. Set Up Google Cloud
Create a Google Cloud Storage Bucket:

```bash
gsutil mb gs://your-bucket-name
Create a BigQuery Dataset and Table:
```


### 4. Configure Environment Variables
Set the following environment variables:

```bash
export GCS_BUCKET_NAME="your-bucket-name"
export DATASET="sales"
export TABLE="orders"
```
---

### Usage
1. Run the Flask Application
Start the Flask web server:

```bash
python app.py

2. Access the Web Interface
Open your browser and navigate to:

```
http://127.0.0.1:5000
```

3. Upload a File
Use the web interface to upload a file (e.g., CSV).
The file will be uploaded to your GCS bucket and automatically loaded into BigQuery.

4. Verify Data in BigQuery
Query the BigQuery table to verify the data:

```sql
SELECT * FROM sales.orders;
```

---

### Screenshots
Web Interface  
<img width="468" alt="image" src="https://github.com/user-attachments/assets/9c23b033-4e70-40f1-9d4f-0a62323ed67d" />


File Uploaded to GCS  
<img width="468" alt="image" src="https://github.com/user-attachments/assets/17e64d83-4487-47cd-a8fd-ae55d6ed4f0a" />


Data Loaded into BigQuery  
<img width="1114" alt="google_cloud_img" src="https://github.com/user-attachments/assets/1f579b3b-fa40-413f-9dd9-c1c5d37f37f4" />


---

### Support

For any questions or issues, please open an issue on Github.





