# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNatFirewallDropTrafficTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeNatFirewallDropTrafficTrendResponseBodyDataList] = None,
        drop_session_max: int = None,
        drop_session_max_time: str = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.drop_session_max = drop_session_max
        self.drop_session_max_time = drop_session_max_time
        self.request_id = request_id

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

        if self.drop_session_max_time is not None:
            result['DropSessionMaxTime'] = self.drop_session_max_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeNatFirewallDropTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('DropSessionMax') is not None:
            self.drop_session_max = m.get('DropSessionMax')

        if m.get('DropSessionMaxTime') is not None:
            self.drop_session_max_time = m.get('DropSessionMaxTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNatFirewallDropTrafficTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        drop_session: int = None,
        time: int = None,
        total_session: int = None,
    ):
        self.drop_session = drop_session
        self.time = time
        self.total_session = total_session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drop_session is not None:
            result['DropSession'] = self.drop_session

        if self.time is not None:
            result['Time'] = self.time

        if self.total_session is not None:
            result['TotalSession'] = self.total_session

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DropSession') is not None:
            self.drop_session = m.get('DropSession')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalSession') is not None:
            self.total_session = m.get('TotalSession')

        return self

