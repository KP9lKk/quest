from typing import List

from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column
from sqlalchemy import String, Text, ForeignKey

from app.extensions import db


class QuestStage(db.Model):
    __table_name__ = "quest_stage"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text, nullable = False)
    image: Mapped[str] = mapped_column(String, nullable = False)
    actions: Mapped[List["QuestStageActions"]] = relationship(back_populates="stage", foreign_keys="[QuestStageActions.stage_id]")

class QuestStageActions(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    stage_id: Mapped[int] = mapped_column(ForeignKey("quest_stage.id"))
    action_text: Mapped[str] = mapped_column(Text, nullable = False)
    route_id: Mapped[int] = mapped_column(ForeignKey("quest_stage.id"))
    stage: Mapped["QuestStage"] = relationship(back_populates="actions", foreign_keys=[stage_id])