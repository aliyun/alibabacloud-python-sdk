# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class ListFunctionInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_code: int = None,
        latency: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.ListFunctionInstancesResponseBodyResult] = None,
        status: str = None,
        total_count: int = None,
    ):
        # The error code.
        self.code = code
        # The HTTP status code.
        self.http_code = http_code
        # The elapsed time.
        self.latency = latency
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned results.
        self.result = result
        # The request status.
        self.status = status
        # The total number of entries.
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

        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.total_count is not None:
            result['totalCount'] = self.total_count

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

        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.ListFunctionInstancesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListFunctionInstancesResponseBodyResult(DaraModel):
    def __init__(
        self,
        belongs: main_models.ListFunctionInstancesResponseBodyResultBelongs = None,
        create_parameters: List[main_models.ListFunctionInstancesResponseBodyResultCreateParameters] = None,
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
        usage_parameters: List[Dict[str, Any]] = None,
        version_id: int = None,
    ):
        # The ownership information.
        self.belongs = belongs
        # The creation parameter body.
        self.create_parameters = create_parameters
        # The creation time.
        self.create_time = create_time
        # The cron expression for the timed scheduling node.
        self.cron = cron
        # The description.
        self.description = description
        # The extended information.
        self.extend_info = extend_info
        # The configuration item.
        self.function_name = function_name
        # The configuration type.
        self.function_type = function_type
        # The configuration name.
        self.instance_name = instance_name
        # The model type.
        self.model_type = model_type
        # The instance source. Valid values:
        # - builtin: system instance
        # - user: user instance (default)
        # - all: all instances.
        self.source = source
        # The status. Valid values:
        # 
        # - available
        # - unavailable.
        self.status = status
        # usageParameters
        self.usage_parameters = usage_parameters
        # The version ID.
        self.version_id = version_id

    def validate(self):
        if self.belongs:
            self.belongs.validate()
        if self.create_parameters:
            for v1 in self.create_parameters:
                 if v1:
                    v1.validate()

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

        if self.usage_parameters is not None:
            result['usageParameters'] = self.usage_parameters

        if self.version_id is not None:
            result['versionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('belongs') is not None:
            temp_model = main_models.ListFunctionInstancesResponseBodyResultBelongs()
            self.belongs = temp_model.from_map(m.get('belongs'))

        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k1 in m.get('createParameters'):
                temp_model = main_models.ListFunctionInstancesResponseBodyResultCreateParameters()
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

        if m.get('usageParameters') is not None:
            self.usage_parameters = m.get('usageParameters')

        if m.get('versionId') is not None:
            self.version_id = m.get('versionId')

        return self

class ListFunctionInstancesResponseBodyResultCreateParameters(DaraModel):
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

class ListFunctionInstancesResponseBodyResultBelongs(DaraModel):
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
        # The language. Valid values:
        # 
        # - zh_CN: Chinese (default)
        # - en_US: English.
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

