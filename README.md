# 🐧 Club Penguin Classifier – ML Playground  

An interactive **machine learning web app** built with [Streamlit](https://streamlit.io/) that predicts penguin species from biological features.  
Play with sliders and dropdowns to adjust traits like **bill length, flipper size, or body mass**, and instantly see the model’s predictions and probabilities.  

---

## 🚀 Features  
- 🔍 **Explore the Data**: Visualize penguin dataset with customizable charts (scatter, bar, line, area).  
- 🎛️ **Interactive Inputs**: Set penguin traits via sidebar sliders & dropdowns.  
- 🤖 **ML-Powered Predictions**: Random Forest Classifier trained on Palmer Penguins dataset.  
- 📊 **Probability Dashboard**: Predictions shown with progress bars for interpretability.  
- 🧹 **Clean Data Pipeline**: Automatic encoding of categorical variables (`island`, `sex`).  

---

## 📊 Dataset  
This app uses the **Palmer Penguins dataset**, a popular alternative to Iris for ML demos.  
Dataset source: [Palmer Penguins on GitHub](https://github.com/allisonhorst/palmerpenguins)  

---

## 🛠️ Tech Stack  
- **Python**  
- **Streamlit** – UI & interactivity  
- **scikit-learn** – ML classification  
- **pandas / numpy** – data wrangling  

---

## ⚡ Quickstart  

Clone the repo and install dependencies:  

```bash
git clone https://github.com/your-username/club-penguin-classifier.git
cd club-penguin-classifier

pip install -r requirements.txt
