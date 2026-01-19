# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class ImportOASResponseBody(DaraModel):
    def __init__(
        self,
        error_messages: main_models.ImportOASResponseBodyErrorMessages = None,
        failed_apis: main_models.ImportOASResponseBodyFailedApis = None,
        failed_models: main_models.ImportOASResponseBodyFailedModels = None,
        operation_id: str = None,
        request_id: str = None,
        success_apis: main_models.ImportOASResponseBodySuccessApis = None,
        success_models: main_models.ImportOASResponseBodySuccessModels = None,
        warning_messages: main_models.ImportOASResponseBodyWarningMessages = None,
    ):
        # The error messages that appear due to the invalid data in the imported file.
        self.error_messages = error_messages
        # The APIs that failed to pass the precheck.
        self.failed_apis = failed_apis
        # The information about the models that failed to pass the precheck.
        self.failed_models = failed_models
        # The ID of the asynchronous API import task that was generated during the import operation. This ID is used to query the execution status of the API import task.
        self.operation_id = operation_id
        # The ID of the request.
        self.request_id = request_id
        # The information about the APIs that have passed the precheck.
        self.success_apis = success_apis
        # The information about the models that have passed the precheck.
        self.success_models = success_models
        # The warning messages that appear due to the invalid data in the imported file.
        self.warning_messages = warning_messages

    def validate(self):
        if self.error_messages:
            self.error_messages.validate()
        if self.failed_apis:
            self.failed_apis.validate()
        if self.failed_models:
            self.failed_models.validate()
        if self.success_apis:
            self.success_apis.validate()
        if self.success_models:
            self.success_models.validate()
        if self.warning_messages:
            self.warning_messages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_messages is not None:
            result['ErrorMessages'] = self.error_messages.to_map()

        if self.failed_apis is not None:
            result['FailedApis'] = self.failed_apis.to_map()

        if self.failed_models is not None:
            result['FailedModels'] = self.failed_models.to_map()

        if self.operation_id is not None:
            result['OperationId'] = self.operation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success_apis is not None:
            result['SuccessApis'] = self.success_apis.to_map()

        if self.success_models is not None:
            result['SuccessModels'] = self.success_models.to_map()

        if self.warning_messages is not None:
            result['WarningMessages'] = self.warning_messages.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessages') is not None:
            temp_model = main_models.ImportOASResponseBodyErrorMessages()
            self.error_messages = temp_model.from_map(m.get('ErrorMessages'))

        if m.get('FailedApis') is not None:
            temp_model = main_models.ImportOASResponseBodyFailedApis()
            self.failed_apis = temp_model.from_map(m.get('FailedApis'))

        if m.get('FailedModels') is not None:
            temp_model = main_models.ImportOASResponseBodyFailedModels()
            self.failed_models = temp_model.from_map(m.get('FailedModels'))

        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuccessApis') is not None:
            temp_model = main_models.ImportOASResponseBodySuccessApis()
            self.success_apis = temp_model.from_map(m.get('SuccessApis'))

        if m.get('SuccessModels') is not None:
            temp_model = main_models.ImportOASResponseBodySuccessModels()
            self.success_models = temp_model.from_map(m.get('SuccessModels'))

        if m.get('WarningMessages') is not None:
            temp_model = main_models.ImportOASResponseBodyWarningMessages()
            self.warning_messages = temp_model.from_map(m.get('WarningMessages'))

        return self

class ImportOASResponseBodyWarningMessages(DaraModel):
    def __init__(
        self,
        warning_message: List[str] = None,
    ):
        self.warning_message = warning_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.warning_message is not None:
            result['WarningMessage'] = self.warning_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WarningMessage') is not None:
            self.warning_message = m.get('WarningMessage')

        return self

