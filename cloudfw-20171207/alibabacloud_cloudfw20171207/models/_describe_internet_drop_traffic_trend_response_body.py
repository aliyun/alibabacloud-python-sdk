# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeInternetDropTrafficTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeInternetDropTrafficTrendResponseBodyDataList] = None,
        drop_session_max: int = None,
        ratio_average: str = None,
        request_id: str = None,
        ring_ratio_average: str = None,
    ):
        self.data_list = data_list
        self.drop_session_max = drop_session_max
        self.ratio_average = ratio_average
        self.request_id = request_id
        self.ring_ratio_average = ring_ratio_average

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

        if self.drop_session_max is not None:
            result['DropSessionMax'] = self.drop_session_max

        if self.ratio_average is not None:
            result['RatioAverage'] = self.ratio_average

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ring_ratio_average is not None:
            result['RingRatioAverage'] = self.ring_ratio_average

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeInternetDropTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('DropSessionMax') is not None:
            self.drop_session_max = m.get('DropSessionMax')

        if m.get('RatioAverage') is not None:
            self.ratio_average = m.get('RatioAverage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RingRatioAverage') is not None:
            self.ring_ratio_average = m.get('RingRatioAverage')

        return self

class DescribeInternetDropTrafficTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        acl_drop: int = None,
        data_time: str = None,
        drop_ratio: str = None,
        drop_ring: int = None,
        drop_ring_ratio: str = None,
        drop_session: int = None,
        ips_drop: int = None,
        ring_data_time: str = None,
        ring_time: int = None,
        time: int = None,
        total_session: int = None,
    ):
        self.acl_drop = acl_drop
        self.data_time = data_time
        self.drop_ratio = drop_ratio
        self.drop_ring = drop_ring
        self.drop_ring_ratio = drop_ring_ratio
        self.drop_session = drop_session
        self.ips_drop = ips_drop
        self.ring_data_time = ring_data_time
        self.ring_time = ring_time
        self.time = time
        self.total_session = total_session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_drop is not None:
            result['AclDrop'] = self.acl_drop

        if self.data_time is not None:
            result['DataTime'] = self.data_time

        if self.drop_ratio is not None:
            result['DropRatio'] = self.drop_ratio

        if self.drop_ring is not None:
            result['DropRing'] = self.drop_ring

        if self.drop_ring_ratio is not None:
            result['DropRingRatio'] = self.drop_ring_ratio

        if self.drop_session is not None:
            result['DropSession'] = self.drop_session

        if self.ips_drop is not None:
            result['IpsDrop'] = self.ips_drop

        if self.ring_data_time is not None:
            result['RingDataTime'] = self.ring_data_time

        if self.ring_time is not None:
            result['RingTime'] = self.ring_time

        if self.time is not None:
            result['Time'] = self.time

        if self.total_session is not None:
            result['TotalSession'] = self.total_session

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclDrop') is not None:
            self.acl_drop = m.get('AclDrop')

        if m.get('DataTime') is not None:
            self.data_time = m.get('DataTime')

        if m.get('DropRatio') is not None:
            self.drop_ratio = m.get('DropRatio')

        if m.get('DropRing') is not None:
            self.drop_ring = m.get('DropRing')

        if m.get('DropRingRatio') is not None:
            self.drop_ring_ratio = m.get('DropRingRatio')

        if m.get('DropSession') is not None:
            self.drop_session = m.get('DropSession')

        if m.get('IpsDrop') is not None:
            self.ips_drop = m.get('IpsDrop')

        if m.get('RingDataTime') is not None:
            self.ring_data_time = m.get('RingDataTime')

        if m.get('RingTime') is not None:
            self.ring_time = m.get('RingTime')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalSession') is not None:
            self.total_session = m.get('TotalSession')

        return self

