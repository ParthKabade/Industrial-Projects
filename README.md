🛡️ ProcSentinel

Automated Process Monitoring & Reporting System using Python

ProcSentinel is a Python-based system monitoring project that collects information about running processes, identifies specific processes, maintains process logs, and automatically sends reports through email.

The project was developed as part of my journey to understand Python system programming, process management, file handling, automation, and email communication.

⸻

🚀 Features

* 🔍 Collects information about running processes
* 🆔 Displays Process ID (PID), Process Name, and Username
* 🎯 Searches for a specific running process
* 📝 Automatically maintains process logs
* 📧 Sends generated logs through email
* ⏰ Executes monitoring tasks periodically
* 🧩 Uses a modular Python architecture

⸻

🏗️ Project Architecture

                    ProcSentinel
                         │
                         ▼
                     Main.py
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
      ProcessInfo   SpecificProcess  LogFile
          .py           Info.py        .py
             │           │             │
             └───────────┴─────────────┘
                         │
                         ▼
                     MailLog.py
                         │
                         ▼
                    Email Report

⸻

📂 Project Structure

ProcSentinel/
│
├── Main.py
├── ProcessInfo.py
├── SpecificProcessInfo.py
├── LogFile.py
├── MailLog.py
├── Demo/
│   └── LogProcInfo.txt
└── README.md

Module Overview

File	Purpose
Main.py	Controls the complete monitoring workflow
ProcessInfo.py	Collects information about running processes
SpecificProcessInfo.py	Searches for a specific process
LogFile.py	Creates and maintains process logs
MailLog.py	Sends logs through email

⸻

🛠️ Technologies Used

* Python
* psutil — Process and system information
* schedule — Task scheduling
* smtplib — Email communication
* EmailMessage — Email creation and attachments
* os — File and directory operations
* sys — Command-line arguments

⸻

⚙️ How It Works

Start
  ↓
Collect Running Processes
  ↓
Display Process Information
  ↓
Search for Specific Process
  ↓
Generate Process Log
  ↓
Attach Log to Email
  ↓
Send Email Report
  ↓
Repeat Automatically

The system periodically executes the monitoring workflow and records the information of the requested process.

⸻

▶️ Running the Project

1. Clone the repository

git clone <your-repository-url>
cd ProcSentinel

2. Install dependencies

pip install psutil schedule

3. Run the project

python Main.py <ProcessName> <LogDirectory> <ReceiverEmail>

Example:

python Main.py python.exe Demo user@gmail.com

⸻

📊 Example Process Information

-------------------------------------------------------------------------------------
User Name : user
Process Name : python.exe
Pid : 12345
-------------------------------------------------------------------------------------

The selected process information is also stored in:

Demo/LogProcInfo.txt

⸻

🎯 Learning Outcomes

Through this project, I explored:

* Python modular programming
* Operating-system process concepts
* Process identification using PID
* System information using psutil
* File and directory handling
* Command-line arguments
* Task scheduling and automation
* SMTP and email automation
* Exception handling
* Building a multi-module Python application

⸻

🔮 Future Improvements

Possible future enhancements include:

* 📈 CPU and memory monitoring
* 🚨 Process-based alerts
* 📊 System resource dashboard
* 🔐 Secure credential management
* 🗄️ Database-based logging
* 🌐 Web-based monitoring dashboard
* 📱 Real-time notifications
* 🧹 Disk sanitisation and cleanup capabilities

⸻

👨‍💻 Author

Parth Kabade

Computer Science Student | Python | Java | System Programming | Automation

⸻

⭐ Project Goal

Learn by building — understand how Python interacts with the operating system and turn individual programming concepts into a practical automation system.

If you find this project useful, consider giving the repository a ⭐.
