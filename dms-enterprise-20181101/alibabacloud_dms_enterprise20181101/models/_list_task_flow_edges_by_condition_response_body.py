# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowEdgesByConditionResponseBody(DaraModel):
    def __init__(
        self,
        edges: main_models.ListTaskFlowEdgesByConditionResponseBodyEdges = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of task flow edges.
        self.edges = edges
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.edges:
            self.edges.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edges is not None:
            result['Edges'] = self.edges.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edges') is not None:
            temp_model = main_models.ListTaskFlowEdgesByConditionResponseBodyEdges()
            self.edges = temp_model.from_map(m.get('Edges'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListTaskFlowEdgesByConditionResponseBodyEdges(DaraModel):
    def __init__(
        self,
        edge: List[main_models.ListTaskFlowEdgesByConditionResponseBodyEdgesEdge] = None,
    ):
        self.edge = edge

    def validate(self):
        if self.edge:
            for v1 in self.edge:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Edge'] = []
        if self.edge is not None:
            for k1 in self.edge:
                result['Edge'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge = []
        if m.get('Edge') is not None:
            for k1 in m.get('Edge'):
                temp_model = main_models.ListTaskFlowEdgesByConditionResponseBodyEdgesEdge()
                self.edge.append(temp_model.from_map(k1))

        return self

class ListTaskFlowEdgesByConditionResponseBodyEdgesEdge(DaraModel):
    def __init__(
        self,
        id: int = None,
        node_end: int = None,
        node_from: int = None,
    ):
        # The ID of the task flow edge.
        self.id = id
        # The ID of the end node on the edge.
        self.node_end = node_end
        # The ID of the start node on the edge.
        self.node_from = node_from

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.node_end is not None:
            result['NodeEnd'] = self.node_end

        if self.node_from is not None:
            result['NodeFrom'] = self.node_from

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeEnd') is not None:
            self.node_end = m.get('NodeEnd')

        if m.get('NodeFrom') is not None:
            self.node_from = m.get('NodeFrom')

        return self

