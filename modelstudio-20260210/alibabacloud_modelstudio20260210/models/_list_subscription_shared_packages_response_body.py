# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class ListSubscriptionSharedPackagesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListSubscriptionSharedPackagesResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The business data.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: The call is successful.
        # - false: The call failed.
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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListSubscriptionSharedPackagesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSubscriptionSharedPackagesResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListSubscriptionSharedPackagesResponseBodyDataItems] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The data entries.
        self.items = items
        # The page number. The value must be greater than 0 and cannot exceed the maximum value of the Integer data type. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The total number of seats.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListSubscriptionSharedPackagesResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSubscriptionSharedPackagesResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        equity_list: List[main_models.ListSubscriptionSharedPackagesResponseBodyDataItemsEquityList] = None,
        instance_code: str = None,
        status: str = None,
    ):
        # The currently active equity instances.
        self.equity_list = equity_list
        # The instance code of the seat.
        self.instance_code = instance_code
        # The seat status. Valid values:
        # 
        # - CREATING: being created.
        # - NORMAL: active.
        # - LIMIT: restricted due to overdue payment.
        # - RELEASE: released upon expiration.
        # - STOP: stopped upon expiration.
        # - REFUNDED: refunded.
        self.status = status

    def validate(self):
        if self.equity_list:
            for v1 in self.equity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EquityList'] = []
        if self.equity_list is not None:
            for k1 in self.equity_list:
                result['EquityList'].append(k1.to_map() if k1 else None)

        if self.instance_code is not None:
            result['InstanceCode'] = self.instance_code

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.equity_list = []
        if m.get('EquityList') is not None:
            for k1 in m.get('EquityList'):
                temp_model = main_models.ListSubscriptionSharedPackagesResponseBodyDataItemsEquityList()
                self.equity_list.append(temp_model.from_map(k1))

        if m.get('InstanceCode') is not None:
            self.instance_code = m.get('InstanceCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListSubscriptionSharedPackagesResponseBodyDataItemsEquityList(DaraModel):
    def __init__(
        self,
        cycle_end_time: int = None,
        cycle_instance_id: str = None,
        cycle_start_time: int = None,
        cycle_surplus_value: float = None,
        cycle_total_value: float = None,
        cycle_version: int = None,
        equity_type: str = None,
    ):
        # The end time of the current cycle, in milliseconds.
        self.cycle_end_time = cycle_end_time
        # The equity code (subscription code). This is not required for consumption in the credits scenario.
        self.cycle_instance_id = cycle_instance_id
        # The start time of the current cycle, in milliseconds.
        self.cycle_start_time = cycle_start_time
        # The remaining quota of the current cycle.
        self.cycle_surplus_value = cycle_surplus_value
        # The total quota of the current cycle.
        self.cycle_total_value = cycle_total_value
        # The sequential version of the current cycle.
        self.cycle_version = cycle_version
        # The equity type, such as CREDITS, SPN, or resource plan.
        self.equity_type = equity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_end_time is not None:
            result['CycleEndTime'] = self.cycle_end_time

        if self.cycle_instance_id is not None:
            result['CycleInstanceId'] = self.cycle_instance_id

        if self.cycle_start_time is not None:
            result['CycleStartTime'] = self.cycle_start_time

        if self.cycle_surplus_value is not None:
            result['CycleSurplusValue'] = self.cycle_surplus_value

        if self.cycle_total_value is not None:
            result['CycleTotalValue'] = self.cycle_total_value

        if self.cycle_version is not None:
            result['CycleVersion'] = self.cycle_version

        if self.equity_type is not None:
            result['EquityType'] = self.equity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleEndTime') is not None:
            self.cycle_end_time = m.get('CycleEndTime')

        if m.get('CycleInstanceId') is not None:
            self.cycle_instance_id = m.get('CycleInstanceId')

        if m.get('CycleStartTime') is not None:
            self.cycle_start_time = m.get('CycleStartTime')

        if m.get('CycleSurplusValue') is not None:
            self.cycle_surplus_value = m.get('CycleSurplusValue')

        if m.get('CycleTotalValue') is not None:
            self.cycle_total_value = m.get('CycleTotalValue')

        if m.get('CycleVersion') is not None:
            self.cycle_version = m.get('CycleVersion')

        if m.get('EquityType') is not None:
            self.equity_type = m.get('EquityType')

        return self

