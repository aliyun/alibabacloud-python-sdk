# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class DescribeTrafficResponseBody(DaraModel):
    def __init__(
        self,
        flow_list: List[main_models.DescribeTrafficResponseBodyFlowList] = None,
        request_id: str = None,
    ):
        # The queried traffic statistics.
        self.flow_list = flow_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.flow_list:
            for v1 in self.flow_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowList'] = []
        if self.flow_list is not None:
            for k1 in self.flow_list:
                result['FlowList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_list = []
        if m.get('FlowList') is not None:
            for k1 in m.get('FlowList'):
                temp_model = main_models.DescribeTrafficResponseBodyFlowList()
                self.flow_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTrafficResponseBodyFlowList(DaraModel):
    def __init__(
        self,
        attack_bps: int = None,
        attack_pps: int = None,
        flow_type: str = None,
        kbps: int = None,
        name: str = None,
        pps: int = None,
        time: int = None,
    ):
        # The bandwidth of attack traffic. Unit: bit/s.
        # 
        # >  This parameter is returned only if attack traffic exists.
        self.attack_bps = attack_bps
        # The packet forwarding rate of attack traffic. Unit: packets per second.
        # 
        # >  This parameter is returned only if attack traffic exists.
        self.attack_pps = attack_pps
        # The type of the traffic statistics. Valid values:
        # 
        # *   **max**: the peak traffic within the specified interval
        # *   **avg**: the average traffic within the specified interval
        self.flow_type = flow_type
        # The bandwidth of the total traffic. Unit: Kbit/s.
        self.kbps = kbps
        # The ID of the traffic statistics.
        self.name = name
        # The packet forwarding rate of the total traffic. Unit: packets per second.
        self.pps = pps
        # The time when the traffic statistics are calculated. This value is a UNIX timestamp. Unit: seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps

        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.kbps is not None:
            result['Kbps'] = self.kbps

        if self.name is not None:
            result['Name'] = self.name

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')

        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('Kbps') is not None:
            self.kbps = m.get('Kbps')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

