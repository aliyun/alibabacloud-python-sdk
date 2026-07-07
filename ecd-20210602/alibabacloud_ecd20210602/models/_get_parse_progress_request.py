# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParseProgressRequest(DaraModel):
    def __init__(
        self,
        task_key: str = None,
    ):
        # The task key for parsing the skill package.
        # 
        # This parameter is required.
        self.task_key = task_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_key is not None:
            result['TaskKey'] = self.task_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskKey') is not None:
            self.task_key = m.get('TaskKey')

        return self

