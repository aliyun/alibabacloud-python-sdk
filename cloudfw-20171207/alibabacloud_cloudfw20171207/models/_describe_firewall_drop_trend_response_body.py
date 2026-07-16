# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallDropTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeFirewallDropTrendResponseBodyDataList] = None,
        max_drop_session: int = None,
        max_drop_time: int = None,
        request_id: str = None,
    ):
        # The returned data list.
        self.data_list = data_list
        # The maximum number of total blocked sessions.
        self.max_drop_session = max_drop_session
        # The time when the maximum number of total blocked sessions occurred. The value is a UNIX timestamp in seconds, such as 1672502400.
        self.max_drop_time = max_drop_time
        # The request ID.
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

        if self.max_drop_session is not None:
            result['MaxDropSession'] = self.max_drop_session

        if self.max_drop_time is not None:
            result['MaxDropTime'] = self.max_drop_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeFirewallDropTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('MaxDropSession') is not None:
            self.max_drop_session = m.get('MaxDropSession')

        if m.get('MaxDropTime') is not None:
            self.max_drop_time = m.get('MaxDropTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFirewallDropTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        internet_drop_session: int = None,
        nat_drop_session: int = None,
        time: int = None,
        total_drop_session: int = None,
        vpc_drop_session: int = None,
    ):
        # The number of sessions blocked by the Internet firewall.
        self.internet_drop_session = internet_drop_session
        # The number of sessions blocked by the NAT firewall.
        self.nat_drop_session = nat_drop_session
        # The time when the traffic occurred. The value is a UNIX timestamp in seconds.
        # 
        # If the data at this point in time has not been processed, the values of all other fields are -1.
        self.time = time
        # The total number of sessions blocked by the firewall.
        self.total_drop_session = total_drop_session
        # The number of sessions blocked by the VPC firewall.
        self.vpc_drop_session = vpc_drop_session

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_drop_session is not None:
            result['InternetDropSession'] = self.internet_drop_session

        if self.nat_drop_session is not None:
            result['NatDropSession'] = self.nat_drop_session

        if self.time is not None:
            result['Time'] = self.time

        if self.total_drop_session is not None:
            result['TotalDropSession'] = self.total_drop_session

        if self.vpc_drop_session is not None:
            result['VpcDropSession'] = self.vpc_drop_session

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetDropSession') is not None:
            self.internet_drop_session = m.get('InternetDropSession')

        if m.get('NatDropSession') is not None:
            self.nat_drop_session = m.get('NatDropSession')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalDropSession') is not None:
            self.total_drop_session = m.get('TotalDropSession')

        if m.get('VpcDropSession') is not None:
            self.vpc_drop_session = m.get('VpcDropSession')

        return self

