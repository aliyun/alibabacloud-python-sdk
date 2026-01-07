# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class SubmitEssayCorrectionTaskRequest(DaraModel):
    def __init__(
        self,
        grade: str = None,
        model_id: str = None,
        other_review_points: str = None,
        question: str = None,
        subject: str = None,
        tasks: List[main_models.SubmitEssayCorrectionTaskRequestTasks] = None,
        total_score: int = None,
    ):
        self.grade = grade
        self.model_id = model_id
        self.other_review_points = other_review_points
        self.question = question
        self.subject = subject
        self.tasks = tasks
        self.total_score = total_score

    def validate(self):
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

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

        result['tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['tasks'].append(k1.to_map() if k1 else None)

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

        self.tasks = []
        if m.get('tasks') is not None:
            for k1 in m.get('tasks'):
                temp_model = main_models.SubmitEssayCorrectionTaskRequestTasks()
                self.tasks.append(temp_model.from_map(k1))

        if m.get('totalScore') is not None:
            self.total_score = m.get('totalScore')

        return self

class SubmitEssayCorrectionTaskRequestTasks(DaraModel):
    def __init__(
        self,
        answer: str = None,
        custom_id: str = None,
        grade: str = None,
        other_review_points: str = None,
        question: str = None,
        subject: str = None,
        total_score: int = None,
    ):
        self.answer = answer
        self.custom_id = custom_id
        self.grade = grade
        self.other_review_points = other_review_points
        self.question = question
        self.subject = subject
        self.total_score = total_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['answer'] = self.answer

        if self.custom_id is not None:
            result['customId'] = self.custom_id

        if self.grade is not None:
            result['grade'] = self.grade

        if self.other_review_points is not None:
            result['otherReviewPoints'] = self.other_review_points

        if self.question is not None:
            result['question'] = self.question

        if self.subject is not None:
            result['subject'] = self.subject

        if self.total_score is not None:
            result['totalScore'] = self.total_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')

        if m.get('customId') is not None:
            self.custom_id = m.get('customId')

        if m.get('grade') is not None:
            self.grade = m.get('grade')

        if m.get('otherReviewPoints') is not None:
            self.other_review_points = m.get('otherReviewPoints')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        if m.get('totalScore') is not None:
            self.total_score = m.get('totalScore')

        return self

