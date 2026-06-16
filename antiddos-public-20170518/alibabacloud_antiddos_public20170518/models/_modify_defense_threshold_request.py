# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDefenseThresholdRequest(DaraModel):
    def __init__(
        self,
        bps: int = None,
        client_token: str = None,
        ddos_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        internet_ip: str = None,
        is_auto: bool = None,
        pps: int = None,
    ):
        # The scrubbing threshold for traffic in Mbps. This value cannot exceed the peak public network traffic of the instance. If you specify Bps, you must also specify Pps. Otherwise, the change does not take effect.
        # 
        # Use the monitoring tools of your instance to query its public network traffic:
        # 
        # - For an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # 
        # - For an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        # 
        # <props="china">
        # 
        # - For an EIP instance, see [View monitoring data](https://help.aliyun.com/document_detail/85354.html).
        self.bps = bps
        self.client_token = client_token
        # The region ID of the asset that is assigned a public IP address.
        # 
        # > Call [DescribeRegions](https://help.aliyun.com/document_detail/353250.html) to query all region IDs.
        # 
        # This parameter is required.
        self.ddos_region_id = ddos_region_id
        # The instance ID of the asset that is assigned a public IP address.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/354191.html) to query the IDs of the ECS, SLB, and EIP instances that belong to your Alibaba Cloud account.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The instance type of the asset that is assigned a public IP address. Valid values:
        # 
        # - **ecs**: Elastic Compute Service (ECS) instance.
        # 
        # - **slb**: Server Load Balancer (SLB) instance.
        # 
        # - **eip**: Elastic IP Address (EIP) instance.
        # 
        # - **ipv6**: IPv6 Gateway instance.
        # 
        # - **swas**: simple application server instance.
        # 
        # - **waf**: dedicated Web Application Firewall (WAF) instance.
        # 
        # - **ga_basic**: basic Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The public IP address of the asset.
        self.internet_ip = internet_ip
        # Specifies whether to automatically adjust the scrubbing threshold based on the traffic loads of the instance. Valid values:
        # 
        # - **true**: The scrubbing threshold is automatically adjusted. You do not need to set the **Bps** and **Pps** parameters.
        # 
        # - **false**: The scrubbing threshold is not automatically adjusted. You must set the **Bps** and **Pps** parameters.
        # 
        # Default value: false
        self.is_auto = is_auto
        # The scrubbing threshold for packets per second (pps). This value cannot exceed the peak packet traffic of the instance. If you specify Pps, you must also specify Bps. Otherwise, the change does not take effect.
        # 
        # Use the monitoring tools of your instance to query its packet traffic:
        # 
        # - For an ECS instance, see [View instance monitoring information](https://help.aliyun.com/document_detail/25482.html).
        # 
        # - For an SLB instance, see [View monitoring data](https://help.aliyun.com/document_detail/85982.html).
        # 
        # <props="china">
        # 
        # - For an EIP instance, see [View monitoring data](https://help.aliyun.com/document_detail/85354.html).
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

