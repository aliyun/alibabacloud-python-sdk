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
        # The ID of the asynchronous task. You must enable the asynchronous task feature in advance.
        # 
        # >  If you use an SDK to invoke a function, we recommend that you specify a business-related ID to facilitate subsequent operations. For example, a video processing function can use video file names as invocation IDs. This way, you can easily check whether a video is successfully processed or terminated before it is processed. The ID can start only with letters or underscores. An ID can contain *letters, digits (0 - 9), underscores*, and hyphens (-). It can be up to 128 characters in length. If you do not specify the ID of the asynchronous invocation, the system automatically generates an ID.
        self.x_fc_async_task_id = x_fc_async_task_id
        # The type of function invocation. Valid values: Sync and Async.
        self.x_fc_invocation_type = x_fc_invocation_type
        # The log type of function invocation. Valid values: None and Tail.
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

