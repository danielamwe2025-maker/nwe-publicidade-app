
import streamlit as st
from PIL import Image
import os
from pptx import Presentation
from pptx.util import Inches

st.set_page_config(page_title="Análise de Publicidade NWE", layout="wide")
st.title("📊 Gerador de Apresentações de Publicidade - NWE")

st.markdown("Faça upload das imagens das campanhas publicitárias e gere automaticamente uma apresentação com gráficos e insights.")

uploaded_files = st.file_uploader("📁 Envie as imagens das campanhas", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} imagem(ns) carregada(s). Clique abaixo para gerar a apresentação.")
    
    if st.button("🎯 Gerar Apresentação"):
        prs = Presentation()
        title_slide_layout = prs.slide_layouts[0]
        content_slide_layout = prs.slide_layouts[5]

        # Slide de título
        slide = prs.slides.add_slide(title_slide_layout)
        slide.shapes.title.text = "Análise de Publicidade - Loja NWE"
        slide.placeholders[1].text = "Relatório gerado automaticamente com base nas imagens enviadas."

        # Slides com imagens
        for img_file in uploaded_files:
            slide = prs.slides.add_slide(content_slide_layout)
            slide.shapes.title.text = f"Campanha: {img_file.name}"
            image_path = os.path.join("temp", img_file.name)
           import tempfile

temp_dir = tempfile.gettempdir()
image_path = os.path.join(temp_dir, img_file.name)

with open(image_path, "wb") as f:
    f.write(img_file.getbuffer())
           
        # Salvar apresentação
        output_path = "Apresentacao_Publicidade_NWE.pptx"
        prs.save(output_path)
        st.success("✅ Apresentação gerada com sucesso!")
        with open(output_path, "rb") as f:
            st.download_button("📥 Baixar Apresentação", f, file_name=output_path)
