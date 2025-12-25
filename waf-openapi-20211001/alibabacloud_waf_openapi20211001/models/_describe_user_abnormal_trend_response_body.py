# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeUserAbnormalTrendResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        trend: List[main_models.DescribeUserAbnormalTrendResponseBodyTrend] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The trends of risks.
        self.trend = trend

    def validate(self):
        if self.trend:
            for v1 in self.trend:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Trend'] = []
        if self.trend is not None:
            for k1 in self.trend:
                result['Trend'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.trend = []
        if m.get('Trend') is not None:
            for k1 in m.get('Trend'):
                temp_model = main_models.DescribeUserAbnormalTrendResponseBodyTrend()
                self.trend.append(temp_model.from_map(k1))

        return self

class DescribeUserAbnormalTrendResponseBodyTrend(DaraModel):
    def __init__(
        self,
        abnormal_high: int = None,
        abnormal_low: int = None,
        abnormal_medium: int = None,
        time_stamp: int = None,
        timestamp: int = None,
    ):
        # The number of high risks.
        self.abnormal_high = abnormal_high
        # The number of low risks.
        self.abnormal_low = abnormal_low
        # The number of medium risks.
        self.abnormal_medium = abnormal_medium
        # The time at which the API was called. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        # 
        # >Notice: The parameter has been deprecated, it is recommended to use the Timestamp parameter.
        self.time_stamp = time_stamp
        # The time at which the API was called. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_high is not None:
            result['AbnormalHigh'] = self.abnormal_high

        if self.abnormal_low is not None:
            result['AbnormalLow'] = self.abnormal_low

        if self.abnormal_medium is not None:
            result['AbnormalMedium'] = self.abnormal_medium

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalHigh') is not None:
            self.abnormal_high = m.get('AbnormalHigh')

        if m.get('AbnormalLow') is not None:
            self.abnormal_low = m.get('AbnormalLow')

        if m.get('AbnormalMedium') is not None:
            self.abnormal_medium = m.get('AbnormalMedium')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

