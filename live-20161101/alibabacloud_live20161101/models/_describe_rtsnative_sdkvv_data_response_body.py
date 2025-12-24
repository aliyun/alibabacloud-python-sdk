# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeRTSNativeSDKVvDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        vv_data: List[main_models.DescribeRTSNativeSDKVvDataResponseBodyVvData] = None,
    ):
        # The time granularity.
        self.data_interval = data_interval
        # The end of the time range for which the data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range for which the data was queried.
        self.start_time = start_time
        # The total number of playbacks and the number of successful playbacks at each interval.
        self.vv_data = vv_data

    def validate(self):
        if self.vv_data:
            for v1 in self.vv_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['VvData'] = []
        if self.vv_data is not None:
            for k1 in self.vv_data:
                result['VvData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.vv_data = []
        if m.get('VvData') is not None:
            for k1 in m.get('VvData'):
                temp_model = main_models.DescribeRTSNativeSDKVvDataResponseBodyVvData()
                self.vv_data.append(temp_model.from_map(k1))

        return self

class DescribeRTSNativeSDKVvDataResponseBodyVvData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        vv_success: str = None,
        vv_total: str = None,
    ):
        # The timestamp of the returned data.
        self.time_stamp = time_stamp
        # The number of successful playbacks within the period of time.
        self.vv_success = vv_success
        # The total number of playbacks within the period of time.
        self.vv_total = vv_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.vv_success is not None:
            result['VvSuccess'] = self.vv_success

        if self.vv_total is not None:
            result['VvTotal'] = self.vv_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('VvSuccess') is not None:
            self.vv_success = m.get('VvSuccess')

        if m.get('VvTotal') is not None:
            self.vv_total = m.get('VvTotal')

        return self

