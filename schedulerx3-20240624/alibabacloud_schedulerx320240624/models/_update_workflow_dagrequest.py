# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_schedulerx320240624 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkflowDAGRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        dag: main_models.UpdateWorkflowDAGRequestDag = None,
        dag_version: str = None,
        workflow_id: int = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.dag = dag
        self.dag_version = dag_version
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        if self.dag:
            self.dag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.dag is not None:
            result['Dag'] = self.dag.to_map()

        if self.dag_version is not None:
            result['DagVersion'] = self.dag_version

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Dag') is not None:
            temp_model = main_models.UpdateWorkflowDAGRequestDag()
            self.dag = temp_model.from_map(m.get('Dag'))

        if m.get('DagVersion') is not None:
            self.dag_version = m.get('DagVersion')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class UpdateWorkflowDAGRequestDag(DaraModel):
    def __init__(
        self,
        edges: List[main_models.UpdateWorkflowDAGRequestDagEdges] = None,
        nodes: List[main_models.UpdateWorkflowDAGRequestDagNodes] = None,
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
                temp_model = main_models.UpdateWorkflowDAGRequestDagEdges()
                self.edges.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.UpdateWorkflowDAGRequestDagNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class UpdateWorkflowDAGRequestDagNodes(DaraModel):
    def __init__(
        self,
        content: str = None,
        coordinate: main_models.UpdateWorkflowDAGRequestDagNodesCoordinate = None,
        id: int = None,
    ):
        self.content = content
        self.coordinate = coordinate
        self.id = id

    def validate(self):
        if self.coordinate:
            self.coordinate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.coordinate is not None:
            result['Coordinate'] = self.coordinate.to_map()

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Coordinate') is not None:
            temp_model = main_models.UpdateWorkflowDAGRequestDagNodesCoordinate()
            self.coordinate = temp_model.from_map(m.get('Coordinate'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class UpdateWorkflowDAGRequestDagNodesCoordinate(DaraModel):
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

class UpdateWorkflowDAGRequestDagEdges(DaraModel):
    def __init__(
        self,
        source: int = None,
        target: int = None,
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

