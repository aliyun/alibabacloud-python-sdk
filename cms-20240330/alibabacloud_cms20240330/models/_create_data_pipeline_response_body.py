# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateDataPipelineResponseBody(DaraModel):
    def __init__(
        self,
        pipeline: main_models.CreateDataPipelineResponseBodyPipeline = None,
        request_id: str = None,
    ):
        # The data pipeline.
        self.pipeline = pipeline
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline is not None:
            result['pipeline'] = self.pipeline.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pipeline') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m.get('pipeline'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateDataPipelineResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        kind: str = None,
        outputs: List[main_models.CreateDataPipelineResponseBodyPipelineOutputs] = None,
        pipeline_name: str = None,
        processors: List[main_models.CreateDataPipelineResponseBodyPipelineProcessors] = None,
        signal_type: str = None,
        sinks: List[main_models.CreateDataPipelineResponseBodyPipelineSinks] = None,
        source: main_models.CreateDataPipelineResponseBodyPipelineSource = None,
        status: str = None,
        status_message: str = None,
        update_time: str = None,
        version: int = None,
    ):
        # The creation time.
        # 
        # This parameter is required.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.create_time = create_time
        # The pipeline description.
        self.description = description
        # The pipeline type.
        # 
        # This parameter is required.
        self.kind = kind
        # The named outputs.
        # 
        # This parameter is required.
        self.outputs = outputs
        # The pipeline name.
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
        # The update time.
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
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputs()
                self.outputs.append(temp_model.from_map(k1))

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        self.processors = []
        if m.get('processors') is not None:
            for k1 in m.get('processors'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessors()
                self.processors.append(temp_model.from_map(k1))

        if m.get('signalType') is not None:
            self.signal_type = m.get('signalType')

        self.sinks = []
        if m.get('sinks') is not None:
            for k1 in m.get('sinks'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineSinks()
                self.sinks.append(temp_model.from_map(k1))

        if m.get('source') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineSource()
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

class CreateDataPipelineResponseBodyPipelineSource(DaraModel):
    def __init__(
        self,
        config: main_models.CreateDataPipelineResponseBodyPipelineSourceConfig = None,
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
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineSourceConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateDataPipelineResponseBodyPipelineSourceConfig(DaraModel):
    def __init__(
        self,
        run_mode: str = None,
        start_from: str = None,
        time_range: main_models.CreateDataPipelineResponseBodyPipelineSourceConfigTimeRange = None,
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
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineSourceConfigTimeRange()
            self.time_range = temp_model.from_map(m.get('timeRange'))

        return self

class CreateDataPipelineResponseBodyPipelineSourceConfigTimeRange(DaraModel):
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

class CreateDataPipelineResponseBodyPipelineSinks(DaraModel):
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

class CreateDataPipelineResponseBodyPipelineProcessors(DaraModel):
    def __init__(
        self,
        config: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfig = None,
        name: str = None,
        type: str = None,
    ):
        # The processor configuration.
        self.config = config
        # The processor name.
        self.name = name
        # The processor type.
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
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfig(DaraModel):
    def __init__(
        self,
        applications: List[str] = None,
        assignments: List[main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigAssignments] = None,
        expression: str = None,
        fields: List[str] = None,
        parameters: Dict[str, Any] = None,
        projections: List[main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigProjections] = None,
        rules: List[main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigRules] = None,
        scope: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScope = None,
        script: str = None,
        selector: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigSelector = None,
        target: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigTarget = None,
    ):
        # The list of applications.
        self.applications = applications
        # The list of field assignments.
        self.assignments = assignments
        # The filter expression.
        self.expression = expression
        # The list of fields.
        self.fields = fields
        # The extended parameters.
        self.parameters = parameters
        # The list of field projections.
        self.projections = projections
        # The list of masking rules.
        self.rules = rules
        # The scope in which the pipeline processing processor takes effect.
        self.scope = scope
        # The SPL script.
        self.script = script
        # The service selector.
        self.selector = selector
        # The processing target.
        self.target = target

    def validate(self):
        if self.assignments:
            for v1 in self.assignments:
                 if v1:
                    v1.validate()
        if self.projections:
            for v1 in self.projections:
                 if v1:
                    v1.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.scope:
            self.scope.validate()
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

        result['assignments'] = []
        if self.assignments is not None:
            for k1 in self.assignments:
                result['assignments'].append(k1.to_map() if k1 else None)

        if self.expression is not None:
            result['expression'] = self.expression

        if self.fields is not None:
            result['fields'] = self.fields

        if self.parameters is not None:
            result['parameters'] = self.parameters

        result['projections'] = []
        if self.projections is not None:
            for k1 in self.projections:
                result['projections'].append(k1.to_map() if k1 else None)

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

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

        self.assignments = []
        if m.get('assignments') is not None:
            for k1 in m.get('assignments'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigAssignments()
                self.assignments.append(temp_model.from_map(k1))

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        self.projections = []
        if m.get('projections') is not None:
            for k1 in m.get('projections'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigProjections()
                self.projections.append(temp_model.from_map(k1))

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('scope') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('script') is not None:
            self.script = m.get('script')

        if m.get('selector') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigSelector()
            self.selector = temp_model.from_map(m.get('selector'))

        if m.get('target') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigTarget()
            self.target = temp_model.from_map(m.get('target'))

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigTarget(DaraModel):
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

class CreateDataPipelineResponseBodyPipelineProcessorsConfigSelector(DaraModel):
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

class CreateDataPipelineResponseBodyPipelineProcessorsConfigScope(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeConditions] = None,
        metric_name: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeMetricName = None,
        service_name: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeServiceName = None,
    ):
        # The additional field conditions.
        self.conditions = conditions
        # The metric name scope.
        self.metric_name = metric_name
        # The service name scope.
        self.service_name = service_name

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.metric_name:
            self.metric_name.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['metricName'] = self.metric_name.to_map()

        if self.service_name is not None:
            result['serviceName'] = self.service_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('metricName') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeMetricName()
            self.metric_name = temp_model.from_map(m.get('metricName'))

        if m.get('serviceName') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeServiceName()
            self.service_name = temp_model.from_map(m.get('serviceName'))

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeServiceName(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The matching method.
        self.match_type = match_type
        # The match values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeMetricName(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The matching method.
        self.match_type = match_type
        # The metric names.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeConditions(DaraModel):
    def __init__(
        self,
        field: main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeConditionsField = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The field reference.
        self.field = field
        # The matching method.
        self.match_type = match_type
        # The match values.
        self.values = values

    def validate(self):
        if self.field:
            self.field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field.to_map()

        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeConditionsField()
            self.field = temp_model.from_map(m.get('field'))

        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigScopeConditionsField(DaraModel):
    def __init__(
        self,
        container: str = None,
        kind: str = None,
        name: str = None,
        path: List[str] = None,
    ):
        # The JSON object container.
        self.container = container
        # The reference data type.
        self.kind = kind
        # The field or dimension name.
        self.name = name
        # The JSON literal key path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container is not None:
            result['container'] = self.container

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('container') is not None:
            self.container = m.get('container')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigRules(DaraModel):
    def __init__(
        self,
        keep_prefix: int = None,
        keep_suffix: int = None,
        keys: List[str] = None,
        mask_char: str = None,
        mode: str = None,
        types: List[str] = None,
    ):
        # The length of the prefix to retain.
        self.keep_prefix = keep_prefix
        # The length of the suffix to retain.
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

class CreateDataPipelineResponseBodyPipelineProcessorsConfigProjections(DaraModel):
    def __init__(
        self,
        source: str = None,
        target: str = None,
    ):
        # The source field.
        self.source = source
        # The target field.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        return self

class CreateDataPipelineResponseBodyPipelineProcessorsConfigAssignments(DaraModel):
    def __init__(
        self,
        expression: str = None,
        field: str = None,
    ):
        # The assignment expression.
        self.expression = expression
        # The output field.
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['expression'] = self.expression

        if self.field is not None:
            result['field'] = self.field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('field') is not None:
            self.field = m.get('field')

        return self

class CreateDataPipelineResponseBodyPipelineOutputs(DaraModel):
    def __init__(
        self,
        name: str = None,
        processors: List[main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessors] = None,
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
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessors()
                self.processors.append(temp_model.from_map(k1))

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessors(DaraModel):
    def __init__(
        self,
        config: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfig = None,
        name: str = None,
        type: str = None,
    ):
        # The processor configuration.
        self.config = config
        # The processor name.
        self.name = name
        # The processor type.
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
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfig(DaraModel):
    def __init__(
        self,
        applications: List[str] = None,
        assignments: List[main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigAssignments] = None,
        expression: str = None,
        fields: List[str] = None,
        parameters: Dict[str, Any] = None,
        projections: List[main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigProjections] = None,
        rules: List[main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigRules] = None,
        scope: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScope = None,
        script: str = None,
        selector: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigSelector = None,
        target: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigTarget = None,
    ):
        # The list of applications.
        self.applications = applications
        # The list of field assignments.
        self.assignments = assignments
        # The filter expression.
        self.expression = expression
        # The list of fields.
        self.fields = fields
        # The extended parameters.
        self.parameters = parameters
        # The list of field projections.
        self.projections = projections
        # The list of masking rules.
        self.rules = rules
        # The scope in which the pipeline processing processor takes effect.
        self.scope = scope
        # The SPL script.
        self.script = script
        # The service selector.
        self.selector = selector
        # The processing target.
        self.target = target

    def validate(self):
        if self.assignments:
            for v1 in self.assignments:
                 if v1:
                    v1.validate()
        if self.projections:
            for v1 in self.projections:
                 if v1:
                    v1.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.scope:
            self.scope.validate()
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

        result['assignments'] = []
        if self.assignments is not None:
            for k1 in self.assignments:
                result['assignments'].append(k1.to_map() if k1 else None)

        if self.expression is not None:
            result['expression'] = self.expression

        if self.fields is not None:
            result['fields'] = self.fields

        if self.parameters is not None:
            result['parameters'] = self.parameters

        result['projections'] = []
        if self.projections is not None:
            for k1 in self.projections:
                result['projections'].append(k1.to_map() if k1 else None)

        result['rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['rules'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

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

        self.assignments = []
        if m.get('assignments') is not None:
            for k1 in m.get('assignments'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigAssignments()
                self.assignments.append(temp_model.from_map(k1))

        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        self.projections = []
        if m.get('projections') is not None:
            for k1 in m.get('projections'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigProjections()
                self.projections.append(temp_model.from_map(k1))

        self.rules = []
        if m.get('rules') is not None:
            for k1 in m.get('rules'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('scope') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('script') is not None:
            self.script = m.get('script')

        if m.get('selector') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigSelector()
            self.selector = temp_model.from_map(m.get('selector'))

        if m.get('target') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigTarget()
            self.target = temp_model.from_map(m.get('target'))

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigTarget(DaraModel):
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

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigSelector(DaraModel):
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

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScope(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeConditions] = None,
        metric_name: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeMetricName = None,
        service_name: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeServiceName = None,
    ):
        # The additional field conditions.
        self.conditions = conditions
        # The metric name scope.
        self.metric_name = metric_name
        # The service name scope.
        self.service_name = service_name

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.metric_name:
            self.metric_name.validate()
        if self.service_name:
            self.service_name.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['metricName'] = self.metric_name.to_map()

        if self.service_name is not None:
            result['serviceName'] = self.service_name.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('metricName') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeMetricName()
            self.metric_name = temp_model.from_map(m.get('metricName'))

        if m.get('serviceName') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeServiceName()
            self.service_name = temp_model.from_map(m.get('serviceName'))

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeServiceName(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The matching method.
        self.match_type = match_type
        # The match values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeMetricName(DaraModel):
    def __init__(
        self,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The matching method.
        self.match_type = match_type
        # The metric names.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeConditions(DaraModel):
    def __init__(
        self,
        field: main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeConditionsField = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The field reference.
        self.field = field
        # The matching method.
        self.match_type = match_type
        # The match values.
        self.values = values

    def validate(self):
        if self.field:
            self.field.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field.to_map()

        if self.match_type is not None:
            result['matchType'] = self.match_type

        if self.values is not None:
            result['values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            temp_model = main_models.CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeConditionsField()
            self.field = temp_model.from_map(m.get('field'))

        if m.get('matchType') is not None:
            self.match_type = m.get('matchType')

        if m.get('values') is not None:
            self.values = m.get('values')

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigScopeConditionsField(DaraModel):
    def __init__(
        self,
        container: str = None,
        kind: str = None,
        name: str = None,
        path: List[str] = None,
    ):
        # The JSON object container.
        self.container = container
        # The reference data type.
        self.kind = kind
        # The field or dimension name.
        self.name = name
        # The JSON literal key path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container is not None:
            result['container'] = self.container

        if self.kind is not None:
            result['kind'] = self.kind

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('container') is not None:
            self.container = m.get('container')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigRules(DaraModel):
    def __init__(
        self,
        keep_prefix: int = None,
        keep_suffix: int = None,
        keys: List[str] = None,
        mask_char: str = None,
        mode: str = None,
        types: List[str] = None,
    ):
        # The length of the prefix to retain.
        self.keep_prefix = keep_prefix
        # The length of the suffix to retain.
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

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigProjections(DaraModel):
    def __init__(
        self,
        source: str = None,
        target: str = None,
    ):
        # The source field.
        self.source = source
        # The target field.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        return self

class CreateDataPipelineResponseBodyPipelineOutputsProcessorsConfigAssignments(DaraModel):
    def __init__(
        self,
        expression: str = None,
        field: str = None,
    ):
        # The assignment expression.
        self.expression = expression
        # The output field.
        self.field = field

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expression is not None:
            result['expression'] = self.expression

        if self.field is not None:
            result['field'] = self.field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')

        if m.get('field') is not None:
            self.field = m.get('field')

        return self

