
from flask import render_template, request, redirect

from . import quest_bp
from ..extensions import db
from ..models import QuestStage, QuestStageActions


@quest_bp.route("/quest/")
@quest_bp.route("/quest/<int:id>")
def quest(id = None):
    if not id:
        q: QuestStage = QuestStage.query.where(QuestStage.id == 1).scalar()
        return render_template('index.html', question = q)
    q: QuestStage = QuestStage.query.where(QuestStage.id == id).scalar()
    return render_template('index.html', question=q)

@quest_bp.route("/change_stage", methods = ["POST"])
def change_stage():
    id = request.form.get("stage")
    return redirect(f"/quest/{id}")
