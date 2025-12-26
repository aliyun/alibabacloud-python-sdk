# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOtaTaskByTaskIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        ota_version: str = None,
        release_note: str = None,
        request_id: str = None,
        task_start_time: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The OTA version.
        self.ota_version = ota_version
        # The version description.
        self.release_note = release_note
        # The request ID.
        self.request_id = request_id
        # The execution time of the OTA update task. The time follows the ISO 8601 standard.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.task_start_time = task_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version

        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')

        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')

        return self

