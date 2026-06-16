# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIpDefenseThresholdRequest(DaraModel):
    def __init__(
        self,
        bps: int = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        pps: int = None,
    ):
        # The traffic scrubbing threshold. Unit: Mbit/s. The traffic scrubbing threshold cannot exceed the peak inbound or outbound Internet traffic, whichever is larger, of the asset. When you modify Bps, Pps is required. Otherwise, Bps does not take effect.
        # 
        # You can use the monitoring tool that is provided by the asset to query the Internet traffic of the asset:
        # 
        # - If the asset is an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # 
        # - If the asset is an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        # 
        # - If the asset is an EIP, see [View monitoring data](https://help.aliyun.com/document_detail/85354.html).
        self.bps = bps
        # The region ID of the asset.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The ID of the asset.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) operation to query the IDs of ECS instances, SLB instances, and EIPs within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the asset. Valid values:
        # 
        # - **ecs**: an Elastic Compute Service (ECS) instance.
        # 
        # - **slb**: a Server Load Balancer (SLB) instance.
        # 
        # - **eip**: an elastic IP address (EIP).
        # 
        # - **ipv6**: an IPv6 gateway.
        # 
        # - **swas**: a simple application server.
        # 
        # - **waf**: a Web Application Firewall (WAF) instance of the Exclusive edition.
        # 
        # - **ga_basic**: a Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The IP address of the asset.
        # 
        # This parameter is required.
        self.internet_ip = internet_ip
        # Specifies whether to automatically adjust the scrubbing threshold based on the traffic load on the asset. Valid values:
        # 
        # - **true**: automatically adjusts the scrubbing threshold. You do not need to configure the **Bps** and **Pps** parameters.
        # 
        # - **false**: The scrubbing threshold is not automatically adjusted. You must configure the **Bps** and **Pps** parameters. This is the default value.
        self.is_auto = is_auto
        # The packet scrubbing threshold. Unit: packets per second (PPS). When you modify Pps, Bps is required. Otherwise, Pps does not take effect.
        # 
        # The packet scrubbing threshold cannot exceed the peak number of inbound or outbound packets, whichever is larger, of the asset. You can use the monitoring tool that is provided by the asset to query the number of packets of the asset:
        # 
        # - If the asset is an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # 
        # - If the asset is an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        # 
        # - If the asset is an EIP, see [View monitoring data](https://help.aliyun.com/document_detail/85354.html).
        self.pps = pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.ddos_region_id is not None:
            result['DdosRegionId'] = self.ddos_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.is_auto is not None:
            result['IsAuto'] = self.is_auto

        if self.pps is not None:
            result['Pps'] = self.pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('DdosRegionId') is not None:
            self.ddos_region_id = m.get('DdosRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IsAuto') is not None:
            self.is_auto = m.get('IsAuto')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        return self

