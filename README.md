# Cloud Data Pipeline: Google Cloud Storage to BigQuery

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


