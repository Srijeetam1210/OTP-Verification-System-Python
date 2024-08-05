# OTP-Verification-System-Python


**Overview :**

This project is a Python-based One-Time Password (OTP) verification system. It generates a random OTP and sends it to a user's email address. The user is then prompted to enter the OTP, and the system verifies if the entered OTP matches the generated one.

**Features :**

OTP Generation: Generates a random 6-digit OTP.
Email Sending: Sends the OTP to the user's email address using SMTP.
User Input: Prompts the user to enter the OTP received.
OTP Verification: Checks if the entered OTP matches the generated one.
Purpose
The primary purpose of this project is to provide an additional layer of security for user authentication. OTP verification is commonly used in scenarios where secure access to systems, applications, or sensitive data is required. By implementing OTP verification, unauthorized access can be minimized, ensuring that only the intended recipient can proceed with authentication.

**Benefits :**

Enhanced Security: Adds an extra layer of security by verifying user identity through a time-sensitive OTP.
User Verification: Ensures that the user has access to the email address provided, reducing the risk of fraudulent activities.
Easy Integration: Can be integrated into various applications and systems that require secure user authentication.
Improved User Trust: Builds user trust by implementing industry-standard security practices.

**Components :**

OTP Generation: Function to generate a random 6-digit OTP.
Email Sending: Function to send the OTP to the user's email address.
User Input: Function to prompt the user to enter the OTP.
OTP Verification: Function to verify if the entered OTP matches the generated OTP.
Main Function: Orchestrates the OTP generation, sending, and verification process.

**Usage :**

Run the Script: Execute the main function to start the OTP verification process.
Input Email: Enter the email address where the OTP will be sent.
Receive OTP: Check your email for the OTP.
Enter OTP: Input the received OTP when prompted.
Verification: The script will verify if the entered OTP is correct and provide feedback.

**Dependencies :**

random: Used to generate a random OTP.
smtplib: Used to send emails via SMTP.
email.message.EmailMessage: Used to create email messages.
