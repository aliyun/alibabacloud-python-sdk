# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreatePipelineRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        execute_policy: main_models.CreatePipelineRequestExecutePolicy = None,
        pipeline: main_models.CreatePipelineRequestPipeline = None,
        pipeline_name: str = None,
        sink: main_models.CreatePipelineRequestSink = None,
        source: main_models.CreatePipelineRequestSource = None,
    ):
        # The pipeline description.
        self.description = description
        # The execution policy.
        self.execute_policy = execute_policy
        # The pipeline configuration.
        self.pipeline = pipeline
        # The pipeline name.
        self.pipeline_name = pipeline_name
        # The data sink for the processed output.
        self.sink = sink
        # The data source.
        self.source = source

    def validate(self):
        if self.execute_policy:
            self.execute_policy.validate()
        if self.pipeline:
            self.pipeline.validate()
        if self.sink:
            self.sink.validate()
        if self.source:
            self.source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.execute_policy is not None:
            result['executePolicy'] = self.execute_policy.to_map()

        if self.pipeline is not None:
            result['pipeline'] = self.pipeline.to_map()

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.sink is not None:
            result['sink'] = self.sink.to_map()

        if self.source is not None:
            result['source'] = self.source.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executePolicy') is not None:
            temp_model = main_models.CreatePipelineRequestExecutePolicy()
            self.execute_policy = temp_model.from_map(m.get('executePolicy'))

        if m.get('pipeline') is not None:
            temp_model = main_models.CreatePipelineRequestPipeline()
            self.pipeline = temp_model.from_map(m.get('pipeline'))

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('sink') is not None:
            temp_model = main_models.CreatePipelineRequestSink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('source') is not None:
            temp_model = main_models.CreatePipelineRequestSource()
            self.source = temp_model.from_map(m.get('source'))

        return self

class CreatePipelineRequestSource(DaraModel):
    def __init__(
        self,
        logstore: main_models.CreatePipelineRequestSourceLogstore = None,
        type: str = None,
    ):
        # The Log Service Logstore configuration. This parameter is required when `source.type` is set to `logstore`.
        self.logstore = logstore
        # The data source type.
        self.type = type

    def validate(self):
        if self.logstore:
            self.logstore.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            temp_model = main_models.CreatePipelineRequestSourceLogstore()
            self.logstore = temp_model.from_map(m.get('logstore'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreatePipelineRequestSourceLogstore(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        query: str = None,
    ):
        # The Logstore name.
        self.logstore = logstore
        # The Log Service Project name.
        self.project = project
        # The query statement to filter logs.
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

class CreatePipelineRequestSink(DaraModel):
    def __init__(
        self,
        dataset: main_models.CreatePipelineRequestSinkDataset = None,
        type: str = None,
    ):
        # The destination dataset configuration. This parameter is required when `sink.type` is set to `dataset`.
        self.dataset = dataset
        # The sink type.
        self.type = type

    def validate(self):
        if self.dataset:
            self.dataset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset is not None:
            result['dataset'] = self.dataset.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataset') is not None:
            temp_model = main_models.CreatePipelineRequestSinkDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreatePipelineRequestSinkDataset(DaraModel):
    def __init__(
        self,
        dataset: str = None,
        workspace: str = None,
    ):
        # The dataset name.
        self.dataset = dataset
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset is not None:
            result['dataset'] = self.dataset

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataset') is not None:
            self.dataset = m.get('dataset')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class CreatePipelineRequestPipeline(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.CreatePipelineRequestPipelineNodes] = None,
    ):
        # The pipeline nodes.
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
                temp_model = main_models.CreatePipelineRequestPipelineNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class CreatePipelineRequestPipelineNodes(DaraModel):
    def __init__(
        self,
        id: str = None,
        parameters: Dict[str, Any] = None,
        type: str = None,
    ):
        # The node ID.
        self.id = id
        # The node parameters.
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

class CreatePipelineRequestExecutePolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        run_once: main_models.CreatePipelineRequestExecutePolicyRunOnce = None,
        scheduled: main_models.CreatePipelineRequestExecutePolicyScheduled = None,
    ):
        # The execution mode. Set to `runOnce` for a single execution, or `scheduled` for a recurring execution.
        self.mode = mode
        # The configuration for a one-time execution. This parameter is required when `executePolicy.mode` is set to `runOnce`.
        self.run_once = run_once
        # The configuration for a scheduled execution. This parameter is required when `executePolicy.mode` is set to `scheduled`.
        self.scheduled = scheduled

    def validate(self):
        if self.run_once:
            self.run_once.validate()
        if self.scheduled:
            self.scheduled.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['mode'] = self.mode

        if self.run_once is not None:
            result['runOnce'] = self.run_once.to_map()

        if self.scheduled is not None:
            result['scheduled'] = self.scheduled.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('runOnce') is not None:
            temp_model = main_models.CreatePipelineRequestExecutePolicyRunOnce()
            self.run_once = temp_model.from_map(m.get('runOnce'))

        if m.get('scheduled') is not None:
            temp_model = main_models.CreatePipelineRequestExecutePolicyScheduled()
            self.scheduled = temp_model.from_map(m.get('scheduled'))

        return self

class CreatePipelineRequestExecutePolicyScheduled(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        interval: str = None,
    ):
        # The start timestamp.
        self.from_time = from_time
        # The execution interval in seconds.
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.interval is not None:
            result['interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        return self

class CreatePipelineRequestExecutePolicyRunOnce(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        to_time: int = None,
    ):
        # The start timestamp.
        self.from_time = from_time
        # The end timestamp.
        self.to_time = to_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

