# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKillInstanceSessionTaskResultRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        node_id: str = None,
        task_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The node ID.
        # 
        # >  You must specify this parameter if your database instance is a PolarDB for MySQL cluster.
        self.node_id = node_id
        # The task ID. You can obtain the task ID from the response parameters of the [CreateKillInstanceSessionTask](https://help.aliyun.com/document_detail/609246.html) operation.
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

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

