# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class AddResolverRuleRequest(DaraModel):
    def __init__(
        self,
        edge_dns_clusters: List[main_models.AddResolverRuleRequestEdgeDnsClusters] = None,
        endpoint_id: str = None,
        forward_ip: List[main_models.AddResolverRuleRequestForwardIp] = None,
        lang: str = None,
        name: str = None,
        type: str = None,
        vpcs: List[main_models.AddResolverRuleRequestVpcs] = None,
        zone_name: str = None,
    ):
        self.edge_dns_clusters = edge_dns_clusters
        # The outbound endpoint ID. The outbound endpoint is used to forward the DNS requests to the specified destination IP addresses.
        self.endpoint_id = endpoint_id
        # The IP addresses and ports of the external DNS servers. Enter the IP addresses and ports of the destination servers to which the DNS requests are forwarded. You can enter up to **six** IP addresses and ports. Both private and public IP addresses are supported.
        # 
        # >  If you specify public IP addresses as the IP addresses of the external DNS servers and Elastic Compute Service (ECS) instances in the outbound VPC are not assigned public IP addresses, you need to activate NAT Gateway for the VPC and create and manage SNAT entries on a NAT gateway.
        # 
        # This parameter is required.
        self.forward_ip = forward_ip
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The name of the forwarding rule. You can name the rule based on your business requirements.
        # 
        # This parameter is required.
        self.name = name
        # The type of the forwarding rule. The parameter value can only be OUTBOUND, which indicates that DNS requests are forwarded to one or more external IP addresses.
        # 
        # >  You cannot change the value of Type after you create the forwarding rule.
        self.type = type
        self.vpcs = vpcs
        # The zone for which you want to forward DNS requests.
        # 
        # >  You cannot change the value of ZoneName after you create the forwarding rule.
        # 
        # This parameter is required.
        self.zone_name = zone_name

    def validate(self):
        if self.edge_dns_clusters:
            for v1 in self.edge_dns_clusters:
                 if v1:
                    v1.validate()
        if self.forward_ip:
            for v1 in self.forward_ip:
                 if v1:
                    v1.validate()
        if self.vpcs:
            for v1 in self.vpcs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EdgeDnsClusters'] = []
        if self.edge_dns_clusters is not None:
            for k1 in self.edge_dns_clusters:
                result['EdgeDnsClusters'].append(k1.to_map() if k1 else None)

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        result['ForwardIp'] = []
        if self.forward_ip is not None:
            for k1 in self.forward_ip:
                result['ForwardIp'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        result['Vpcs'] = []
        if self.vpcs is not None:
            for k1 in self.vpcs:
                result['Vpcs'].append(k1.to_map() if k1 else None)

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_dns_clusters = []
        if m.get('EdgeDnsClusters') is not None:
            for k1 in m.get('EdgeDnsClusters'):
                temp_model = main_models.AddResolverRuleRequestEdgeDnsClusters()
                self.edge_dns_clusters.append(temp_model.from_map(k1))

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        self.forward_ip = []
        if m.get('ForwardIp') is not None:
            for k1 in m.get('ForwardIp'):
                temp_model = main_models.AddResolverRuleRequestForwardIp()
                self.forward_ip.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k1 in m.get('Vpcs'):
                temp_model = main_models.AddResolverRuleRequestVpcs()
                self.vpcs.append(temp_model.from_map(k1))

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class AddResolverRuleRequestVpcs(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_type: str = None,
        vpc_user_id: int = None,
    ):
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.vpc_type = vpc_type
        self.vpc_user_id = vpc_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        if self.vpc_user_id is not None:
            result['VpcUserId'] = self.vpc_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        if m.get('VpcUserId') is not None:
            self.vpc_user_id = m.get('VpcUserId')

        return self

class AddResolverRuleRequestForwardIp(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        # The IP address of the destination server.
        # 
        # >  The following CIDR blocks are reserved by the system: 100.100.2.136 to 100.100.2.138 and 100.100.2.116 to 100.100.2.118. You cannot specify the IP addresses within these CIDR blocks for the external DNS servers.
        # 
        # This parameter is required.
        self.ip = ip
        # The port of the destination server.
        # 
        # This parameter is required.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class AddResolverRuleRequestEdgeDnsClusters(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

