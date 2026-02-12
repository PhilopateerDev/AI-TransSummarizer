# استخدام نسخة بايثون رسمية وخفيفة
FROM python:3.9

# إنشاء مجلد للمشروع داخل السيرفر
WORKDIR /code

# نسخ ملف المكتبات وتثبيتها
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# تشغيل السيرفر على بورت 7860 (الخاص بـ Hugging Face)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
