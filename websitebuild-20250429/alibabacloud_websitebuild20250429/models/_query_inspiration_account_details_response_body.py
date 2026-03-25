# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class QueryInspirationAccountDetailsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.QueryInspirationAccountDetailsResponseBodyModule = None,
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
            temp_model = main_models.QueryInspirationAccountDetailsResponseBodyModule()
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

class QueryInspirationAccountDetailsResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryInspirationAccountDetailsResponseBodyModuleData] = None,
        next: main_models.QueryInspirationAccountDetailsResponseBodyModuleNext = None,
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
                temp_model = main_models.QueryInspirationAccountDetailsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.QueryInspirationAccountDetailsResponseBodyModuleNext()
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

class QueryInspirationAccountDetailsResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        acquisition_time: str = None,
        balance: int = None,
        end_date: str = None,
        expired: bool = None,
        init_quota: int = None,
        source_type: str = None,
        source_type_name: str = None,
    ):
        self.acquisition_time = acquisition_time
        self.balance = balance
        self.end_date = end_date
        self.expired = expired
        self.init_quota = init_quota
        self.source_type = source_type
        self.source_type_name = source_type_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acquisition_time is not None:
            result['AcquisitionTime'] = self.acquisition_time

        if self.balance is not None:
            result['Balance'] = self.balance

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.init_quota is not None:
            result['InitQuota'] = self.init_quota

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_type_name is not None:
            result['SourceTypeName'] = self.source_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcquisitionTime') is not None:
            self.acquisition_time = m.get('AcquisitionTime')

        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('InitQuota') is not None:
            self.init_quota = m.get('InitQuota')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceTypeName') is not None:
            self.source_type_name = m.get('SourceTypeName')

        return self

class QueryInspirationAccountDetailsResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        acquisition_time: str = None,
        balance: int = None,
        end_date: str = None,
        expired: bool = None,
        init_quota: int = None,
        source_type: str = None,
        source_type_name: str = None,
        status: str = None,
    ):
        self.acquisition_time = acquisition_time
        self.balance = balance
        self.end_date = end_date
        self.expired = expired
        self.init_quota = init_quota
        self.source_type = source_type
        self.source_type_name = source_type_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acquisition_time is not None:
            result['AcquisitionTime'] = self.acquisition_time

        if self.balance is not None:
            result['Balance'] = self.balance

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.init_quota is not None:
            result['InitQuota'] = self.init_quota

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_type_name is not None:
            result['SourceTypeName'] = self.source_type_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcquisitionTime') is not None:
            self.acquisition_time = m.get('AcquisitionTime')

        if m.get('Balance') is not None:
            self.balance = m.get('Balance')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('InitQuota') is not None:
            self.init_quota = m.get('InitQuota')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceTypeName') is not None:
            self.source_type_name = m.get('SourceTypeName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

