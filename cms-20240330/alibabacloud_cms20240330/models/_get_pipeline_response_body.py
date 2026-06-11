# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetPipelineResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        execute_policy: main_models.GetPipelineResponseBodyExecutePolicy = None,
        pipeline: main_models.GetPipelineResponseBodyPipeline = None,
        pipeline_name: str = None,
        region_id: str = None,
        request_id: str = None,
        sink: main_models.GetPipelineResponseBodySink = None,
        source: main_models.GetPipelineResponseBodySource = None,
        update_time: str = None,
        workspace: str = None,
    ):
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The description of the pipeline.
        self.description = description
        # The execution policy.
        self.execute_policy = execute_policy
        # The pipeline configuration.
        self.pipeline = pipeline
        # The pipeline name.
        self.pipeline_name = pipeline_name
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The pipeline\\"s data sink.
        self.sink = sink
        # The pipeline\\"s data source.
        self.source = source
        # The update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time
        # The workspace ID.
        self.workspace = workspace

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
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.execute_policy is not None:
            result['executePolicy'] = self.execute_policy.to_map()

        if self.pipeline is not None:
            result['pipeline'] = self.pipeline.to_map()

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.sink is not None:
            result['sink'] = self.sink.to_map()

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('executePolicy') is not None:
            temp_model = main_models.GetPipelineResponseBodyExecutePolicy()
            self.execute_policy = temp_model.from_map(m.get('executePolicy'))

        if m.get('pipeline') is not None:
            temp_model = main_models.GetPipelineResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m.get('pipeline'))

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('sink') is not None:
            temp_model = main_models.GetPipelineResponseBodySink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('source') is not None:
            temp_model = main_models.GetPipelineResponseBodySource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetPipelineResponseBodySource(DaraModel):
    def __init__(
        self,
        logstore: main_models.GetPipelineResponseBodySourceLogstore = None,
        type: str = None,
    ):
        # The configuration of the Log Service Logstore.
        self.logstore = logstore
        # The type of the data source.
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
            temp_model = main_models.GetPipelineResponseBodySourceLogstore()
            self.logstore = temp_model.from_map(m.get('logstore'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetPipelineResponseBodySourceLogstore(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        query: str = None,
    ):
        # The name of the Log Service Logstore.
        self.logstore = logstore
        # The name of the Log Service project.
        self.project = project
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

class GetPipelineResponseBodySink(DaraModel):
    def __init__(
        self,
        dataset: main_models.GetPipelineResponseBodySinkDataset = None,
        type: str = None,
    ):
        # The dataset configuration.
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
            temp_model = main_models.GetPipelineResponseBodySinkDataset()
            self.dataset = temp_model.from_map(m.get('dataset'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetPipelineResponseBodySinkDataset(DaraModel):
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

class GetPipelineResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.GetPipelineResponseBodyPipelineNodes] = None,
    ):
        # The nodes in the pipeline.
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
                temp_model = main_models.GetPipelineResponseBodyPipelineNodes()
                self.nodes.append(temp_model.from_map(k1))

        return self

class GetPipelineResponseBodyPipelineNodes(DaraModel):
    def __init__(
        self,
        id: str = None,
        parameters: Dict[str, Any] = None,
        type: str = None,
    ):
        # The node ID.
        self.id = id
        # The parameters for the node.
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

class GetPipelineResponseBodyExecutePolicy(DaraModel):
    def __init__(
        self,
        mode: str = None,
        run_once: main_models.GetPipelineResponseBodyExecutePolicyRunOnce = None,
        scheduled: main_models.GetPipelineResponseBodyExecutePolicyScheduled = None,
    ):
        # The execution mode.
        self.mode = mode
        # The configuration for a one-time execution.
        self.run_once = run_once
        # The configuration for a scheduled execution.
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
            temp_model = main_models.GetPipelineResponseBodyExecutePolicyRunOnce()
            self.run_once = temp_model.from_map(m.get('runOnce'))

        if m.get('scheduled') is not None:
            temp_model = main_models.GetPipelineResponseBodyExecutePolicyScheduled()
            self.scheduled = temp_model.from_map(m.get('scheduled'))

        return self

class GetPipelineResponseBodyExecutePolicyScheduled(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        interval: str = None,
    ):
        # The start time of the execution, as a Unix timestamp.
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

class GetPipelineResponseBodyExecutePolicyRunOnce(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        to_time: int = None,
    ):
        # The start time of the execution, as a Unix timestamp.
        self.from_time = from_time
        # The end time of the execution, as a Unix timestamp.
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

