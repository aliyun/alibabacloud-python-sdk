# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetLlmProxyConfigForAdminResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.GetLlmProxyConfigForAdminResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed. Valid values:  
        # - false: Retry is not allowed.  
        # - true: Retry is allowed.
        self.allow_retry = allow_retry
        # Application name. Query the application with this name.
        self.app_name = app_name
        # Dynamic code. This parameter is not used and can be ignored.
        self.dynamic_code = dynamic_code
        # Dynamic error message used to replace the `%s` placeholder in the **ErrMessage** error message.  
        # > For example, if **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # Error parameters returned.
        self.error_args = error_args
        # Returned object.
        self.module = module
        # Id of the request
        self.request_id = request_id
        # Error code
        self.root_error_code = root_error_code
        # Abnormal message
        self.root_error_msg = root_error_msg
        # Indicates whether the request is processed synchronously.
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
            temp_model = main_models.GetLlmProxyConfigForAdminResponseBodyModule()
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

class GetLlmProxyConfigForAdminResponseBodyModule(DaraModel):
    def __init__(
        self,
        allowed_models: str = None,
        biz_id: str = None,
        blocked_models: str = None,
        capability: str = None,
        daily_limit: int = None,
        daily_token_limit: int = None,
        enabled: bool = None,
        extend: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        ip_blacklist: str = None,
        ip_whitelist: str = None,
        rpm_limit: int = None,
        status: int = None,
        suspend_reason: str = None,
    ):
        # List of supported models
        self.allowed_models = allowed_models
        # Business ID of the application instance
        self.biz_id = biz_id
        # List of blocked models
        self.blocked_models = blocked_models
        # Grants specific permissions to processes within the container. Currently, only NET_ADMIN and NET_RAW are supported.  
        # 
        # > NET_RAW is not supported by default. You must submit a ticket to request it.
        self.capability = capability
        # Daily request quota
        self.daily_limit = daily_limit
        # Daily token quota
        self.daily_token_limit = daily_token_limit
        # Indicates whether scheduled delivery of resource snapshots is enabled.  
        # 
        # Valid values:  
        # - true: Enabled.  
        # - false: Shutdown.
        self.enabled = enabled
        # Extension configuration (in JSON format)
        self.extend = extend
        # Creation Time
        self.gmt_create = gmt_create
        # Updated At
        self.gmt_modified = gmt_modified
        # Primary key
        self.id = id
        # IP blacklist
        self.ip_blacklist = ip_blacklist
        # IP whitelist, with multiple entries separated by commas
        self.ip_whitelist = ip_whitelist
        # Requests per minute quota
        self.rpm_limit = rpm_limit
        # trial, draft, live, refunded, expired, released
        self.status = status
        # Reason for pause.
        self.suspend_reason = suspend_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_models is not None:
            result['AllowedModels'] = self.allowed_models

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.blocked_models is not None:
            result['BlockedModels'] = self.blocked_models

        if self.capability is not None:
            result['Capability'] = self.capability

        if self.daily_limit is not None:
            result['DailyLimit'] = self.daily_limit

        if self.daily_token_limit is not None:
            result['DailyTokenLimit'] = self.daily_token_limit

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_blacklist is not None:
            result['IpBlacklist'] = self.ip_blacklist

        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist

        if self.rpm_limit is not None:
            result['RpmLimit'] = self.rpm_limit

        if self.status is not None:
            result['Status'] = self.status

        if self.suspend_reason is not None:
            result['SuspendReason'] = self.suspend_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedModels') is not None:
            self.allowed_models = m.get('AllowedModels')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BlockedModels') is not None:
            self.blocked_models = m.get('BlockedModels')

        if m.get('Capability') is not None:
            self.capability = m.get('Capability')

        if m.get('DailyLimit') is not None:
            self.daily_limit = m.get('DailyLimit')

        if m.get('DailyTokenLimit') is not None:
            self.daily_token_limit = m.get('DailyTokenLimit')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpBlacklist') is not None:
            self.ip_blacklist = m.get('IpBlacklist')

        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')

        if m.get('RpmLimit') is not None:
            self.rpm_limit = m.get('RpmLimit')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SuspendReason') is not None:
            self.suspend_reason = m.get('SuspendReason')

        return self

