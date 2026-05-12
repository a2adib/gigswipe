from datetime import datetime

from sqlalchemy import DateTime, func
from sqlmodel import Field, SQLModel

from src.common.utils import generate_public_id


class TimestampMixin(SQLModel):
    created_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now()},
        nullable=False,
    )
    updated_at: datetime = Field(
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now(), "onupdate": func.now()},
        nullable=False,
    )


class IDMixin(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    public_id: str = Field(default_factory=lambda: generate_public_id(), unique=True, max_length=11)


class CreatedByMixin(SQLModel):
    created_by: int | None = Field(default=None)
    updated_by: int | None = Field(default=None)


class CommonFieldMixin(IDMixin, TimestampMixin):
    is_active: bool | None = Field(default=True, nullable=False)


class CommonFieldMixinWithHandler(CreatedByMixin, CommonFieldMixin):
    is_active: bool | None = Field(default=True, nullable=False)
