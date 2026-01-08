# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInvadeEcsTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeInvadeEcsTrendResponseBodyDataList] = None,
        end_time: int = None,
        interval: int = None,
        invade_ecs_count: int = None,
        request_id: str = None,
        start_time: int = None,
    ):
        self.data_list = data_list
        self.end_time = end_time
        self.interval = interval
        self.invade_ecs_count = invade_ecs_count
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.invade_ecs_count is not None:
            result['InvadeEcsCount'] = self.invade_ecs_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeInvadeEcsTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('InvadeEcsCount') is not None:
            self.invade_ecs_count = m.get('InvadeEcsCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeInvadeEcsTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        ecs_count: int = None,
        time: int = None,
    ):
        self.ecs_count = ecs_count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

