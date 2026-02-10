# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomBlockRecordsResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeCustomBlockRecordsResponseBodyPageInfo = None,
        record_list: List[main_models.DescribeCustomBlockRecordsResponseBodyRecordList] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # An array that consists of the defense rules.
        self.record_list = record_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.record_list:
            for v1 in self.record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['RecordList'] = []
        if self.record_list is not None:
            for k1 in self.record_list:
                result['RecordList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeCustomBlockRecordsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.record_list = []
        if m.get('RecordList') is not None:
            for k1 in m.get('RecordList'):
                temp_model = main_models.DescribeCustomBlockRecordsResponseBodyRecordList()
                self.record_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCustomBlockRecordsResponseBodyRecordList(DaraModel):
    def __init__(
        self,
        block_expire_date: int = None,
        block_ip: str = None,
        bound: str = None,
        enable_count: int = None,
        id: int = None,
        server_count: int = None,
        source: str = None,
        status: int = None,
        target_list: List[main_models.DescribeCustomBlockRecordsResponseBodyRecordListTargetList] = None,
    ):
        # The timestamp generated when the block action on the IP address becomes invalid.
        self.block_expire_date = block_expire_date
        # The blocked IP address.
        self.block_ip = block_ip
        # The direction of the traffic that is sent by the blocked IP address. Valid values:
        # 
        # *   **in**
        # *   **out**
        self.bound = bound
        # The number of servers for which the defense rule is enabled.
        self.enable_count = enable_count
        # The record ID.
        self.id = id
        # The total number of servers on which the IP address is blocked.
        self.server_count = server_count
        # The source of the defense rule.
        self.source = source
        # The status of the defense rule against brute-force attacks. Valid values:
        # 
        # *   **0**: invalid.
        # *   **1**: enabled.
        # *   **2**: failed.
        self.status = status
        # The servers for which the defense rule is enabled.
        self.target_list = target_list

    def validate(self):
        if self.target_list:
            for v1 in self.target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_expire_date is not None:
            result['BlockExpireDate'] = self.block_expire_date

        if self.block_ip is not None:
            result['BlockIp'] = self.block_ip

        if self.bound is not None:
            result['Bound'] = self.bound

        if self.enable_count is not None:
            result['EnableCount'] = self.enable_count

        if self.id is not None:
            result['Id'] = self.id

        if self.server_count is not None:
            result['ServerCount'] = self.server_count

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        result['TargetList'] = []
        if self.target_list is not None:
            for k1 in self.target_list:
                result['TargetList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockExpireDate') is not None:
            self.block_expire_date = m.get('BlockExpireDate')

        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('Bound') is not None:
            self.bound = m.get('Bound')

        if m.get('EnableCount') is not None:
            self.enable_count = m.get('EnableCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.target_list = []
        if m.get('TargetList') is not None:
            for k1 in m.get('TargetList'):
                temp_model = main_models.DescribeCustomBlockRecordsResponseBodyRecordListTargetList()
                self.target_list.append(temp_model.from_map(k1))

        return self

class DescribeCustomBlockRecordsResponseBodyRecordListTargetList(DaraModel):
    def __init__(
        self,
        target: str = None,
        target_type: str = None,
    ):
        # The ID of the destination asset.
        self.target = target
        # The type of the query. Valid values:
        # 
        # *   Set the value to **uuid**.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class DescribeCustomBlockRecordsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
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
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

