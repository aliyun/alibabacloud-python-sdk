# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class QueryPenetrationTestListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryPenetrationTestListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        # 
        # - **200**: Success.
        # - **Other values (such as 400 and 500)**: Failure.
        self.code = code
        # The query results.
        self.data = data
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # - **true**: The call is successful.                               
        # - **false**: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryPenetrationTestListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPenetrationTestListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryPenetrationTestListResponseBodyDataList] = None,
        page_info: main_models.QueryPenetrationTestListResponseBodyDataPageInfo = None,
    ):
        # The event data.
        self.list = list
        # The pagination information.
        self.page_info = page_info

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryPenetrationTestListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.QueryPenetrationTestListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        return self

class QueryPenetrationTestListResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The page number from which the query results are displayed.
        # 
        # > Default value: 1, which indicates that the query results are displayed starting from the first page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of events.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryPenetrationTestListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        apply_time: int = None,
        asset_type: str = None,
        id: int = None,
        ip: str = None,
        status: str = None,
        test_end_date: int = None,
        test_start_date: int = None,
    ):
        # The application time.
        self.apply_time = apply_time
        # The type of the asset. Valid values:
        # 
        # - **EIP**: The public IP address of a VPC.
        # - **SLB**: Server Load Balancer.
        # - **ECS**: The public IP address of an ECS instance in the classic network.
        self.asset_type = asset_type
        # The unique identifier of the alert event record.
        # 
        # > The data type of this field is Long. Precision loss may occur during the serialization or deserialization process. Make sure that the value does not exceed 9007199254740991.
        self.id = id
        # The IP address of the asset.
        self.ip = ip
        # The status of the task. Valid values:
        # 
        # - **early_end**: The user applied for early termination.
        # - **expired**: The authorization expired.
        # - **auditing**: The application is being reviewed.
        # - **approved**: The application is approved.
        # - **rejected**: The application is rejected.
        self.status = status
        # The end time of the test.
        self.test_end_date = test_end_date
        # The start date of the test.
        self.test_start_date = test_start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.status is not None:
            result['Status'] = self.status

        if self.test_end_date is not None:
            result['TestEndDate'] = self.test_end_date

        if self.test_start_date is not None:
            result['TestStartDate'] = self.test_start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TestEndDate') is not None:
            self.test_end_date = m.get('TestEndDate')

        if m.get('TestStartDate') is not None:
            self.test_start_date = m.get('TestStartDate')

        return self

