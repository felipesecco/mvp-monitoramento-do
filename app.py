import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="Monitoramento de D.O.", layout="wide")

# =========================
# Carregamento dos dados
# =========================
with open("eventos.json", encoding="utf-8") as f:
    data = json.load(f)

if not data:
    st.warning("Nenhum evento encontrado. Execute o processamento antes de abrir o painel.")
    st.stop()

df = pd.DataFrame(data)

campos_obrigatorios = ["tipo", "texto", "orgao", "data_publicacao", "pessoa", "observacao"]
campos_faltantes = [campo for campo in campos_obrigatorios if campo not in df.columns]

if campos_faltantes:
    st.error(f"Erro na estrutura dos dados. Campos ausentes: {', '.join(campos_faltantes)}")
    st.stop()

# =========================
# Estilo e cabeçalho
# =========================
st.markdown("""
    <style>
        .main-title {
            font-size: 2rem;
            font-weight: 700;
            margin-bottom: 0.2rem;
        }
        .sub-title {
            color: #666;
            margin-bottom: 1.5rem;
        }
        .section-title {
            font-size: 1.2rem;
            font-weight: 600;
            margin-top: 1.2rem;
            margin-bottom: 0.8rem;
        }
        .info-box {
            padding: 1rem;
            border-radius: 0.5rem;
            background-color: #1e293b;
            border: 1px solid #334155;
            color: #f1f5f9;
            margin-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📄 Monitoramento Inteligente de Diários Oficiais</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">MVP funcional para visualização estruturada de eventos monitorados em Diários Oficiais</div>',
    unsafe_allow_html=True
)

# =========================
# KPIs
# =========================
st.markdown('<div class="section-title">📊 Indicadores gerais</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de eventos", len(df))
col2.metric("Tipos de evento", df["tipo"].nunique())
col3.metric("Órgãos no dataset de demonstração", df["orgao"].nunique())
col4.metric("Datas monitoradas", df["data_publicacao"].nunique())

# =========================
# Filtros
# =========================
st.markdown('<div class="section-title">🔎 Filtros</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    filtro_tipo = st.selectbox(
        "Tipo de evento",
        ["Todos"] + sorted(df["tipo"].dropna().unique().tolist())
    )

with col2:
    filtro_orgao = st.selectbox(
        "Órgão",
        ["Todos"] + sorted(df["orgao"].dropna().unique().tolist())
    )

with col3:
    filtro_data = st.selectbox(
        "Data de publicação",
        ["Todos"] + sorted(df["data_publicacao"].dropna().unique().tolist(), reverse=True)
    )

df_filtrado = df.copy()

if filtro_tipo != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == filtro_tipo]

if filtro_orgao != "Todos":
    df_filtrado = df_filtrado[df_filtrado["orgao"] == filtro_orgao]

if filtro_data != "Todos":
    df_filtrado = df_filtrado[df_filtrado["data_publicacao"] == filtro_data]

# =========================
# Resumo dos filtros
# =========================
st.markdown('<div class="section-title">📌 Resumo da consulta</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.write(
        f"Exibindo **{len(df_filtrado)}** evento(s) "
        f"com os filtros selecionados."
    )
with col2:
    st.metric("Eventos filtrados", len(df_filtrado))

# =========================
# Tabela principal
# =========================
st.markdown('<div class="section-title">📋 Eventos identificados</div>', unsafe_allow_html=True)

if df_filtrado.empty:
    st.info("Nenhum evento encontrado para os filtros selecionados.")
else:
    tabela = df_filtrado[
        ["data_publicacao", "orgao", "tipo", "pessoa", "observacao", "texto"]
    ].rename(columns={
        "data_publicacao": "Data",
        "orgao": "Órgão",
        "tipo": "Tipo de Evento",
        "pessoa": "Pessoa",
        "observacao": "Observação",
        "texto": "Descrição"
    })

    st.dataframe(tabela, use_container_width=True, hide_index=True)

# =========================
# Gráficos
# =========================
st.markdown('<div class="section-title">📈 Distribuições</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Distribuição por tipo de evento**")
    st.bar_chart(df_filtrado["tipo"].value_counts().sort_values(ascending=False))

with col2:
    st.markdown("**Distribuição por órgão**")
    st.bar_chart(df_filtrado["orgao"].value_counts().head(10))

# =========================
# Amostra detalhada
# =========================
st.markdown('<div class="section-title">🧾 Exemplo de registro detalhado</div>', unsafe_allow_html=True)

if not df_filtrado.empty:
    exemplo = df_filtrado.iloc[0]

    st.markdown(f"""
    <div class="info-box">
        <b>Data:</b> {exemplo["data_publicacao"]}<br>
        <b>Órgão:</b> {exemplo["orgao"]}<br>
        <b>Tipo de evento:</b> {exemplo["tipo"]}<br>
        <b>Pessoa:</b> {exemplo["pessoa"] if exemplo["pessoa"] else "-"}<br>
        <b>Observação:</b> {exemplo["observacao"]}<br><br>
        <b>📌 Trecho identificado no D.O.:</b><br>
        {exemplo["texto"]}
    </div>
    """, unsafe_allow_html=True)

# =========================
# Rodapé explicativo
# =========================
st.markdown('<div class="section-title">ℹ️ Contexto do MVP</div>', unsafe_allow_html=True)
st.info(
    "Este ambiente representa um MVP funcional em desenvolvimento, voltado à demonstração "
    "da capacidade de estruturar, classificar e visualizar eventos relevantes extraídos de "
    "Diários Oficiais. Em uma evolução futura, a solução poderá incorporar automação de ingestão, "
    "ampliação das fontes monitoradas, enriquecimento semântico e mecanismos de busca mais avançados."
)
st.caption("Dados fictícios utilizados exclusivamente para demonstração do MVP.")