from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
from app.models import UserOrders
from app.services import process_file
from app.utils import validate_file_extension
from fastapi.middleware.cors import CORSMiddleware
import os
import logging

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/upload", response_model=List[UserOrders])
async def upload_file(file: UploadFile = File(...)):
    try:
        logger.info(f"Recebendo arquivo: {file.filename}")

        if not validate_file_extension(file.filename):
            raise HTTPException(status_code=400, detail="O arquivo deve ser um .txt")

        file_content = await file.read()
        if not file_content:
            raise HTTPException(status_code=400, detail="O arquivo está vazio.")

        file_path = f"/tmp/{file.filename}"
        logger.info(f"Salvando arquivo temporário em: {file_path}")

        with open(file_path, "wb") as buffer:
            buffer.write(file_content)

        logger.info("Processando arquivo...")
        result = process_file(file_path)
        logger.info(f"Arquivo processado com sucesso. Resultado: {result}")

        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Erro ao processar o arquivo: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if 'file_path' in locals() and os.path.exists(file_path):
            logger.info(f"Removendo arquivo temporário: {file_path}")
            os.remove(file_path)