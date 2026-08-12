# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetBatchImportTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetBatchImportTaskResponseBodyData = None,
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
            temp_model = main_models.GetBatchImportTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetBatchImportTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_message: str = None,
        processed_count: int = None,
        result: main_models.GetBatchImportTaskResponseBodyDataResult = None,
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
            temp_model = main_models.GetBatchImportTaskResponseBodyDataResult()
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

class GetBatchImportTaskResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        api_type: str = None,
        dry_run: bool = None,
        dry_run_results: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResults] = None,
        failure_items: List[main_models.GetBatchImportTaskResponseBodyDataResultFailureItems] = None,
        gateway_id: str = None,
        import_request: main_models.GetBatchImportTaskResponseBodyDataResultImportRequest = None,
        success_items: List[main_models.GetBatchImportTaskResponseBodyDataResultSuccessItems] = None,
    ):
        self.api_type = api_type
        self.dry_run = dry_run
        self.dry_run_results = dry_run_results
        self.failure_items = failure_items
        self.gateway_id = gateway_id
        self.import_request = import_request
        self.success_items = success_items

    def validate(self):
        if self.dry_run_results:
            for v1 in self.dry_run_results:
                 if v1:
                    v1.validate()
        if self.failure_items:
            for v1 in self.failure_items:
                 if v1:
                    v1.validate()
        if self.import_request:
            self.import_request.validate()
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

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        result['dryRunResults'] = []
        if self.dry_run_results is not None:
            for k1 in self.dry_run_results:
                result['dryRunResults'].append(k1.to_map() if k1 else None)

        result['failureItems'] = []
        if self.failure_items is not None:
            for k1 in self.failure_items:
                result['failureItems'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.import_request is not None:
            result['importRequest'] = self.import_request.to_map()

        result['successItems'] = []
        if self.success_items is not None:
            for k1 in self.success_items:
                result['successItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        self.dry_run_results = []
        if m.get('dryRunResults') is not None:
            for k1 in m.get('dryRunResults'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResults()
                self.dry_run_results.append(temp_model.from_map(k1))

        self.failure_items = []
        if m.get('failureItems') is not None:
            for k1 in m.get('failureItems'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultFailureItems()
                self.failure_items.append(temp_model.from_map(k1))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('importRequest') is not None:
            temp_model = main_models.GetBatchImportTaskResponseBodyDataResultImportRequest()
            self.import_request = temp_model.from_map(m.get('importRequest'))

        self.success_items = []
        if m.get('successItems') is not None:
            for k1 in m.get('successItems'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultSuccessItems()
                self.success_items.append(temp_model.from_map(k1))

        return self

class GetBatchImportTaskResponseBodyDataResultSuccessItems(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        error_message: str = None,
        file_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.error_message = error_message
        self.file_name = file_name

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

        if self.file_name is not None:
            result['fileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        return self

class GetBatchImportTaskResponseBodyDataResultImportRequest(DaraModel):
    def __init__(
        self,
        allow_update: bool = None,
        api_type: str = None,
        dry_run: bool = None,
        gateway_id: str = None,
        resource_group_id: str = None,
        spec_file_url: str = None,
        spec_oss_config: main_models.GetBatchImportTaskResponseBodyDataResultImportRequestSpecOssConfig = None,
        strategy: str = None,
        with_gateway_extension: bool = None,
    ):
        self.allow_update = allow_update
        self.api_type = api_type
        self.dry_run = dry_run
        self.gateway_id = gateway_id
        self.resource_group_id = resource_group_id
        self.spec_file_url = spec_file_url
        self.spec_oss_config = spec_oss_config
        self.strategy = strategy
        self.with_gateway_extension = with_gateway_extension

    def validate(self):
        if self.spec_oss_config:
            self.spec_oss_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_update is not None:
            result['allowUpdate'] = self.allow_update

        if self.api_type is not None:
            result['apiType'] = self.api_type

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.spec_file_url is not None:
            result['specFileUrl'] = self.spec_file_url

        if self.spec_oss_config is not None:
            result['specOssConfig'] = self.spec_oss_config.to_map()

        if self.strategy is not None:
            result['strategy'] = self.strategy

        if self.with_gateway_extension is not None:
            result['withGatewayExtension'] = self.with_gateway_extension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowUpdate') is not None:
            self.allow_update = m.get('allowUpdate')

        if m.get('apiType') is not None:
            self.api_type = m.get('apiType')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('specFileUrl') is not None:
            self.spec_file_url = m.get('specFileUrl')

        if m.get('specOssConfig') is not None:
            temp_model = main_models.GetBatchImportTaskResponseBodyDataResultImportRequestSpecOssConfig()
            self.spec_oss_config = temp_model.from_map(m.get('specOssConfig'))

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        if m.get('withGatewayExtension') is not None:
            self.with_gateway_extension = m.get('withGatewayExtension')

        return self

class GetBatchImportTaskResponseBodyDataResultImportRequestSpecOssConfig(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        object_key: str = None,
        region_id: str = None,
    ):
        self.bucket_name = bucket_name
        self.object_key = object_key
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.object_key is not None:
            result['objectKey'] = self.object_key

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('objectKey') is not None:
            self.object_key = m.get('objectKey')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class GetBatchImportTaskResponseBodyDataResultFailureItems(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        error_message: str = None,
        file_name: str = None,
    ):
        self.api_id = api_id
        self.api_name = api_name
        self.error_message = error_message
        self.file_name = file_name

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

        if self.file_name is not None:
            result['fileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiId') is not None:
            self.api_id = m.get('apiId')

        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResults(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        dry_run_info: main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfo = None,
        error: str = None,
        file_name: str = None,
    ):
        self.api_name = api_name
        self.dry_run_info = dry_run_info
        self.error = error
        self.file_name = file_name

    def validate(self):
        if self.dry_run_info:
            self.dry_run_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['apiName'] = self.api_name

        if self.dry_run_info is not None:
            result['dryRunInfo'] = self.dry_run_info.to_map()

        if self.error is not None:
            result['error'] = self.error

        if self.file_name is not None:
            result['fileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')

        if m.get('dryRunInfo') is not None:
            temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfo()
            self.dry_run_info = temp_model.from_map(m.get('dryRunInfo'))

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfo(DaraModel):
    def __init__(
        self,
        error_messages: List[str] = None,
        exist_http_api_info: main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoExistHttpApiInfo = None,
        failure_components: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureComponents] = None,
        failure_operations: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureOperations] = None,
        failure_routes: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureRoutes] = None,
        success_components: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessComponents] = None,
        success_operations: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessOperations] = None,
        success_routes: List[main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessRoutes] = None,
        warning_messages: List[str] = None,
    ):
        self.error_messages = error_messages
        self.exist_http_api_info = exist_http_api_info
        self.failure_components = failure_components
        self.failure_operations = failure_operations
        self.failure_routes = failure_routes
        self.success_components = success_components
        self.success_operations = success_operations
        self.success_routes = success_routes
        self.warning_messages = warning_messages

    def validate(self):
        if self.exist_http_api_info:
            self.exist_http_api_info.validate()
        if self.failure_components:
            for v1 in self.failure_components:
                 if v1:
                    v1.validate()
        if self.failure_operations:
            for v1 in self.failure_operations:
                 if v1:
                    v1.validate()
        if self.failure_routes:
            for v1 in self.failure_routes:
                 if v1:
                    v1.validate()
        if self.success_components:
            for v1 in self.success_components:
                 if v1:
                    v1.validate()
        if self.success_operations:
            for v1 in self.success_operations:
                 if v1:
                    v1.validate()
        if self.success_routes:
            for v1 in self.success_routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_messages is not None:
            result['errorMessages'] = self.error_messages

        if self.exist_http_api_info is not None:
            result['existHttpApiInfo'] = self.exist_http_api_info.to_map()

        result['failureComponents'] = []
        if self.failure_components is not None:
            for k1 in self.failure_components:
                result['failureComponents'].append(k1.to_map() if k1 else None)

        result['failureOperations'] = []
        if self.failure_operations is not None:
            for k1 in self.failure_operations:
                result['failureOperations'].append(k1.to_map() if k1 else None)

        result['failureRoutes'] = []
        if self.failure_routes is not None:
            for k1 in self.failure_routes:
                result['failureRoutes'].append(k1.to_map() if k1 else None)

        result['successComponents'] = []
        if self.success_components is not None:
            for k1 in self.success_components:
                result['successComponents'].append(k1.to_map() if k1 else None)

        result['successOperations'] = []
        if self.success_operations is not None:
            for k1 in self.success_operations:
                result['successOperations'].append(k1.to_map() if k1 else None)

        result['successRoutes'] = []
        if self.success_routes is not None:
            for k1 in self.success_routes:
                result['successRoutes'].append(k1.to_map() if k1 else None)

        if self.warning_messages is not None:
            result['warningMessages'] = self.warning_messages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessages') is not None:
            self.error_messages = m.get('errorMessages')

        if m.get('existHttpApiInfo') is not None:
            temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoExistHttpApiInfo()
            self.exist_http_api_info = temp_model.from_map(m.get('existHttpApiInfo'))

        self.failure_components = []
        if m.get('failureComponents') is not None:
            for k1 in m.get('failureComponents'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureComponents()
                self.failure_components.append(temp_model.from_map(k1))

        self.failure_operations = []
        if m.get('failureOperations') is not None:
            for k1 in m.get('failureOperations'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureOperations()
                self.failure_operations.append(temp_model.from_map(k1))

        self.failure_routes = []
        if m.get('failureRoutes') is not None:
            for k1 in m.get('failureRoutes'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureRoutes()
                self.failure_routes.append(temp_model.from_map(k1))

        self.success_components = []
        if m.get('successComponents') is not None:
            for k1 in m.get('successComponents'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessComponents()
                self.success_components.append(temp_model.from_map(k1))

        self.success_operations = []
        if m.get('successOperations') is not None:
            for k1 in m.get('successOperations'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessOperations()
                self.success_operations.append(temp_model.from_map(k1))

        self.success_routes = []
        if m.get('successRoutes') is not None:
            for k1 in m.get('successRoutes'):
                temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessRoutes()
                self.success_routes.append(temp_model.from_map(k1))

        if m.get('warningMessages') is not None:
            self.warning_messages = m.get('warningMessages')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessRoutes(DaraModel):
    def __init__(
        self,
        action: str = None,
        name: str = None,
    ):
        self.action = action
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessOperations(DaraModel):
    def __init__(
        self,
        action: str = None,
        method: str = None,
        name: str = None,
        path: str = None,
    ):
        self.action = action
        self.method = method
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoSuccessComponents(DaraModel):
    def __init__(
        self,
        action: str = None,
        name: str = None,
    ):
        self.action = action
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureRoutes(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        name: str = None,
    ):
        self.error_message = error_message
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureOperations(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        method: str = None,
        path: str = None,
    ):
        self.error_message = error_message
        self.method = method
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.method is not None:
            result['method'] = self.method

        if self.path is not None:
            result['path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('path') is not None:
            self.path = m.get('path')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoFailureComponents(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        name: str = None,
    ):
        self.error_message = error_message
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoExistHttpApiInfo(DaraModel):
    def __init__(
        self,
        base_path: str = None,
        gateway_id: str = None,
        http_api_id: str = None,
        name: str = None,
        type: str = None,
        version_info: main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoExistHttpApiInfoVersionInfo = None,
    ):
        self.base_path = base_path
        self.gateway_id = gateway_id
        self.http_api_id = http_api_id
        self.name = name
        self.type = type
        self.version_info = version_info

    def validate(self):
        if self.version_info:
            self.version_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_path is not None:
            result['basePath'] = self.base_path

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.version_info is not None:
            result['versionInfo'] = self.version_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('versionInfo') is not None:
            temp_model = main_models.GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoExistHttpApiInfoVersionInfo()
            self.version_info = temp_model.from_map(m.get('versionInfo'))

        return self

class GetBatchImportTaskResponseBodyDataResultDryRunResultsDryRunInfoExistHttpApiInfoVersionInfo(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        header_name: str = None,
        query_name: str = None,
        scheme: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.header_name = header_name
        self.query_name = query_name
        self.scheme = scheme
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.header_name is not None:
            result['headerName'] = self.header_name

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.scheme is not None:
            result['scheme'] = self.scheme

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

