# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetFootprintListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFootprintListResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetFootprintListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetFootprintListResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[main_models.GetFootprintListResponseBodyDataRecords] = None,
        total: int = None,
        total_page: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries returned on each page.
        self.page_size = page_size
        # Product Detail List.
        self.records = records
        # The total number of entries returned.
        self.total = total
        # Total Pages
        self.total_page = total_page

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetFootprintListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class GetFootprintListResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        amount: float = None,
        auth_status: int = None,
        check_end_time: str = None,
        check_start_time: str = None,
        code: str = None,
        created_by: str = None,
        id: int = None,
        is_demo_model: int = None,
        life_cycle: str = None,
        life_cycle_type: int = None,
        name: str = None,
        type: str = None,
        unit: str = None,
    ):
        # The amount of the product.
        self.amount = amount
        # Authentication status enumeration value, please refer to [link](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.auth_status = auth_status
        # Calculation end time.
        self.check_end_time = check_end_time
        # Calculation start time.
        self.check_start_time = check_start_time
        # The enterprise code.
        self.code = code
        # The user who created it.
        self.created_by = created_by
        # The product ID.
        self.id = id
        # Indicates whether the demo model is a built-in model. A value of 1 indicates a true value and a value of 0 indicates a false value.
        self.is_demo_model = is_demo_model
        # The literal expression corresponding to lifeCycleType, `From Cradle to Gate` and `From Cradle to Grave`.
        self.life_cycle = life_cycle
        # 1 is `From Cradle to Gate`, and 2 is `From Cradle to Grave`.
        self.life_cycle_type = life_cycle_type
        # The product name.
        self.name = name
        # Product category enumeration value, please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.type = type
        # Unit enumeration value. Please refer to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['amount'] = self.amount

        if self.auth_status is not None:
            result['authStatus'] = self.auth_status

        if self.check_end_time is not None:
            result['checkEndTime'] = self.check_end_time

        if self.check_start_time is not None:
            result['checkStartTime'] = self.check_start_time

        if self.code is not None:
            result['code'] = self.code

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.id is not None:
            result['id'] = self.id

        if self.is_demo_model is not None:
            result['isDemoModel'] = self.is_demo_model

        if self.life_cycle is not None:
            result['lifeCycle'] = self.life_cycle

        if self.life_cycle_type is not None:
            result['lifeCycleType'] = self.life_cycle_type

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')

        if m.get('authStatus') is not None:
            self.auth_status = m.get('authStatus')

        if m.get('checkEndTime') is not None:
            self.check_end_time = m.get('checkEndTime')

        if m.get('checkStartTime') is not None:
            self.check_start_time = m.get('checkStartTime')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isDemoModel') is not None:
            self.is_demo_model = m.get('isDemoModel')

        if m.get('lifeCycle') is not None:
            self.life_cycle = m.get('lifeCycle')

        if m.get('lifeCycleType') is not None:
            self.life_cycle_type = m.get('lifeCycleType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

