# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveRealtimeDeliveryAccResponseBody(DaraModel):
    def __init__(
        self,
        real_time_delivery_acc_data: main_models.DescribeLiveRealtimeDeliveryAccResponseBodyRealTimeDeliveryAccData = None,
        request_id: str = None,
    ):
        # The information about real-time log deliveries.
        self.real_time_delivery_acc_data = real_time_delivery_acc_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.real_time_delivery_acc_data:
            self.real_time_delivery_acc_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.real_time_delivery_acc_data is not None:
            result['RealTimeDeliveryAccData'] = self.real_time_delivery_acc_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RealTimeDeliveryAccData') is not None:
            temp_model = main_models.DescribeLiveRealtimeDeliveryAccResponseBodyRealTimeDeliveryAccData()
            self.real_time_delivery_acc_data = temp_model.from_map(m.get('RealTimeDeliveryAccData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveRealtimeDeliveryAccResponseBodyRealTimeDeliveryAccData(DaraModel):
    def __init__(
        self,
        acc_data: List[main_models.DescribeLiveRealtimeDeliveryAccResponseBodyRealTimeDeliveryAccDataAccData] = None,
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
                temp_model = main_models.DescribeLiveRealtimeDeliveryAccResponseBodyRealTimeDeliveryAccDataAccData()
                self.acc_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveRealtimeDeliveryAccResponseBodyRealTimeDeliveryAccDataAccData(DaraModel):
    def __init__(
        self,
        failed_num: int = None,
        success_num: int = None,
        time_stamp: str = None,
    ):
        # The number of failed real-time log deliveries.
        self.failed_num = failed_num
        # The number of successful real-time log deliveries.
        self.success_num = success_num
        # The timestamp of the data returned.
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

