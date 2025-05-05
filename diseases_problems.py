import streamlit as st
import datetime

# تعديل شكل الصفحة والألوان
st.set_page_config(
    page_title="Genetic and Chronic Diseases App",
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# خلفية وألوان مبهجة
page_bg_img = """
<style>
body {
background-color: #e0f7fa;
color: #00695c;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# عنوان رئيسي
st.title("🧬 Genetic and Chronic Diseases Explorer")
st.write("استكشاف شامل للأمراض الوراثية والمزمنة - Detailed medical insights.")

# خانة الموبايل أو الإيميل
st.sidebar.header("Set Reminder")
contact = st.sidebar.text_input("Enter your phone number or email (أدخل رقم هاتفك أو بريدك الإلكتروني):")
reminder_time = st.sidebar.time_input("Select reminder time (حدد وقت التذكير):", datetime.time(9, 0))

# قائمة الأمراض
diseases = [
    "Type 1 Diabetes",
    "Cystic Fibrosis",
    "Sickle Cell Anemia",
    "Hereditary Cancer",
    "Down Syndrome",
    "Aplastic Anemia",
    "Hereditary Blindness",
    "Wilson's Disease",
    "Multiple Sclerosis",
    "Lupus (SLE)",
    "Rheumatoid Arthritis",
    "Hypertension",
    "Asthma",
    "Type 2 Diabetes",
    "Autism Spectrum Disorder",
    "Schizophrenia",
    "Breast Cancer",
    "Alzheimer's Disease",
    "Amyotrophic Lateral Sclerosis (ALS)"
]

# اختيار المرض
selected_disease = st.selectbox("Choose a Disease (اختر مرضًا):", diseases)

# دالة عرض المعلومات
def show_disease_info(name):
    if name == "Type 1 Diabetes":
        st.header("Type 1 Diabetes (سكري النوع الأول)")
        st.subheader("Definition (تعريف):")
        st.write("Type 1 diabetes is a chronic condition in which the pancreas produces little or no insulin. It usually appears during childhood or adolescence.")
        st.write("سكري النوع الأول هو حالة مزمنة حيث ينتج البنكرياس القليل أو لا ينتج الإنسولين. يظهر عادة في الطفولة أو المراهقة.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Increased thirst (العطش الشديد)
        - Frequent urination (التبول المتكرر)
        - Hunger (الجوع)
        - Fatigue (التعب)
        - Blurred vision (تشوش الرؤية)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("An autoimmune destruction of insulin-producing beta cells in the pancreas triggered by genetic factors and possibly viruses.")
        st.write("تدمير مناعي ذاتي لخلايا بيتا المنتجة للإنسولين في البنكرياس، ناجم عن عوامل وراثية وربما فيروسات.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Administer fast-acting sugar if low blood sugar suspected (تناول سكر سريع الامتصاص في حالة الاشتباه في انخفاض السكر).
        - Monitor blood glucose levels regularly (مراقبة مستويات السكر باستمرار).
        - Seek emergency help if unconsciousness occurs (طلب إسعاف في حالة فقدان الوعي).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Genetic Disorder (اضطراب مناعي وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with genes like HLA-DR3 and HLA-DR4, affecting immune response.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Maintain a consistent eating schedule and monitor your blood sugar before and after meals.")
        st.success("احرص على تناول وجبات منتظمة ومراقبة السكر قبل وبعد الأكل.")

    elif name == "Cystic Fibrosis":
        st.header("Cystic Fibrosis (التليف الكيسي)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder that affects the lungs, pancreas, and other organs, causing thick, sticky mucus production.")
        st.write("اضطراب جيني يؤثر على الرئتين والبنكرياس وأعضاء أخرى، ويسبب إنتاج مخاط سميك ولزج.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Chronic cough (سعال مزمن)
        - Difficulty breathing (صعوبة في التنفس)
        - Frequent lung infections (عدوى رئوية متكررة)
        - Poor growth (نمو ضعيف)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Caused by mutations in the CFTR gene, affecting chloride channels and leading to mucus buildup.")
        st.write("ينتج عن طفرات في جين CFTR تؤثر على قنوات الكلوريد وتؤدي إلى تراكم المخاط.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Chest physiotherapy to clear mucus (العلاج الطبيعي للصدر لتنظيف المخاط).
        - Use of medications like bronchodilators (استخدام أدوية مثل موسعات الشعب الهوائية).
        - Seek medical advice for respiratory distress (طلب استشارة طبية في حالة ضيق التنفس).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Disorder (اضطراب وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Caused by mutations in the CFTR gene, leading to faulty chloride transport.")
        st.write("ناجم عن طفرات في جين CFTR مما يؤدي إلى النقل الخاطئ للكلوريد.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early diagnosis and lung function monitoring are crucial for better management.")
        st.success("التشخيص المبكر ومراقبة وظائف الرئة أمران حاسمان لإدارة أفضل.")
    elif name == "Sickle Cell Anemia":
        st.header("Sickle Cell Anemia (الأنيميا المنجلية)")
        st.subheader("Definition (تعريف):")
        st.write("A hereditary blood disorder causing red blood cells to become crescent-shaped, leading to blockages in blood flow.")
        st.write("اضطراب دموي وراثي يؤدي إلى تحول خلايا الدم الحمراء لشكل منجلي مما يسبب انسداد الأوعية الدموية.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Pain episodes (نوبات ألم)
        - Fatigue (إرهاق)
        - Swelling in hands and feet (تورم اليدين والقدمين)
        - Frequent infections (عدوى متكررة)
        - Delayed growth (تأخر النمو)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Caused by mutations in the HBB gene affecting hemoglobin structure.")
        st.write("ناتج عن طفرات في جين HBB تؤثر على تركيب الهيموغلوبين.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Provide hydration and warmth (توفير السوائل والدفء).
        - Use pain relievers as prescribed (استخدام مسكنات الألم حسب وصف الطبيب).
        - Seek emergency care during severe crises (طلب رعاية طبية في النوبات الشديدة).
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Blood Disorder (اضطراب دم وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Mutation in the HBB gene leads to abnormal hemoglobin S formation.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Avoid dehydration and extreme temperatures.")
        st.success("تجنب الجفاف ودرجات الحرارة الشديدة.")

    elif name == "Hereditary Cancer":
        st.header("Hereditary Cancer (السرطان الوراثي)")
        st.subheader("Definition (تعريف):")
        st.write("Cancers caused by inherited genetic mutations that increase cancer risk.")
        st.write("أنواع السرطان الناتجة عن طفرات جينية موروثة تزيد خطر الإصابة بالسرطان.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Depends on cancer type (تختلف حسب نوع السرطان)
        - Unusual lumps (كتل غير طبيعية)
        - Persistent pain or fatigue (ألم أو تعب مستمر)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Mutations in tumor suppressor genes like BRCA1, BRCA2, or TP53.")
        st.write("طفرات في جينات مثبطة للأورام مثل BRCA1، BRCA2 أو TP53.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("""
        - Regular screenings (فحوصات منتظمة)
        - Early detection improves outcome (الكشف المبكر يحسن فرص الشفاء)
        """)

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Cancer Predisposition (استعداد وراثي للإصابة بالسرطان)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("BRCA1/2 mutations increase breast and ovarian cancer risks.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Consider genetic testing if there's a strong family history.")
        st.success("فكر في إجراء فحص جيني إذا كان هناك تاريخ عائلي قوي.")
    elif name == "Down Syndrome":
        st.header("Down Syndrome (متلازمة داون)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder caused by the presence of an extra chromosome 21.")
        st.write("اضطراب جيني ناتج عن وجود نسخة إضافية من الكروموسوم 21.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Intellectual disability (إعاقة ذهنية)
        - Distinct facial features (ملامح وجه مميزة)
        - Delayed development (تأخر في النمو)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Trisomy 21 – three copies of chromosome 21.")
        st.write("التثلث الصبغي 21 – ثلاث نسخ من الكروموسوم 21.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Supportive care and early developmental interventions.")
        st.write("رعاية داعمة وتدخل مبكر في النمو والتعلم.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Chromosomal Genetic Disorder (اضطراب وراثي صبغي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Caused by nondisjunction during cell division.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early therapy improves quality of life.")
        st.success("التدخل المبكر يُحسّن نوعية الحياة.")

    elif name == "Aplastic Anemia":
        st.header("Aplastic Anemia (فقر الدم اللاتنسجي)")
        st.subheader("Definition (تعريف):")
        st.write("A rare condition where the bone marrow fails to produce enough blood cells.")
        st.write("حالة نادرة يفشل فيها نخاع العظم في إنتاج ما يكفي من خلايا الدم.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Fatigue (تعب شديد)
        - Frequent infections (عدوى متكررة)
        - Easy bruising or bleeding (سهولة النزيف أو ظهور الكدمات)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Can be autoimmune, inherited, or due to toxins/radiation.")
        st.write("قد يكون مناعي ذاتي، وراثي، أو ناتج عن سموم أو إشعاع.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Avoid infections, rest, and seek urgent medical care.")
        st.write("تجنب العدوى، الراحة، وطلب رعاية طبية عاجلة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Bone marrow failure – possibly autoimmune or inherited.")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("May involve genes like TERT, TERC in inherited cases.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Avoid crowded places to reduce infection risk.")
        st.success("تجنب الأماكن المزدحمة للحد من خطر العدوى.")

    elif name == "Hereditary Blindness":
        st.header("Hereditary Blindness (العمى الوراثي)")
        st.subheader("Definition (تعريف):")
        st.write("Genetic conditions leading to progressive or congenital vision loss.")
        st.write("حالات وراثية تؤدي إلى فقدان البصر التدريجي أو الولادي.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Night blindness (العمى الليلي)
        - Tunnel vision (رؤية أنبوبية)
        - Total blindness (فقدان البصر الكامل)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Mutations in genes related to retina function (e.g. RPE65, RPGR).")
        st.write("طفرات في جينات مسؤولة عن وظائف الشبكية مثل RPE65 و RPGR.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Provide mobility support and safe environment.")
        st.write("توفير دعم للحركة وبيئة آمنة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Inherited Retinal Degeneration (تنكس شبكي وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Mutations in over 100 genes can cause hereditary blindness.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Genetic testing helps identify treatment options.")
        st.success("الفحص الجيني يساعد في تحديد الخيارات العلاجية.")

    elif name == "Wilson's Disease":
        st.header("Wilson's Disease (مرض ويلسون)")
        st.subheader("Definition (تعريف):")
        st.write("A genetic disorder causing copper accumulation in organs like the liver and brain.")
        st.write("اضطراب وراثي يؤدي إلى تراكم النحاس في الأعضاء مثل الكبد والدماغ.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Liver disease (أمراض الكبد)
        - Neurological symptoms (أعراض عصبية)
        - Behavioral changes (تغيرات سلوكية)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Mutation in ATP7B gene affecting copper transport.")
        st.write("طفرة في جين ATP7B تؤثر على نقل النحاس.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Avoid high-copper foods and seek urgent medical care.")
        st.write("تجنب الأطعمة الغنية بالنحاس وطلب العناية الطبية فورًا.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Metabolic Genetic Disorder (اضطراب وراثي أيضي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("ATP7B gene mutations lead to defective copper excretion.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Chelation therapy and diet control are essential.")
        st.success("العلاج المخلب والتحكم في النظام الغذائي ضروريان.")
          elif name == "Multiple Sclerosis":
        st.header("Multiple Sclerosis (التصلب المتعدد)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic autoimmune disorder affecting the central nervous system.")
        st.write("اضطراب مناعي مزمن يؤثر على الجهاز العصبي المركزي.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Muscle weakness (ضعف العضلات)
        - Numbness (تنميل)
        - Vision problems (مشاكل في الرؤية)
        - Balance difficulties (صعوبات في التوازن)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Unknown exact cause; likely involves genetic and environmental factors.")
        st.write("السبب الدقيق غير معروف، لكن غالبًا بسبب عوامل وراثية وبيئية.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Support during flare-ups and avoid triggers.")
        st.write("الدعم خلال النوبات وتجنب المحفزات.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Neurological Disorder (اضطراب عصبي مناعي ذاتي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with HLA-DRB1 and other immune-related genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Physical therapy helps maintain function.")
        st.success("العلاج الطبيعي يساعد في الحفاظ على الوظائف الحركية.")

    elif name == "Lupus (SLE)":
        st.header("Lupus (SLE) - الذئبة الحمراء")
        st.subheader("Definition (تعريف):")
        st.write("A chronic autoimmune disease that can affect various body systems.")
        st.write("مرض مناعي ذاتي مزمن يمكن أن يؤثر على أنظمة الجسم المختلفة.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Fatigue (إرهاق)
        - Joint pain (ألم في المفاصل)
        - Skin rash (طفح جلدي)
        - Kidney or heart problems (مشاكل في الكلى أو القلب)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Combination of genetic, hormonal, and environmental factors.")
        st.write("خليط من العوامل الوراثية والهرمونية والبيئية.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Avoid sun exposure and manage stress.")
        st.write("تجنب الشمس والتعامل مع التوتر.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Systemic Autoimmune Disease (مرض مناعي ذاتي جهازي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to genes like HLA-DR2, HLA-DR3.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Regular follow-up helps monitor organ function.")
        st.success("المتابعة المنتظمة تساعد في مراقبة وظائف الأعضاء.")

    elif name == "Rheumatoid Arthritis":
        st.header("Rheumatoid Arthritis (الروماتويد)")
        st.subheader("Definition (تعريف):")
        st.write("An autoimmune disease that causes joint inflammation and pain.")
        st.write("مرض مناعي ذاتي يسبب التهاب وألم في المفاصل.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Swollen joints (تورم المفاصل)
        - Morning stiffness (تيبس صباحي)
        - Fatigue (إرهاق)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Autoimmune attack on joint linings; genetic factors involved.")
        st.write("هجوم مناعي ذاتي على بطانة المفاصل؛ عوامل وراثية متورطة.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Rest inflamed joints and apply cold compresses.")
        st.write("إراحة المفاصل الملتهبة ووضع كمادات باردة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Autoimmune Inflammatory Disease (مرض مناعي التهابي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with HLA-DR4 and PTPN22 genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early treatment prevents joint damage.")
        st.success("العلاج المبكر يمنع تلف المفاصل.")

    elif name == "Hypertension":
        st.header("Hypertension (الضغط العالي)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic condition with persistently elevated blood pressure.")
        st.write("حالة مزمنة يتكرر فيها ارتفاع ضغط الدم.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Often asymptomatic (غالبًا بدون أعراض)
        - Headaches (صداع)
        - Dizziness (دوخة)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Can be essential (unknown cause) or secondary to other diseases.")
        st.write("قد يكون أوليًا (بدون سبب واضح) أو ثانويًا لأمراض أخرى.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Rest, deep breathing, and monitor blood pressure.")
        st.write("الراحة، التنفس العميق، ومراقبة ضغط الدم.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Cardiovascular Chronic Condition (حالة قلبية وعائية مزمنة)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with ACE, AGT, and other blood pressure genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Limit salt intake and exercise regularly.")
        st.success("قلل من تناول الملح ومارس الرياضة بانتظام.")

    elif name == "Asthma":
        st.header("Asthma (الربو)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic lung condition causing inflammation and narrowing of airways.")
        st.write("حالة رئوية مزمنة تسبب التهاب وتضيق الشعب الهوائية.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Wheezing (صفير التنفس)
        - Shortness of breath (ضيق تنفس)
        - Chest tightness (ضيق الصدر)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Genetic predisposition with environmental triggers (e.g. allergens).")
        st.write("استعداد وراثي مع محفزات بيئية مثل المهيجات.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Use inhaler and seek medical help if severe.")
        st.write("استخدام البخاخ وطلب المساعدة الطبية في الحالات الشديدة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Chronic Inflammatory Respiratory Condition (حالة تنفسية التهابية مزمنة)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to ADAM33, IL4, and ORMDL3 genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Avoid allergens and always carry your inhaler.")
        st.success("تجنب مسببات الحساسية واحمل البخاخ دائمًا.")
    elif name == "Type 2 Diabetes":
        st.header("Type 2 Diabetes (سكري النوع الثاني)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic condition that affects the way the body processes blood sugar (glucose).")
        st.write("حالة مزمنة تؤثر على طريقة معالجة الجسم لسكر الدم (الجلوكوز).")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Increased thirst (عطش زائد)
        - Frequent urination (تبول متكرر)
        - Fatigue (تعب)
        - Blurred vision (رؤية مشوشة)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Combination of insulin resistance and genetic factors.")
        st.write("مزيج من مقاومة الإنسولين والعوامل الوراثية.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Manage blood sugar and seek help if symptoms of hyper/hypoglycemia occur.")
        st.write("إدارة مستويات السكر وطلب المساعدة في حال ظهور أعراض ارتفاع/انخفاض السكر.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Metabolic Disorder (اضطراب أيضي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to TCF7L2, PPARG, and FTO genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Focus on a healthy diet and regular exercise.")
        st.success("ركز على نظام غذائي صحي وممارسة الرياضة بانتظام.")

    elif name == "Autism Spectrum Disorder":
        st.header("Autism Spectrum Disorder (اضطراب طيف التوحد)")
        st.subheader("Definition (تعريف):")
        st.write("A developmental disorder affecting communication, behavior, and social interaction.")
        st.write("اضطراب نمائي يؤثر على التواصل والسلوك والتفاعل الاجتماعي.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Delayed speech (تأخر في الكلام)
        - Limited eye contact (تواصل بصري محدود)
        - Repetitive behaviors (سلوكيات متكررة)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Combination of genetic and environmental factors.")
        st.write("مزيج من العوامل الوراثية والبيئية.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Provide a calm environment and avoid overstimulation.")
        st.write("توفير بيئة هادئة وتجنب المثيرات الزائدة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Neurodevelopmental Disorder (اضطراب نمائي عصبي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with genes like SHANK3, NRXN1, and MECP2.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Early behavioral therapy improves outcomes.")
        st.success("العلاج السلوكي المبكر يحسن النتائج بشكل كبير.")

    elif name == "Schizophrenia":
        st.header("Schizophrenia (الفصام)")
        st.subheader("Definition (تعريف):")
        st.write("A chronic mental disorder affecting how a person thinks, feels, and behaves.")
        st.write("اضطراب نفسي مزمن يؤثر على التفكير والمشاعر والسلوك.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Delusions (هلاوس)
        - Hallucinations (تهيؤات)
        - Disorganized thinking (تفكير مشوش)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Genetic and environmental influences.")
        st.write("تأثيرات وراثية وبيئية.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Provide reassurance and avoid confrontation.")
        st.write("تقديم الطمأنينة وتجنب الجدال أو المواجهة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Psychiatric Disorder (اضطراب نفسي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Linked to DISC1, NRG1, and COMT genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Medication adherence and therapy are key.")
        st.success("الالتزام بالأدوية والعلاج النفسي أمر أساسي.")

    elif name == "Breast Cancer":
        st.header("Breast Cancer (سرطان الثدي)")
        st.subheader("Definition (تعريف):")
        st.write("A malignant tumor that originates in the cells of the breast.")
        st.write("ورم خبيث ينشأ في خلايا الثدي.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Breast lump (كتلة في الثدي)
        - Skin changes (تغيرات في الجلد)
        - Nipple discharge (إفرازات من الحلمة)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Genetic mutations, including BRCA1 and BRCA2.")
        st.write("طفرات وراثية مثل BRCA1 وBRCA2.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Early screening and doctor consultation.")
        st.write("الفحص المبكر واستشارة الطبيب.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Genetic Oncological Disorder (اضطراب سرطاني وراثي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("BRCA1 and BRCA2 gene mutations increase risk.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Regular screening and self-exams are important.")
        st.success("الفحص المنتظم والفحص الذاتي مهمان للغاية.")

    elif name == "Alzheimer's Disease":
        st.header("Alzheimer's Disease (الزهايمر)")
        st.subheader("Definition (تعريف):")
        st.write("A progressive neurodegenerative disorder affecting memory and cognition.")
        st.write("اضطراب تنكسي عصبي تدريجي يؤثر على الذاكرة والإدراك.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Memory loss (فقدان الذاكرة)
        - Confusion (ارتباك)
        - Difficulty with daily tasks (صعوبة في المهام اليومية)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Accumulation of amyloid plaques and tau tangles; genetic predisposition.")
        st.write("تراكم لويحات أميلويد وتشابكات تاو؛ واستعداد وراثي.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Provide reminders and a structured environment.")
        st.write("توفير بيئة منظمة وتذكيرات مستمرة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Neurodegenerative Disorder (اضطراب تنكسي عصبي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Associated with APOE-e4 gene and others.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Mental stimulation and a healthy lifestyle may delay symptoms.")
        st.success("التحفيز الذهني ونمط الحياة الصحي قد يؤخر الأعراض.")

    elif name == "Amyotrophic Lateral Sclerosis (ALS)":
        st.header("Amyotrophic Lateral Sclerosis (ALS) - التصلب الجانبي الضموري")
        st.subheader("Definition (تعريف):")
        st.write("A rare neurological disease that affects motor neurons.")
        st.write("مرض عصبي نادر يؤثر على الخلايا العصبية الحركية.")

        st.subheader("Symptoms (الأعراض):")
        st.write("""
        - Muscle weakness (ضعف العضلات)
        - Trouble speaking or swallowing (صعوبة في الكلام أو البلع)
        - Paralysis (شلل)
        """)

        st.subheader("Causes (الأسباب):")
        st.write("Mostly unknown; about 10% of cases are inherited (familial ALS).")
        st.write("غير معروفة غالبًا؛ حوالي 10٪ من الحالات وراثية.")

        st.subheader("First Aid (الإسعافات الأولية):")
        st.write("Support breathing and feeding; seek emergency care as needed.")
        st.write("دعم التنفس والتغذية؛ وطلب الرعاية الطارئة عند الحاجة.")

        st.subheader("Type of Disorder (نوع الخلل):")
        st.write("Neurodegenerative Motor Neuron Disease (مرض عصبي حركي تنكسي)")

        st.subheader("Gene Information (معلومات جينية):")
        st.write("Mutations in SOD1, C9orf72, and FUS genes.")

        st.subheader("Medical Tip (نصيحة طبية):")
        st.info("Multidisciplinary care improves quality of life.")
        st.success("الرعاية متعددة التخصصات تحسن جودة الحياة.")
