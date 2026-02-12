from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# تعريف نموذج البيانات لاستقبال النص عبر POST
class TextInput(BaseModel):
    text: str

# استدعاء موديلات الذكاء الاصطناعي عند بدء التشغيل
# موديل التلخيص الإنجليزي
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
# موديل الترجمة من إنجليزي لعربي
translator = pipeline("translation_en_to_ar", model="Helsinki-NLP/opus-mt-en-ar")

@app.post("/process")
def process_ai_logic(item: TextInput):
    # الحصول على النص المرسل من الواجهة الأمامية
    user_text = item.text

    # التحقق من وجود نص
    if not user_text or not user_text.strip():
        return "No text provided"

    current_text = user_text

    # أولاً: التلخيص (يتم تنفيذه إذا وجدت كلمة لخص أو summarize)
    if "summarize" in user_text or "لخص" in user_text:
        # الموديل يخرج قائمة، نأخذ منها النص الصافي
        summary_data = summarizer(current_text, max_length=100, min_length=30, do_sample=False)
        current_text = summary_data[0]['summary_text']

    # ثانياً: الترجمة (تتم على النص الناتج سواء كان الأصلي أو الملخص)
    if "ترجم" in user_text:
        # تحويل النص للغة العربية
        translation_data = translator(current_text)
        current_text = translation_data[0]['translation_text']
    
    # إرجاع النتيجة النهائية
    return current_text
