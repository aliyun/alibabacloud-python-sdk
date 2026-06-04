# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class GetAppInstanceEntitlementResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.GetAppInstanceEntitlementResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.allow_retry = allow_retry
        self.app_name = app_name
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_args = error_args
        self.module = module
        # Id of the request
        self.request_id = request_id
        self.root_error_code = root_error_code
        self.root_error_msg = root_error_msg
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
            temp_model = main_models.GetAppInstanceEntitlementResponseBodyModule()
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

class GetAppInstanceEntitlementResponseBodyModule(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        items: List[main_models.GetAppInstanceEntitlementResponseBodyModuleItems] = None,
    ):
        self.biz_id = biz_id
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetAppInstanceEntitlementResponseBodyModuleItems()
                self.items.append(temp_model.from_map(k1))

        return self

class GetAppInstanceEntitlementResponseBodyModuleItems(DaraModel):
    def __init__(
        self,
        allocated: bool = None,
        available: bool = None,
        code: str = None,
        configured: bool = None,
        entitled: bool = None,
        feature_type: str = None,
        instance_id: str = None,
        name: str = None,
        plugin_id: str = None,
        quota: int = None,
        remaining: int = None,
        resource_code: str = None,
        resource_type: str = None,
        running: bool = None,
        type: str = None,
        usage_percent: int = None,
        used: int = None,
    ):
        self.allocated = allocated
        self.available = available
        self.code = code
        self.configured = configured
        self.entitled = entitled
        self.feature_type = feature_type
        self.instance_id = instance_id
        self.name = name
        self.plugin_id = plugin_id
        self.quota = quota
        self.remaining = remaining
        self.resource_code = resource_code
        self.resource_type = resource_type
        self.running = running
        self.type = type
        self.usage_percent = usage_percent
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocated is not None:
            result['Allocated'] = self.allocated

        if self.available is not None:
            result['Available'] = self.available

        if self.code is not None:
            result['Code'] = self.code

        if self.configured is not None:
            result['Configured'] = self.configured

        if self.entitled is not None:
            result['Entitled'] = self.entitled

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.remaining is not None:
            result['Remaining'] = self.remaining

        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.running is not None:
            result['Running'] = self.running

        if self.type is not None:
            result['Type'] = self.type

        if self.usage_percent is not None:
            result['UsagePercent'] = self.usage_percent

        if self.used is not None:
            result['Used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Allocated') is not None:
            self.allocated = m.get('Allocated')

        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Configured') is not None:
            self.configured = m.get('Configured')

        if m.get('Entitled') is not None:
            self.entitled = m.get('Entitled')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('Remaining') is not None:
            self.remaining = m.get('Remaining')

        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsagePercent') is not None:
            self.usage_percent = m.get('UsagePercent')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

