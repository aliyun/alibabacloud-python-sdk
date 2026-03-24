# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnUserBillPredictionResponseBody(DaraModel):
    def __init__(
        self,
        bill_prediction_data: main_models.DescribeCdnUserBillPredictionResponseBodyBillPredictionData = None,
        bill_type: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.bill_prediction_data = bill_prediction_data
        # The metering method.
        # 
        # > If the metering method ends with _overseas, the billable region is outside the Chinese mainland. For example, BillType": "month_avg_day_bandwidth_overseas specifies a billable region outside the Chinese mainland and that the metering method is pay by daily peak bandwidth per month.
        # 
        # Valid values:
        # 
        # *   hour_flow: pay by hourly data transfer
        # *   day_bandwidth: pay by daily bandwidth
        # *   month_95: pay by monthly 95th percentile bandwidth.
        # *   month_avg_day_bandwidth: pay by average daily peak bandwidth per month
        # *   month_4th_day_bandwidth: pay by monthly 4th peak bandwidth
        # *   month_avg_day_95: pay by average daily 95th percentile bandwidth per month
        # *   month_95_night_half: pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00.
        # *   hour_vas: pay by value-added services per hour
        # *   day_count: pay by daily requests
        self.bill_type = bill_type
        # The end time of the estimation.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The start time of the estimation.
        self.start_time = start_time

    def validate(self):
        if self.bill_prediction_data:
            self.bill_prediction_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_prediction_data is not None:
            result['BillPredictionData'] = self.bill_prediction_data.to_map()

        if self.bill_type is not None:
            result['BillType'] = self.bill_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillPredictionData') is not None:
            temp_model = main_models.DescribeCdnUserBillPredictionResponseBodyBillPredictionData()
            self.bill_prediction_data = temp_model.from_map(m.get('BillPredictionData'))

        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeCdnUserBillPredictionResponseBodyBillPredictionData(DaraModel):
    def __init__(
        self,
        bill_prediction_data_item: List[main_models.DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem] = None,
    ):
        self.bill_prediction_data_item = bill_prediction_data_item

    def validate(self):
        if self.bill_prediction_data_item:
            for v1 in self.bill_prediction_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BillPredictionDataItem'] = []
        if self.bill_prediction_data_item is not None:
            for k1 in self.bill_prediction_data_item:
                result['BillPredictionDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_prediction_data_item = []
        if m.get('BillPredictionDataItem') is not None:
            for k1 in m.get('BillPredictionDataItem'):
                temp_model = main_models.DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem()
                self.bill_prediction_data_item.append(temp_model.from_map(k1))

        return self

class DescribeCdnUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem(DaraModel):
    def __init__(
        self,
        area: str = None,
        time_stp: str = None,
        value: float = None,
    ):
        self.area = area
        self.time_stp = time_stp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.time_stp is not None:
            result['TimeStp'] = self.time_stp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('TimeStp') is not None:
            self.time_stp = m.get('TimeStp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

