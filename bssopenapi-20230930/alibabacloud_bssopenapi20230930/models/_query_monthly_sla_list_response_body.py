# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class QueryMonthlySlaListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.QueryMonthlySlaListResponseBodyData] = None,
        metadata: Any = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.metadata = metadata
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryMonthlySlaListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryMonthlySlaListResponseBodyData(DaraModel):
    def __init__(
        self,
        available_rate: float = None,
        damaged_id: str = None,
        instance_id: str = None,
        month: int = None,
        monthly_service_charge: float = None,
        pay_description: str = None,
        pay_rate: float = None,
        pay_status: int = None,
        product_code: str = None,
        should_pay_sum: float = None,
    ):
        self.available_rate = available_rate
        self.damaged_id = damaged_id
        self.instance_id = instance_id
        self.month = month
        self.monthly_service_charge = monthly_service_charge
        self.pay_description = pay_description
        self.pay_rate = pay_rate
        self.pay_status = pay_status
        self.product_code = product_code
        self.should_pay_sum = should_pay_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_rate is not None:
            result['AvailableRate'] = self.available_rate

        if self.damaged_id is not None:
            result['DamagedId'] = self.damaged_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.month is not None:
            result['Month'] = self.month

        if self.monthly_service_charge is not None:
            result['MonthlyServiceCharge'] = self.monthly_service_charge

        if self.pay_description is not None:
            result['PayDescription'] = self.pay_description

        if self.pay_rate is not None:
            result['PayRate'] = self.pay_rate

        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.should_pay_sum is not None:
            result['ShouldPaySum'] = self.should_pay_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableRate') is not None:
            self.available_rate = m.get('AvailableRate')

        if m.get('DamagedId') is not None:
            self.damaged_id = m.get('DamagedId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('MonthlyServiceCharge') is not None:
            self.monthly_service_charge = m.get('MonthlyServiceCharge')

        if m.get('PayDescription') is not None:
            self.pay_description = m.get('PayDescription')

        if m.get('PayRate') is not None:
            self.pay_rate = m.get('PayRate')

        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ShouldPaySum') is not None:
            self.should_pay_sum = m.get('ShouldPaySum')

        return self

