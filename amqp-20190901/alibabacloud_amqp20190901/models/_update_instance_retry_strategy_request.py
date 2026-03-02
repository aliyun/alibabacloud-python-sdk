# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceRetryStrategyRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        retry_interval: int = None,
        retry_times: int = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.retry_interval = retry_interval
        self.retry_times = retry_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')

        return self

