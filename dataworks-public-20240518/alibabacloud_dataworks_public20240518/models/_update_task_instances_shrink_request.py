# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        task_instances_shrink: str = None,
    ):
        # The remarks.
        self.comment = comment
        # The instances.
        self.task_instances_shrink = task_instances_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.task_instances_shrink is not None:
            result['TaskInstances'] = self.task_instances_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('TaskInstances') is not None:
            self.task_instances_shrink = m.get('TaskInstances')

        return self

