# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx220190430 import models as main_models
from darabonba.model import DaraModel

class GetWorkFlowResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetWorkFlowResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Error codes
        self.code = code
        # The data of the workflow.
        self.data = data
        # Error message
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # The result of the API call.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetWorkFlowResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWorkFlowResponseBodyData(DaraModel):
    def __init__(
        self,
        work_flow_info: main_models.GetWorkFlowResponseBodyDataWorkFlowInfo = None,
        work_flow_node_info: main_models.GetWorkFlowResponseBodyDataWorkFlowNodeInfo = None,
    ):
        # The basic information of the workflow.
        self.work_flow_info = work_flow_info
        # The node information of the workflow.
        self.work_flow_node_info = work_flow_node_info

    def validate(self):
        if self.work_flow_info:
            self.work_flow_info.validate()
        if self.work_flow_node_info:
            self.work_flow_node_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.work_flow_info is not None:
            result['WorkFlowInfo'] = self.work_flow_info.to_map()

        if self.work_flow_node_info is not None:
            result['WorkFlowNodeInfo'] = self.work_flow_node_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkFlowInfo') is not None:
            temp_model = main_models.GetWorkFlowResponseBodyDataWorkFlowInfo()
            self.work_flow_info = temp_model.from_map(m.get('WorkFlowInfo'))

        if m.get('WorkFlowNodeInfo') is not None:
            temp_model = main_models.GetWorkFlowResponseBodyDataWorkFlowNodeInfo()
            self.work_flow_node_info = temp_model.from_map(m.get('WorkFlowNodeInfo'))

        return self

class GetWorkFlowResponseBodyDataWorkFlowNodeInfo(DaraModel):
    def __init__(
        self,
        edges: List[main_models.GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges] = None,
        nodes: List[main_models.GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes] = None,
    ):
        # The workflow edges.
        self.edges = edges
        # The list of workflow nodes.
        self.nodes = nodes

    def validate(self):
        if self.edges:
            for v1 in self.edges:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Edges'] = []
        if self.edges is not None:
            for k1 in self.edges:
                result['Edges'].append(k1.to_map() if k1 else None)

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edges = []
        if m.get('Edges') is not None:
            for k1 in m.get('Edges'):
                temp_model = main_models.GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges()
                self.edges.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetWorkFlowResponseBodyDataWorkFlowNodeInfoNodes(DaraModel):
    def __init__(
        self,
        id: int = None,
        label: str = None,
        status: int = None,
    ):
        # The ID of the job.
        self.id = id
        # The name of the job.
        self.label = label
        # The status of the job.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetWorkFlowResponseBodyDataWorkFlowNodeInfoEdges(DaraModel):
    def __init__(
        self,
        source: int = None,
        target: int = None,
    ):
        # The ID of the source job.
        self.source = source
        # The ID of the object job.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

class GetWorkFlowResponseBodyDataWorkFlowInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        max_concurrency: str = None,
        name: str = None,
        namespace: str = None,
        status: str = None,
        time_expression: str = None,
        time_type: str = None,
        workflow_id: int = None,
    ):
        # The description of the workflow.
        self.description = description
        self.group_id = group_id
        self.max_concurrency = max_concurrency
        # The name of the workflow.
        self.name = name
        self.namespace = namespace
        # The status of the workflow.
        self.status = status
        # The time expression of the workflow.
        self.time_expression = time_expression
        # The time type of the workflow.
        self.time_type = time_type
        # The ID of the workflow.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.status is not None:
            result['Status'] = self.status

        if self.time_expression is not None:
            result['TimeExpression'] = self.time_expression

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeExpression') is not None:
            self.time_expression = m.get('TimeExpression')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

