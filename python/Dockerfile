# Python 람다 함수를 위한 Dockerfile(Linux/ARM64)
FROM public.ecr.aws/lambda/python:3.9

# Poetry 버전 정의
ENV POETRY_VERSION=1.3.2

# Poetry 설치
RUN pip install "poetry==$POETRY_VERSION"

# 경로 정의
WORKDIR ${LAMBDA_TASK_ROOT}

# 로컬에 있는 pyproject.toml, poetry.lock 파일을 컨테이너로 복사
COPY poetry.lock pyproject.toml ${LAMBDA_TASK_ROOT}/

# Poetry를 이용하여 의존성 설치
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# 로컬에 있는 소스코드를 컨테이너로 복사
COPY app ${LAMBDA_TASK_ROOT}/

# 람다 함수의 핸들러를 지정
CMD [ "main.handler" ]