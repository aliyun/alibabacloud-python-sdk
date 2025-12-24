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
        # The estimated bill data.
        self.bill_prediction_data = bill_prediction_data
        # The metering method. Valid values:
        # 
        # *   hour_flow: pay by hourly data transfer
        # *   day_bandwidth: pay by daily bandwidth
        # *   month_95: pay by monthly 95th percentile bandwidth
        # *   month_avg_day_bandwidth: pay by average daily peak bandwidth per month
        # *   month_4th_day_bandwidth: pay by 4th peak bandwidth per month
        # *   month_avg_day_95: pay by average daily 95th percentile bandwidth per month
        # *   month_95_night_half: pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00
        # *   hour_vas: pay by value-added services per hour
        # *   day_count: pay by daily requests
        self.bill_type = bill_type
        # The end time. If you do not specify the request parameter EndTime, the end time is the current time by default. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The start time. If you do not specify the request parameter StartTime, the start time is 00:00 on the first day of the month by default. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
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
        # The billable region. Valid values:
        # 
        # *   CN: Chinese mainland
        # *   OverSeas: countries and regions outside the Chinese mainland
        # *   AP1: Asia Pacific 1, including Hong Kong (China), Macao (China), Taiwan (China), Japan, and other Southeast Asia countries and regions except Vietnam and Indonesia
        # *   AP2: Asia Pacific 2, including Indonesia, South Korea, and Vietnam
        # *   AP3: Asia Pacific 3, including Australia and New Zealand
        # *   NA: North America, including US and Canada
        # *   SA: South America, specifically meaning Brazil
        # *   EU: Europe, including Ukraine, UK, France, Netherlands, Spain, Italy, Sweden, and Germany
        # *   MEAA: Middle East and Africa, including South Africa, Oman, UAE, and Kuwait
        # 
        # By default, data of all regions is aggregated and returned.
        self.area = area
        # The time at which the estimated value occurs. This parameter is returned only if the metering method is pay by 95th percentile bandwidth, pay by 95th percentile bandwidth with 50% off from 00:00 to 08:00, or pay by 4th peak bandwidth per month.
        self.time_stp = time_stp
        # The estimated value.
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

