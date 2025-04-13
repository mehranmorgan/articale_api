# 📰 Article API

یک پروژه ساده و حرفه‌ای برای مدیریت مقالات با استفاده از Django و Django REST Framework.

## 📌 ویژگی‌ها

- ساخت، ویرایش، حذف و نمایش مقالات
- احراز هویت JWT برای کاربران
- تعریف مدل‌های شخصی‌سازی‌شده برای مقاله و کاربر
- استفاده از ViewSets و Router برای ساخت سریع API

## 🛠 تکنولوژی‌ها

- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT
- SQLite (قابل تغییر به PostgreSQL یا ...)

## 🚀 نصب و اجرا

1. مخزن را کلون کنید:

```bash
git clone https://github.com/mehranmorgan/articale_api.git
cd articale_api
```

2. ساخت و فعال‌سازی محیط مجازی:

```bash
python -m venv venv
source venv/bin/activate  # برای ویندوز: venv\Scripts\activate
```

3. نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```

4. اجرای مایگریشن‌ها:

```bash
python manage.py migrate
```

5. اجرای سرور:

```bash
python manage.py runserver
```

## 🔐 احراز هویت JWT

- برای دریافت توکن:

```
POST /api/token/
{
  "username": "your_username",
  "password": "your_password"
}
```

- برای رفرش توکن:

```
POST /api/token/refresh/
{
  "refresh": "your_refresh_token"
}
```

## 📂 ساختار پروژه

```
articale_api/
│
├── articale/          # اپلیکیشن اصلی مقالات
├── users/             # اپلیکیشن مدیریت کاربران
├── manage.py
└── requirements.txt
```

## 📮 API Endpointها (نمونه)

| Method | Endpoint            | توضیح |
|--------|---------------------|--------|
| GET    | /articles/          | دریافت لیست مقالات |
| POST   | /articles/          | ایجاد مقاله جدید (با توکن) |
| PUT    | /articles/<id>/     | ویرایش مقاله |
| DELETE | /articles/<id>/     | حذف مقاله |
| POST   | /api/token/         | دریافت JWT |
| POST   | /api/token/refresh/ | رفرش توکن |

## ✍️ توسعه‌دهنده

- [Mehran Morgan](https://github.com/mehranmorgan)

## 📃 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.
