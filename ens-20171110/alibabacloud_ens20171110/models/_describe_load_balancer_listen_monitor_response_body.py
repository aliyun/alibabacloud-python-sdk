# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeLoadBalancerListenMonitorResponseBody(DaraModel):
    def __init__(
        self,
        load_balancer_monitor_listen_data: List[main_models.DescribeLoadBalancerListenMonitorResponseBodyLoadBalancerMonitorListenData] = None,
        request_id: str = None,
    ):
        # The TCP/UDP monitoring data of the ELB instance.
        self.load_balancer_monitor_listen_data = load_balancer_monitor_listen_data
        # Id of the request.
        self.request_id = request_id

    def validate(self):
        if self.load_balancer_monitor_listen_data:
            for v1 in self.load_balancer_monitor_listen_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LoadBalancerMonitorListenData'] = []
        if self.load_balancer_monitor_listen_data is not None:
            for k1 in self.load_balancer_monitor_listen_data:
                result['LoadBalancerMonitorListenData'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_monitor_listen_data = []
        if m.get('LoadBalancerMonitorListenData') is not None:
            for k1 in m.get('LoadBalancerMonitorListenData'):
                temp_model = main_models.DescribeLoadBalancerListenMonitorResponseBodyLoadBalancerMonitorListenData()
                self.load_balancer_monitor_listen_data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLoadBalancerListenMonitorResponseBodyLoadBalancerMonitorListenData(DaraModel):
    def __init__(
        self,
        act_conns: str = None,
        biz_time: str = None,
        conns: str = None,
        drop_conns: str = None,
        ens_region_id: str = None,
        in_act_conns: str = None,
        in_bytes: str = None,
        in_drop_bytes: str = None,
        in_drop_pkts: str = None,
        in_pkts: str = None,
        in_valid_rs_num: str = None,
        load_balancer_id: str = None,
        out_bytes: str = None,
        out_drop_bytes: str = None,
        out_drop_pkts: str = None,
        out_pkts: str = None,
        proto: str = None,
        vport: str = None,
        valid_rs_num: str = None,
        vip: str = None,
        vni: str = None,
    ):
        # The number of active connections.
        self.act_conns = act_conns
        # The business time.
        self.biz_time = biz_time
        # The number of new connections.
        self.conns = conns
        # The number of dropped connections.
        self.drop_conns = drop_conns
        # The ID of the node to which the ELB instance belongs.
        self.ens_region_id = ens_region_id
        # The number of inactive connections.
        self.in_act_conns = in_act_conns
        # The inbound traffic.
        self.in_bytes = in_bytes
        # The dropped inbound traffic.
        self.in_drop_bytes = in_drop_bytes
        # The number of dropped inbound packets.
        self.in_drop_pkts = in_drop_pkts
        # The number of inbound packets.
        self.in_pkts = in_pkts
        # The number of unavailable servers that are attached to the monitored ELB instance.
        self.in_valid_rs_num = in_valid_rs_num
        # The ID of the ELB instance.
        self.load_balancer_id = load_balancer_id
        # The outbound traffic.
        self.out_bytes = out_bytes
        # The dropped outbound traffic.
        self.out_drop_bytes = out_drop_bytes
        # The number of dropped outbound packets.
        self.out_drop_pkts = out_drop_pkts
        # The number of outbound packets.
        self.out_pkts = out_pkts
        # The network protocol.
        self.proto = proto
        # The VIP port of the ELB instance.
        self.vport = vport
        # The number of available servers that are attached to the monitored ELB instance.
        self.valid_rs_num = valid_rs_num
        # The virtual IP address (VIP) of the instance.
        self.vip = vip
        # The ID of the tunnel.
        self.vni = vni

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.act_conns is not None:
            result['ActConns'] = self.act_conns

        if self.biz_time is not None:
            result['BizTime'] = self.biz_time

        if self.conns is not None:
            result['Conns'] = self.conns

        if self.drop_conns is not None:
            result['DropConns'] = self.drop_conns

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.in_act_conns is not None:
            result['InActConns'] = self.in_act_conns

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.in_drop_bytes is not None:
            result['InDropBytes'] = self.in_drop_bytes

        if self.in_drop_pkts is not None:
            result['InDropPkts'] = self.in_drop_pkts

        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts

        if self.in_valid_rs_num is not None:
            result['InValidRsNum'] = self.in_valid_rs_num

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.out_drop_bytes is not None:
            result['OutDropBytes'] = self.out_drop_bytes

        if self.out_drop_pkts is not None:
            result['OutDropPkts'] = self.out_drop_pkts

        if self.out_pkts is not None:
            result['OutPkts'] = self.out_pkts

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.vport is not None:
            result['VPort'] = self.vport

        if self.valid_rs_num is not None:
            result['ValidRsNum'] = self.valid_rs_num

        if self.vip is not None:
            result['Vip'] = self.vip

        if self.vni is not None:
            result['Vni'] = self.vni

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActConns') is not None:
            self.act_conns = m.get('ActConns')

        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')

        if m.get('Conns') is not None:
            self.conns = m.get('Conns')

        if m.get('DropConns') is not None:
            self.drop_conns = m.get('DropConns')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InActConns') is not None:
            self.in_act_conns = m.get('InActConns')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('InDropBytes') is not None:
            self.in_drop_bytes = m.get('InDropBytes')

        if m.get('InDropPkts') is not None:
            self.in_drop_pkts = m.get('InDropPkts')

        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')

        if m.get('InValidRsNum') is not None:
            self.in_valid_rs_num = m.get('InValidRsNum')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('OutDropBytes') is not None:
            self.out_drop_bytes = m.get('OutDropBytes')

        if m.get('OutDropPkts') is not None:
            self.out_drop_pkts = m.get('OutDropPkts')

        if m.get('OutPkts') is not None:
            self.out_pkts = m.get('OutPkts')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('VPort') is not None:
            self.vport = m.get('VPort')

        if m.get('ValidRsNum') is not None:
            self.valid_rs_num = m.get('ValidRsNum')

        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        if m.get('Vni') is not None:
            self.vni = m.get('Vni')

        return self

