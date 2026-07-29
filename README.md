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

این اپ (`Home`) یک سیستم مدیریت **کتاب‌ها (Books)** و **نویسنده‌ها (Authors)** هست — یعنی دو مدل جدا داره که هرکدوم عملیات CRUD کامل (نمایش، افزودن، ویرایش، حذف) روشون پیاده‌سازی شده. با توجه به این‌که در Django معمول‌ترین رابطه بین این دو مدل، یک فیلد `author` روی مدل `Book` به‌صورت `ForeignKey` به مدل `Author` هست، به‌احتمال زیاد همین رابطه اینجا هم برقراره — ولی چون هنوز `Home/models.py` رو ندیدم، این نکته رو با علامت ❓ مشخص کردم تا با تأیید یا فرستادن اون فایل قطعیش کنیم.

## 🔗 مسیرها (Endpoints)

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

> این مسیرها همگی زیرمجموعه‌ی `Home` هستن؛ آدرس نهایی به این بستگی داره که در `config/urls.py` با چه پیشوندی `include` شدن (مثلاً اگه با `path("", include("Home.urls"))` اضافه شده باشن، آدرس‌های بالا همون‌طور که نوشته شده کار می‌کنن).

## 🧭 نحوه‌ی استفاده (گام‌به‌گام)

1. سرور رو با `runserver` بالا بیار (بخش «نصب و اجرا» بالاتر).
2. برای دیدن لیست کتاب‌ها برو به `http://127.0.0.1:8000/books/`
3. برای افزودن کتاب جدید برو به `http://127.0.0.1:8000/books/add/` و فرم رو پر کن.
4. برای ویرایش یا حذف یک کتاب خاص، از دکمه‌های داخل صفحه‌ی لیست استفاده کن (که به `books/update/<id>/` یا `books/remove/<id>/` لینک می‌دن) — یا مستقیم با شناسه‌ی موردنظر توی مرورگر برو.
5. همین جریان دقیقاً برای نویسنده‌ها هم با مسیرهای `authors/...` تکرار می‌شه.

## ⚠️ بخشی که هنوز نیاز به تکمیل داره

هنوز به `Home/models.py` و `Home/views.py` دسترسی ندارم، پس این‌ها هنوز نامشخصن:

- **فیلدهای دقیق مدل `Book`** (مثلاً `title`, `author`, `published_date`, …؟)
- **فیلدهای دقیق مدل `Author`** (مثلاً `name`, `bio`, …؟)
- این‌که آیا رابطه‌ی `Book → Author` واقعاً `ForeignKey` هست یا نه
- این‌که ویوها function-based هستن یا class-based

اگه این دو فایل رو هم برام بفرستی، بخش «موضوع پروژه» بالا رو با فیلدهای واقعی و دقیق آپدیت می‌کنم و علامت‌های ❓ رو برمی‌دارم.

---

## 🛡️ نکات قبل از Production

- مقدار `SECRET_KEY` و `DEBUG` احتمالاً هنوز روی حالت پیش‌فرض توسعه‌ست — قبل از هر دیپلوی واقعی حتماً این‌ها رو عوض کن و `DEBUG=False` کن.
- `db.sqlite3` فقط برای توسعه مناسبه؛ برای production از PostgreSQL یا MySQL استفاده کن.
- `ALLOWED_HOSTS` رو در `config/settings.py` برای دامنه‌ی واقعی تنظیم کن.

---

