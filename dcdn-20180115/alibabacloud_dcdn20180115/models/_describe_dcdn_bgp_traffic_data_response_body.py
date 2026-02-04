# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnBgpTrafficDataResponseBody(DaraModel):
    def __init__(
        self,
        bgp_data_interval: List[main_models.DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval] = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The BGP traffic at each time interval.
        self.bgp_data_interval = bgp_data_interval
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.bgp_data_interval:
            for v1 in self.bgp_data_interval:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BgpDataInterval'] = []
        if self.bgp_data_interval is not None:
            for k1 in self.bgp_data_interval:
                result['BgpDataInterval'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bgp_data_interval = []
        if m.get('BgpDataInterval') is not None:
            for k1 in m.get('BgpDataInterval'):
                temp_model = main_models.DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval()
                self.bgp_data_interval.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDcdnBgpTrafficDataResponseBodyBgpDataInterval(DaraModel):
    def __init__(
        self,
        in_: int = None,
        out: int = None,
        time_stamp: str = None,
    ):
        # The inbound traffic. Unit: bytes.
        self.in_ = in_
        # The outbound traffic. Unit: bytes.
        self.out = out
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_ is not None:
            result['In'] = self.in_

        if self.out is not None:
            result['Out'] = self.out

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('In') is not None:
            self.in_ = m.get('In')

        if m.get('Out') is not None:
            self.out = m.get('Out')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

