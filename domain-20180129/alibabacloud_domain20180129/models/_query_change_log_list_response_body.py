# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryChangeLogListResponseBody(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: main_models.QueryChangeLogListResponseBodyData = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        request_id: str = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        self.current_page_num = current_page_num
        self.data = data
        self.next_page = next_page
        self.page_size = page_size
        self.pre_page = pre_page
        self.request_id = request_id
        self.result_limit = result_limit
        self.total_item_num = total_item_num
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('Data') is not None:
            temp_model = main_models.QueryChangeLogListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class QueryChangeLogListResponseBodyData(DaraModel):
    def __init__(
        self,
        change_log: List[main_models.QueryChangeLogListResponseBodyDataChangeLog] = None,
    ):
        self.change_log = change_log

    def validate(self):
        if self.change_log:
            for v1 in self.change_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChangeLog'] = []
        if self.change_log is not None:
            for k1 in self.change_log:
                result['ChangeLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_log = []
        if m.get('ChangeLog') is not None:
            for k1 in m.get('ChangeLog'):
                temp_model = main_models.QueryChangeLogListResponseBodyDataChangeLog()
                self.change_log.append(temp_model.from_map(k1))

        return self

class QueryChangeLogListResponseBodyDataChangeLog(DaraModel):
    def __init__(
        self,
        details: str = None,
        domain_name: str = None,
        operation: str = None,
        operation_ipaddress: str = None,
        remark: str = None,
        result: str = None,
        time: str = None,
    ):
        self.details = details
        self.domain_name = domain_name
        self.operation = operation
        self.operation_ipaddress = operation_ipaddress
        self.remark = remark
        self.result = result
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.details is not None:
            result['Details'] = self.details

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.operation_ipaddress is not None:
            result['OperationIPAddress'] = self.operation_ipaddress

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.result is not None:
            result['Result'] = self.result

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('OperationIPAddress') is not None:
            self.operation_ipaddress = m.get('OperationIPAddress')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

