# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class QueryInspirationBalanceForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.QueryInspirationBalanceForPartnerResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The access denied details.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic message.
        self.dynamic_message = dynamic_message
        # The error parameters.
        self.error_args = error_args
        # The response data.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The error message.
        self.root_error_msg = root_error_msg
        # The reserved parameter.
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
            temp_model = main_models.QueryInspirationBalanceForPartnerResponseBodyModule()
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

class QueryInspirationBalanceForPartnerResponseBodyModule(DaraModel):
    def __init__(
        self,
        remaining: int = None,
        remaining_str: str = None,
        total_quota: int = None,
        total_quota_str: str = None,
        total_used: int = None,
        total_used_str: str = None,
    ):
        # The remaining amount, calculated as totalQuota minus totalUsed.
        self.remaining = remaining
        # The remaining amount as a precise value. This field is of the String type and supports decimal display.
        self.remaining_str = remaining_str
        # The total quota, which is the sum of initQuota for all valid accounts.
        self.total_quota = total_quota
        # The total quota as a precise value. This field is of the String type and supports decimal display.
        self.total_quota_str = total_quota_str
        # The total consumed amount, which is the sum of used for all valid accounts.
        self.total_used = total_used
        # The total consumed amount as a precise value. This field is of the String type and supports decimal display.
        self.total_used_str = total_used_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remaining is not None:
            result['Remaining'] = self.remaining

        if self.remaining_str is not None:
            result['RemainingStr'] = self.remaining_str

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.total_quota_str is not None:
            result['TotalQuotaStr'] = self.total_quota_str

        if self.total_used is not None:
            result['TotalUsed'] = self.total_used

        if self.total_used_str is not None:
            result['TotalUsedStr'] = self.total_used_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remaining') is not None:
            self.remaining = m.get('Remaining')

        if m.get('RemainingStr') is not None:
            self.remaining_str = m.get('RemainingStr')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('TotalQuotaStr') is not None:
            self.total_quota_str = m.get('TotalQuotaStr')

        if m.get('TotalUsed') is not None:
            self.total_used = m.get('TotalUsed')

        if m.get('TotalUsedStr') is not None:
            self.total_used_str = m.get('TotalUsedStr')

        return self

