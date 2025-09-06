Overview:

This project implements a smart home security system using IoT and facial recognition. The system authenticates authorized users and enhances security by capturing and sending images of unauthorized persons via email alerts in real time.

Features:

*Facial recognition-based access control

*Real-time image capture of unauthorized persons

*Automatic email alerts with captured images

*Live monitoring through IoT integration

*Secure data storage for access logs

Technologies & Tools Used:

*Languages/Frameworks: Python, OpenCV, TensorFlow/Keras

*IoT Components: Raspberry Pi / Arduino, Camera Module, Sensors

Other Tools: Flask/Django (web interface), SMTP (email alerts), Firebase/MySQL (data storage), Git/GitHub

Installation & Setup:

1.Clone this repository:

git clone https://github.com/your-username/SmartHomeSecurity-IoT.git
cd SmartHomeSecurity-IoT


2.Install dependencies:

pip install -r requirements.txt


3.Connect IoT hardware (Raspberry Pi/Arduino + Camera + Sensors).

4.Update your email credentials in the config file for SMTP alerts.

5.Run the application:

python main.py

Usage:

1.Authorized users: Face recognized → access granted.

2.Unauthorized users: Image captured → email alert sent.

3.Logs stored in database for monitoring.

Research Publication:

This project was published as a research paper:

“Smart Home Security for Facial Recognition using IoT” – Published in JETIR journal, [Nov,2024].

Contributors:(My Team)

B.Bhavani(group leader)
K.Suhasini
M.HemaLatha
D.Manasa
