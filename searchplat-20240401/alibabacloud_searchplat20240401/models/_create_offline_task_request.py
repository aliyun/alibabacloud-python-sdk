# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class CreateOfflineTaskRequest(DaraModel):
    def __init__(
        self,
        meta: main_models.CreateOfflineTaskRequestMeta = None,
        parameters: Dict[str, Any] = None,
        processors: List[main_models.CreateOfflineTaskRequestProcessors] = None,
        sink: List[main_models.CreateOfflineTaskRequestSink] = None,
        source: List[main_models.CreateOfflineTaskRequestSource] = None,
        status: main_models.CreateOfflineTaskRequestStatus = None,
        draft: bool = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        # The task metadata.
        self.meta = meta
        # The task processing parameters.
        self.parameters = parameters
        # The processing pipeline operators.
        self.processors = processors
        # The data sink information.
        self.sink = sink
        # The data source information.
        self.source = source
        # The task status.
        self.status = status
        # Specifies whether the task is a draft.
        self.draft = draft
        # Specifies whether to validate the parameters without creating the task.
        self.dry_run = dry_run
        # The region ID.
        self.region_id = region_id

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
            result['meta'] = self.meta.to_map()

        if self.parameters is not None:
            result['parameters'] = self.parameters

        result['processors'] = []
        if self.processors is not None:
            for k1 in self.processors:
                result['processors'].append(k1.to_map() if k1 else None)

        result['sink'] = []
        if self.sink is not None:
            for k1 in self.sink:
                result['sink'].append(k1.to_map() if k1 else None)

        result['source'] = []
        if self.source is not None:
            for k1 in self.source:
                result['source'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.draft is not None:
            result['draft'] = self.draft

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meta') is not None:
            temp_model = main_models.CreateOfflineTaskRequestMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        self.processors = []
        if m.get('processors') is not None:
            for k1 in m.get('processors'):
                temp_model = main_models.CreateOfflineTaskRequestProcessors()
                self.processors.append(temp_model.from_map(k1))

        self.sink = []
        if m.get('sink') is not None:
            for k1 in m.get('sink'):
                temp_model = main_models.CreateOfflineTaskRequestSink()
                self.sink.append(temp_model.from_map(k1))

        self.source = []
        if m.get('source') is not None:
            for k1 in m.get('source'):
                temp_model = main_models.CreateOfflineTaskRequestSource()
                self.source.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            temp_model = main_models.CreateOfflineTaskRequestStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('draft') is not None:
            self.draft = m.get('draft')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class CreateOfflineTaskRequestStatus(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        delete_time: int = None,
        error_message: str = None,
        status: str = None,
    ):
        # The task start time.
        self.create_time = create_time
        # The task stop time.
        self.delete_time = delete_time
        # The error message.
        self.error_message = error_message
        # The task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class CreateOfflineTaskRequestSource(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        primary_key: str = None,
        schema: List[Dict[str, str]] = None,
        type: str = None,
    ):
        # **The data source name.**.
        self.name = name
        # **The datasource config parameters, which are determined by the type.**.
        self.parameters = parameters
        # The primary key field of the data source.
        self.primary_key = primary_key
        # **The data source schema.**.
        self.schema = schema
        # **The data source type.**.
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

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key

        if self.schema is not None:
            result['schema'] = self.schema

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateOfflineTaskRequestSink(DaraModel):
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
            result['name'] = self.name

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key

        if self.schema is not None:
            result['schema'] = self.schema

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('primaryKey') is not None:
            self.primary_key = m.get('primaryKey')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateOfflineTaskRequestProcessors(DaraModel):
    def __init__(
        self,
        input: Dict[str, Any] = None,
        name: str = None,
        output: Dict[str, Any] = None,
        parameters: Dict[str, Any] = None,
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
            result['input'] = self.input

        if self.name is not None:
            result['name'] = self.name

        if self.output is not None:
            result['output'] = self.output

        if self.parameters is not None:
            result['parameters'] = self.parameters

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('input') is not None:
            self.input = m.get('input')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('output') is not None:
            self.output = m.get('output')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateOfflineTaskRequestMeta(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        compute_resource: str = None,
        labels: List[str] = None,
        region_id: str = None,
        task_name: str = None,
    ):
        # The access credential.
        self.api_key = api_key
        # The billing specification.
        self.compute_resource = compute_resource
        # The list of labels.
        self.labels = labels
        # The region ID.
        self.region_id = region_id
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.labels is not None:
            result['labels'] = self.labels

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

