# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class PreviewPipelineRequest(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        pipeline: main_models.PreviewPipelineRequestPipeline = None,
        source: main_models.PreviewPipelineRequestSource = None,
        to_time: int = None,
    ):
        # The start time of the preview data window, in UNIX seconds.
        self.from_time = from_time
        # The pipeline configuration, which defines the node orchestration.
        self.pipeline = pipeline
        # The pipeline data source.
        self.source = source
        # The end time of the preview data window, in UNIX seconds.
        self.to_time = to_time

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.pipeline is not None:
            result['pipeline'] = self.pipeline.to_map()

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('pipeline') is not None:
            temp_model = main_models.PreviewPipelineRequestPipeline()
            self.pipeline = temp_model.from_map(m.get('pipeline'))

        if m.get('source') is not None:
            temp_model = main_models.PreviewPipelineRequestSource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

class PreviewPipelineRequestSource(DaraModel):
    def __init__(
        self,
        dataset: main_models.PreviewPipelineRequestSourceDataset = None,
        input_fields: List[main_models.PreviewPipelineRequestSourceInputFields] = None,
        logstore: main_models.PreviewPipelineRequestSourceLogstore = None,
        type: str = None,
    ):
        # The Dataset datasource config under the current AgentSpace.
        self.dataset = dataset
        # The input fields and field types. This parameter applies to all data source types.
        self.input_fields = input_fields
        # The SLS Logstore datasource config.
        self.logstore = logstore
        # The data source type. Currently, Simple Log Service (SLS) is supported.
        self.type = type

    def validate(self):
        if self.dataset:
            self.dataset.validate()
        if self.input_fields:
            for v1 in self.input_fields:
                 if v1:
                    v1.validate()
        if self.logstore:
            self.logstore.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset is not None:
            result['dataset'] = self.dataset.to_map()

        result['inputFields'] = []
        if self.input_fields is not None:
            for k1 in self.input_fields:
                result['inputFields'].append(k1.to_map() if k1 else None)

        if self.logstore is not None:
            result['logstore'] = self.logstore.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataset') is not None:
            temp_model = main_models.PreviewPipelineRequestSourceDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        self.input_fields = []
        if m.get('inputFields') is not None:
            for k1 in m.get('inputFields'):
                temp_model = main_models.PreviewPipelineRequestSourceInputFields()
                self.input_fields.append(temp_model.from_map(k1))

        if m.get('logstore') is not None:
            temp_model = main_models.PreviewPipelineRequestSourceLogstore()
            self.logstore = temp_model.from_map(m.get('logstore'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PreviewPipelineRequestSourceLogstore(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        query: str = None,
    ):
        # The name of the SLS Logstore.
        self.logstore = logstore
        # The name of the SLS project.
        self.project = project
        # The data filtered query statement in SLS query/analysis syntax.
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

class PreviewPipelineRequestSourceInputFields(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The field name.
        self.name = name
        # The field type. Valid values: text, long, double, and json.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class PreviewPipelineRequestSourceDataset(DaraModel):
    def __init__(
        self,
        dataset: str = None,
        filter: str = None,
    ):
        # The name of the source dataset.
        self.dataset = dataset
        # The filter condition for dataset data.
        self.filter = filter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset is not None:
            result['dataset'] = self.dataset

        if self.filter is not None:
            result['filter'] = self.filter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataset') is not None:
            self.dataset = m.get('dataset')

        if m.get('filter') is not None:
            self.filter = m.get('filter')

        return self

class PreviewPipelineRequestPipeline(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.PreviewPipelineRequestPipelineNodes] = None,
    ):
        # The list of nodes.
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['nodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('nodes') is not None:
            for k1 in m.get('nodes'):
                temp_model = main_models.PreviewPipelineRequestPipelineNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class PreviewPipelineRequestPipelineNodes(DaraModel):
    def __init__(
        self,
        id: str = None,
        parameters: Dict[str, Any] = None,
        type: str = None,
    ):
        # The node ID.
        self.id = id
        # The node parameters in key-value format. The parameters vary based on the node type.
        self.parameters = parameters
        # The node type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

