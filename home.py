import dotenv

dotenv.load_dotenv(
    override=True,
)

import os
import warnings

os.environ["HYDRA_FULL_ERROR"] = "1"
warnings.filterwarnings("ignore")

import streamlit as st

# Langsmith tracing을 위한 키 로드
if "LANGSMITH_PROJECT" not in st.session_state:
    st.session_state["LANGSMITH_PROJECT"] = st.secrets["LANGSMITH_PROJECT"]
    os.environ["LANGSMITH_PROJECT"] = st.session_state["LANGSMITH_PROJECT"]
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"

from hydra import initialize, compose
from hydra.core.global_hydra import GlobalHydra

from src.pipelines.pipeline import pipeline


def main(
    config_path: str,
    job_name: str,
    config_name: str,
) -> None:
    def initialize_hydra():
        if GlobalHydra().is_initialized():
            GlobalHydra().clear()
        initialize(
            config_path=config_path,
            job_name=job_name,
        )

    initialize_hydra()
    config = compose(config_name=config_name)
    return pipeline(config)


if __name__ == "__main__":
    CONFIG_PATH = "configs/"
    JOB_NAME = "withpet"
    CONFIG_NAME = "home.yaml"
    main(
        config_path=CONFIG_PATH,
        job_name=JOB_NAME,
        config_name=CONFIG_NAME,
    )
