# 🤖 MAVIS BOT — Your Personal Agentic AI Assistant

MAVIS BOT is an **agentic AI assistant** powered by **Google Gemini 2.5 Pro**, capable of executing real-world actions on your behalf. It goes far beyond traditional LLMs by not only generating content — it **acts** on it.

With MAVIS BOT, you can:

* 📧 **Send and receive emails**
* 📜 **Summarize and manage inbox content**
* 💬 **Generate smart replies for incoming emails**
* 🌐 **Perform live web searches** in real-time
* 💬 **Send WhatsApp messages**
* 📲 **Send SMS messages**
* ✅ **Send generated replies directly from the interface**

All actions are performed **on your behalf**, securely and seamlessly.

---

## 🚀 Live Demo

> MAVIS BOT is deployed using **Streamlit**, offering a fast and intuitive web-based interface.

---

## 🌟 Features

### ✉️ Email Automation

* Connect with your **Gmail** account
* **Read, summarize, and manage** emails
* Automatically **generate intelligent replies**
* With your permission, MAVIS BOT can **send replies autonomously**

### 🔍 Real-Time Web Search

* Integrated with **DuckDuckGo API** for **live, privacy-respecting** search
* Provides up-to-date answers to dynamic queries

### 💬 WhatsApp + SMS Integration

* Send WhatsApp messages using **Twilio API**
* Instantly send **SMS/Text messages** to any number
* All messages are personalized and generated via the LLM

### 🧠 Agentic Intelligence

* Unlike traditional LLMs that only **generate suggestions**, MAVIS BOT **executes** the task:

  * Writes the message ✅
  * Sends it for you ✅
  * Even follows up if needed ✅

---

## 🛠️ Tech Stack

| Component         | Technology                       |
| ----------------- | -------------------------------- |
| Frontend          | Streamlit                        |
| LLM Model         | Google Gemini 2.5 Pro            |
| Email Integration | Gmail API via LangChain Toolkits |
| Messaging         | Twilio API for SMS & WhatsApp    |
| Web Search        | DuckDuckGo Search API            |
| Agent Management  | Custom LangChain agents          |
| Deployment        | Streamlit Cloud / Localhost      |

---

## 📦 Setup & Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shivam4776/mavis-bot.git
   cd mavis-bot
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   Create a `.env` file in the root directory and include:

   ```env
   GMAIL_CLIENT_ID=your_client_id
   GMAIL_CLIENT_SECRET=your_client_secret
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone
   ```

4. **Run the App**

   ```bash
   streamlit run app.py
   ```

---

## 🔐 Security Note

MAVIS BOT operates with APIs that require access to sensitive data (email, messages). Always handle credentials securely and never hardcode them into your codebase. Use `.env` files or environment variables.

---

## 📸 Screenshots

## UI
<img width="564" height="441" alt="image" src="https://github.com/user-attachments/assets/7ee40a4f-ae5d-4c38-beac-53a47e59a7e2" />

## Sending Mail
<img width="532" height="477" alt="image" src="https://github.com/user-attachments/assets/f2f44f4f-3eb9-4ab1-8945-d55b5ea82b76" />

## Generating Latest News
<img width="531" height="582" alt="image" src="https://github.com/user-attachments/assets/658f8fb5-4b8d-43a4-99bc-d93b5383c409" />

## Summarize the mail
<img width="514" height="462" alt="image" src="https://github.com/user-attachments/assets/1795ffe0-3d31-40c3-8d36-aa4264c92509" />

## Sending SMS
<img width="536" height="474" alt="image" src="https://github.com/user-attachments/assets/f7d19027-be46-449a-afdd-9d70e0ba3a63" />

## MultiTasking
<img width="544" height="386" alt="image" src="https://github.com/user-attachments/assets/2f5848db-bb08-4260-8fa1-28f2b1cc37dc" />

---

## 💡 Why MAVIS BOT is Different

Most AI tools **stop at generating** — MAVIS BOT goes a step further:

✅ **Generate smart content**
✅ **Take action on your behalf**
✅ **Integrate across channels (Email, WhatsApp, SMS)**
✅ **Live information retrieval**

> “Normal LLMs can only write the message. MAVIS BOT sends it.”

---

## 📬 Future Roadmap

* Add voice command capabilities
* Integration with Slack, Telegram, and Discord
* Calendar event creation
* Multilingual support
* UI enhancements and dark mode

---

## 🤝 Contributing

Pull requests are welcome! If you have feature suggestions, bug reports, or improvements, feel free to open an issue or submit a PR.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔗 Connect

Built by Shivam Kashyap(https://github.com/shivam4776) with ❤️
