# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class GetWorkflowExecutionDAGResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetWorkflowExecutionDAGResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
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
            temp_model = main_models.GetWorkflowExecutionDAGResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWorkflowExecutionDAGResponseBodyData(DaraModel):
    def __init__(
        self,
        edges: List[main_models.GetWorkflowExecutionDAGResponseBodyDataEdges] = None,
        nodes: List[main_models.GetWorkflowExecutionDAGResponseBodyDataNodes] = None,
    ):
        self.edges = edges
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
                temp_model = main_models.GetWorkflowExecutionDAGResponseBodyDataEdges()
                self.edges.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetWorkflowExecutionDAGResponseBodyDataNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetWorkflowExecutionDAGResponseBodyDataNodes(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        coordinate: main_models.GetWorkflowExecutionDAGResponseBodyDataNodesCoordinate = None,
        id: str = None,
        job_id: int = None,
        job_type: str = None,
        name: str = None,
        status: int = None,
    ):
        self.app_name = app_name
        self.coordinate = coordinate
        # ID。
        self.id = id
        self.job_id = job_id
        self.job_type = job_type
        self.name = name
        self.status = status

    def validate(self):
        if self.coordinate:
            self.coordinate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.coordinate is not None:
            result['Coordinate'] = self.coordinate.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Coordinate') is not None:
            temp_model = main_models.GetWorkflowExecutionDAGResponseBodyDataNodesCoordinate()
            self.coordinate = temp_model.from_map(m.get('Coordinate'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetWorkflowExecutionDAGResponseBodyDataNodesCoordinate(DaraModel):
    def __init__(
        self,
        height: float = None,
        width: float = None,
        x: float = None,
        y: float = None,
    ):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.height is not None:
            result['Height'] = self.height

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class GetWorkflowExecutionDAGResponseBodyDataEdges(DaraModel):
    def __init__(
        self,
        source: str = None,
        target: str = None,
    ):
        self.source = source
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

