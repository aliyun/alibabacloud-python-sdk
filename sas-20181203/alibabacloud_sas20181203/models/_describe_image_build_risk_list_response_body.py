# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageBuildRiskListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeImageBuildRiskListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. The status code **200** indicates that the request was successful. Other status codes indicate that the request failed. You can identify the cause of the failure based on the status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.DescribeImageBuildRiskListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeImageBuildRiskListResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.DescribeImageBuildRiskListResponseBodyDataList] = None,
        page_info: main_models.DescribeImageBuildRiskListResponseBodyDataPageInfo = None,
    ):
        # The risks.
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
                temp_model = main_models.DescribeImageBuildRiskListResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageBuildRiskListResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        return self

class DescribeImageBuildRiskListResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImageBuildRiskListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        count: int = None,
        first_scan_time: int = None,
        last_scan_time: int = None,
        risk_class: str = None,
        risk_class_name: str = None,
        risk_key: str = None,
        risk_key_name: str = None,
        risk_level: str = None,
        unprocessed_num: int = None,
    ):
        # The number of affected images.
        self.count = count
        # The timestamp generated when the first scan was performed. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The timestamp generated when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The type key of the risk.
        self.risk_class = risk_class
        # The type name of the risk.
        self.risk_class_name = risk_class_name
        # The key of the risk. You can call the [DescribeImageBuildRiskList](~~~~) operation to obtain the value of **RiskKey**.
        self.risk_key = risk_key
        # The rule name of the risk.
        self.risk_key_name = risk_key_name
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # The number of unprocessed images.
        self.unprocessed_num = unprocessed_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.risk_class is not None:
            result['RiskClass'] = self.risk_class

        if self.risk_class_name is not None:
            result['RiskClassName'] = self.risk_class_name

        if self.risk_key is not None:
            result['RiskKey'] = self.risk_key

        if self.risk_key_name is not None:
            result['RiskKeyName'] = self.risk_key_name

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.unprocessed_num is not None:
            result['UnprocessedNum'] = self.unprocessed_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('RiskClass') is not None:
            self.risk_class = m.get('RiskClass')

        if m.get('RiskClassName') is not None:
            self.risk_class_name = m.get('RiskClassName')

        if m.get('RiskKey') is not None:
            self.risk_key = m.get('RiskKey')

        if m.get('RiskKeyName') is not None:
            self.risk_key_name = m.get('RiskKeyName')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('UnprocessedNum') is not None:
            self.unprocessed_num = m.get('UnprocessedNum')

        return self

