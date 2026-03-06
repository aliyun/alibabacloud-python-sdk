# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppCommoditySpecificationsV2ForPartnerResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: main_models.ListAppCommoditySpecificationsV2ForPartnerResponseBodyModule = None,
        next_token: str = None,
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
        self.max_results = max_results
        self.module = module
        self.next_token = next_token
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

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

        if m.get('Module') is not None:
            temp_model = main_models.ListAppCommoditySpecificationsV2ForPartnerResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

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

class ListAppCommoditySpecificationsV2ForPartnerResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.ListAppCommoditySpecificationsV2ForPartnerResponseBodyModuleData] = None,
        next: main_models.ListAppCommoditySpecificationsV2ForPartnerResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next = next
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppCommoditySpecificationsV2ForPartnerResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.ListAppCommoditySpecificationsV2ForPartnerResponseBodyModuleNext()
            self.next = temp_model.from_map(m.get('Next'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class ListAppCommoditySpecificationsV2ForPartnerResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        code: str = None,
        components: Dict[str, main_models.ModuleNextComponentsValue] = None,
        name: str = None,
        properties: Dict[str, main_models.ModuleNextPropertiesValue] = None,
    ):
        self.code = code
        self.components = components
        self.name = name
        self.properties = properties

    def validate(self):
        if self.components:
            for v1 in self.components.values():
                 if v1:
                    v1.validate()
        if self.properties:
            for v1 in self.properties.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Components'] = {}
        if self.components is not None:
            for k1, v1 in self.components.items():
                result['Components'][k1] = v1.to_map() if v1 else None

        if self.name is not None:
            result['Name'] = self.name

        result['Properties'] = {}
        if self.properties is not None:
            for k1, v1 in self.properties.items():
                result['Properties'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.components = {}
        if m.get('Components') is not None:
            for k1, v1 in m.get('Components').items():
                temp_model = main_models.ModuleNextComponentsValue()
                self.components[k1] = temp_model.from_map(v1)

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.properties = {}
        if m.get('Properties') is not None:
            for k1, v1 in m.get('Properties').items():
                temp_model = main_models.ModuleNextPropertiesValue()
                self.properties[k1] = temp_model.from_map(v1)

        return self

class ListAppCommoditySpecificationsV2ForPartnerResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        code: str = None,
        components: Dict[str, main_models.ModuleDataComponentsValue] = None,
        name: str = None,
        properties: Dict[str, main_models.ModuleDataPropertiesValue] = None,
    ):
        self.code = code
        self.components = components
        self.name = name
        self.properties = properties

    def validate(self):
        if self.components:
            for v1 in self.components.values():
                 if v1:
                    v1.validate()
        if self.properties:
            for v1 in self.properties.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Components'] = {}
        if self.components is not None:
            for k1, v1 in self.components.items():
                result['Components'][k1] = v1.to_map() if v1 else None

        if self.name is not None:
            result['Name'] = self.name

        result['Properties'] = {}
        if self.properties is not None:
            for k1, v1 in self.properties.items():
                result['Properties'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.components = {}
        if m.get('Components') is not None:
            for k1, v1 in m.get('Components').items():
                temp_model = main_models.ModuleDataComponentsValue()
                self.components[k1] = temp_model.from_map(v1)

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.properties = {}
        if m.get('Properties') is not None:
            for k1, v1 in m.get('Properties').items():
                temp_model = main_models.ModuleDataPropertiesValue()
                self.properties[k1] = temp_model.from_map(v1)

        return self

