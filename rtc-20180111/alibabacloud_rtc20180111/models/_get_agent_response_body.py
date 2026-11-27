# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgentResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        stop_time: str = None,
    ):
        # Status message.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Start timestamp, in Unix time, measured in milliseconds.
        self.start_time = start_time
        # Agent status. Valid values: 0 (not started), 1 (starting), 2 (running), 3 (stopping), 4 (stopped), or 5 (failed).
        self.status = status
        # End timestamp, in Unix time, measured in milliseconds.
        self.stop_time = stop_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_time is not None:
            result['StopTime'] = self.stop_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')

        return self

