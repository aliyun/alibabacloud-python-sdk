# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class GetFunctionInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetFunctionInstanceResponseBodyResult = None,
        status: str = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The time consumed.
        self.latency = latency
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result
        # The request status.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.latency is not None:
            result['latency'] = self.latency

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.GetFunctionInstanceResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetFunctionInstanceResponseBodyResult(DaraModel):
    def __init__(
        self,
        belongs: main_models.GetFunctionInstanceResponseBodyResultBelongs = None,
        create_parameters: List[main_models.GetFunctionInstanceResponseBodyResultCreateParameters] = None,
        create_time: int = None,
        cron: str = None,
        description: str = None,
        extend_info: str = None,
        function_name: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
        source: str = None,
        status: str = None,
        task: main_models.GetFunctionInstanceResponseBodyResultTask = None,
        version_id: int = None,
    ):
        # The ownership information.
        self.belongs = belongs
        # The specific configuration items.
        self.create_parameters = create_parameters
        # The creation time.
        self.create_time = create_time
        # The cron expression for the timed scheduling task.
        self.cron = cron
        # The description.
        self.description = description
        # The extended information.
        self.extend_info = extend_info
        # The configuration type. Valid values:
        # - nl2sql
        # - embedding-tuning
        # - deployment
        # - notebook.
        self.function_name = function_name
        # The configuration type. PAAS (default): requires training before use.
        self.function_type = function_type
        # The configuration name.
        self.instance_name = instance_name
        # The model type. The valid values vary based on the configuration type (functionName):
        # 
        # - ops-query-analyze-nl2sql-001 (nl2sql)
        # - ops-embedding-dim-reduction-001 (embedding-tuning)
        # - native (deployment)
        # - dsw (notebook).
        self.model_type = model_type
        # The source.
        self.source = source
        # The status. Valid values:
        # - available
        # - unavailable.
        self.status = status
        # The task information.
        self.task = task
        # The training version ID.
        self.version_id = version_id

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for v1 in self.create_parameters:
                 if v1:
                    v1.validate()
        if self.task:
            self.task.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.belongs is not None:
            result['belongs'] = self.belongs.to_map()

        result['createParameters'] = []
        if self.create_parameters is not None:
            for k1 in self.create_parameters:
                result['createParameters'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.cron is not None:
            result['cron'] = self.cron

        if self.description is not None:
            result['description'] = self.description

        if self.extend_info is not None:
            result['extendInfo'] = self.extend_info

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.function_type is not None:
            result['functionType'] = self.function_type

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        if self.task is not None:
            result['task'] = self.task.to_map()

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('belongs') is not None:
            temp_model = main_models.GetFunctionInstanceResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m.get('belongs'))

        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k1 in m.get('createParameters'):
                temp_model = main_models.GetFunctionInstanceResponseBodyResultCreateParameters()
                self.create_parameters.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('extendInfo') is not None:
            self.extend_info = m.get('extendInfo')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task') is not None:
            temp_model = main_models.GetFunctionInstanceResponseBodyResultTask()
            self.task = temp_model.from_map(m.get('task'))

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

class GetFunctionInstanceResponseBodyResultTask(DaraModel):
    def __init__(
        self,
        dag_status: str = None,
        last_run_time: int = None,
    ):
        # The task status. Valid values:
        # - success: Succeeded.
        # - failed: Failed.
        # - untrained: Pending training.
        # - pending: Scheduling.
        # - running: Training in progress.
        self.dag_status = dag_status
        # The last training time.
        self.last_run_time = last_run_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_status is not None:
            result['dagStatus'] = self.dag_status

        if self.last_run_time is not None:
            result['lastRunTime'] = self.last_run_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dagStatus') is not None:
            self.dag_status = m.get('dagStatus')

        if m.get('lastRunTime') is not None:
            self.last_run_time = m.get('lastRunTime')

        return self

class GetFunctionInstanceResponseBodyResultCreateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class GetFunctionInstanceResponseBodyResultBelongs(DaraModel):
    def __init__(
        self,
        category: str = None,
        domain: str = None,
        language: str = None,
    ):
        # The category.
        self.category = category
        # The industry type.
        self.domain = domain
        # The language.
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.domain is not None:
            result['domain'] = self.domain

        if self.language is not None:
            result['language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('language') is not None:
            self.language = m.get('language')

        return self

