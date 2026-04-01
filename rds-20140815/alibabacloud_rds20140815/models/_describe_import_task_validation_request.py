# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImportTaskValidationRequest(DaraModel):
    def __init__(
        self,
        db_instance_id: str = None,
        owner_id: int = None,
        task_id: int = None,
    ):
        # This parameter is required.
        self.db_instance_id = db_instance_id
        self.owner_id = owner_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_instance_id is not None:
            result['DbInstanceId'] = self.db_instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbInstanceId') is not None:
            self.db_instance_id = m.get('DbInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

