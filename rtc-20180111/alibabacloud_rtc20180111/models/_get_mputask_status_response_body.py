# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMPUTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        status: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The status ID of the bypass transcoding task. Valid values:
        #  - **0**: Waiting for the channel to start.
        # > If the task is not started within 30 days, the task is automatically stopped.
        # 
        #  - **1**: The task is running.
        # 
        #  - **2**: The task is stopped.
        # 
        #  - **3**: The task is stopped by the user.
        # 
        #  - **4**: The channel is stopped.
        # 
        #  - **5**: Live streaming is stopped due to CDN network issues.
        # 
        #  - **6**: Live streaming is stopped due to live streaming URL issues.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

