# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetBatchExportTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBatchExportTaskResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetBatchExportTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetBatchExportTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_message: str = None,
        processed_count: int = None,
        result: main_models.GetBatchExportTaskResponseBodyDataResult = None,
        status: str = None,
        task_id: str = None,
        task_type: str = None,
        total_count: int = None,
    ):
        self.create_time = create_time
        self.error_message = error_message
        self.processed_count = processed_count
        self.result = result
        self.status = status
        self.task_id = task_id
        self.task_type = task_type
        self.total_count = total_count

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.processed_count is not None:
            result['processedCount'] = self.processed_count

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_type is not None:
            result['taskType'] = self.task_type

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('processedCount') is not None:
            self.processed_count = m.get('processedCount')

        if m.get('result') is not None:
            temp_model = main_models.GetBatchExportTaskResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetBatchExportTaskResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        api_type: str = None,
        failure_items: List[main_models.GetBatchExportTaskResponseBodyDataResultFailureItems] = None,
        gateway_id: str = None,
        spec_content_base_64: str = None,
        success_items: List[main_models.GetBatchExportTaskResponseBodyDataResultSuccessItems] = None,
    ):
        self.api_type = api_type
        self.failure_items = failure_items
        self.gateway_id = gateway_id
        self.spec_content_base_64 = spec_content_base_64
        self.success_items = success_items

    def validate(self):
        if self.failure_items:
            for v1 in self.failure_items:
                 if v1:
                    v1.validate()
        if self.success_items:
            for v1 in self.success_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_type is not None:
            result['apiType'] = self.api_type

        result['failureItems'] = []
        if self.failure_items is not None:
            for k1 in self.failure_items:
                result['failureItems'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.spec_content_base_64 is not None:
            result['specContentBase64'] = self.spec_content_base_64

        result['successItems'] = []
        if self.success_items is not None:
            for k1 in self.success_items:
                result['successItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        self.failure_items = []
        if m.get('failureItems') is not None:
            for k1 in m.get('failureItems'):
                temp_model = main_models.GetBatchExportTaskResponseBodyDataResultFailureItems()
                self.failure_items.append(temp_model.from_map(k1))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('specContentBase64') is not None:
            self.spec_content_base_64 = m.get('specContentBase64')

        self.success_items = []
        if m.get('successItems') is not None:
            for k1 in m.get('successItems'):
                temp_model = main_models.GetBatchExportTaskResponseBodyDataResultSuccessItems()
                self.success_items.append(temp_model.from_map(k1))

        return self

class GetBatchExportTaskResponseBodyDataResultSuccessItems(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        error_message: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        return self

class GetBatchExportTaskResponseBodyDataResultFailureItems(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        error_message: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['apiId'] = self.api_id

        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        return self

