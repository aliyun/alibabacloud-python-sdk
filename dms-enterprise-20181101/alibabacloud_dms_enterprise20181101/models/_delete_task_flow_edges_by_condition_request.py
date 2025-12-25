# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTaskFlowEdgesByConditionRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        id: int = None,
        node_end: int = None,
        node_from: int = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The ID of the task flow edge to delete.
        self.id = id
        # The ID of the end node of the edge to delete.
        self.node_end = node_end
        # The ID of the start node on the edge to delete.
        self.node_from = node_from
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
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.id is not None:
            result['Id'] = self.id

        if self.node_end is not None:
            result['NodeEnd'] = self.node_end

        if self.node_from is not None:
            result['NodeFrom'] = self.node_from

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeEnd') is not None:
            self.node_end = m.get('NodeEnd')

        if m.get('NodeFrom') is not None:
            self.node_from = m.get('NodeFrom')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

