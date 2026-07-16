# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetValidDeductInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetValidDeductInstancesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetValidDeductInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetValidDeductInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        body: main_models.GetValidDeductInstancesResponseBodyDataBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.GetValidDeductInstancesResponseBodyDataBody()
            self.body = temp_model.from_map(m.get('Body'))

        return self

class GetValidDeductInstancesResponseBodyDataBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetValidDeductInstancesResponseBodyDataBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetValidDeductInstancesResponseBodyDataBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetValidDeductInstancesResponseBodyDataBodyData(DaraModel):
    def __init__(
        self,
        can_try: bool = None,
        deduct_package_list: List[main_models.GetValidDeductInstancesResponseBodyDataBodyDataDeductPackageList] = None,
    ):
        self.can_try = can_try
        self.deduct_package_list = deduct_package_list

    def validate(self):
        if self.deduct_package_list:
            for v1 in self.deduct_package_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_try is not None:
            result['CanTry'] = self.can_try

        result['DeductPackageList'] = []
        if self.deduct_package_list is not None:
            for k1 in self.deduct_package_list:
                result['DeductPackageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')

        self.deduct_package_list = []
        if m.get('DeductPackageList') is not None:
            for k1 in m.get('DeductPackageList'):
                temp_model = main_models.GetValidDeductInstancesResponseBodyDataBodyDataDeductPackageList()
                self.deduct_package_list.append(temp_model.from_map(k1))

        return self

class GetValidDeductInstancesResponseBodyDataBodyDataDeductPackageList(DaraModel):
    def __init__(
        self,
        current_period_used: int = None,
        end_time: int = None,
        init_capacity: float = None,
        instance_id: str = None,
        module: str = None,
        period_capacity: float = None,
        start_time: int = None,
        status: str = None,
    ):
        self.current_period_used = current_period_used
        self.end_time = end_time
        self.init_capacity = init_capacity
        self.instance_id = instance_id
        self.module = module
        self.period_capacity = period_capacity
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_period_used is not None:
            result['CurrentPeriodUsed'] = self.current_period_used

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module is not None:
            result['Module'] = self.module

        if self.period_capacity is not None:
            result['PeriodCapacity'] = self.period_capacity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPeriodUsed') is not None:
            self.current_period_used = m.get('CurrentPeriodUsed')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('PeriodCapacity') is not None:
            self.period_capacity = m.get('PeriodCapacity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

