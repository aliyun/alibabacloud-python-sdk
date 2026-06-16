# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class UpdatePipelineRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        execute_policy: main_models.UpdatePipelineRequestExecutePolicy = None,
        pipeline: main_models.UpdatePipelineRequestPipeline = None,
        sink: main_models.UpdatePipelineRequestSink = None,
        source: main_models.UpdatePipelineRequestSource = None,
        client_token: str = None,
    ):
        self.description = description
        self.execute_policy = execute_policy
        self.pipeline = pipeline
        self.sink = sink
        self.source = source
        self.client_token = client_token

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

        if self.sink is not None:
            result['sink'] = self.sink.to_map()

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executePolicy') is not None:
            temp_model = main_models.UpdatePipelineRequestExecutePolicy()
            self.execute_policy = temp_model.from_map(m.get('executePolicy'))

        if m.get('pipeline') is not None:
            temp_model = main_models.UpdatePipelineRequestPipeline()
            self.pipeline = temp_model.from_map(m.get('pipeline'))

        if m.get('sink') is not None:
            temp_model = main_models.UpdatePipelineRequestSink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('source') is not None:
            temp_model = main_models.UpdatePipelineRequestSource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

class UpdatePipelineRequestSource(DaraModel):
    def __init__(
        self,
        logstore: main_models.UpdatePipelineRequestSourceLogstore = None,
        type: str = None,
    ):
        self.logstore = logstore
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
            temp_model = main_models.UpdatePipelineRequestSourceLogstore()
            self.logstore = temp_model.from_map(m.get('logstore'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdatePipelineRequestSourceLogstore(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        query: str = None,
    ):
        self.logstore = logstore
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

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

class UpdatePipelineRequestSink(DaraModel):
    def __init__(
        self,
        dataset: main_models.UpdatePipelineRequestSinkDataset = None,
        type: str = None,
    ):
        self.dataset = dataset
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
            temp_model = main_models.UpdatePipelineRequestSinkDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdatePipelineRequestSinkDataset(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        dataset: str = None,
    ):
        self.agent_space = agent_space
        self.dataset = dataset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.dataset is not None:
            result['dataset'] = self.dataset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('dataset') is not None:
            self.dataset = m.get('dataset')

        return self

class UpdatePipelineRequestPipeline(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.UpdatePipelineRequestPipelineNodes] = None,
    ):
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
                temp_model = main_models.UpdatePipelineRequestPipelineNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class UpdatePipelineRequestPipelineNodes(DaraModel):
    def __init__(
        self,
        id: str = None,
        parameters: Dict[str, Any] = None,
        type: str = None,
    ):
        self.id = id
        self.parameters = parameters
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

class UpdatePipelineRequestExecutePolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        run_once: main_models.UpdatePipelineRequestExecutePolicyRunOnce = None,
        scheduled: main_models.UpdatePipelineRequestExecutePolicyScheduled = None,
    ):
        self.mode = mode
        self.run_once = run_once
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
            temp_model = main_models.UpdatePipelineRequestExecutePolicyRunOnce()
            self.run_once = temp_model.from_map(m.get('runOnce'))

        if m.get('scheduled') is not None:
            temp_model = main_models.UpdatePipelineRequestExecutePolicyScheduled()
            self.scheduled = temp_model.from_map(m.get('scheduled'))

        return self

class UpdatePipelineRequestExecutePolicyScheduled(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        interval: str = None,
    ):
        self.from_time = from_time
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

class UpdatePipelineRequestExecutePolicyRunOnce(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        to_time: int = None,
    ):
        self.from_time = from_time
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

