from redis import StrictRedis

# تعيين المعلمات الخاصة بالاتصال
host = "containers-us-west-140.railway.app"  # عنوان خادم Redis
port = 7830  # المنفذ الذي ترغب في استخدامه
password = "L8YVyI93d2QAjVJCiTcj"  # كلمة المرور إذا كانت مطلوبة

# إنشاء اتصال Redis
db = StrictRedis(host=host, port=port, password=password, decode_responses=True)

# الآن يمكنك استخدام الاتصال db للقيام بالعمليات على خادم Redis بالمنفذ المحدد
