# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelAreaDistributionStatDataResponseBody(DaraModel):
    def __init__(
        self,
        area_stat_list: List[main_models.DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList] = None,
        request_id: str = None,
    ):
        self.area_stat_list = area_stat_list
        self.request_id = request_id

    def validate(self):
        if self.area_stat_list:
            for v1 in self.area_stat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AreaStatList'] = []
        if self.area_stat_list is not None:
            for k1 in self.area_stat_list:
                result['AreaStatList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.area_stat_list = []
        if m.get('AreaStatList') is not None:
            for k1 in m.get('AreaStatList'):
                temp_model = main_models.DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList()
                self.area_stat_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChannelAreaDistributionStatDataResponseBodyAreaStatList(DaraModel):
    def __init__(
        self,
        area_name: str = None,
        call_user_count: int = None,
        high_quality_transmission_rate: str = None,
        pub_user_count: int = None,
        sub_user_count: int = None,
    ):
        self.area_name = area_name
        self.call_user_count = call_user_count
        self.high_quality_transmission_rate = high_quality_transmission_rate
        self.pub_user_count = pub_user_count
        self.sub_user_count = sub_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_name is not None:
            result['AreaName'] = self.area_name

        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count

        if self.high_quality_transmission_rate is not None:
            result['HighQualityTransmissionRate'] = self.high_quality_transmission_rate

        if self.pub_user_count is not None:
            result['PubUserCount'] = self.pub_user_count

        if self.sub_user_count is not None:
            result['SubUserCount'] = self.sub_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')

        if m.get('HighQualityTransmissionRate') is not None:
            self.high_quality_transmission_rate = m.get('HighQualityTransmissionRate')

        if m.get('PubUserCount') is not None:
            self.pub_user_count = m.get('PubUserCount')

        if m.get('SubUserCount') is not None:
            self.sub_user_count = m.get('SubUserCount')

        return self

