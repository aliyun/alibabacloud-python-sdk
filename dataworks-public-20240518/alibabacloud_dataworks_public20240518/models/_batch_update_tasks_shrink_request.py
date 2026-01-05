# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchUpdateTasksShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        tasks_shrink: str = None,
    ):
        # The remarks.
        self.comment = comment
        # The list of tasks.
        self.tasks_shrink = tasks_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.tasks_shrink is not None:
            result['Tasks'] = self.tasks_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')

        return self

