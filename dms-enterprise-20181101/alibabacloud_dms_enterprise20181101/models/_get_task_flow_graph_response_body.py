# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetTaskFlowGraphResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        task_flow_graph: main_models.GetTaskFlowGraphResponseBodyTaskFlowGraph = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The list of DAG variables of the task flow.
        self.task_flow_graph = task_flow_graph

    def validate(self):
        if self.task_flow_graph:
            self.task_flow_graph.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.task_flow_graph is not None:
            result['TaskFlowGraph'] = self.task_flow_graph.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskFlowGraph') is not None:
            temp_model = main_models.GetTaskFlowGraphResponseBodyTaskFlowGraph()
            self.task_flow_graph = temp_model.from_map(m.get('TaskFlowGraph'))

        return self

class GetTaskFlowGraphResponseBodyTaskFlowGraph(DaraModel):
    def __init__(
        self,
        can_edit: bool = None,
        dag_name: str = None,
        edges: main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphEdges = None,
        nodes: main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphNodes = None,
        status: int = None,
    ):
        # Indicates whether the task flow is editable. Valid values:
        # 
        # - **true**: editable
        # - **false**: non-editable
        self.can_edit = can_edit
        # The name of the task flow.
        self.dag_name = dag_name
        # The list of task flow edges.
        self.edges = edges
        # The node list of the task flow.
        self.nodes = nodes
        # The status of the task flow. Valid values:
        # 
        # - **0**: invalid
        # - **1**: not scheduled
        # - **2**: to be scheduled
        self.status = status

    def validate(self):
        if self.edges:
            self.edges.validate()
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_edit is not None:
            result['CanEdit'] = self.can_edit

        if self.dag_name is not None:
            result['DagName'] = self.dag_name

        if self.edges is not None:
            result['Edges'] = self.edges.to_map()

        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanEdit') is not None:
            self.can_edit = m.get('CanEdit')

        if m.get('DagName') is not None:
            self.dag_name = m.get('DagName')

        if m.get('Edges') is not None:
            temp_model = main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphEdges()
            self.edges = temp_model.from_map(m.get('Edges'))

        if m.get('Nodes') is not None:
            temp_model = main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphNodes()
            self.nodes = temp_model.from_map(m.get('Nodes'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetTaskFlowGraphResponseBodyTaskFlowGraphNodes(DaraModel):
    def __init__(
        self,
        node: List[main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphNodesNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for v1 in self.node:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Node'] = []
        if self.node is not None:
            for k1 in self.node:
                result['Node'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k1 in m.get('Node'):
                temp_model = main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphNodesNode()
                self.node.append(temp_model.from_map(k1))

        return self

class GetTaskFlowGraphResponseBodyTaskFlowGraphNodesNode(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        graph_param: str = None,
        node_config: str = None,
        node_content: str = None,
        node_id: int = None,
        node_name: str = None,
        node_type: int = None,
        time_variables: str = None,
    ):
        # The ID of the task flow.
        self.dag_id = dag_id
        # The position of the node in the DAG.
        self.graph_param = graph_param
        # The advanced configuration of the node.
        self.node_config = node_config
        # The configuration of the node.
        self.node_content = node_content
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The type of the node. For more information about the valid values for this parameter, see [NodeType parameter](https://help.aliyun.com/document_detail/424705.html).
        self.node_type = node_type
        # The time variables for the node.
        self.time_variables = time_variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.graph_param is not None:
            result['GraphParam'] = self.graph_param

        if self.node_config is not None:
            result['NodeConfig'] = self.node_config

        if self.node_content is not None:
            result['NodeContent'] = self.node_content

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.time_variables is not None:
            result['TimeVariables'] = self.time_variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('GraphParam') is not None:
            self.graph_param = m.get('GraphParam')

        if m.get('NodeConfig') is not None:
            self.node_config = m.get('NodeConfig')

        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('TimeVariables') is not None:
            self.time_variables = m.get('TimeVariables')

        return self

class GetTaskFlowGraphResponseBodyTaskFlowGraphEdges(DaraModel):
    def __init__(
        self,
        edge: List[main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphEdgesEdge] = None,
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
                temp_model = main_models.GetTaskFlowGraphResponseBodyTaskFlowGraphEdgesEdge()
                self.edge.append(temp_model.from_map(k1))

        return self

class GetTaskFlowGraphResponseBodyTaskFlowGraphEdgesEdge(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        id: int = None,
        node_end: int = None,
        node_from: int = None,
    ):
        # The ID of the task flow.
        self.dag_id = dag_id
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
        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.id is not None:
            result['Id'] = self.id

        if self.node_end is not None:
            result['NodeEnd'] = self.node_end

        if self.node_from is not None:
            result['NodeFrom'] = self.node_from

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

        return self

