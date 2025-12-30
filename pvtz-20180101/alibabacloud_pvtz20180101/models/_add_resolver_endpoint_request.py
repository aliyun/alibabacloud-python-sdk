# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class AddResolverEndpointRequest(DaraModel):
    def __init__(
        self,
        ip_config: List[main_models.AddResolverEndpointRequestIpConfig] = None,
        lang: str = None,
        name: str = None,
        security_group_id: str = None,
        vpc_id: str = None,
        vpc_region_id: str = None,
    ):
        # The source IP addresses of outbound traffic. You must add two to six source IP addresses.
        # 
        # >  You must add at least two source IP addresses for outbound traffic to ensure high availability. We recommend that you add two IP addresses that reside in different zones. You can add up to six source IP addresses.
        # 
        # This parameter is required.
        self.ip_config = ip_config
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The endpoint name. The name can be up to 20 characters in length. If the upper limit is exceeded, an error message is returned.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the security group. The security group rules are applied to the outbound VPC.
        # 
        # >  After you create the outbound endpoint, you cannot change the value of SecurityGroupId. This prevents the forwarding of DNS requests from being interrupted due to misoperations.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The outbound VPC ID. All outbound Domain Name System (DNS) requests of the resolver are forwarded by this VPC.
        # 
        # >  After you create the outbound endpoint, you cannot change the value of VpcId. This prevents the forwarding of DNS requests from being interrupted due to misoperations.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The region ID of the outbound virtual private cloud (VPC).
        # 
        # This parameter is required.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        if self.ip_config:
            for v1 in self.ip_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpConfig'] = []
        if self.ip_config is not None:
            for k1 in self.ip_config:
                result['IpConfig'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_region_id is not None:
            result['VpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_config = []
        if m.get('IpConfig') is not None:
            for k1 in m.get('IpConfig'):
                temp_model = main_models.AddResolverEndpointRequestIpConfig()
                self.ip_config.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcRegionId') is not None:
            self.vpc_region_id = m.get('VpcRegionId')

        return self



class AddResolverEndpointRequestIpConfig(DaraModel):
    def __init__(
        self,
        az_id: str = None,
        cidr_block: str = None,
        ip: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the zone to which the vSwitch belongs.
        # 
        # This parameter is required.
        self.az_id = az_id
        # The IPv4 CIDR block of the vSwitch.
        # 
        # This parameter is required.
        self.cidr_block = cidr_block
        # The source IP address of outbound traffic. The IP address must be within the specified CIDR block. If you leave this parameter empty, the system automatically allocates an IP address.
        self.ip = ip
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.az_id is not None:
            result['AzId'] = self.az_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AzId') is not None:
            self.az_id = m.get('AzId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

