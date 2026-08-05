# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class StartOfflineTaskResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.StartOfflineTaskResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.StartOfflineTaskResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class StartOfflineTaskResponseBodyResult(DaraModel):
    def __init__(
        self,
        meta: main_models.StartOfflineTaskResponseBodyResultMeta = None,
        parameters: Dict[str, Any] = None,
        processors: List[main_models.StartOfflineTaskResponseBodyResultProcessors] = None,
        sink: List[main_models.StartOfflineTaskResponseBodyResultSink] = None,
        source: List[main_models.StartOfflineTaskResponseBodyResultSource] = None,
        status: main_models.StartOfflineTaskResponseBodyResultStatus = None,
    ):
        # The metadata.
        self.meta = meta
        # The task processing parameters.
        self.parameters = parameters
        # The processing operators.
        self.processors = processors
        # The data sink information.
        self.sink = sink
        # The source.
        self.source = source
        # The task status. Valid values:
        # - PENDING: In progress.
        # - SUCCESS: Parsing succeeded.
        # - FAILED: Parsing failed.
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meta') is not None:
            temp_model = main_models.StartOfflineTaskResponseBodyResultMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        self.processors = []
        if m.get('processors') is not None:
            for k1 in m.get('processors'):
                temp_model = main_models.StartOfflineTaskResponseBodyResultProcessors()
                self.processors.append(temp_model.from_map(k1))

        self.sink = []
        if m.get('sink') is not None:
            for k1 in m.get('sink'):
                temp_model = main_models.StartOfflineTaskResponseBodyResultSink()
                self.sink.append(temp_model.from_map(k1))

        self.source = []
        if m.get('source') is not None:
            for k1 in m.get('source'):
                temp_model = main_models.StartOfflineTaskResponseBodyResultSource()
                self.source.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            temp_model = main_models.StartOfflineTaskResponseBodyResultStatus()
            self.status = temp_model.from_map(m.get('status'))

        return self

class StartOfflineTaskResponseBodyResultStatus(DaraModel):
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
        # The request status.
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

class StartOfflineTaskResponseBodyResultSource(DaraModel):
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
        # The datasource config parameters, which are determined by the type.
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

class StartOfflineTaskResponseBodyResultSink(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameters: Dict[str, str] = None,
        primary_key: str = None,
        schema: List[Dict[str, str]] = None,
        type: str = None,
    ):
        # The task name.
        self.name = name
        # The data sink configuration parameters, which are determined by the type.
        self.parameters = parameters
        # The primary key field of the data sink.
        self.primary_key = primary_key
        # The data sink schema.
        self.schema = schema
        # The type. Valid values:
        # - standard.
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

class StartOfflineTaskResponseBodyResultProcessors(DaraModel):
    def __init__(
        self,
        input: Dict[str, Any] = None,
        name: str = None,
        parameters: Dict[str, Any] = None,
        type: str = None,
    ):
        # The input parameters.
        self.input = input
        # The data source name.
        self.name = name
        # The processor processing parameters.
        self.parameters = parameters
        # The data sink type.
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

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class StartOfflineTaskResponseBodyResultMeta(DaraModel):
    def __init__(
        self,
        compute_resource: str = None,
        task_name: str = None,
    ):
        # The billing specification.
        self.compute_resource = compute_resource
        # The task name.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_resource is not None:
            result['computeResource'] = self.compute_resource

        if self.task_name is not None:
            result['taskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeResource') is not None:
            self.compute_resource = m.get('computeResource')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        return self

