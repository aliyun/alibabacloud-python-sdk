# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        expire_days: int = None,
        hour: int = None,
        instance_id: str = None,
        minute: int = None,
        recurrence_type: str = None,
        recurrence_values: List[int] = None,
        timeout_seconds: int = None,
    ):
        self.expire_days = expire_days
        self.hour = hour
        self.instance_id = instance_id
        self.minute = minute
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_days is not None:
            result['ExpireDays'] = self.expire_days

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireDays') is not None:
            self.expire_days = m.get('ExpireDays')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

