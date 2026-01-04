# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeServerLoadBalancerListenMonitorResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        server_load_balancer_monitor_data: List[main_models.DescribeServerLoadBalancerListenMonitorResponseBodyServerLoadBalancerMonitorData] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The array of the monitoring data.
        self.server_load_balancer_monitor_data = server_load_balancer_monitor_data

    def validate(self):
        if self.server_load_balancer_monitor_data:
            for v1 in self.server_load_balancer_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServerLoadBalancerMonitorData'] = []
        if self.server_load_balancer_monitor_data is not None:
            for k1 in self.server_load_balancer_monitor_data:
                result['ServerLoadBalancerMonitorData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.server_load_balancer_monitor_data = []
        if m.get('ServerLoadBalancerMonitorData') is not None:
            for k1 in m.get('ServerLoadBalancerMonitorData'):
                temp_model = main_models.DescribeServerLoadBalancerListenMonitorResponseBodyServerLoadBalancerMonitorData()
                self.server_load_balancer_monitor_data.append(temp_model.from_map(k1))

        return self

class DescribeServerLoadBalancerListenMonitorResponseBodyServerLoadBalancerMonitorData(DaraModel):
    def __init__(
        self,
        acc: int = None,
        biz_time: str = None,
        ens_region_id: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        proto: str = None,
        reqs_2xx: int = None,
        reqs_3xx: int = None,
        reqs_4xx: int = None,
        reqs_5xx: int = None,
        rt_avg: int = None,
        vip: str = None,
        vni: int = None,
        vport: int = None,
    ):
        # The total number of requests.
        self.acc = acc
        # The business time of the log. Logs are collected every minute.
        self.biz_time = biz_time
        # The ID of the node to which the ELB instance belongs.
        self.ens_region_id = ens_region_id
        # The ID of the ELB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the ELB instance.
        self.load_balancer_name = load_balancer_name
        # The specification of the ELB instance.
        self.load_balancer_spec = load_balancer_spec
        # The request protocol, such as http, https, or tcp.
        self.proto = proto
        # The number of requests with HTTP 2xx status code returned.
        self.reqs_2xx = reqs_2xx
        # The number of requests with HTTP 3xx status code returned.
        self.reqs_3xx = reqs_3xx
        # The number of requests with HTTP 4xx status code returned.
        self.reqs_4xx = reqs_4xx
        # The number of requests with HTTP 5xx status code returned.
        self.reqs_5xx = reqs_5xx
        # The average response time. Unit: milliseconds.
        self.rt_avg = rt_avg
        # The VIP of the instance.
        self.vip = vip
        # The ID of the tunnel.
        self.vni = vni
        # The VIP port, such as 80, 8080, or 443.
        self.vport = vport

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.biz_time is not None:
            result['BizTime'] = self.biz_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.reqs_2xx is not None:
            result['Reqs2xx'] = self.reqs_2xx

        if self.reqs_3xx is not None:
            result['Reqs3xx'] = self.reqs_3xx

        if self.reqs_4xx is not None:
            result['Reqs4xx'] = self.reqs_4xx

        if self.reqs_5xx is not None:
            result['Reqs5xx'] = self.reqs_5xx

        if self.rt_avg is not None:
            result['RtAvg'] = self.rt_avg

        if self.vip is not None:
            result['Vip'] = self.vip

        if self.vni is not None:
            result['Vni'] = self.vni

        if self.vport is not None:
            result['Vport'] = self.vport

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('Reqs2xx') is not None:
            self.reqs_2xx = m.get('Reqs2xx')

        if m.get('Reqs3xx') is not None:
            self.reqs_3xx = m.get('Reqs3xx')

        if m.get('Reqs4xx') is not None:
            self.reqs_4xx = m.get('Reqs4xx')

        if m.get('Reqs5xx') is not None:
            self.reqs_5xx = m.get('Reqs5xx')

        if m.get('RtAvg') is not None:
            self.rt_avg = m.get('RtAvg')

        if m.get('Vip') is not None:
            self.vip = m.get('Vip')

        if m.get('Vni') is not None:
            self.vni = m.get('Vni')

        if m.get('Vport') is not None:
            self.vport = m.get('Vport')

        return self

