# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class QueryInspirationConsumeRecordsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        module: main_models.QueryInspirationConsumeRecordsResponseBodyModule = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # Detailed reason for access denial.
        self.access_denied_detail = access_denied_detail
        # Is retry allowed
        self.allow_retry = allow_retry
        # Application Name. Query the application with this name.
        self.app_name = app_name
        # Dynamic error code.
        self.dynamic_code = dynamic_code
        # Dynamic message. Not currently used. Please ignore.
        self.dynamic_message = dynamic_message
        # Returned error parameters
        self.error_args = error_args
        # Whether the deletion succeeded
        self.module = module
        # Id of the request
        self.request_id = request_id
        # Error code
        self.root_error_code = root_error_code
        # Abnormal message
        self.root_error_msg = root_error_msg
        # Is processed synchronously
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
            temp_model = main_models.QueryInspirationConsumeRecordsResponseBodyModule()
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

class QueryInspirationConsumeRecordsResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.QueryInspirationConsumeRecordsResponseBodyModuleData] = None,
        next: main_models.QueryInspirationConsumeRecordsResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # Current page number.
        self.current_page_num = current_page_num
        # Request Result.
        self.data = data
        # Next feature ID
        self.next = next
        # Indicates whether there is a next page.
        self.next_page = next_page
        # Paging size.
        self.page_size = page_size
        # Whether there is a previous page.
        self.pre_page = pre_page
        # In addition to paging limits, the server-side processes at most the latest 1 000 records for the current query. If the result exceeds 1 000 records, **ResultLimit** is **true**; you should narrow the Time Range and search again. Otherwise, **ResultLimit** is **false**.
        self.result_limit = result_limit
        # Total number of records.
        self.total_item_num = total_item_num
        # Total number of pages.
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
                temp_model = main_models.QueryInspirationConsumeRecordsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.QueryInspirationConsumeRecordsResponseBodyModuleNext()
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

class QueryInspirationConsumeRecordsResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        amount: int = None,
        amount_str: str = None,
        consume_time: str = None,
        consume_type: str = None,
        meta_data: str = None,
        scene_name: str = None,
    ):
        # Quantity of inspiration value consumed
        self.amount = amount
        self.amount_str = amount_str
        # Consumption Time
        self.consume_time = consume_time
        self.consume_type = consume_type
        # Extension information (in JSON string format)
        self.meta_data = meta_data
        # Consumption scenario Name (such as AI application development, AI creative image generation, AI Video creation, AI Content creation)
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.amount_str is not None:
            result['AmountStr'] = self.amount_str

        if self.consume_time is not None:
            result['ConsumeTime'] = self.consume_time

        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AmountStr') is not None:
            self.amount_str = m.get('AmountStr')

        if m.get('ConsumeTime') is not None:
            self.consume_time = m.get('ConsumeTime')

        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

class QueryInspirationConsumeRecordsResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        amount: int = None,
        amount_str: str = None,
        consume_time: str = None,
        consume_type: str = None,
        meta_data: str = None,
        record_key: str = None,
        scene_name: str = None,
    ):
        # Quantity of inspiration value consumed
        self.amount = amount
        self.amount_str = amount_str
        # Consumption time
        self.consume_time = consume_time
        self.consume_type = consume_type
        # Extension information (in JSON string format)
        self.meta_data = meta_data
        self.record_key = record_key
        # Consumption scenario Name (such as AI application development, AI creative image generation, AI Video creation, AI Content creation)
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.amount_str is not None:
            result['AmountStr'] = self.amount_str

        if self.consume_time is not None:
            result['ConsumeTime'] = self.consume_time

        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type

        if self.meta_data is not None:
            result['MetaData'] = self.meta_data

        if self.record_key is not None:
            result['RecordKey'] = self.record_key

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AmountStr') is not None:
            self.amount_str = m.get('AmountStr')

        if m.get('ConsumeTime') is not None:
            self.consume_time = m.get('ConsumeTime')

        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')

        if m.get('MetaData') is not None:
            self.meta_data = m.get('MetaData')

        if m.get('RecordKey') is not None:
            self.record_key = m.get('RecordKey')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        return self

