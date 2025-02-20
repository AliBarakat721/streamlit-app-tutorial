import streamlit as st

# عرض محتويات session_state للتصحيح
st.write("Session state:", st.session_state)

# تأكد من عدم إعادة تعيين st.session_state إلى قيمة غير صحيحة (مثلاً لا تستخدم st.session_state = 1)
# يُرجى التأكد أيضاً من عدم وجود ملف باسم session_state.py في مجلد المشروع

# تهيئة المتغيرات في session_state باستخدام طريقة المؤشر (dictionary style)
if "text_list" not in st.session_state:
    st.session_state["text_list"] = []

if "user_input" not in st.session_state:
    st.session_state["user_input"] = ""

# إدخال نص من المستخدم مع تعيين القيمة الافتراضية من session_state
user_input = st.text_input("أدخل نصاً", value=st.session_state["user_input"])

# تحديث قيمة الإدخال في session_state
st.session_state["user_input"] = user_input

# زر لإضافة النص إلى القائمة
if st.button("أضف"):
    if st.session_state["user_input"].strip():  # التأكد من أن الإدخال غير فارغ
        st.session_state["text_list"].append(st.session_state["user_input"])
        # إعادة تعيين الإدخال بعد الإضافة
        st.session_state["user_input"] = ""

# زر لمسح القائمة
if st.button("مسح"):
    st.session_state["text_list"] = []

# عرض قائمة النصوص
st.write("قائمة النصوص:", st.session_state["text_list"])
