# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeBlackholeStatusResponseBody(DaraModel):
    def __init__(
        self,
        blackhole_status: List[main_models.DescribeBlackholeStatusResponseBodyBlackholeStatus] = None,
        request_id: str = None,
    ):
        # An array that consists of the blackhole filtering status of the instance.
        self.blackhole_status = blackhole_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.blackhole_status:
            for v1 in self.blackhole_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BlackholeStatus'] = []
        if self.blackhole_status is not None:
            for k1 in self.blackhole_status:
                result['BlackholeStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.blackhole_status = []
        if m.get('BlackholeStatus') is not None:
            for k1 in m.get('BlackholeStatus'):
                temp_model = main_models.DescribeBlackholeStatusResponseBodyBlackholeStatus()
                self.blackhole_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBlackholeStatusResponseBodyBlackholeStatus(DaraModel):
    def __init__(
        self,
        black_status: str = None,
        end_time: int = None,
        ip: str = None,
        start_time: int = None,
    ):
        # Indicates whether blackhole filtering is triggered for the instance. Valid values:
        # 
        # *   **blackhole**: yes
        # *   **normal**: no
        self.black_status = black_status
        # The end time of blackhole filtering. The value is a UNIX timestamp. Unit: seconds.
        self.end_time = end_time
        # The IP address of the instance.
        self.ip = ip
        # The start time of blackhole filtering. The value is a UNIX timestamp. Unit: seconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_status is not None:
            result['BlackStatus'] = self.black_status

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackStatus') is not None:
            self.black_status = m.get('BlackStatus')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

