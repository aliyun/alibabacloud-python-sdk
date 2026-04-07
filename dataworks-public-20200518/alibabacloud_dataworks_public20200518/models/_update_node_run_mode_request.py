# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNodeRunModeRequest(DaraModel):
    def __init__(
        self,
        node_id: int = None,
        project_env: str = None,
        scheduler_type: int = None,
    ):
        # The node ID. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the node ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The environment in which the node runs. Valid values: DEV and PROD. The value DEV indicates the development environment, and the value PROD indicates the production environment.
        # 
        # *   PROD
        # *   DEV
        # 
        # This parameter is required.
        self.project_env = project_env
        # The operation that you want to perform on the node. Valid values:
        # 
        # *   0: indicates that you want to unfreeze the node.
        # *   2: indicates that you want to freeze the node.
        # 
        # This parameter is required.
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

