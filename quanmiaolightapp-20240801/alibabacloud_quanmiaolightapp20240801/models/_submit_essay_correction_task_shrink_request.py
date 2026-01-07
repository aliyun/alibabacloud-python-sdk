# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitEssayCorrectionTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        grade: str = None,
        model_id: str = None,
        other_review_points: str = None,
        question: str = None,
        subject: str = None,
        tasks_shrink: str = None,
        total_score: int = None,
    ):
        self.grade = grade
        self.model_id = model_id
        self.other_review_points = other_review_points
        self.question = question
        self.subject = subject
        self.tasks_shrink = tasks_shrink
        self.total_score = total_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grade is not None:
            result['grade'] = self.grade

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.other_review_points is not None:
            result['otherReviewPoints'] = self.other_review_points

        if self.question is not None:
            result['question'] = self.question

        if self.subject is not None:
            result['subject'] = self.subject

        if self.tasks_shrink is not None:
            result['tasks'] = self.tasks_shrink

        if self.total_score is not None:
            result['totalScore'] = self.total_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('otherReviewPoints') is not None:
            self.other_review_points = m.get('otherReviewPoints')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('tasks') is not None:
            self.tasks_shrink = m.get('tasks')

        if m.get('totalScore') is not None:
            self.total_score = m.get('totalScore')

        return self

