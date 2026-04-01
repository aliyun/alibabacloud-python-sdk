# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCollationTimeZoneResponseBody(DaraModel):
    def __init__(
        self,
        collation: str = None,
        dbinstance_id: str = None,
        request_id: str = None,
        task_id: str = None,
        timezone: str = None,
    ):
        # The character set collation of the instance.
        self.collation = collation
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id
        # The time zone.
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collation is not None:
            result['Collation'] = self.collation

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collation') is not None:
            self.collation = m.get('Collation')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

