import streamlit as st

st.set_page_config(page_title="ESI Triage | Telepatia", page_icon="🏥", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap');
*{font-family:'IBM Plex Sans',sans-serif!important}
#MainMenu,footer,.stDeployButton,header{display:none!important}
.block-container{padding-top:2rem!important;padding-bottom:2rem!important;max-width:1200px!important}
/* Force light mode */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #FFFFFF !important;
    color: #111827 !important;
}
[data-testid="stSidebar"], [data-testid="stHeader"] {
    background-color: #FFFFFF !important;
}
.stTextInput>div>div>input, .stNumberInput>div>div>input, .stTextArea>div>div>textarea {
    background-color: #FFFFFF !important;
    color: #111827 !important;
}
</style>
""", unsafe_allow_html=True)

LOGO_SVG = '<svg width="180" height="42" viewBox="0 0 918 396" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M793.982 240.744C780.094 240.744 770.67 233.8 770.67 222.268C770.67 209.62 779.474 202.552 796.09 202.552H814.69V198.212C814.69 189.656 808.862 185.068 798.942 185.068C789.642 185.068 784.062 189.284 782.822 195.732H772.654C774.142 183.332 784.186 176.016 799.438 176.016C815.558 176.016 824.858 184.076 824.858 198.832V226.484C824.858 229.832 826.098 230.7 828.95 230.7H832.174V240H826.594C818.534 240 815.186 236.28 815.186 230.452V230.204C811.466 235.908 804.894 240.744 793.982 240.744ZM794.726 232.064C807.374 232.064 814.69 224.748 814.69 214.208V211.108H795.098C786.046 211.108 780.962 214.456 780.962 221.648C780.962 228.344 786.294 232.064 794.726 232.064Z" fill="#1F2937"/><path d="M748.456 240V176.76H758.624V240H748.456ZM753.54 165.972C749.944 165.972 747.092 163.244 747.092 159.524C747.092 155.804 749.944 153.076 753.54 153.076C757.136 153.076 759.988 155.804 759.988 159.524C759.988 163.244 757.136 165.972 753.54 165.972Z" fill="#1F2937"/><path d="M726.911 240C714.759 240 710.419 234.668 710.419 223.508V186.06H699.011V176.76H710.419V159.028H720.587V176.76H737.947V186.06H720.587V223.384C720.587 228.716 722.447 230.7 727.903 230.7H737.947V240H726.911Z" fill="#1F2937"/><path d="M660.537 240.744C646.649 240.744 637.225 233.8 637.225 222.268C637.225 209.62 646.029 202.552 662.645 202.552H681.245V198.212C681.245 189.656 675.417 185.068 665.497 185.068C656.197 185.068 650.617 189.284 649.377 195.732H639.209C640.697 183.332 650.741 176.016 665.993 176.016C682.113 176.016 691.413 184.076 691.413 198.832V226.484C691.413 229.832 692.653 230.7 695.505 230.7H698.729V240H693.149C685.089 240 681.741 236.28 681.741 230.452V230.204C678.021 235.908 671.449 240.744 660.537 240.744ZM661.281 232.064C673.929 232.064 681.245 224.748 681.245 214.208V211.108H661.653C652.601 211.108 647.517 214.456 647.517 221.648C647.517 228.344 652.849 232.064 661.281 232.064Z" fill="#1F2937"/><path d="M565.725 264.8V176.76H574.529L575.893 186.928C580.109 181.1 586.929 176.016 597.593 176.016C615.077 176.016 627.973 187.796 627.973 208.38C627.973 227.724 615.077 240.744 597.593 240.744C586.929 240.744 579.737 236.404 575.893 230.328V264.8H565.725ZM596.601 231.692C609.125 231.692 617.557 222.144 617.557 208.38C617.557 194.616 609.125 185.068 596.601 185.068C584.201 185.068 575.769 194.616 575.769 208.132C575.769 222.02 584.201 231.692 596.601 231.692Z" fill="#1F2937"/><path d="M525.225 240.744C506.253 240.744 493.853 227.724 493.853 208.38C493.853 189.16 506.005 176.016 523.861 176.016C541.593 176.016 553.621 187.548 553.621 206.768V210.364H504.517V211.232C504.517 223.26 512.453 231.692 524.481 231.692C533.657 231.692 540.601 226.98 542.709 218.796H553.001C550.521 231.444 539.857 240.744 525.225 240.744ZM504.889 201.808H542.957C541.965 191.02 534.525 184.944 523.985 184.944C514.685 184.944 506.005 191.268 504.889 201.808Z" fill="#1F2937"/><path d="M471.514 240V153.2H481.682V240H471.514Z" fill="#1F2937"/><path d="M431.014 240.744C412.042 240.744 399.642 227.724 399.642 208.38C399.642 189.16 411.794 176.016 429.65 176.016C447.382 176.016 459.41 187.548 459.41 206.768V210.364H410.306V211.232C410.306 223.26 418.242 231.692 430.27 231.692C439.446 231.692 446.39 226.98 448.498 218.796H458.79C456.31 231.444 445.646 240.744 431.014 240.744ZM410.678 201.808H448.746C447.754 191.02 440.314 184.944 429.774 184.944C420.474 184.944 411.794 191.268 410.678 201.808Z" fill="#1F2937"/><path d="M382.52 240C370.368 240 366.028 234.668 366.028 223.508V186.06H354.62V176.76H366.028V159.028H376.196V176.76H393.556V186.06H376.196V223.384C376.196 228.716 378.056 230.7 383.512 230.7H393.556V240H382.52Z" fill="#1F2937"/><path d="M196.147 84C218.966 84 237.464 102.652 237.464 125.66V155.417H260.977C267.55 155.417 272.879 160.747 272.879 167.32C272.879 173.894 267.55 179.223 260.977 179.224H225.659C219.14 179.224 213.855 173.938 213.854 167.419V125.66C213.606 115.552 205.774 107.806 196.147 107.806C186.368 107.806 178.44 115.8 178.439 125.66V167.419C178.439 173.938 173.154 179.223 166.635 179.224H126.398V179.25C125.975 179.232 125.647 179.223 125.317 179.223C115.538 179.223 107.611 187.217 107.61 197.077C107.61 206.938 115.538 214.932 125.317 214.932C125.647 214.932 125.975 214.921 126.301 214.903V214.934H166.635C173.154 214.933 178.439 220.218 178.439 226.737V268.495C178.44 278.356 186.368 286.35 196.147 286.35C205.774 286.349 213.606 278.603 213.849 268.956V226.737C213.855 220.218 219.14 214.933 225.659 214.933H266.878C276.603 214.932 284.435 207.186 284.678 197.539C284.684 190.504 290.013 185.175 296.587 185.175H314.098C320.671 185.175 326.001 190.504 326.001 197.078C326.001 203.652 320.671 208.98 314.098 208.98H306.58C301.5 226.189 285.693 238.738 266.977 238.738H237.464V268.495C237.464 291.503 218.966 310.155 196.147 310.155C173.484 310.155 155.085 291.757 154.835 268.966V238.738H126.398C125.742 238.732 125.53 238.737 125.317 238.737C102.499 238.737 84 220.085 84 197.077C84 174.069 102.499 155.417 125.317 155.417H154.83V125.562C154.836 125.199 155.081 102.403 196.147 84Z" fill="url(#grad1)"/><defs><linearGradient id="grad1" x1="251" y1="255" x2="125" y2="156" gradientUnits="userSpaceOnUse"><stop stop-color="#068450"/><stop offset=".42" stop-color="#38A64A"/><stop offset="1" stop-color="#2FA879"/></linearGradient></defs></svg>'

ESI = {
    1: {'l': 'ESI 1', 'n': 'Ressuscitacao', 'c': '#DC2626', 'bg': '#FEE2E2', 'tx': '#991B1B', 'desc': 'Risco de vida iminente', 't': 'Imediato'},
    2: {'l': 'ESI 2', 'n': 'Emergente', 'c': '#EA580C', 'bg': '#FFEDD5', 'tx': '#9A3412', 'desc': 'Nao pode esperar', 't': '10 min'},
    3: {'l': 'ESI 3', 'n': 'Urgente', 'c': '#CA8A04', 'bg': '#FEF9C3', 'tx': '#713F12', 'desc': 'Precisa de varios exames', 't': '30-60 min'},
    4: {'l': 'ESI 4', 'n': 'Menos Urgente', 'c': '#16A34A', 'bg': '#DCFCE7', 'tx': '#166534', 'desc': 'Precisa de 1 exame', 't': '1-2 horas'},
    5: {'l': 'ESI 5', 'n': 'Nao Urgente', 'c': '#2563EB', 'bg': '#DBEAFE', 'tx': '#1E40AF', 'desc': 'Apenas consulta', 't': '2-4 horas'}
}

RESOURCES = {
    'labs': 'Exames de sangue ou urina',
    'ecg': 'Eletrocardiograma (ECG)',
    'xray': 'Raio-X',
    'ct': 'Tomografia (CT)',
    'mri': 'Ressonancia magnetica (MRI)',
    'us': 'Ultrassonografia',
    'iv_fluids': 'Soro na veia (hidratacao IV)',
    'iv_meds': 'Medicacao injetavel (IV/IM) ou inalatoria',
    'consult': 'Avaliacao de especialista',
    'simple_proc': 'Procedimento simples (ex: sutura, sonda)',
    'complex_proc': 'Procedimento complexo (ex: drenagem, reducao)'
}

NOT_RESOURCES = [
    'Apenas conversa e exame fisico',
    'Glicemia capilar (ponta de dedo)',
    'Acesso venoso sem medicacao',
    'Medicacao via oral',
    'Vacina antitetanica',
    'Receita medica',
    'Troca de curativo simples',
    'Muletas ou talas prontas'
]

def check_danger(hr, rr, spo2):
    a = []
    if hr < 50 or hr > 100: a.append(f'FC {hr}')
    if rr < 12 or rr > 20: a.append(f'FR {rr}')
    if spo2 < 92: a.append(f'SpO2 {spo2}%')
    return a

def gen_summary(lvl, dp, f, rc, rl):
    e = ESI[lvl]
    s = [f"CLASSIFICACAO: {e['l']} - {e['n']}", f"Tempo: {e['t']}", f"Decisao: {dp}", ""]
    if f: s.append("Achados:"); s.extend([f"  - {x}" for x in f])
    if rl: s.append(""); s.append(f"Recursos: {rc}"); s.extend([f"  - {RESOURCES.get(x,x)}" for x in rl])
    return "\n".join(s)

st.markdown(f'<div style="background:#FFF;padding:24px 32px;border-radius:16px;box-shadow:0 4px 12px rgba(0,0,0,.08);margin-bottom:32px;display:flex;align-items:center;gap:24px;">{LOGO_SVG}<div style="width:1px;height:40px;background:#E5E7EB;"></div><div><div style="font-size:22px;font-weight:600;color:#111827;">Emergency Severity Index (ESI)</div><div style="font-size:14px;color:#6B7280;margin-top:4px;">Algoritmo de Triagem v5</div></div></div>', unsafe_allow_html=True)

rph = st.empty()
esi_level = None; decision_point = ''; findings = []; resources_selected = []

# POINT A
st.markdown('<div style="font-size:18px;font-weight:600;color:#374151;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #DC2626;">Passo 1: Intervencao imediata para salvar a vida</div>', unsafe_allow_html=True)
st.markdown('<div style="background:#FEF2F2;border-left:4px solid #DC2626;padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:16px;"><span style="font-weight:500;color:#991B1B;">Requer manejo de via aerea, ventilacao, ressuscitacao ou medicacao de emergencia = ESI 1</span></div>', unsafe_allow_html=True)

ca1, ca2 = st.columns(2)
with ca1:
    a1 = st.checkbox("Intubado ou necessita intubacao imediata")
    a2 = st.checkbox("Apneico ou em parada cardiorrespiratoria")
    a3 = st.checkbox("Ausencia de pulso")
    a4 = st.checkbox("Insuficiencia respiratoria grave")
    a5 = st.checkbox("SpO2 < 90%")
with ca2:
    a6 = st.checkbox("Irresponsivo (nao responde a estimulos)")
    a7 = st.checkbox("Rebaixamento agudo do nivel de consciencia")
    a8 = st.checkbox("Comprometimento de via aerea")
    a9 = st.checkbox("Necessita medicacao de emergencia")
    a10 = st.checkbox("Necessita intervencao hemodinamica")

pa = any([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
if pa:
    esi_level = 1; decision_point = 'Passo 1 - Risco iminente'
    for v, n in [(a1,'Intubacao'),(a2,'PCR/Apneia'),(a3,'Sem pulso'),(a4,'Insuf resp'),(a5,'SpO2<90%'),(a6,'Irresponsivo'),(a7,'Alt consciencia'),(a8,'Via aerea'),(a9,'Med emergencia'),(a10,'Instab hemod')]:
        if v: findings.append(n)

# POINT B
st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:18px;font-weight:600;color:#374151;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #EA580C;">Passo 2: Situacao de alto risco</div>', unsafe_allow_html=True)
st.markdown('<div style="background:#FFF7ED;border-left:4px solid #EA580C;padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:16px;"><span style="font-weight:500;color:#9A3412;">Paciente que voce colocaria no ultimo leito disponivel = ESI 2</span></div>', unsafe_allow_html=True)

db = pa
cb1, cb2 = st.columns(2)
with cb1:
    b1 = st.checkbox("Confuso, letargico ou desorientado", disabled=db)
    b2 = st.checkbox("Risco de deterioracao clinica", disabled=db)
    b3 = st.checkbox("Dor intensa (EVA >= 7/10)", disabled=db)
    b4 = st.checkbox("Desconforto grave ou agitacao", disabled=db)
with cb2:
    b5 = st.checkbox("Dor toracica sugestiva de SCA", disabled=db)
    b6 = st.checkbox("Deficit neurologico agudo (suspeita AVC)", disabled=db)
    b7 = st.checkbox("Suspeita de sepse", disabled=db)
    b8 = st.checkbox("Intoxicacao exogena / overdose", disabled=db)
    b9 = st.checkbox("Ideacao suicida ou risco de autolesao", disabled=db)

pb = any([b1,b2,b3,b4,b5,b6,b7,b8,b9])
if not pa and pb:
    esi_level = 2; decision_point = 'Passo 2 - Alto risco'
    for v, n in [(b1,'Confuso'),(b2,'Risco piora'),(b3,'Dor>=7'),(b4,'Desconforto'),(b5,'Dor toracica'),(b6,'AVC'),(b7,'Sepse'),(b8,'Overdose'),(b9,'Risco suicidio')]:
        if v: findings.append(n)

# POINT C
st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:18px;font-weight:600;color:#374151;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #CA8A04;">Passo 3: Estimativa de recursos</div>', unsafe_allow_html=True)
st.markdown('<div style="background:#FEFCE8;border-left:4px solid #CA8A04;padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:16px;"><span style="font-weight:500;color:#713F12;">Conte TIPOS diferentes de recursos (ex: laboratorio + imagem = 2). Nao conte quantidade de exames.</span></div>', unsafe_allow_html=True)

dc = pa or pb
cc1, cc2 = st.columns(2)
with cc1:
    st.markdown('<div style="font-size:12px;color:#6B7280;margin-bottom:8px;font-weight:500;">EXAMES</div>', unsafe_allow_html=True)
    r1 = st.checkbox("Laboratorio (sangue, urina)", disabled=dc)
    r2 = st.checkbox("ECG", disabled=dc)
    r3 = st.checkbox("Radiografia", disabled=dc)
    r4 = st.checkbox("Tomografia (CT)", disabled=dc)
    r5 = st.checkbox("Ressonancia (MRI)", disabled=dc)
    r6 = st.checkbox("Ultrassonografia", disabled=dc)
with cc2:
    st.markdown('<div style="font-size:12px;color:#6B7280;margin-bottom:8px;font-weight:500;">TRATAMENTOS</div>', unsafe_allow_html=True)
    r7 = st.checkbox("Hidratacao IV", disabled=dc)
    r8 = st.checkbox("Medicacao IV/IM/nebulizacao", disabled=dc)
    r9 = st.checkbox("Interconsulta", disabled=dc)
    r10 = st.checkbox("Procedimento simples (sutura, sonda)", disabled=dc)
    r11 = st.checkbox("Procedimento complexo (conta como 2)", disabled=dc)

for v, k in [(r1,'labs'),(r2,'ecg'),(r3,'xray'),(r4,'ct'),(r5,'mri'),(r6,'us'),(r7,'iv_fluids'),(r8,'iv_meds'),(r9,'consult'),(r10,'simple_proc'),(r11,'complex_proc')]:
    if v: resources_selected.append(k)
rc = len(resources_selected) + (1 if r11 else 0)

st.markdown(f'<div style="background:#F3F4F6;padding:16px;border-radius:8px;margin-top:16px;"><div style="font-size:14px;color:#6B7280;">Total de recursos previstos</div><div style="font-size:32px;font-weight:700;color:#111827;">{rc}</div><div style="font-size:12px;color:#9CA3AF;margin-top:4px;">0 = ESI 5 | 1 = ESI 4 | 2+ = ESI 3</div></div>', unsafe_allow_html=True)

# POINT D
st.markdown('<div style="height:24px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:18px;font-weight:600;color:#374151;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #6B7280;">Passo 4: Avaliacao de sinais vitais</div>', unsafe_allow_html=True)
st.markdown('<div style="background:#F3F4F6;border-left:4px solid #6B7280;padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:16px;"><span style="font-weight:500;color:#374151;">Sinais vitais na zona de perigo podem indicar necessidade de reclassificacao para ESI 2.</span></div>', unsafe_allow_html=True)

cd1, cd2, cd3 = st.columns(3)
with cd1: hr = st.number_input("Frequencia cardiaca (bpm)", 30, 250, 80)
with cd2: rr = st.number_input("Frequencia respiratoria (rpm)", 4, 60, 16)
with cd3: spo2 = st.number_input("Saturacao de oxigenio (%)", 50, 100, 98)

da = check_danger(hr, rr, spo2)
if da and not dc:
    st.markdown(f'<div style="background:#FEF3C7;border-left:4px solid #F59E0B;padding:12px 16px;border-radius:0 8px 8px 0;margin-top:16px;"><div style="font-weight:600;color:#92400E;">Zona de perigo: {", ".join(da)}</div><div style="font-size:13px;color:#78350F;margin-top:4px;">Considere upgrade para ESI 2</div></div>', unsafe_allow_html=True)

up2 = st.checkbox("Upgrade para ESI 2 (zona de perigo)", disabled=dc or not da)

if not pa and not pb:
    if up2 and da:
        esi_level = 2; decision_point = 'Passo 4 - Sinais vitais'; findings.extend(da)
    elif rc >= 2:
        esi_level = 3; decision_point = f'Passo 3 - {rc} recursos'
    elif rc == 1:
        esi_level = 4; decision_point = 'Passo 3 - 1 recurso'
    else:
        esi_level = 5; decision_point = 'Passo 3 - 0 recursos'

if esi_level is None: esi_level = 5; decision_point = 'Sem criterios de urgencia'

# RESULT TOP
e = ESI[esi_level]
ft = "".join([f'<span style="display:inline-block;padding:4px 12px;border-radius:16px;font-size:12px;font-weight:500;color:#FFF;background:{e["c"]};margin:2px 4px 2px 0;">{f}</span>' for f in findings[:6]])

with rph.container():
    st.markdown(f'<div style="background:{e["bg"]};border:2px solid {e["c"]};border-radius:16px;padding:24px 32px;margin-bottom:24px;"><div style="display:flex;align-items:center;justify-content:space-between;"><div><div style="font-size:14px;color:{e["tx"]};opacity:.8;">Classificacao ESI</div><div style="font-size:36px;font-weight:700;color:{e["tx"]};">{e["l"]}</div><div style="font-size:16px;color:{e["tx"]};margin-top:4px;">{e["n"]}</div><div style="margin-top:12px;">{ft if ft else decision_point}</div></div><div style="text-align:right;"><div style="font-size:14px;color:{e["tx"]};opacity:.8;">Tempo</div><div style="font-size:32px;font-weight:700;color:{e["tx"]};">{e["t"]}</div></div></div></div>', unsafe_allow_html=True)

if st.button("Limpar e comecar nova triagem"): st.rerun()

# LEGEND
st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:16px;font-weight:600;color:#374151;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #E5E7EB;">Resumo dos niveis ESI</div>', unsafe_allow_html=True)
lg = "".join([f'<div style="background:{v["bg"]};border-left:4px solid {v["c"]};padding:16px;border-radius:0 8px 8px 0;"><div style="font-size:18px;font-weight:700;color:{v["tx"]};">{v["l"]}</div><div style="font-size:13px;color:{v["tx"]};">{v["n"]}</div><div style="font-size:11px;color:{v["tx"]};opacity:.8;margin-top:8px;">{v["desc"]}</div></div>' for k, v in ESI.items()])
st.markdown(f'<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px;">{lg}</div>', unsafe_allow_html=True)

# RESOURCES
st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:16px;font-weight:600;color:#374151;margin-bottom:8px;">O que sao recursos?</div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:14px;color:#6B7280;margin-bottom:16px;">Recursos sao exames, tratamentos ou procedimentos que o paciente provavelmente vai precisar durante o atendimento. A quantidade de recursos ajuda a definir a prioridade (ESI 3, 4 ou 5).</div>', unsafe_allow_html=True)

cr1, cr2 = st.columns(2)
with cr1:
    st.markdown('<div style="font-size:14px;font-weight:600;color:#16A34A;margin-bottom:12px;">Conta como recurso</div>', unsafe_allow_html=True)
    rl = "".join([f'<div style="padding:4px 0;font-size:13px;">- {v}</div>' for k, v in RESOURCES.items()])
    st.markdown(f'<div style="background:#F0FDF4;padding:16px;border-radius:8px;">{rl}</div>', unsafe_allow_html=True)
with cr2:
    st.markdown('<div style="font-size:14px;font-weight:600;color:#DC2626;margin-bottom:12px;">NAO conta como recurso</div>', unsafe_allow_html=True)
    nr = "".join([f'<div style="padding:4px 0;font-size:13px;">- {r}</div>' for r in NOT_RESOURCES])
    st.markdown(f'<div style="background:#FEF2F2;padding:16px;border-radius:8px;">{nr}</div>', unsafe_allow_html=True)

# RESULT BOTTOM
st.markdown('<div style="height:32px;"></div>', unsafe_allow_html=True)
st.markdown('<div style="font-size:16px;font-weight:600;color:#374151;margin-bottom:16px;padding-bottom:8px;border-bottom:2px solid #E5E7EB;">Resultado</div>', unsafe_allow_html=True)
st.markdown(f'<div style="background:{e["bg"]};border:2px solid {e["c"]};border-radius:16px;padding:24px 32px;margin-bottom:24px;"><div style="display:flex;align-items:center;justify-content:space-between;"><div><div style="font-size:14px;color:{e["tx"]};opacity:.8;">Classificacao ESI</div><div style="font-size:36px;font-weight:700;color:{e["tx"]};">{e["l"]}</div><div style="font-size:16px;color:{e["tx"]};margin-top:4px;">{e["n"]}</div><div style="margin-top:12px;">{ft if ft else decision_point}</div></div><div style="text-align:right;"><div style="font-size:14px;color:{e["tx"]};opacity:.8;">Tempo</div><div style="font-size:32px;font-weight:700;color:{e["tx"]};">{e["t"]}</div></div></div></div>', unsafe_allow_html=True)

st.markdown('<div style="font-size:14px;font-weight:500;color:#374151;margin-bottom:8px;">Resumo</div>', unsafe_allow_html=True)
st.text_area("r", value=gen_summary(esi_level, decision_point, findings, rc, resources_selected), height=180, label_visibility="collapsed")

st.markdown('<div style="margin-top:40px;padding:20px;text-align:center;border-top:1px solid #E5E7EB;"><div style="font-size:13px;color:#6B7280;"><strong style="color:#059669;">telepatia.ai</strong> - ESI v5</div><div style="font-size:12px;color:#9CA3AF;margin-top:4px;">Ferramenta de apoio. Nao substitui julgamento clinico.</div></div>', unsafe_allow_html=True)