class ImportOASResponseBodySuccessModels(DaraModel):
    def __init__(
        self,
        success_model: List[main_models.ImportOASResponseBodySuccessModelsSuccessModel] = None,
    ):
        self.success_model = success_model

    def validate(self):
        if self.success_model:
            for v1 in self.success_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SuccessModel'] = []
        if self.success_model is not None:
            for k1 in self.success_model:
                result['SuccessModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.success_model = []
        if m.get('SuccessModel') is not None:
            for k1 in m.get('SuccessModel'):
                temp_model = main_models.ImportOASResponseBodySuccessModelsSuccessModel()
                self.success_model.append(temp_model.from_map(k1))

        return self

class ImportOASResponseBodySuccessModelsSuccessModel(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        model_name: str = None,
        model_operation: str = None,
        model_uid: str = None,
    ):
        # The ID of the API group.
        self.group_id = group_id
        # The name of the model.
        self.model_name = model_name
        # The operation of the model. Valid values: CREATE and MODIFY.
        self.model_operation = model_operation
        # The UID of the model.
        self.model_uid = model_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_operation is not None:
            result['ModelOperation'] = self.model_operation

        if self.model_uid is not None:
            result['ModelUid'] = self.model_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelOperation') is not None:
            self.model_operation = m.get('ModelOperation')

        if m.get('ModelUid') is not None:
            self.model_uid = m.get('ModelUid')

        return self

class ImportOASResponseBodySuccessApis(DaraModel):
    def __init__(
        self,
        success_api: List[main_models.ImportOASResponseBodySuccessApisSuccessApi] = None,
    ):
        self.success_api = success_api

    def validate(self):
        if self.success_api:
            for v1 in self.success_api:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SuccessApi'] = []
        if self.success_api is not None:
            for k1 in self.success_api:
                result['SuccessApi'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.success_api = []
        if m.get('SuccessApi') is not None:
            for k1 in m.get('SuccessApi'):
                temp_model = main_models.ImportOASResponseBodySuccessApisSuccessApi()
                self.success_api.append(temp_model.from_map(k1))

        return self

class ImportOASResponseBodySuccessApisSuccessApi(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_operation: str = None,
        http_method: str = None,
        path: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # Indicates that the operation is CREATE or MODIFY.
        self.api_operation = api_operation
        # The HTTP method configured when you created the API.
        self.http_method = http_method
        # The request path configured when you created the API.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_operation is not None:
            result['ApiOperation'] = self.api_operation

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiOperation') is not None:
            self.api_operation = m.get('ApiOperation')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class ImportOASResponseBodyFailedModels(DaraModel):
    def __init__(
        self,
        failed_model: List[main_models.ImportOASResponseBodyFailedModelsFailedModel] = None,
    ):
        self.failed_model = failed_model

    def validate(self):
        if self.failed_model:
            for v1 in self.failed_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedModel'] = []
        if self.failed_model is not None:
            for k1 in self.failed_model:
                result['FailedModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_model = []
        if m.get('FailedModel') is not None:
            for k1 in m.get('FailedModel'):
                temp_model = main_models.ImportOASResponseBodyFailedModelsFailedModel()
                self.failed_model.append(temp_model.from_map(k1))

        return self

class ImportOASResponseBodyFailedModelsFailedModel(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        group_id: str = None,
        model_name: str = None,
    ):
        # The error message.
        self.error_msg = error_msg
        # The ID of the API group.
        self.group_id = group_id
        # The name of the model.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        return self

class ImportOASResponseBodyFailedApis(DaraModel):
    def __init__(
        self,
        failed_api: List[main_models.ImportOASResponseBodyFailedApisFailedApi] = None,
    ):
        self.failed_api = failed_api

    def validate(self):
        if self.failed_api:
            for v1 in self.failed_api:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedApi'] = []
        if self.failed_api is not None:
            for k1 in self.failed_api:
                result['FailedApi'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_api = []
        if m.get('FailedApi') is not None:
            for k1 in m.get('FailedApi'):
                temp_model = main_models.ImportOASResponseBodyFailedApisFailedApi()
                self.failed_api.append(temp_model.from_map(k1))

        return self

class ImportOASResponseBodyFailedApisFailedApi(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        http_method: str = None,
        path: str = None,
    ):
        # The error message.
        self.error_msg = error_msg
        # The HTTP method configured when you created the API.
        self.http_method = http_method
        # The request path configured when you created the API.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class ImportOASResponseBodyErrorMessages(DaraModel):
    def __init__(
        self,
        error_message: List[str] = None,
    ):
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

