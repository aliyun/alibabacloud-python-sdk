# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListIsvPaymentPluginConfigsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: List[main_models.ListIsvPaymentPluginConfigsResponseBodyModule] = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether retry is allowed.
        self.allow_retry = allow_retry
        # App name.
        self.app_name = app_name
        # Dynamic code; currently unused. Ignore this field.
        self.dynamic_code = dynamic_code
        # Dynamic error message used to replace the `%s` placeholder in the **ErrMessage** error message.  
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the provided request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # Returned error parameters
        self.error_args = error_args
        # Number of results per query.  
        # 
        # Value range: 10–100. Default Value: 20.
        self.max_results = max_results
        # Response data
        self.module = module
        # Token for starting the next query. It is empty if there is no next query.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # Error code
        self.root_error_code = root_error_code
        # abnormal message
        self.root_error_msg = root_error_msg
        # Reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.ListIsvPaymentPluginConfigsResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListIsvPaymentPluginConfigsResponseBodyModule(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        extend: Dict[str, str] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        id: int = None,
        plugin_config: str = None,
        plugin_desc: str = None,
        plugin_id: str = None,
        plugin_name: str = None,
        site_name: str = None,
        user_id: str = None,
    ):
        # Business ID
        self.biz_id = biz_id
        # Extension information
        self.extend = extend
        # Creation Time
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_create_time = gmt_create_time
        # Updated At
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.gmt_modified_time = gmt_modified_time
        # Primary key
        self.id = id
        # Plugin configuration
        self.plugin_config = plugin_config
        # Plugin description
        self.plugin_desc = plugin_desc
        # Plugin ID
        self.plugin_id = plugin_id
        # Plugin name
        self.plugin_name = plugin_name
        # Site name
        self.site_name = site_name
        # User ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.id is not None:
            result['Id'] = self.id

        if self.plugin_config is not None:
            result['PluginConfig'] = self.plugin_config

        if self.plugin_desc is not None:
            result['PluginDesc'] = self.plugin_desc

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PluginConfig') is not None:
            self.plugin_config = m.get('PluginConfig')

        if m.get('PluginDesc') is not None:
            self.plugin_desc = m.get('PluginDesc')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

