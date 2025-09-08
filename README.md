  # 🎯 Virtual Career Consultant  
An AI-powered **career recommendation system** built with **Streamlit**.  
Users can enter their **skills, education, and interests** to receive personalized career suggestions based on a predefined knowledge base (`career_data.json`).  

---

## 🚀 Features  
- Input skills (comma separated)  
- Select education level from dropdown  
- Choose multiple interests  
- Get career recommendations instantly  
- Expandable database (`career_data.json`) for new careers  
- User-friendly interface with **Streamlit**  

---

## 🗂️ Project Structure  
virtual-career-consultant/
│── app.py # Main Streamlit app (UI)
│── assistent.py # Logic: parsing + recommendations
│── career_data.json # Knowledge base of careers
│── requirements.txt # Dependencies list
│── README.md # Project documentation

# Create venv
python -m venv venv  

# Activate venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate
📌 Example requirements.txt
streamlit

▶️ Running the App Locally

Start the Streamlit server:

streamlit run app.py

🧑‍💻 Usage

Enter your skills (e.g., Python, SQL, Excel).

Select your education level (e.g., BSC/BTech).

Choose your interests (e.g., Data, AI).

Click Get Recommendations.

View careers that best match your profile.
