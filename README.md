# VoltEye API - Monitoramento de Consumo Elétrico

API desenvolvida com **FastAPI** para receber medições de dispositivos IoT, processar e disponibilizar dados de consumo elétrico.

---

## 📦 1. Clonar o projeto

```bash
git clone https://github.com/ezequielhenrique/volteye-api.git
cd volteye-api
```

---

## 🧪 2. Criar ambiente virtual

### Linux / Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows:

```bash
py -m venv venv
.venv\Scripts\activate
```

---

## 📥 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ 4. Executar o projeto

```bash
fastapi dev
```

O servidor será iniciado em:

```
http://localhost:8000
```

---

## 📚 5. Documentação automática

O FastAPI gera documentação interativa automaticamente:

### 🔹 Swagger UI:

```
http://localhost:8000/docs
```

---

## 📡 6. Exemplo de requisição

### Endpoint:

```
POST /dispositivos/{id_dispositivo}/medicoes
```

### Exemplo:

```
POST /dispositivos/tomada-01/medicoes
```

### Headers:

```
token: token_do_dispositivo
Content-Type: application/json
```

### Body (JSON):

```json
{
  "corrente": 2.5,
  "tensao": 220,
  "potencia": 550,
  "device_timestamp": "2026-04-25T14:30:00Z"
}
```
