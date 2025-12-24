# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceConsoleOutputResponseBody(DaraModel):
    def __init__(
        self,
        console_output: str = None,
        instance_id: str = None,
        last_update_time: str = None,
        request_id: str = None,
    ):
        # The Base64-encoded command output of the instance.
        self.console_output = console_output
        # The instance ID.
        self.instance_id = instance_id
        # The time when the last log entry was generated in the Linux kernel. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC+8.
        self.last_update_time = last_update_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_output is not None:
            result['ConsoleOutput'] = self.console_output

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleOutput') is not None:
            self.console_output = m.get('ConsoleOutput')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

