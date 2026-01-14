# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class ExecuteMigrationOperationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ExecuteMigrationOperationResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ExecuteMigrationOperationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ExecuteMigrationOperationResponseBodyData(DaraModel):
    def __init__(
        self,
        business_status: str = None,
        create_time: str = None,
        migration_id: int = None,
        operation_id: int = None,
        operation_key: str = None,
        operation_param: main_models.ExecuteMigrationOperationResponseBodyDataOperationParam = None,
        operation_result: main_models.ExecuteMigrationOperationResponseBodyDataOperationResult = None,
        operation_status: str = None,
        operation_type: str = None,
        stage_type: str = None,
        update_time: str = None,
    ):
        self.business_status = business_status
        self.create_time = create_time
        self.migration_id = migration_id
        self.operation_id = operation_id
        self.operation_key = operation_key
        self.operation_param = operation_param
        self.operation_result = operation_result
        self.operation_status = operation_status
        self.operation_type = operation_type
        self.stage_type = stage_type
        self.update_time = update_time

    def validate(self):
        if self.operation_param:
            self.operation_param.validate()
        if self.operation_result:
            self.operation_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_status is not None:
            result['businessStatus'] = self.business_status

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.migration_id is not None:
            result['migrationId'] = self.migration_id

        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.operation_key is not None:
            result['operationKey'] = self.operation_key

        if self.operation_param is not None:
            result['operationParam'] = self.operation_param.to_map()

        if self.operation_result is not None:
            result['operationResult'] = self.operation_result.to_map()

        if self.operation_status is not None:
            result['operationStatus'] = self.operation_status

        if self.operation_type is not None:
            result['operationType'] = self.operation_type

        if self.stage_type is not None:
            result['stageType'] = self.stage_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('businessStatus') is not None:
            self.business_status = m.get('businessStatus')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('migrationId') is not None:
            self.migration_id = m.get('migrationId')

        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('operationKey') is not None:
            self.operation_key = m.get('operationKey')

        if m.get('operationParam') is not None:
            temp_model = main_models.ExecuteMigrationOperationResponseBodyDataOperationParam()
            self.operation_param = temp_model.from_map(m.get('operationParam'))

        if m.get('operationResult') is not None:
            temp_model = main_models.ExecuteMigrationOperationResponseBodyDataOperationResult()
            self.operation_result = temp_model.from_map(m.get('operationResult'))

        if m.get('operationStatus') is not None:
            self.operation_status = m.get('operationStatus')

        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')

        if m.get('stageType') is not None:
            self.stage_type = m.get('stageType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ExecuteMigrationOperationResponseBodyDataOperationResult(DaraModel):
    def __init__(
        self,
        result_data: Any = None,
    ):
        self.result_data = result_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_data is not None:
            result['resultData'] = self.result_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resultData') is not None:
            self.result_data = m.get('resultData')

        return self

class ExecuteMigrationOperationResponseBodyDataOperationParam(DaraModel):
    def __init__(
        self,
        param_data: Any = None,
    ):
        self.param_data = param_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_data is not None:
            result['paramData'] = self.param_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('paramData') is not None:
            self.param_data = m.get('paramData')

        return self

