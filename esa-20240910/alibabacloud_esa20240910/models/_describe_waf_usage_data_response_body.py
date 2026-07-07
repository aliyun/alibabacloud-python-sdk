# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeWafUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        usage_data: List[main_models.DescribeWafUsageDataResponseBodyUsageData] = None,
    ):
        # The end of the time range for the returned data. The time is in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is in UTC+0.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC+0.
        self.start_time = start_time
        # The returned data.
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for v1 in self.usage_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['UsageData'] = []
        if self.usage_data is not None:
            for k1 in self.usage_data:
                result['UsageData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.usage_data = []
        if m.get('UsageData') is not None:
            for k1 in m.get('UsageData'):
                temp_model = main_models.DescribeWafUsageDataResponseBodyUsageData()
                self.usage_data.append(temp_model.from_map(k1))

        return self

class DescribeWafUsageDataResponseBodyUsageData(DaraModel):
    def __init__(
        self,
        access_count: int = None,
        block_count: int = None,
        observe_count: int = None,
        record_name: str = None,
        time_stamp: str = None,
    ):
        # The number of requests with normal access.
        self.access_count = access_count
        # The number of blocked requests.
        self.block_count = block_count
        # The number of observed requests.
        self.observe_count = observe_count
        # The domain record name.
        self.record_name = record_name
        # The beginning of the time interval.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_count is not None:
            result['AccessCount'] = self.access_count

        if self.block_count is not None:
            result['BlockCount'] = self.block_count

        if self.observe_count is not None:
            result['ObserveCount'] = self.observe_count

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessCount') is not None:
            self.access_count = m.get('AccessCount')

        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')

        if m.get('ObserveCount') is not None:
            self.observe_count = m.get('ObserveCount')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

