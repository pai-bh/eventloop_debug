import logging
import asyncio
import uvicorn
from fastapi import FastAPI

# 로깅 레벨 설정
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()


@app.get("/")
async def root():
    logging.debug("루트 엔드포인트 호출됨")
    return {"message": "Hello World"}


@app.get("/async-task")
async def async_task():
    logging.debug("비동기 태스크 엔드포인트 호출 시작")
    # 비동기 작업 시뮬레이션
    await asyncio.sleep(2)
    current_loop = asyncio.get_running_loop()
    logging.debug(f"현재 실행 중인 이벤트 루프: {current_loop}")
    logging.debug(f"이벤트 루프 디버그 모드: {current_loop.get_debug()}")
    logging.debug("비동기 태스크 엔드포인트 작업 완료")
    return {"message": "Async task completed", "loop_info": str(current_loop)}


# app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
