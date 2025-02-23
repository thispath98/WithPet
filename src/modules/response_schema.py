from typing import Literal

from pydantic import BaseModel, Field


class QueryRouter(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["pet_places", "not_relevant"] = Field(
        ...,
        description="Given a user question choose which datasource would be most relevant for answering their question",
    )
