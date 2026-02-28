# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFeedbackRequest(DaraModel):
    def __init__(
        self,
        feedback: str = None,
        instance_id: str = None,
        rating: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.feedback = feedback
        # This parameter is required.
        self.instance_id = instance_id
        self.rating = rating
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.rating is not None:
            result['Rating'] = self.rating

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Rating') is not None:
            self.rating = m.get('Rating')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

