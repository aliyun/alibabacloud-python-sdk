# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobConfig(DaraModel):
    def __init__(
        self,
        max_retry_time: int = None,
        trigger_interval: int = None,
    ):
        # The maximum number of retries. Valid values: 0 to 100. This parameter specifies the maximum number of retries allowed when Simple Log Service triggers a function based on the trigger interval if an error occurs, such as insufficient permissions, network failures, and function execution exceptions. If the trigger fails after the maximum number of retries is reached, Simple Log Service triggers the function again when the next trigger interval arrives.
        self.max_retry_time = max_retry_time
        # The time interval at which Simple Log Service triggers function execution. For example, you can retrieve data from the Logstore within the last 120 seconds to Function Compute every 120 seconds to perform custom computing.
        self.trigger_interval = trigger_interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_retry_time is not None:
            result['maxRetryTime'] = self.max_retry_time

        if self.trigger_interval is not None:
            result['triggerInterval'] = self.trigger_interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxRetryTime') is not None:
            self.max_retry_time = m.get('maxRetryTime')

        if m.get('triggerInterval') is not None:
            self.trigger_interval = m.get('triggerInterval')

        return self

