# Django Simple CRUD

یک پروژه‌ی نمونه/آموزشی با **Django** برای انجام عملیات **CRUD** (ایجاد، نمایش، ویرایش، حذف) روی یک مدل ساده.

---

## 🧱 پیش‌نیازها

- **Python 3.11+**
- **Django 5.2.16** (طبق `pyproject.toml`)
- **[uv](https://docs.astral.sh/uv/)** به‌عنوان مدیر پکیج (پروژه با `uv` ساخته شده و فایل `uv.lock` داره)

---

## 📁 ساختار پروژه

```
django-simple-crud/
├── config/          # تنظیمات اصلی پروژه‌ی جنگو (settings.py، urls.py، wsgi.py، asgi.py)
├── Home/            # اپلیکیشنی که منطق CRUD توش پیاده‌سازی شده
├── templates/       # قالب‌های HTML
├── db.sqlite3       # دیتابیس SQLite برای توسعه
├── manage.py        # اسکریپت مدیریتی جنگو
├── main.py          # باقی‌مانده‌ی uv init — در اجرای واقعی پروژه استفاده نمی‌شه
└── pyproject.toml   # وابستگی‌ها
```

---

## 🚀 نصب و اجرا

### روش پیشنهادی (با uv)

```bash
git clone https://github.com/xorep1/django-simple-crud.git
cd django-simple-crud

uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser   # اختیاری، برای دسترسی به پنل ادمین
uv run python manage.py runserver
```

### روش سنتی (با venv + pip)

```bash
git clone https://github.com/xorep1/django-simple-crud.git
cd django-simple-crud

python -m venv venv
source venv/bin/activate        # ویندوز: venv\Scripts\activate

pip install "django>=5.2.16"
python manage.py migrate
python manage.py runserver
```

بعد از اجرا، پروژه روی این آدرس بالا میاد:

```
http://127.0.0.1:8000/
```

پنل ادمین جنگو هم (در صورت ساخت superuser) در این آدرس:

```
http://127.0.0.1:8000/admin/
```

---

## ⚠️ بخش‌هایی که هنوز نیاز به تکمیل دارن

GitHub اجازه نمی‌ده صفحات فهرست پوشه (tree) رو به‌صورت خودکار بخونم، برای همین نتونستم داخل `Home/` و `config/` رو مستقیماً ببینم. برای این‌که این داکیومنت ۱۰۰٪ دقیق بشه، این اطلاعات رو نیاز دارم (یا خودت پر کن، یا محتوای این فایل‌ها رو برام بفرست تا کامل‌ش کنم):

- **`Home/models.py`** → مدل و فیلدهاش دقیقاً چیه؟ (مثلاً یک مدل `Task` با فیلدهای `title`, `description`, `created_at`)
- **`Home/urls.py`** و **`config/urls.py`** → مسیرهای URL دقیق (مثلاً `/`, `/create/`, `/update/<id>/`, `/delete/<id>/`)
- **`Home/views.py`** → ویوها function-based هستن یا class-based؟
- **`templates/`** → چه فایل‌های html‌ای داخلشه (مثلاً `list.html`, `form.html`)؟

با این اطلاعات می‌تونم بخش **«نحوه‌ی استفاده»** و **«مسیرها (Endpoints)»** رو با جزئیات دقیق کامل کنم — همون بخشی که معمولاً بیشترین سردرگمی رو برای بازدیدکننده‌ی جدید ایجاد می‌کنه.

---

## 🛡️ نکات قبل از Production

- مقدار `SECRET_KEY` و `DEBUG` احتمالاً هنوز روی حالت پیش‌فرض توسعه‌ست — قبل از هر دیپلوی واقعی حتماً این‌ها رو عوض کن و `DEBUG=False` کن.
- `db.sqlite3` فقط برای توسعه مناسبه؛ برای production از PostgreSQL یا MySQL استفاده کن.
- `ALLOWED_HOSTS` رو در `config/settings.py` برای دامنه‌ی واقعی تنظیم کن.

---
