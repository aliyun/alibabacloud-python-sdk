# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOssCheckResultsBatchFeedbackRequest(DaraModel):
    def __init__(
        self,
        feedback: str = None,
        items: str = None,
        parent_task_id: str = None,
    ):
        self.feedback = feedback
        self.items = items
        self.parent_task_id = parent_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.items is not None:
            result['Items'] = self.items

        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')

        return self

