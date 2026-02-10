# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class FinishGuidTaskRequest(DaraModel):
    def __init__(
        self,
        task_type_name: str = None,
    ):
        # The name of the task type.
        # 
        # This parameter is required.
        self.task_type_name = task_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.task_type_name is not None:
            result['TaskTypeName'] = self.task_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskTypeName') is not None:
            self.task_type_name = m.get('TaskTypeName')

        return self

