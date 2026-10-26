# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class CheckResourceMeasureResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.CheckResourceMeasureResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Specifies whether retries are allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** response parameter.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error parameters returned.
        self.error_args = error_args
        # The application module.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The root error code.
        self.root_error_code = root_error_code
        # The exception message.
        self.root_error_msg = root_error_msg
        # The backup parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('Module') is not None:
            temp_model = main_models.CheckResourceMeasureResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class CheckResourceMeasureResponseBodyModule(DaraModel):
    def __init__(
        self,
        desired_total: int = None,
        error_code: str = None,
        error_message: str = None,
        limit: int = None,
        passed: bool = None,
        resource_code: str = None,
        upgrade_available: bool = None,
    ):
        # The desired total returned only for APP_WORKSPACE. This is the target total for the current check, which is the sum of the existing usage in the saved configuration and ResourceValue. If the compatible DesiredTotal is provided, this total is used directly. The existing usage of issues is the sum of common and word-of-mouth issues in the saved configuration, and the existing usage of competitors is the number of competitors. This parameter is empty for APP and USER checks.
        self.desired_total = desired_total
        # The error code returned when the check fails. This parameter is null when the check passes.
        self.error_code = error_code
        # The error message returned when the check fails. This parameter is null when the check passes.
        self.error_message = error_message
        # The limit returned only for APP_WORKSPACE quantity pre-checks. This is the maximum number of issues or competitors allowed by the current commodity edition, not the remaining quota. This parameter is empty for APP and USER checks or when the edition benefits cannot be determined.
        self.limit = limit
        # Indicates whether the check is passed.
        self.passed = passed
        # The resource identifier.
        self.resource_code = resource_code
        # Indicates whether a purchasable higher edition that can accommodate the DesiredTotal exists. This parameter is true only when the capacity of the current edition is insufficient and a higher edition meets the requirements. Otherwise, this parameter is false. This parameter may be empty for APP and USER checks. This field does not indicate that an upgrade has been performed or an upgrade order has been created.
        self.upgrade_available = upgrade_available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_total is not None:
            result['DesiredTotal'] = self.desired_total

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code

        if self.upgrade_available is not None:
            result['UpgradeAvailable'] = self.upgrade_available

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredTotal') is not None:
            self.desired_total = m.get('DesiredTotal')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')

        if m.get('UpgradeAvailable') is not None:
            self.upgrade_available = m.get('UpgradeAvailable')

        return self

