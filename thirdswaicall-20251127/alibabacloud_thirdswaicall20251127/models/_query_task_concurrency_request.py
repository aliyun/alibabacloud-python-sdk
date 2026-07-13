# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskConcurrencyRequest(DaraModel):
    def __init__(
        self,
        application_code: str = None,
        task_id: int = None,
    ):
        self.application_code = application_code
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_code is not None:
            result['ApplicationCode'] = self.application_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationCode') is not None:
            self.application_code = m.get('ApplicationCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

