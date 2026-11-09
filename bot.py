import os
from google import genai

# تهيئة العميل باستخدام مفتاحك السري
client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY"),
)

# تفعيل أداة بحث جوجل لجلب التريندات الحصرية
tools = [
    {
        'type': 'google_search',
    },
]

generation_config = {
    'max_output_tokens': 65536,
    'thinking_level': 'medium',
}

def run_affiliate_worker(session_type="الصباح"):
    prompt = f"""
    أنت موظف تسويق بالعمولة (Affiliate Marketing Bot) ذكي ومهني لصالح منصات BMB Tchad 07.
    هذه جلسة العمل الخاصة بـ: {session_type}.
    
    الرجاء تنفيذ الآتي بدقة:
    1. ابحث عبر الإنترنت عن منتجين حالياً في قمة الطلب:
       - المنتج الأول: من **أمازون (Amazon)**.
       - المنتج الثاني: من **علي إكسبريس (AliExpress)**.
    2. لكل منتج، قم بإنشاء:
       - عنوان جذاب واسم المنتج.
       - خطاف (Hook) ناري في أول 3 ثوانٍ لفيديو ترويجي قصير (TikTok / Reels).
       - سيناريو فيديو قصير مدته 25 ثانية مع نص التعليق الصوتي ووصف المشاهد.
       - منشور ترويجي جاهز للنشر على (TikTok, Instagram, Facebook, X) مع الهاشتاغات ومكان مخصص لرابط العمولة.
    """

    try:
        print(f"🤖 الموظف الاصطناعي يبدأ العمل لجلسة ({session_type})...")
        interaction = client.interactions.create(
            model='models/gemini-3.8-flash',
            input=prompt,
            tools=tools,
            generation_config=generation_config,
        )
        
        print(f"\n=== 📊 تقرير الموظف ({session_type}) ===")
        if interaction.steps:
            print(interaction.steps[-1])
        else:
            print("تم تنفيذ جلسة العمل بنجاح.")

    except Exception as e:
        print(f"حدث خطأ في جلسة {session_type}: {e}")

if __name__ == "__main__":
    run_affiliate_worker(session_type="جلسة منتجات أمازون وعلي إكسبريس")
