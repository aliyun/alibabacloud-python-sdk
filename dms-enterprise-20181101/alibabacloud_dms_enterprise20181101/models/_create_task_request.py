# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTaskRequest(DaraModel):
    def __init__(
        self,
        dag_id: int = None,
        graph_param: str = None,
        node_content: str = None,
        node_name: str = None,
        node_output: str = None,
        node_type: str = None,
        tid: int = None,
        time_variables: str = None,
    ):
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The position of the node on the Directed Acyclic Graph (DAG).
        self.graph_param = graph_param
        # The configuration of the node.
        self.node_content = node_content
        # The name of the node that you want to create.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The output variables configured for the task.
        self.node_output = node_output
        # The type of the node that you want to create. For more information about the valid values for this parameter, see [NodeType parameter](https://help.aliyun.com/document_detail/424705.html).
        # 
        # This parameter is required.
        self.node_type = node_type
        # The tenant ID.
        # 
        # >  To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html) topic.
        self.tid = tid
        # The time variables configured for the node.
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

        if self.node_content is not None:
            result['NodeContent'] = self.node_content

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_output is not None:
            result['NodeOutput'] = self.node_output

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.time_variables is not None:
            result['TimeVariables'] = self.time_variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('GraphParam') is not None:
            self.graph_param = m.get('GraphParam')

        if m.get('NodeContent') is not None:
            self.node_content = m.get('NodeContent')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeOutput') is not None:
            self.node_output = m.get('NodeOutput')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('TimeVariables') is not None:
            self.time_variables = m.get('TimeVariables')

        return self

