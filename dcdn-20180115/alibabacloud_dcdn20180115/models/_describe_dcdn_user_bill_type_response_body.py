# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnUserBillTypeResponseBody(DaraModel):
    def __init__(
        self,
        bill_type_data: main_models.DescribeDcdnUserBillTypeResponseBodyBillTypeData = None,
        request_id: str = None,
    ):
        # The information about the metering method.
        self.bill_type_data = bill_type_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bill_type_data:
            self.bill_type_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_type_data is not None:
            result['BillTypeData'] = self.bill_type_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillTypeData') is not None:
            temp_model = main_models.DescribeDcdnUserBillTypeResponseBodyBillTypeData()
            self.bill_type_data = temp_model.from_map(m.get('BillTypeData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnUserBillTypeResponseBodyBillTypeData(DaraModel):
    def __init__(
        self,
        bill_type_data_item: List[main_models.DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem] = None,
    ):
        self.bill_type_data_item = bill_type_data_item

    def validate(self):
        if self.bill_type_data_item:
            for v1 in self.bill_type_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BillTypeDataItem'] = []
        if self.bill_type_data_item is not None:
            for k1 in self.bill_type_data_item:
                result['BillTypeDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_type_data_item = []
        if m.get('BillTypeDataItem') is not None:
            for k1 in m.get('BillTypeDataItem'):
                temp_model = main_models.DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem()
                self.bill_type_data_item.append(temp_model.from_map(k1))

        return self

class DescribeDcdnUserBillTypeResponseBodyBillTypeDataBillTypeDataItem(DaraModel):
    def __init__(
        self,
        bill_type: str = None,
        billing_cycle: str = None,
        dimension: str = None,
        end_time: str = None,
        product: str = None,
        start_time: str = None,
    ):
        # The metering method. Valid values:
        # 
        # *   **hour_flow**: pay by hourly traffic
        # *   **day_bandwidth**: pay by daily bandwidth
        # *   **month_95**: pay by monthly 95th percentile
        # *   **month_avg_day_bandwidth**: pay by average daily peak bandwidth per month
        # *   **month_4th_day_bandwidth**: pay by 4th peak bandwidth per month
        # *   **month_avg_day_95**: pay by average daily 95th percentile per month
        # *   **month_95_night_half**: pay by 95th percentile (50% off during nighttime)
        # *   **hour_vas**: pay by value-added service per month
        # *   **quic_hour_count**: pay by QUIC request per hour
        # *   **hour_count**: pay by request per hour
        # *   **rtlog_count_day**: pay by the number of real-time logs per day
        self.bill_type = bill_type
        # The metering cycle.
        self.billing_cycle = billing_cycle
        # The dimension. Valid values:
        # 
        # *   **flow**: network traffic and bandwidth
        # *   **vas**: value-added services (HTTPS and requests for dynamic content)
        # *   **websocket**: WebSocket
        # *   **quic**: QUIC requests
        # *   **rtlog2sls**: log entries delivered to Log Service in real time
        self.dimension = dimension
        # The time when the metering method ends.
        self.end_time = end_time
        # The name of the service.
        self.product = product
        # The time when the metering method takes effect.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.product is not None:
            result['Product'] = self.product

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

