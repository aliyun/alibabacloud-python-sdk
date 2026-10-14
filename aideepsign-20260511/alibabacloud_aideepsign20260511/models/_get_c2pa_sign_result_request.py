# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetC2paSignResultRequest(DaraModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The opaque task ID returned by CreateC2paSignTask, up to 64 characters in length.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

