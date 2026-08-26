# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveUserBillPredictionResponseBody(DaraModel):
    def __init__(
        self,
        bill_prediction_data: main_models.DescribeLiveUserBillPredictionResponseBodyBillPredictionData = None,
        bill_type: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.bill_prediction_data = bill_prediction_data
        # The billing method. The following billing methods are supported:
        # 
        # - hour_flow: Pay-by-traffic on an hourly basis.
        # 
        # - day_bandwidth: Pay-by-bandwidth on a daily basis.
        # 
        # - month_95: Pay-by-monthly 95th percentile peak bandwidth.
        # 
        # - month_avg_day_bandwidth: Pay-by-monthly average of daily peak bandwidth.
        # 
        # - month_4th_day_bandwidth: Pay-by-monthly 4th peak bandwidth.
        # 
        # - month_avg_day_95: Pay-by-monthly average of daily 95th percentile peak bandwidth.
        # 
        # - month_95_night_half: Pay-by-nightly 95th percentile peak bandwidth with a 50% discount.
        # 
        # - hour_vas: Pay-for-value-added services on an hourly basis.
        # 
        # - day_count: Pay-by-daily request count.
        self.bill_type = bill_type
        # The end time of the query. The time is in UTC and follows the ISO 8601 standard.
        # Format: YYYY-MM-DDThh:mm:ssZ. The default value is the current time.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The start time of the query. The time is in UTC and follows the ISO 8601 standard.
        # Format: YYYY-MM-DDThh:mm:ssZ. The default value is 00:00 on the first day of the month.
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
            temp_model = main_models.DescribeLiveUserBillPredictionResponseBodyBillPredictionData()
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

class DescribeLiveUserBillPredictionResponseBodyBillPredictionData(DaraModel):
    def __init__(
        self,
        bill_prediction_data_item: List[main_models.DescribeLiveUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem] = None,
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
                temp_model = main_models.DescribeLiveUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem()
                self.bill_prediction_data_item.append(temp_model.from_map(k1))

        return self

class DescribeLiveUserBillPredictionResponseBodyBillPredictionDataBillPredictionDataItem(DaraModel):
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

