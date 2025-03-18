from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
from app.services.file_processing import process_file
from app.database.mongo_db import save_orders_to_db
from app.models.user_orders import UserOrders
import os
import logging

router = APIRouter()

@router.post("/", response_model=List[UserOrders])
async def upload_file(file: UploadFile = File(...)):
    try:
        logging.info(f"Recebendo arquivo: {file.filename}")

        if not file.filename.endswith(".txt"):
            raise HTTPException(status_code=400, detail="O arquivo deve ser um .txt")

        file_content = await file.read()
        if not file_content:
            raise HTTPException(status_code=400, detail="O arquivo está vazio.")

        file_path = f"/tmp/{file.filename}"
        logging.info(f"Salvando arquivo temporário em: {file_path}")

        with open(file_path, "wb") as buffer:
            buffer.write(file_content)

        logging.info("Processando arquivo...")
        result = process_file(file_path)
        logging.info(f"Arquivo processado com sucesso. Resultado: {result}")

        save_orders_to_db(result)

        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(f"Erro ao processar o arquivo: {e}", exc_info=True)
        raise HTTPException(status_code=400, detail="Formato de arquivo inválido.")
    finally:
        if 'file_path' in locals() and os.path.exists(file_path):
            logging.info(f"Removendo arquivo temporário: {file_path}")
            os.remove(file_path)