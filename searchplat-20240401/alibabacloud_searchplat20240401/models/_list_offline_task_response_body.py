# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListOfflineTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListOfflineTaskResponseBodyResult] = None,
        total_count: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListOfflineTaskResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOfflineTaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        meta: main_models.ListOfflineTaskResponseBodyResultMeta = None,
        processors: List[main_models.ListOfflineTaskResponseBodyResultProcessors] = None,
        sink: List[main_models.ListOfflineTaskResponseBodyResultSink] = None,
        source: List[main_models.ListOfflineTaskResponseBodyResultSource] = None,
        status: main_models.ListOfflineTaskResponseBodyResultStatus = None,
    ):
        # The task metadata.
        self.meta = meta
        # The processing pipeline operators.
        self.processors = processors
        # The data sink information.
        self.sink = sink
        # The data source information.
        self.source = source
        # The task status.
        self.status = status

    def validate(self):
        if self.meta:
            self.meta.validate()
        if self.processors:
            for v1 in self.processors:
                 if v1:
                    v1.validate()
        if self.sink:
            for v1 in self.sink:
                 if v1:
                    v1.validate()
        if self.source:
            for v1 in self.source:
                 if v1:
                    v1.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        result['Processors'] = []
        if self.processors is not None:
            for k1 in self.processors:
                result['Processors'].append(k1.to_map() if k1 else None)

        result['Sink'] = []
        if self.sink is not None:
            for k1 in self.sink:
                result['Sink'].append(k1.to_map() if k1 else None)

        result['Source'] = []
        if self.source is not None:
            for k1 in self.source:
                result['Source'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = main_models.ListOfflineTaskResponseBodyResultMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        self.processors = []
        if m.get('Processors') is not None:
            for k1 in m.get('Processors'):
                temp_model = main_models.ListOfflineTaskResponseBodyResultProcessors()
                self.processors.append(temp_model.from_map(k1))

        self.sink = []
        if m.get('Sink') is not None:
            for k1 in m.get('Sink'):
                temp_model = main_models.ListOfflineTaskResponseBodyResultSink()
                self.sink.append(temp_model.from_map(k1))

        self.source = []
        if m.get('Source') is not None:
            for k1 in m.get('Source'):
                temp_model = main_models.ListOfflineTaskResponseBodyResultSource()
                self.source.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            temp_model = main_models.ListOfflineTaskResponseBodyResultStatus()
            self.status = temp_model.from_map(m.get('Status'))

        return self

class ListOfflineTaskResponseBodyResultStatus(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        metric_data: Dict[str, str] = None,
        status: str = None,
        update_time: int = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The monitoring information.
        self.metric_data = metric_data
        # The task status.
        self.status = status
        # The time when the task was last modified.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.metric_data is not None:
            result['MetricData'] = self.metric_data

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('MetricData') is not None:
            self.metric_data = m.get('MetricData')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListOfflineTaskResponseBodyResultSource(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        primary_key: str = None,
        schema: List[Dict[str, str]] = None,
        type: str = None,
    ):
        # The data source name.
        self.name = name
        # The data source configuration parameters.
        self.parameters = parameters
        # The primary key field of the data source.
        self.primary_key = primary_key
        # The data source schema.
        self.schema = schema
        # The data source type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListOfflineTaskResponseBodyResultSink(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        primary_key: str = None,
        schema: List[Dict[str, str]] = None,
        type: str = None,
    ):
        # The data sink name.
        self.name = name
        # The data sink configuration parameters, which are determined by the type.
        self.parameters = parameters
        # The primary key field of the data sink.
        self.primary_key = primary_key
        # The data sink schema.
        self.schema = schema
        # The data sink type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListOfflineTaskResponseBodyResultProcessors(DaraModel):
    def __init__(
        self,
        input: Dict[str, str] = None,
        name: str = None,
        output: Dict[str, str] = None,
        parameters: Dict[str, str] = None,
        type: str = None,
    ):
        # The input parameters.
        self.input = input
        # The name.
        self.name = name
        # The output parameters.
        self.output = output
        # The processor parameters.
        self.parameters = parameters
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListOfflineTaskResponseBodyResultMeta(DaraModel):
    def __init__(
        self,
        labels: List[str] = None,
        region_id: str = None,
        task_name: str = None,
        workspace_id: str = None,
    ):
        # The list of labels.
        self.labels = labels
        # The region ID of the task.
        self.region_id = region_id
        # The task name.
        self.task_name = task_name
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

