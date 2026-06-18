# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAiOutboundTaskRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: int = None,
    ):
        # The Artificial Intelligence Cloud Call Service (AICCS) instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The job ID.
        # 
        # You can invoke the [CreateAiOutboundTask](https://help.aliyun.com/document_detail/312260.html) API and view the **Data** field in the response, or invoke the [GetAiOutboundTaskList](https://help.aliyun.com/document_detail/2718026.html) API and view the **TaskId** field in the response.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

