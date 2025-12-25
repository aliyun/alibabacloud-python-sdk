# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskConfigRequest(DaraModel):
    def __init__(
        self,
        node_config: str = None,
        node_id: str = None,
        tid: int = None,
    ):
        # The advanced configuration for the node. The value of this parameter must be a JSON string.
        # 
        # This parameter is required.
        self.node_config = node_config
        # The ID of the task node. You can call the [GetTaskInstanceRelation](https://help.aliyun.com/document_detail/424711.html) operation to query the node ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_config is not None:
            result['NodeConfig'] = self.node_config

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeConfig') is not None:
            self.node_config = m.get('NodeConfig')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

