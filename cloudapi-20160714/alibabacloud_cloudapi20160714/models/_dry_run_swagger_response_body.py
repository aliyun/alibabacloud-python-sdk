# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DryRunSwaggerResponseBody(DaraModel):
    def __init__(
        self,
        failed: main_models.DryRunSwaggerResponseBodyFailed = None,
        global_condition: str = None,
        model_failed: main_models.DryRunSwaggerResponseBodyModelFailed = None,
        model_success: main_models.DryRunSwaggerResponseBodyModelSuccess = None,
        request_id: str = None,
        success: main_models.DryRunSwaggerResponseBodySuccess = None,
    ):
        # The APIs that failed to be created based on the Swagger-compliant data imported this time.
        self.failed = failed
        # The global condition.
        self.global_condition = global_condition
        # The models that failed to be imported through the Swagger-compliant data this time.
        self.model_failed = model_failed
        # The models that failed to be imported through the Swagger-compliant data this time.
        self.model_success = model_success
        # The ID of the request.
        self.request_id = request_id
        # The APIs that are created based on the Swagger-compliant data imported this time.
        self.success = success

    def validate(self):
        if self.failed:
            self.failed.validate()
        if self.model_failed:
            self.model_failed.validate()
        if self.model_success:
            self.model_success.validate()
        if self.success:
            self.success.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed.to_map()

        if self.global_condition is not None:
            result['GlobalCondition'] = self.global_condition

        if self.model_failed is not None:
            result['ModelFailed'] = self.model_failed.to_map()

        if self.model_success is not None:
            result['ModelSuccess'] = self.model_success.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            temp_model = main_models.DryRunSwaggerResponseBodyFailed()
            self.failed = temp_model.from_map(m.get('Failed'))

        if m.get('GlobalCondition') is not None:
            self.global_condition = m.get('GlobalCondition')

        if m.get('ModelFailed') is not None:
            temp_model = main_models.DryRunSwaggerResponseBodyModelFailed()
            self.model_failed = temp_model.from_map(m.get('ModelFailed'))

        if m.get('ModelSuccess') is not None:
            temp_model = main_models.DryRunSwaggerResponseBodyModelSuccess()
            self.model_success = temp_model.from_map(m.get('ModelSuccess'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            temp_model = main_models.DryRunSwaggerResponseBodySuccess()
            self.success = temp_model.from_map(m.get('Success'))

        return self

class DryRunSwaggerResponseBodySuccess(DaraModel):
    def __init__(
        self,
        api_dry_run_swagger_success: List[main_models.DryRunSwaggerResponseBodySuccessApiDryRunSwaggerSuccess] = None,
    ):
        self.api_dry_run_swagger_success = api_dry_run_swagger_success

    def validate(self):
        if self.api_dry_run_swagger_success:
            for v1 in self.api_dry_run_swagger_success:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiDryRunSwaggerSuccess'] = []
        if self.api_dry_run_swagger_success is not None:
            for k1 in self.api_dry_run_swagger_success:
                result['ApiDryRunSwaggerSuccess'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_dry_run_swagger_success = []
        if m.get('ApiDryRunSwaggerSuccess') is not None:
            for k1 in m.get('ApiDryRunSwaggerSuccess'):
                temp_model = main_models.DryRunSwaggerResponseBodySuccessApiDryRunSwaggerSuccess()
                self.api_dry_run_swagger_success.append(temp_model.from_map(k1))

        return self

class DryRunSwaggerResponseBodySuccessApiDryRunSwaggerSuccess(DaraModel):
    def __init__(
        self,
        api_operation: str = None,
        api_swagger: str = None,
        api_uid: str = None,
        http_method: str = None,
        path: str = None,
    ):
        # Specifies whether the operation is CREATE or MODIFY.
        self.api_operation = api_operation
        # The API definition that complies with the Swagger specification.
        self.api_swagger = api_swagger
        # The UID of the successfully imported API.
        self.api_uid = api_uid
        # The HTTP method configured when the API is created.
        self.http_method = http_method
        # The request path configured when the API is created.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_operation is not None:
            result['ApiOperation'] = self.api_operation

        if self.api_swagger is not None:
            result['ApiSwagger'] = self.api_swagger

        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

        if self.http_method is not None:
            result['HttpMethod'] = self.http_method

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiOperation') is not None:
            self.api_operation = m.get('ApiOperation')

        if m.get('ApiSwagger') is not None:
            self.api_swagger = m.get('ApiSwagger')

        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('HttpMethod') is not None:
            self.http_method = m.get('HttpMethod')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class DryRunSwaggerResponseBodyModelSuccess(DaraModel):
    def __init__(
        self,
        api_import_model_success: List[main_models.DryRunSwaggerResponseBodyModelSuccessApiImportModelSuccess] = None,
    ):
        self.api_import_model_success = api_import_model_success

    def validate(self):
        if self.api_import_model_success:
            for v1 in self.api_import_model_success:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiImportModelSuccess'] = []
        if self.api_import_model_success is not None:
            for k1 in self.api_import_model_success:
                result['ApiImportModelSuccess'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_model_success = []
        if m.get('ApiImportModelSuccess') is not None:
            for k1 in m.get('ApiImportModelSuccess'):
                temp_model = main_models.DryRunSwaggerResponseBodyModelSuccessApiImportModelSuccess()
                self.api_import_model_success.append(temp_model.from_map(k1))

        return self

class DryRunSwaggerResponseBodyModelSuccessApiImportModelSuccess(DaraModel):
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
        # The model operation.
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

class DryRunSwaggerResponseBodyModelFailed(DaraModel):
    def __init__(
        self,
        api_import_model_failed: List[main_models.DryRunSwaggerResponseBodyModelFailedApiImportModelFailed] = None,
    ):
        self.api_import_model_failed = api_import_model_failed

    def validate(self):
        if self.api_import_model_failed:
            for v1 in self.api_import_model_failed:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiImportModelFailed'] = []
        if self.api_import_model_failed is not None:
            for k1 in self.api_import_model_failed:
                result['ApiImportModelFailed'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_model_failed = []
        if m.get('ApiImportModelFailed') is not None:
            for k1 in m.get('ApiImportModelFailed'):
                temp_model = main_models.DryRunSwaggerResponseBodyModelFailedApiImportModelFailed()
                self.api_import_model_failed.append(temp_model.from_map(k1))

        return self

class DryRunSwaggerResponseBodyModelFailedApiImportModelFailed(DaraModel):
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

class DryRunSwaggerResponseBodyFailed(DaraModel):
    def __init__(
        self,
        api_import_swagger_failed: List[main_models.DryRunSwaggerResponseBodyFailedApiImportSwaggerFailed] = None,
    ):
        self.api_import_swagger_failed = api_import_swagger_failed

    def validate(self):
        if self.api_import_swagger_failed:
            for v1 in self.api_import_swagger_failed:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiImportSwaggerFailed'] = []
        if self.api_import_swagger_failed is not None:
            for k1 in self.api_import_swagger_failed:
                result['ApiImportSwaggerFailed'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_import_swagger_failed = []
        if m.get('ApiImportSwaggerFailed') is not None:
            for k1 in m.get('ApiImportSwaggerFailed'):
                temp_model = main_models.DryRunSwaggerResponseBodyFailedApiImportSwaggerFailed()
                self.api_import_swagger_failed.append(temp_model.from_map(k1))

        return self

class DryRunSwaggerResponseBodyFailedApiImportSwaggerFailed(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        http_method: str = None,
        path: str = None,
    ):
        # The error message returned when the API is created.
        self.error_msg = error_msg
        # The HTTP method configured when the API is created.
        self.http_method = http_method
        # The request path configured when the API is created.
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

