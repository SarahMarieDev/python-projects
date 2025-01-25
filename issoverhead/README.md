# ISS Overhead Notifier

This project checks if the International Space Station (ISS) is overhead and sends an email notification if it is and it's dark outside.

---

## Features
- Fetches the current position of the ISS.
- Determines if it’s nighttime at your location.
- Sends an email if the ISS is overhead and it’s nighttime.

---

## Prerequisites
- Python 3.x
- A Gmail account
- A `.env` file

---

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/iss-overhead-notifier.git
cd iss-overhead-notifier
```

### 2. Install Dependencies
```bash
pip install requests python-dotenv
```

### 3. Create a `.env` File
Add your email credentials to a `.env` file:
```bash
GMAIL=your_email@gmail.com
PASSWORD=your_app_specific_password
```

### 4. Update Your Location
Edit the `MY_LAT` and `MY_LNG` variables in `main.py` to set your latitude and longitude.

---

## Usage

### Run the Script Manually
```bash
python main.py
```

### Set Up a Cron Job
1. Open the crontab file:
   ```bash
   crontab -e
   ```

2. Add the following line:
   ```bash
   * * * * * /path/to/micromamba/bin/python3 /path/to/project/main.py >> /path/to/project/cron.log 2>&1
   ```

---

## Logs
Monitor the logs in real-time:
```bash
tail -f cron.log
```

---
