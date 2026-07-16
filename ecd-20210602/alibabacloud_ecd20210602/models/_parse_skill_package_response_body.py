# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ParseSkillPackageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        task_key: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The key of the skill package parsing task.
        self.task_key = task_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_key is not None:
            result['TaskKey'] = self.task_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')

        return self

