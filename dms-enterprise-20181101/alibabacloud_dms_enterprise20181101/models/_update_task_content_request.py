# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskContentRequest(DaraModel):
    def __init__(
        self,
        node_content: str = None,
        node_id: str = None,
        tid: int = None,
    ):
        # The node configurations after modification.
        self.node_content = node_content
        # The ID of the task node. You can call the [GetTaskInstanceRelation](https://help.aliyun.com/document_detail/424711.html) operation to query the node ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the ["View information about the current tenant"](https://help.aliyun.com/document_detail/181330.html) section of the Manage DMS tenants topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_content is not None:
            result['NodeContent'] = self.node_content

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

