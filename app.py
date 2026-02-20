import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="OBAL PRO | Эко-Математика", layout="wide")

st.title("🍏 «OBAL PRO» – Қалдықсыз өңдеу моделі")
st.markdown("""
Бұл **интерактивті веб-қосымша** алманы терең өңдеу процесін математикалық модельдеуге арналған. 
Сол жақтағы параметрлерді өзгертіп, жүйенің эконмикалық тиімділігін (ROI) және қалдық мөлшерін тексеріп көріңіз!
""")

st.sidebar.header("⚙️ Кіріс параметрлері")
mass_in = st.sidebar.slider("Шикізат массасы (кг):", min_value=100, max_value=5000, value=1000, step=100)
price_per_kg = st.sidebar.number_input("1 кг алма бағасы (теңге):", min_value=50, max_value=300, value=150)

juice = mass_in * 0.65
fiber = mass_in * 0.22
pectin = mass_in * 0.03
acids = mass_in * 0.02
waste = mass_in * 0.08

investment = (mass_in * price_per_kg) + 80000 + 90000
revenue = (juice * 700) + (pectin * 8000) + (fiber * 500)
net_profit = revenue - investment
roi = (net_profit / investment) * 100

st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("Жалпы инвестиция", f"{investment:,.0f} ₸")
col2.metric("Күтілетін табыс", f"{revenue:,.0f} ₸")
col3.metric("Таза пайда (ROI)", f"{roi:.1f} %", f"+{net_profit:,.0f} ₸")

st.subheader("📊 Өнімнің үлестік бөлінісі (Zero Waste)")
data = {
    'Өнім түрі': ['Табиғи шырын', 'Тағамдық талшық', 'Пектин', 'Қышқылдар', 'Қалдық (Биогаз үшін)'],
    'Массасы (кг)': [juice, fiber, pectin, acids, waste]
}
df = pd.DataFrame(data)

fig = px.pie(df, values='Массасы (кг)', names='Өнім түрі', hole=0.4, 
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.info("🤖 **Жобаның Telegram-ботын сынап көріңіз:** Tulkibas_agro_bot")
