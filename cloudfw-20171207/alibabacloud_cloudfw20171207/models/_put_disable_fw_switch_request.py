# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PutDisableFwSwitchRequest(DaraModel):
    def __init__(
        self,
        ip_version: str = None,
        ipaddr_list: List[str] = None,
        lang: str = None,
        member_uid: str = None,
        region_list: List[str] = None,
        resource_type_list: List[str] = None,
        source_ip: str = None,
    ):
        # The IP version.
        self.ip_version = ip_version
        # The IP addresses.
        # 
        # > You must specify a value for at least one of the following parameters: `IpaddrList`, `RegionList`, and `ResourceTypeList`.
        self.ipaddr_list = ipaddr_list
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The unique identifier of the member.
        self.member_uid = member_uid
        # The regions.
        # 
        # > You must specify a value for at least one of the following parameters: `IpaddrList`, `RegionList`, and `ResourceTypeList`.
        self.region_list = region_list
        # The asset types. Valid values:
        # 
        # - **BastionHostEgressIP**: The egress IP address of a bastion host.
        # 
        # - **BastionHostIngressIP**: The ingress IP address of a bastion host.
        # 
        # - **EcsEIP**: The Elastic IP Address (EIP) of an ECS instance.
        # 
        # - **EcsPublicIP**: The public IP address of an ECS instance.
        # 
        # - **EIP**: An Elastic IP Address (EIP).
        # 
        # - **EniEIP**: The EIP of an elastic network interface (ENI).
        # 
        # - **NatEIP**: The EIP of a NAT Gateway instance.
        # 
        # - **SlbEIP**: The EIP of a Server Load Balancer (SLB) or Classic Load Balancer (CLB) instance.
        # 
        # - **SlbPublicIP**: The public IP address of an SLB or CLB instance.
        # 
        # - **NatPublicIP**: The public IP address of a NAT Gateway instance.
        # 
        # - **HAVIP**: A High-availability Virtual IP (HAVIP).
        # 
        # - **NlbEIP**: The EIP of a Network Load Balancer (NLB) instance.
        # 
        # - **ApiGatewayEIP**: The public IP address of an API Gateway instance.
        # 
        # - **AlbEIP**: The EIP of an Application Load Balancer (ALB) instance.
        # 
        # - **AiGatewayEIP**: The public IP address of an AI Gateway instance.
        # 
        # - **GaEIP**: The EIP of a Global Accelerator (GA) instance.
        # 
        # - **SwasEIP**: The public IP address of a Simple Application Server instance.
        # 
        # - **EcdEIP**: The public IP address of an Elastic Desktop Service (ECD) instance.
        # 
        # - **BastionHostIP**: The IP address of a bastion host.
        # 
        # > You must specify a value for at least one of the following parameters: `IpaddrList`, `RegionList`, and `ResourceTypeList`.
        self.resource_type_list = resource_type_list
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ipaddr_list is not None:
            result['IpaddrList'] = self.ipaddr_list

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.region_list is not None:
            result['RegionList'] = self.region_list

        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IpaddrList') is not None:
            self.ipaddr_list = m.get('IpaddrList')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')

        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

