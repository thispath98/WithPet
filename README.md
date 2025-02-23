# TourGuideRAG(WithPet)
관광지(부산)의 맛집/관광지 알려주는 가이드 챗봇

## .streamlit/secrets.toml guide
```shell
PROJECT_DIR="{project_dir}"
CONNECTED_DIR="{connected_dir}"
LANGCHAIN_API_KEY="{langchain_api_key}"
LANGCHAIN_PROJECT="TourGuideRAG"
OPENAI_API_KEY="{openai_api_key}"
SERPAPI_API_KEY="{servapi_api_key}"
LANGSMITH_API_KEY="{langsmith_api_key}"
LANGSMITH_PROJECT="WithPet"
```
- project_dir: project directory(ex: /home/ubuntu)
- connected_dir: data and faiss directory(ex: /home/ubuntu)

## Branch 전략

### 1. **메인 브랜치 (`main`)**
- `main` 브랜치는 **배포 브랜치**입니다.
- 배포 가능한 코드만 포함됩니다.
- `main` 브랜치에 직접 커밋은 허용되지 않습니다.

### 2. **개발 브랜치 (`dev`)**
- `dev` 브랜치는 **테스트 브랜치**입니다.
- 새로운 기능을 통합하고 테스트하는 데 사용됩니다.
- feature 브랜치에서 생성된 PR(Pull Request)만 `dev` 브랜치에 병합됩니다.

### 3. **feature 브랜치 (`feature-[name]-[feature_name]`)**
- 각 기능 개발은 별도의 feature 브랜치에서 진행됩니다.
- feature 브랜치의 이름 규칙은 다음과 같습니다:
  ```
  feature-[name]-[feature_name]
  ```
  - `name`: 개발자의 이름 또는 식별자.
  - `feature_name`: 개발 중인 기능의 간단한 설명.
  - e.g. feature-jiyoon-extract-constant
- feature 브랜치는 `dev` 브랜치에서 생성됩니다.
- 개발과 초기 테스트가 완료되면 PR을 생성하여 feature 브랜치를 `dev` 브랜치에 병합합니다.

### Merge Rules
1. **feature 브랜치에서 `dev`로 병합**
   - feature 브랜치를 `dev` 브랜치로 병합하려면 PR이 필요합니다.
   - PR은 **최소 1명의 reviewer**의 검토와 승인을 받아야 병합 가능합니다.

2. **`dev`에서 `main`으로 병합**
   - `dev` 브랜치를 `main` 브랜치로 병합하려면 PR이 필요합니다.
   - PR은 **최소 1명의 reviewer**의 검토와 승인을 받아야 병합 가능합니다.

## Commit Convention

### Format
```
tag: contents
```
- **`tag`**: 변경 유형을 나타냅니다. 허용되는 태그는 다음과 같습니다:
  - `feature`: 새로운 기능 또는 기능 추가.
  - `fix`: 버그 수정.
  - `refactor`: 기능 변경 없이 코드 구조 개선.
  - `test`: 테스트 또는 테스트 인프라 관련 변경.
- **`contents`**: 변경 사항에 대한 간단한 설명.
- e.g. `feature: introduce config` or `refactor: extract prompt`
