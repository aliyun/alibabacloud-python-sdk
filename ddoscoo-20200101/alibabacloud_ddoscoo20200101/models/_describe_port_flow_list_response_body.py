# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortFlowListResponseBody(DaraModel):
    def __init__(
        self,
        port_flow_list: List[main_models.DescribePortFlowListResponseBodyPortFlowList] = None,
        request_id: str = None,
    ):
        # The returned traffic data.
        self.port_flow_list = port_flow_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.port_flow_list:
            for v1 in self.port_flow_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PortFlowList'] = []
        if self.port_flow_list is not None:
            for k1 in self.port_flow_list:
                result['PortFlowList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.port_flow_list = []
        if m.get('PortFlowList') is not None:
            for k1 in m.get('PortFlowList'):
                temp_model = main_models.DescribePortFlowListResponseBodyPortFlowList()
                self.port_flow_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePortFlowListResponseBodyPortFlowList(DaraModel):
    def __init__(
        self,
        attack_bps: int = None,
        attack_pps: int = None,
        in_bps: int = None,
        in_pps: int = None,
        index: int = None,
        out_bps: int = None,
        out_pps: int = None,
        region: str = None,
        sla_bps_drop_bps: int = None,
        sla_bps_drop_pps: int = None,
        sla_conn_drop_bps: int = None,
        sla_conn_drop_pps: int = None,
        sla_cps_drop_bps: int = None,
        sla_cps_drop_pps: int = None,
        sla_pps_drop_bps: int = None,
        sla_pps_drop_pps: int = None,
        time: int = None,
    ):
        # The bandwidth of attack traffic. Unit: bit/s.
        self.attack_bps = attack_bps
        # The packet forwarding rate of attack traffic. Unit: pps.
        self.attack_pps = attack_pps
        # The inbound bandwidth. Unit: bit/s.
        self.in_bps = in_bps
        # The packet forwarding rate of inbound traffic. Unit: packets per second.
        self.in_pps = in_pps
        # The index number of the returned data.
        self.index = index
        # The outbound bandwidth. Unit: bit/s.
        self.out_bps = out_bps
        # The packet forwarding rate of outbound traffic. Unit: packets per second (pps).
        self.out_pps = out_pps
        # The source region of the traffic. Valid values:
        # 
        # *   **cn**: mainland China
        # *   **alb-ap-northeast-1-gf-x**: Japan (Tokyo)
        # *   **alb-ap-southeast-gf-x**: Singapore
        # *   **alb-cn-hongkong-gf-x**: Hong Kong (China)
        # *   **alb-eu-central-1-gf-x**: Germany (Frankfurt)
        # *   **alb-us-west-1-gf-x**: US (Silicon Valley)
        # 
        # > The values except **cn** are returned only when **RegionId** is set to **ap-southeast-1**.
        self.region = region
        self.sla_bps_drop_bps = sla_bps_drop_bps
        self.sla_bps_drop_pps = sla_bps_drop_pps
        self.sla_conn_drop_bps = sla_conn_drop_bps
        self.sla_conn_drop_pps = sla_conn_drop_pps
        self.sla_cps_drop_bps = sla_cps_drop_bps
        self.sla_cps_drop_pps = sla_cps_drop_pps
        self.sla_pps_drop_bps = sla_pps_drop_bps
        self.sla_pps_drop_pps = sla_pps_drop_pps
        # The time when the data was collected. The value is a UNIX timestamp. Unit: seconds.
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

        if self.in_bps is not None:
            result['InBps'] = self.in_bps

        if self.in_pps is not None:
            result['InPps'] = self.in_pps

        if self.index is not None:
            result['Index'] = self.index

        if self.out_bps is not None:
            result['OutBps'] = self.out_bps

        if self.out_pps is not None:
            result['OutPps'] = self.out_pps

        if self.region is not None:
            result['Region'] = self.region

        if self.sla_bps_drop_bps is not None:
            result['SlaBpsDropBps'] = self.sla_bps_drop_bps

        if self.sla_bps_drop_pps is not None:
            result['SlaBpsDropPps'] = self.sla_bps_drop_pps

        if self.sla_conn_drop_bps is not None:
            result['SlaConnDropBps'] = self.sla_conn_drop_bps

        if self.sla_conn_drop_pps is not None:
            result['SlaConnDropPps'] = self.sla_conn_drop_pps

        if self.sla_cps_drop_bps is not None:
            result['SlaCpsDropBps'] = self.sla_cps_drop_bps

        if self.sla_cps_drop_pps is not None:
            result['SlaCpsDropPps'] = self.sla_cps_drop_pps

        if self.sla_pps_drop_bps is not None:
            result['SlaPpsDropBps'] = self.sla_pps_drop_bps

        if self.sla_pps_drop_pps is not None:
            result['SlaPpsDropPps'] = self.sla_pps_drop_pps

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')

        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')

        if m.get('InBps') is not None:
            self.in_bps = m.get('InBps')

        if m.get('InPps') is not None:
            self.in_pps = m.get('InPps')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('OutBps') is not None:
            self.out_bps = m.get('OutBps')

        if m.get('OutPps') is not None:
            self.out_pps = m.get('OutPps')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SlaBpsDropBps') is not None:
            self.sla_bps_drop_bps = m.get('SlaBpsDropBps')

        if m.get('SlaBpsDropPps') is not None:
            self.sla_bps_drop_pps = m.get('SlaBpsDropPps')

        if m.get('SlaConnDropBps') is not None:
            self.sla_conn_drop_bps = m.get('SlaConnDropBps')

        if m.get('SlaConnDropPps') is not None:
            self.sla_conn_drop_pps = m.get('SlaConnDropPps')

        if m.get('SlaCpsDropBps') is not None:
            self.sla_cps_drop_bps = m.get('SlaCpsDropBps')

        if m.get('SlaCpsDropPps') is not None:
            self.sla_cps_drop_pps = m.get('SlaCpsDropPps')

        if m.get('SlaPpsDropBps') is not None:
            self.sla_pps_drop_bps = m.get('SlaPpsDropBps')

        if m.get('SlaPpsDropPps') is not None:
            self.sla_pps_drop_pps = m.get('SlaPpsDropPps')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

