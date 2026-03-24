# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeRealtimeDeliveryAccResponseBody(DaraModel):
    def __init__(
        self,
        reat_time_delivery_acc_data: main_models.DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData = None,
        request_id: str = None,
    ):
        self.reat_time_delivery_acc_data = reat_time_delivery_acc_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.reat_time_delivery_acc_data:
            self.reat_time_delivery_acc_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reat_time_delivery_acc_data is not None:
            result['ReatTimeDeliveryAccData'] = self.reat_time_delivery_acc_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReatTimeDeliveryAccData') is not None:
            temp_model = main_models.DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData()
            self.reat_time_delivery_acc_data = temp_model.from_map(m.get('ReatTimeDeliveryAccData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccData(DaraModel):
    def __init__(
        self,
        acc_data: List[main_models.DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData] = None,
    ):
        self.acc_data = acc_data

    def validate(self):
        if self.acc_data:
            for v1 in self.acc_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccData'] = []
        if self.acc_data is not None:
            for k1 in self.acc_data:
                result['AccData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acc_data = []
        if m.get('AccData') is not None:
            for k1 in m.get('AccData'):
                temp_model = main_models.DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData()
                self.acc_data.append(temp_model.from_map(k1))

        return self

class DescribeRealtimeDeliveryAccResponseBodyReatTimeDeliveryAccDataAccData(DaraModel):
    def __init__(
        self,
        failed_num: int = None,
        success_num: int = None,
        time_stamp: str = None,
    ):
        self.failed_num = failed_num
        self.success_num = success_num
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num

        if self.success_num is not None:
            result['SuccessNum'] = self.success_num

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')

        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

