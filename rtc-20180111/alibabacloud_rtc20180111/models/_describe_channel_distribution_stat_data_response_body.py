# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeChannelDistributionStatDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[main_models.DescribeChannelDistributionStatDataResponseBodyStatList] = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list

    def validate(self):
        if self.stat_list:
            for v1 in self.stat_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StatList'] = []
        if self.stat_list is not None:
            for k1 in self.stat_list:
                result['StatList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.stat_list = []
        if m.get('StatList') is not None:
            for k1 in m.get('StatList'):
                temp_model = main_models.DescribeChannelDistributionStatDataResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k1))

        return self

class DescribeChannelDistributionStatDataResponseBodyStatList(DaraModel):
    def __init__(
        self,
        call_user_count: int = None,
        call_user_ratio: str = None,
        name: str = None,
    ):
        self.call_user_count = call_user_count
        self.call_user_ratio = call_user_ratio
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_user_count is not None:
            result['CallUserCount'] = self.call_user_count

        if self.call_user_ratio is not None:
            result['CallUserRatio'] = self.call_user_ratio

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallUserCount') is not None:
            self.call_user_count = m.get('CallUserCount')

        if m.get('CallUserRatio') is not None:
            self.call_user_ratio = m.get('CallUserRatio')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

