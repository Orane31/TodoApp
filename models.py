import app

from dataclasses import dataclass


@dataclass
class Task(app.db.Model):
    id: int
    title: str
    completed: bool

    id = app.db.Column(app.db.Integer(), primary_key=True)
    title = app.db.Column(app.db.String(140))
    completed = app.db.Column(app.db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Task id: {self.id} - {self.title}"
