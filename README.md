# XSS Vulnerability & Prevention Demo

## Overview

This project is an interactive web application built with Python and Flask to demonstrate Cross-Site Scripting (XSS) vulnerabilities and their prevention. The app provides a real-time, side-by-side comparison of insecure and secure handling of user input, helping developers and learners understand the importance of input sanitization in web development.

---

## Features

- **Dual Output Panels:** Displays user comments in both vulnerable (unsanitized) and secure (sanitized) formats.
- **Real-Time Demonstration:** Instantly see the effects of XSS attacks and their prevention.
- **Input Sanitization:** Uses the `bleach` library to filter unsafe HTML and scripts.
- **Educational UI:** Clear visual cues and labels to highlight security risks and solutions.
- **Safe Experimentation:** Submit various payloads to observe XSS behavior and protection.

---

## How It Works

1. **User Input:**  
   Users submit comments through a web form.

2. **Vulnerable Output:**  
   The comment is displayed without any sanitization, making it susceptible to XSS attacks (e.g., `alert('XSS')` will execute).

3. **Secure Output:**  
   The same comment is sanitized using `bleach` before display, neutralizing any malicious scripts.

4. **Side-by-Side Comparison:**  
   Both outputs are shown together, providing a clear, interactive demonstration of the impact of input sanitization.

---

## Installation & Usage

### 1. Clone the Repository


### 2. Set Up a Virtual Environment

```bash
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (macOS/Linux)
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install Flask bleach
```

### 4. Project Structure

```
xss-demo/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
```

### 5. Run the Application

```bash
python app.py
```

### 6. Access the Demo

Open your browser and go to:  
`http://127.0.0.1:5000/`

---

## Usage Example

- Try submitting a comment like:
  ```
  alert('XSS!')
  ```
  - The **vulnerable panel** will execute the script (showing a popup).
  - The **secure panel** will display the code as plain text, preventing the attack.

---

## Why This Matters

XSS is one of the most common web vulnerabilities. This demo makes it easy to see how untrusted user input can compromise web applications and how simple measures like input sanitization can prevent attacks.

---

## Key Learnings

- Always sanitize or escape user input before rendering it in HTML.
- Use libraries like `bleach` to allow only safe HTML tags and attributes.
- Never trust user input—validate and sanitize at every step.

---

## License

This project is for educational purposes. Feel free to use, modify, and share!

---

**Happy Learning & Secure Coding!**
