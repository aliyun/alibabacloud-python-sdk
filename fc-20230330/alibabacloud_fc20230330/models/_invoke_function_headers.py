# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class InvokeFunctionHeaders(DaraModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_fc_async_task_id: str = None,
        x_fc_invocation_type: str = None,
        x_fc_log_type: str = None,
    ):
        self.common_headers = common_headers
        # Asynchronous task ID. Enable asynchronous tasks beforehand.
        # 
        # > When using the SDK for invocation, set a business-related ID. This helps with subsequent operations on the execution. For example, a video processing function can use the video filename as the invocation ID. Use this ID to check if the video processing is complete or to stop it. The ID naming convention must start with an English letter (uppercase or lowercase) or an underscore (_). It can contain English letters (uppercase or lowercase), digits (0-9), underscores (_), and hyphens (-). The ID cannot exceed 128 characters. If you do not set an ID for asynchronous invocation, the system automatically generates one.
        self.x_fc_async_task_id = x_fc_async_task_id
        # Function invocation type. Sync or Async.
        self.x_fc_invocation_type = x_fc_invocation_type
        # Log type returned by function invocation. None or Tail.
        self.x_fc_log_type = x_fc_log_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers

        if self.x_fc_async_task_id is not None:
            result['x-fc-async-task-id'] = self.x_fc_async_task_id

        if self.x_fc_invocation_type is not None:
            result['x-fc-invocation-type'] = self.x_fc_invocation_type

        if self.x_fc_log_type is not None:
            result['x-fc-log-type'] = self.x_fc_log_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')

        if m.get('x-fc-async-task-id') is not None:
            self.x_fc_async_task_id = m.get('x-fc-async-task-id')

        if m.get('x-fc-invocation-type') is not None:
            self.x_fc_invocation_type = m.get('x-fc-invocation-type')

        if m.get('x-fc-log-type') is not None:
            self.x_fc_log_type = m.get('x-fc-log-type')

        return self

