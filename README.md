# 🌶️ Chili DeliRico

**Bilingual e-commerce website** for *Chili DeliRico*, a Costa Rican artisanal hot sauce brand established in 1972.

---

## 🇨🇷 Sobre la marca

Chili DeliRico es una marca familiar costarricense inspirada en recetas tradicionales transmitidas por generaciones.
Nuestras salsas son 100% naturales, sin gluten y elaboradas a fuego lento para lograr un sabor auténtico.

---

## 🚀 Features

* 🛒 Catálogo de productos (3 salsas × 2 tamaños)
* 🧾 Carrito y sistema de checkout
* 📱 Integración con WhatsApp (pedido automático)
* 🌐 Página bilingüe (Español / Inglés)
* 📦 Almacenamiento de pedidos en MongoDB
* ⚡ Interfaz rápida y responsive

---

## 🧑‍💻 Tecnologías

* **Frontend:** React (Vite)
* **Backend:** FastAPI
* **Base de datos:** MongoDB

---

## 📁 Estructura del proyecto

```id="y36ycs"
chili-delirico/
 ├── frontend/
 ├── backend/
 ├── README.md
 └── .gitignore
```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```id="c7up6q"
git clone https://github.com/TU-USUARIO/chili-delirico.git
cd chili-delirico
```

---

### 2. Backend

```id="kxclt5"
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 3. Frontend

```id="y5o1cu"
cd frontend
npm install
npm run dev
```

---

## 🔑 Variables de entorno

### Backend (.env)

```id="6i0mgb"
MONGO_URL=tu_url_de_mongodb
DB_NAME=chili_delirico
```

### Frontend (.env)

```id="6x22vn"
VITE_API_URL=http://localhost:8000
```

---

## 📲 Integración WhatsApp

Los pedidos se envían automáticamente a:

```id="eyuwfj"
+506 7184 1865
```

---

## 🌎 Deploy

* Frontend: Vercel
* Backend: Render
* Base de datos: MongoDB Atlas

---

## 📬 Contacto

* 📧 [chilidelirico55@gmail.com](mailto:chilidelirico55@gmail.com)
* 📱 WhatsApp: +506 7184 1865

---

## 🏷️ Licencia

© 2026 Chili DeliRico. Todos los derechos reservados.
