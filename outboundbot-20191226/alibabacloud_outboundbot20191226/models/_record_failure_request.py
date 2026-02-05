# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecordFailureRequest(DaraModel):
    def __init__(
        self,
        actual_time: int = None,
        call_id: str = None,
        called_number: str = None,
        calling_number: str = None,
        disposition_code: str = None,
        exception_codes: str = None,
        instance_id: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.actual_time = actual_time
        # This parameter is required.
        self.call_id = call_id
        # This parameter is required.
        self.called_number = called_number
        # This parameter is required.
        self.calling_number = calling_number
        # This parameter is required.
        self.disposition_code = disposition_code
        self.exception_codes = exception_codes
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.disposition_code is not None:
            result['DispositionCode'] = self.disposition_code

        if self.exception_codes is not None:
            result['ExceptionCodes'] = self.exception_codes

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('DispositionCode') is not None:
            self.disposition_code = m.get('DispositionCode')

        if m.get('ExceptionCodes') is not None:
            self.exception_codes = m.get('ExceptionCodes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

