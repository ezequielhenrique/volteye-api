from fastapi import FastAPI, Header, HTTPException
from datetime import datetime
from src.bd.connect import connect
from schemas import Medicao


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "VoltEye API"}


@app.post(
    "/dispositivos/{dispositivo_id}/medicoes",
    summary="Recebe dados de consumo elétrico",
    description="Endpoint responsável por receber medições enviadas por dispositivos.",
    responses={
        200: {"description": "Sucesso"},
        403: {"description": "Não autorizado"}
    }
)
async def receber_medicao(
        dispositivo_id: str, 
        medicao: Medicao, 
        # token: str = Header(..., description="Token do dispositivo") 
    ):

    supabase = connect()

    #if token != 'token_do_dispositivo':
    #   raise HTTPException(status_code=403, detail='Dispositivo não autorizado')

    print(medicao.model_dump(mode="json"))
    response = (
        supabase.table("test_readings")
        .insert(medicao.model_dump(mode="json"))
        .execute()
    )

    return {
        'status': 'sucesso',
        # 'id_dispositivo': dispositivo_id,
        'response': response
    }
