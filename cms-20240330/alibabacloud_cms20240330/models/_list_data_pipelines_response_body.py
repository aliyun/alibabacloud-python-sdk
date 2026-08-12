# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListDataPipelinesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        pipelines: List[main_models.ListDataPipelinesResponseBodyPipelines] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of results per page.
        self.max_results = max_results
        # The token for the next page.
        self.next_token = next_token
        # The list of data pipelines.
        self.pipelines = pipelines
        # The request ID.
        self.request_id = request_id
        # The total number of data pipelines.
        self.total_count = total_count

    def validate(self):
        if self.pipelines:
            for v1 in self.pipelines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['pipelines'] = []
        if self.pipelines is not None:
            for k1 in self.pipelines:
                result['pipelines'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.pipelines = []
        if m.get('pipelines') is not None:
            for k1 in m.get('pipelines'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelines()
                self.pipelines.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListDataPipelinesResponseBodyPipelines(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        kind: str = None,
        outputs: List[main_models.ListDataPipelinesResponseBodyPipelinesOutputs] = None,
        pipeline_name: str = None,
        processors: List[main_models.ListDataPipelinesResponseBodyPipelinesProcessors] = None,
        signal_type: str = None,
        sinks: List[main_models.ListDataPipelinesResponseBodyPipelinesSinks] = None,
        source: main_models.ListDataPipelinesResponseBodyPipelinesSource = None,
        status: str = None,
        status_message: str = None,
        update_time: str = None,
        version: int = None,
    ):
        # The time when the pipeline was created.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # The description of the pipeline.
        self.description = description
        # The type of the pipeline.
        # 
        # This parameter is required.
        self.kind = kind
        # The named outputs.
        # 
        # This parameter is required.
        self.outputs = outputs
        # The name of the pipeline.
        # 
        # This parameter is required.
        self.pipeline_name = pipeline_name
        # The common processors.
        # 
        # This parameter is required.
        self.processors = processors
        # The signal type.
        # 
        # This parameter is required.
        self.signal_type = signal_type
        # The output destinations.
        # 
        # This parameter is required.
        self.sinks = sinks
        # The data source.
        # 
        # This parameter is required.
        self.source = source
        # The running status.
        # 
        # This parameter is required.
        self.status = status
        # The status message.
        self.status_message = status_message
        # The time when the pipeline was last updated.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.update_time = update_time
        # The configuration version.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        if self.outputs:
            for v1 in self.outputs:
                 if v1:
                    v1.validate()
        if self.processors:
            for v1 in self.processors:
                 if v1:
                    v1.validate()
        if self.sinks:
            for v1 in self.sinks:
                 if v1:
                    v1.validate()
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

        if self.kind is not None:
            result['kind'] = self.kind

        result['outputs'] = []
        if self.outputs is not None:
            for k1 in self.outputs:
                result['outputs'].append(k1.to_map() if k1 else None)

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        result['processors'] = []
        if self.processors is not None:
            for k1 in self.processors:
                result['processors'].append(k1.to_map() if k1 else None)

        if self.signal_type is not None:
            result['signalType'] = self.signal_type

        result['sinks'] = []
        if self.sinks is not None:
            for k1 in self.sinks:
                result['sinks'].append(k1.to_map() if k1 else None)

        if self.source is not None:
            result['source'] = self.source.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.status_message is not None:
            result['statusMessage'] = self.status_message

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        self.outputs = []
        if m.get('outputs') is not None:
            for k1 in m.get('outputs'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelinesOutputs()
                self.outputs.append(temp_model.from_map(k1))

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        self.processors = []
        if m.get('processors') is not None:
            for k1 in m.get('processors'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelinesProcessors()
                self.processors.append(temp_model.from_map(k1))

        if m.get('signalType') is not None:
            self.signal_type = m.get('signalType')

        self.sinks = []
        if m.get('sinks') is not None:
            for k1 in m.get('sinks'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelinesSinks()
                self.sinks.append(temp_model.from_map(k1))

        if m.get('source') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesSource()
            self.source = temp_model.from_map(m.get('source'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('statusMessage') is not None:
            self.status_message = m.get('statusMessage')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListDataPipelinesResponseBodyPipelinesSource(DaraModel):
    def __init__(
        self,
        config: main_models.ListDataPipelinesResponseBodyPipelinesSourceConfig = None,
        type: str = None,
    ):
        # The datasource config.
        self.config = config
        # The type of the data source.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesSourceConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDataPipelinesResponseBodyPipelinesSourceConfig(DaraModel):
    def __init__(
        self,
        run_mode: str = None,
        start_from: str = None,
        time_range: main_models.ListDataPipelinesResponseBodyPipelinesSourceConfigTimeRange = None,
    ):
        # The run mode.
        self.run_mode = run_mode
        # The read start point.
        self.start_from = start_from
        # The backfill time range.
        self.time_range = time_range

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.run_mode is not None:
            result['runMode'] = self.run_mode

        if self.start_from is not None:
            result['startFrom'] = self.start_from

        if self.time_range is not None:
            result['timeRange'] = self.time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runMode') is not None:
            self.run_mode = m.get('runMode')

        if m.get('startFrom') is not None:
            self.start_from = m.get('startFrom')

        if m.get('timeRange') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesSourceConfigTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class ListDataPipelinesResponseBodyPipelinesSourceConfigTimeRange(DaraModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        # The start time.
        self.from_ = from_
        # The end time.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

class ListDataPipelinesResponseBodyPipelinesSinks(DaraModel):
    def __init__(
        self,
        datasets: List[str] = None,
        logstore: str = None,
        name: str = None,
        project: str = None,
        type: str = None,
    ):
        # The list of datasets.
        self.datasets = datasets
        # SLS Logstore
        self.logstore = logstore
        # The name of the output destination.
        self.name = name
        # SLS Project
        self.project = project
        # The type of the output destination.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasets is not None:
            result['datasets'] = self.datasets

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.name is not None:
            result['name'] = self.name

        if self.project is not None:
            result['project'] = self.project

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasets') is not None:
            self.datasets = m.get('datasets')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDataPipelinesResponseBodyPipelinesProcessors(DaraModel):
    def __init__(
        self,
        config: main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfig = None,
        name: str = None,
        type: str = None,
    ):
        # The processor configuration.
        self.config = config
        # The name of the processor.
        self.name = name
        # The type of the processor.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDataPipelinesResponseBodyPipelinesProcessorsConfig(DaraModel):
    def __init__(
        self,
        applications: List[str] = None,
        expression: str = None,
        fields: List[str] = None,
        rules: List[main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfigRules] = None,
        script: str = None,
        selector: main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfigSelector = None,
        target: main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfigTarget = None,
    ):
        # The list of applications.
        self.applications = applications
        # The filter expression.
        self.expression = expression
        # The list of fields.
        self.fields = fields
        # The list of masking rules.
        self.rules = rules
        # The SPL script.
        self.script = script
        # The service selector.
        self.selector = selector
        # The processing target.
        self.target = target

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.selector:
            self.selector.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applications is not None:
            result['applications'] = self.applications

        if self.expression is not None:
            result['expression'] = self.expression

        if self.fields is not None:
            result['fields'] = self.fields

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        if self.script is not None:
            result['script'] = self.script

        if self.selector is not None:
            result['selector'] = self.selector.to_map()

        if self.target is not None:
            result['target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applications') is not None:
            self.applications = m.get('applications')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfigRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('script') is not None:
            self.script = m.get('script')

        if m.get('selector') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfigSelector()
            self.selector = temp_model.from_map(m.get('selector'))

        if m.get('target') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesProcessorsConfigTarget()
            self.target = temp_model.from_map(m.get('target'))

        return self

class ListDataPipelinesResponseBodyPipelinesProcessorsConfigTarget(DaraModel):
    def __init__(
        self,
        workspace: str = None,
    ):
        # The target workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListDataPipelinesResponseBodyPipelinesProcessorsConfigSelector(DaraModel):
    def __init__(
        self,
        service_names: List[str] = None,
    ):
        # The list of service names.
        self.service_names = service_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_names is not None:
            result['serviceNames'] = self.service_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')

        return self

class ListDataPipelinesResponseBodyPipelinesProcessorsConfigRules(DaraModel):
    def __init__(
        self,
        keep_prefix: int = None,
        keep_suffix: int = None,
        keys: List[str] = None,
        mask_char: str = None,
        mode: str = None,
        types: List[str] = None,
    ):
        # The length of the prefix to keep.
        self.keep_prefix = keep_prefix
        # The length of the suffix to keep.
        self.keep_suffix = keep_suffix
        # The sensitive keywords.
        self.keys = keys
        # The mask character.
        self.mask_char = mask_char
        # The masking mode.
        self.mode = mode
        # The built-in sensitive types.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_prefix is not None:
            result['keepPrefix'] = self.keep_prefix

        if self.keep_suffix is not None:
            result['keepSuffix'] = self.keep_suffix

        if self.keys is not None:
            result['keys'] = self.keys

        if self.mask_char is not None:
            result['maskChar'] = self.mask_char

        if self.mode is not None:
            result['mode'] = self.mode

        if self.types is not None:
            result['types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keepPrefix') is not None:
            self.keep_prefix = m.get('keepPrefix')

        if m.get('keepSuffix') is not None:
            self.keep_suffix = m.get('keepSuffix')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        if m.get('maskChar') is not None:
            self.mask_char = m.get('maskChar')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

class ListDataPipelinesResponseBodyPipelinesOutputs(DaraModel):
    def __init__(
        self,
        name: str = None,
        processors: List[main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessors] = None,
    ):
        # The output name.
        self.name = name
        # The branch processors.
        self.processors = processors

    def validate(self):
        if self.processors:
            for v1 in self.processors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        result['processors'] = []
        if self.processors is not None:
            for k1 in self.processors:
                result['processors'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        self.processors = []
        if m.get('processors') is not None:
            for k1 in m.get('processors'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessors()
                self.processors.append(temp_model.from_map(k1))

        return self

class ListDataPipelinesResponseBodyPipelinesOutputsProcessors(DaraModel):
    def __init__(
        self,
        config: main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfig = None,
        name: str = None,
        type: str = None,
    ):
        # The processor configuration.
        self.config = config
        # The name of the processor.
        self.name = name
        # The type of the processor.
        self.type = type

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfig(DaraModel):
    def __init__(
        self,
        applications: List[str] = None,
        expression: str = None,
        fields: List[str] = None,
        rules: List[main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigRules] = None,
        script: str = None,
        selector: main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigSelector = None,
        target: main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigTarget = None,
    ):
        # The list of applications.
        self.applications = applications
        # The filter expression.
        self.expression = expression
        # The list of fields.
        self.fields = fields
        # The list of masking rules.
        self.rules = rules
        # The SPL script.
        self.script = script
        # The service selector.
        self.selector = selector
        # The processing target.
        self.target = target

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.selector:
            self.selector.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applications is not None:
            result['applications'] = self.applications

        if self.expression is not None:
            result['expression'] = self.expression

        if self.fields is not None:
            result['fields'] = self.fields

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        if self.script is not None:
            result['script'] = self.script

        if self.selector is not None:
            result['selector'] = self.selector.to_map()

        if self.target is not None:
            result['target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applications') is not None:
            self.applications = m.get('applications')

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('script') is not None:
            self.script = m.get('script')

        if m.get('selector') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigSelector()
            self.selector = temp_model.from_map(m.get('selector'))

        if m.get('target') is not None:
            temp_model = main_models.ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigTarget()
            self.target = temp_model.from_map(m.get('target'))

        return self

class ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigTarget(DaraModel):
    def __init__(
        self,
        workspace: str = None,
    ):
        # The target workspace.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigSelector(DaraModel):
    def __init__(
        self,
        service_names: List[str] = None,
    ):
        # The list of service names.
        self.service_names = service_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_names is not None:
            result['serviceNames'] = self.service_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')

        return self

class ListDataPipelinesResponseBodyPipelinesOutputsProcessorsConfigRules(DaraModel):
    def __init__(
        self,
        keep_prefix: int = None,
        keep_suffix: int = None,
        keys: List[str] = None,
        mask_char: str = None,
        mode: str = None,
        types: List[str] = None,
    ):
        # The length of the prefix to keep.
        self.keep_prefix = keep_prefix
        # The length of the suffix to keep.
        self.keep_suffix = keep_suffix
        # The sensitive keywords.
        self.keys = keys
        # The mask character.
        self.mask_char = mask_char
        # The masking mode.
        self.mode = mode
        # The built-in sensitive types.
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_prefix is not None:
            result['keepPrefix'] = self.keep_prefix

        if self.keep_suffix is not None:
            result['keepSuffix'] = self.keep_suffix

        if self.keys is not None:
            result['keys'] = self.keys

        if self.mask_char is not None:
            result['maskChar'] = self.mask_char

        if self.mode is not None:
            result['mode'] = self.mode

        if self.types is not None:
            result['types'] = self.types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keepPrefix') is not None:
            self.keep_prefix = m.get('keepPrefix')

        if m.get('keepSuffix') is not None:
            self.keep_suffix = m.get('keepSuffix')

        if m.get('keys') is not None:
            self.keys = m.get('keys')

        if m.get('maskChar') is not None:
            self.mask_char = m.get('maskChar')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

