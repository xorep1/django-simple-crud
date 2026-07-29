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

## 📖 موضوع پروژه

این اپ (`Home`) یک سیستم مدیریت **کتاب‌ها (Books)** و **نویسنده‌ها (Authors)** هست — یعنی دو مدل جدا داره که هرکدوم عملیات CRUD کامل (نمایش، افزودن، ویرایش، حذف) روشون پیاده‌سازی شده. با توجه به این‌که در Django معمول‌ترین رابطه بین این دو مدل، یک فیلد `author` روی مدل `Book` به‌صورت `ForeignKey` به مدل `Author` است
بر اساس `Home/urls.py`:

| مسیر | نام (name) | کاربرد |
|---|---|---|
| `/books/` | `books` | نمایش لیست همه‌ی کتاب‌ها |
| `/books/add/` | `add_book` | فرم افزودن کتاب جدید |
| `/books/update/<id>/` | `update_book` | ویرایش کتابی با شناسه‌ی `id` |
| `/books/remove/<id>/` | `remove_book` | حذف کتابی با شناسه‌ی `id` |
| `/authors/` | `authors` | نمایش لیست همه‌ی نویسنده‌ها |
| `/authors/add/` | `add_author` | فرم افزودن نویسنده‌ی جدید |
| `/authors/update/<id>/` | `update_author` | ویرایش نویسنده‌ای با شناسه‌ی `id` |
| `/authors/remove/<id>/` | `remove_author` | حذف نویسنده‌ای با شناسه‌ی `id` |


---

## 🛡️ نکات قبل از Production

- مقدار `SECRET_KEY` و `DEBUG` احتمالاً هنوز روی حالت پیش‌فرض توسعه‌ست — قبل از هر دیپلوی واقعی حتماً این‌ها رو عوض کن و `DEBUG=False` کن.
- `db.sqlite3` فقط برای توسعه مناسبه؛ برای production از PostgreSQL یا MySQL استفاده کن.
- `ALLOWED_HOSTS` رو در `config/settings.py` برای دامنه‌ی واقعی تنظیم کن.

---

