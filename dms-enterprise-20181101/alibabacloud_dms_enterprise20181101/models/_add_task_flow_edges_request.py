# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class AddTaskFlowEdgesRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        edges: List[main_models.AddTaskFlowEdgesRequestEdges] = None,
        tid: int = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The list of edges of the task flow.
        # 
        # This parameter is required.
        self.edges = edges
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        if self.edges:
            for v1 in self.edges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        result['Edges'] = []
        if self.edges is not None:
            for k1 in self.edges:
                result['Edges'].append(k1.to_map() if k1 else None)

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        self.edges = []
        if m.get('Edges') is not None:
            for k1 in m.get('Edges'):
                temp_model = main_models.AddTaskFlowEdgesRequestEdges()
                self.edges.append(temp_model.from_map(k1))

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class AddTaskFlowEdgesRequestEdges(DaraModel):
    def __init__(
        self,
        node_end: int = None,
        node_from: int = None,
    ):
        # The ID of the node where the end node of the edge is located.
        # 
        # This parameter is required.
        self.node_end = node_end
        # The ID of the node where the start node of the edge is located.
        # 
        # This parameter is required.
        self.node_from = node_from

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_end is not None:
            result['NodeEnd'] = self.node_end

        if self.node_from is not None:
            result['NodeFrom'] = self.node_from

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeEnd') is not None:
            self.node_end = m.get('NodeEnd')

        if m.get('NodeFrom') is not None:
            self.node_from = m.get('NodeFrom')

        return self

