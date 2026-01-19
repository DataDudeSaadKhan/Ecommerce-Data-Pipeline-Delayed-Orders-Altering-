Enjoy :)

## ✅ README.md 

```markdown
# Airflow + dbt + Snowflake Pipeline 🚀

This repository contains a complete data engineering setup using **Apache Airflow**, **dbt**, and **Snowflake**.  
It demonstrates how to orchestrate dbt models and monitor delayed orders in Snowflake with Airflow running inside Docker.

---

## 📂 Project Structure

```
Ecommerce_Project/
├─ Dockerfile
├─ docker-compose.yml
├─ snowflake_config.yaml
├─ user.yaml
├─ dags/
│  ├─ order-monitoring.py
│  └─ utils/
│     └─ check_delayed_orders.py
└─ dbt_ecommerce/
   ├─ dbt_project.yml
   └─ models/...
```

---

## ⚙️ Setup Instructions

### 1. Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
- Clone this repository:
  ```bash
  git clone https://github.com/YOUR_USERNAME/airflow-dbt-snowflake-pipeline.git
  cd airflow-dbt-snowflake-pipeline
  ```

### 2. Configure Snowflake
Edit `snowflake_config.yaml` with your credentials:
```yaml
snowflake:
  user: YOUR_SNOWFLAKE_USER
  password: YOUR_SNOWFLAKE_PASSWORD
  account: YOUR_SNOWFLAKE_ACCOUNT
  warehouse: YOUR_SNOWFLAKE_WAREHOUSE
  database: ECOMMERCE_DB
  schema: ANALYTICS
  role: YOUR_SNOWFLAKE_ROLE
```

### 3. Build and Run Airflow
```bash
docker compose build
docker compose up -d
```

### 4. Access Airflow UI
- Open `http://localhost:8080` [(localhost in Bing)](https://www.bing.com/search?q="http%3A%2F%2Flocalhost%3A8080%2F")
- Default login: `airflow / airflow`

---

## 📊 DAGs

### `order_monitoring_dag`
- **Task 1:** Run dbt models (`dbt run`)
- **Task 2:** Check delayed orders in Snowflake (`check_delayed_orders.py`)

### `check_delayed_orders.py`
- Connects to Snowflake
- Queries delayed orders
- Fails the task if delayed orders are found (Airflow sends email alert)

---

## 📧 Email Alerts
Airflow is configured to send email alerts via Gmail SMTP.  
Set your Gmail App Password in `docker-compose.yml`:
```yaml
AIRFLOW__SMTP__SMTP_USER: your_email@gmail.com
AIRFLOW__SMTP__SMTP_PASSWORD: your_app_password
```

---

## 🛠️ Development Notes
- All project files are mounted into `/opt/airflow` inside the container.
- Use **Linux paths** (`/opt/airflow/...`) in DAGs, not Windows `D:\...`.
- Extend Airflow image with dbt installed via `Dockerfile`.

---

## 👤 Metadata
`user.yaml` contains project metadata:
```yaml
user:
  id: 77631b86-65f1-4b35-b598-0a161293eaa9
```

---

## ✅ Next Steps
- Add more dbt models to `dbt_ecommerce/`.
- Extend DAGs with testing (`dbt test`) and documentation (`dbt docs generate`).
- Deploy to production with a cloud Snowflake account.

---

## 📜 License
MIT License
```

---

## ✅ Repo Structure on GitHub
```
airflow-dbt-snowflake-pipeline/
├─ README.md
├─ Dockerfile
├─ docker-compose.yml
├─ snowflake_config.yaml
├─ user.yaml
├─ dags/
│  ├─ order-monitoring.py
│  └─ utils/check_delayed_orders.py
└─ dbt_ecommerce/
```
 

Would you like me to also give you the **exact git commands** to initialize and push this project to GitHub (from your Windows machine)?
