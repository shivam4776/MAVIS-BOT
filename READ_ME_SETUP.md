# 🛠️ MAVIS BOT - Setup Guide Before Running the Project

Before you can run **MAVIS BOT** on your local machine, you need to complete a few essential setup steps. This guide will walk you through everything required to connect your own LLM, email account, and messaging services.

---

## 🔑 1. Connect to an LLM (Language Model)

You must integrate a Language Model (LLM) before using MAVIS BOT.

### Option A: Use a cloud-hosted LLM (e.g., Google Gemini, OpenAI)

* Sign up and get API access from the provider (e.g., [Google AI Studio](https://aistudio.google.com) for Gemini or [OpenAI](https://platform.openai.com/) for GPT).
* Add your API key in the `.env` file:

  ```env
  GEMINI_API_KEY=your_gemini_api_key
  ```

### Option B: Run a local LLM

* Use a locally hosted LLM like **llama.cpp**, **Ollama**, or **LM Studio**.
* Ensure it’s running and accessible on `localhost`.
* Update the code to point to your local LLM endpoint if needed.

---

## 📧 2. Set Up Gmail Toolkit for Email Automation

MAVIS BOT uses the Gmail API to send, read, and reply to emails.

### Steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable **Gmail API**.
4. Configure **OAuth 2.0 credentials** and download the `credentials.json` file.
5. Add the file to your project directory.
6. On first run, authentication will prompt you to log into your Gmail and authorize access.
7. Tokens will be saved for future sessions.

> ✅ After completing this step, MAVIS BOT will be able to **read**, **summarize**, and **send emails on your behalf**.

---

## 📲 3. Set Up Twilio for SMS & WhatsApp Messaging

MAVIS BOT uses **Twilio API** to send messages.

### Steps:

1. Go to [Twilio’s website](https://www.twilio.com/).

2. Create a free or paid Twilio account.

3. Verify your phone number.

4. Get your **Account SID** and **Auth Token** from the Twilio dashboard.

5. Set them in your `.env` file like this:

   ```env
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   ```

6. If using WhatsApp messaging:

   * Join Twilio's **WhatsApp Sandbox** or get a production number.
   * Follow their setup guide [here](https://www.twilio.com/docs/whatsapp/sandbox).

> ✅ Now MAVIS BOT can **send SMS and WhatsApp messages** from your verified Twilio number.

---

## ✅ Final Step: Run MAVIS BOT

After completing all of the above, you’re ready to launch MAVIS BOT:

```bash
streamlit run app.py
```

The Streamlit interface will open in your browser. From there, you can:

* Send emails
* Generate and reply to email conversations
* Perform live web searches
* Send SMS and WhatsApp messages
* Let the bot act on your behalf

---

## 🔐 Security Note

* Never hardcode credentials directly into your code.
* Use a `.env` file to store sensitive information securely.
* Do not share your `.env` or `credentials.json` file publicly.

---

## 📄 Sample `.env` File Format

```env
GEMINI_API_KEY=your_gemini_api_key

TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

---

Once these steps are completed, MAVIS BOT will be fully functional and ready to assist you with real-world tasks using your own accounts. Enjoy your personal agentic AI assistant! 🚀
