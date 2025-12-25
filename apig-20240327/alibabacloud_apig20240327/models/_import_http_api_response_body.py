# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ImportHttpApiResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ImportHttpApiResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The API information.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.ImportHttpApiResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ImportHttpApiResponseBodyData(DaraModel):
    def __init__(
        self,
        dry_run_info: main_models.ImportHttpApiResponseBodyDataDryRunInfo = None,
        http_api_id: str = None,
        name: str = None,
    ):
        # The dry run result.
        self.dry_run_info = dry_run_info
        # The API ID.
        self.http_api_id = http_api_id
        # The API name.
        self.name = name

    def validate(self):
        if self.dry_run_info:
            self.dry_run_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run_info is not None:
            result['dryRunInfo'] = self.dry_run_info.to_map()

        if self.http_api_id is not None:
            result['httpApiId'] = self.http_api_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRunInfo') is not None:
            temp_model = main_models.ImportHttpApiResponseBodyDataDryRunInfo()
            self.dry_run_info = temp_model.from_map(m.get('dryRunInfo'))

        if m.get('httpApiId') is not None:
            self.http_api_id = m.get('httpApiId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ImportHttpApiResponseBodyDataDryRunInfo(DaraModel):
    def __init__(
        self,
        error_messages: List[str] = None,
        exist_http_api_info: main_models.HttpApiApiInfo = None,
        failure_components: List[main_models.ImportHttpApiResponseBodyDataDryRunInfoFailureComponents] = None,
        failure_operations: List[main_models.ImportHttpApiResponseBodyDataDryRunInfoFailureOperations] = None,
        success_components: List[main_models.ImportHttpApiResponseBodyDataDryRunInfoSuccessComponents] = None,
        success_operations: List[main_models.ImportHttpApiResponseBodyDataDryRunInfoSuccessOperations] = None,
        warning_messages: List[str] = None,
    ):
        # The error messages. If an error message is returned, the API fails to be imported.
        self.error_messages = error_messages
        # The existing APIs. If an existing API is returned, the import updates the existing API.
        self.exist_http_api_info = exist_http_api_info
        # The data structs that fail the dry run.
        self.failure_components = failure_components
        # The operations that fail the dry run.
        self.failure_operations = failure_operations
        # The data structs that pass the dry run.
        self.success_components = success_components
        # The operations that pass the dry run.
        self.success_operations = success_operations
        # The alerts. If an alert is returned, specific operations or structs may fail to be imported.
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
        if self.success_components:
            for v1 in self.success_components:
                 if v1:
                    v1.validate()
        if self.success_operations:
            for v1 in self.success_operations:
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

        result['successComponents'] = []
        if self.success_components is not None:
            for k1 in self.success_components:
                result['successComponents'].append(k1.to_map() if k1 else None)

        result['successOperations'] = []
        if self.success_operations is not None:
            for k1 in self.success_operations:
                result['successOperations'].append(k1.to_map() if k1 else None)

        if self.warning_messages is not None:
            result['warningMessages'] = self.warning_messages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessages') is not None:
            self.error_messages = m.get('errorMessages')

        if m.get('existHttpApiInfo') is not None:
            temp_model = main_models.HttpApiApiInfo()
            self.exist_http_api_info = temp_model.from_map(m.get('existHttpApiInfo'))

        self.failure_components = []
        if m.get('failureComponents') is not None:
            for k1 in m.get('failureComponents'):
                temp_model = main_models.ImportHttpApiResponseBodyDataDryRunInfoFailureComponents()
                self.failure_components.append(temp_model.from_map(k1))

        self.failure_operations = []
        if m.get('failureOperations') is not None:
            for k1 in m.get('failureOperations'):
                temp_model = main_models.ImportHttpApiResponseBodyDataDryRunInfoFailureOperations()
                self.failure_operations.append(temp_model.from_map(k1))

        self.success_components = []
        if m.get('successComponents') is not None:
            for k1 in m.get('successComponents'):
                temp_model = main_models.ImportHttpApiResponseBodyDataDryRunInfoSuccessComponents()
                self.success_components.append(temp_model.from_map(k1))

        self.success_operations = []
        if m.get('successOperations') is not None:
            for k1 in m.get('successOperations'):
                temp_model = main_models.ImportHttpApiResponseBodyDataDryRunInfoSuccessOperations()
                self.success_operations.append(temp_model.from_map(k1))

        if m.get('warningMessages') is not None:
            self.warning_messages = m.get('warningMessages')

        return self

class ImportHttpApiResponseBodyDataDryRunInfoSuccessOperations(DaraModel):
    def __init__(
        self,
        action: str = None,
        method: str = None,
        name: str = None,
        path: str = None,
    ):
        # The action that will be performed for the operation after the dry run.
        # 
        # *   Create: The operation is created.
        # *   Update: The operation is updated.
        self.action = action
        # The HTTP method of the operation.
        self.method = method
        # The operation name.
        self.name = name
        # The operation path.
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

class ImportHttpApiResponseBodyDataDryRunInfoSuccessComponents(DaraModel):
    def __init__(
        self,
        action: str = None,
        name: str = None,
    ):
        # The action that will be performed for the data struct after the dry run.
        # 
        # *   Create: The data struct is created.
        # *   Update: The data struct is updated.
        self.action = action
        # The data struct name.
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

class ImportHttpApiResponseBodyDataDryRunInfoFailureOperations(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        method: str = None,
        path: str = None,
    ):
        # The error message.
        self.error_message = error_message
        # The HTTP method of the operation.
        self.method = method
        # The operation path.
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

class ImportHttpApiResponseBodyDataDryRunInfoFailureComponents(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        name: str = None,
    ):
        # The error message.
        self.error_message = error_message
        # The data struct name.
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

