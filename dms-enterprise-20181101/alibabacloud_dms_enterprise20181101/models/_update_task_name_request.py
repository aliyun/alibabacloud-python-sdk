# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskNameRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        node_name: str = None,
        tid: int = None,
    ):
        # The ID of the node. You can call the [GetTaskInstanceRelation](https://help.aliyun.com/document_detail/424711.html) operation to query the node ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The name of the node. You can call the [GetTaskInstanceRelation](https://help.aliyun.com/document_detail/424711.html) operation to query the node name.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

