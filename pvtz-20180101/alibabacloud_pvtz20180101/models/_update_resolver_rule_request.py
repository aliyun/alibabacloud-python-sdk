# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class UpdateResolverRuleRequest(DaraModel):
    def __init__(
        self,
        endpoint_id: str = None,
        forward_ip: List[main_models.UpdateResolverRuleRequestForwardIp] = None,
        lang: str = None,
        name: str = None,
        priority_forward_configs: List[main_models.UpdateResolverRuleRequestPriorityForwardConfigs] = None,
        rule_id: str = None,
    ):
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The IP addresses and ports of the external Domain Name System (DNS) servers. Enter the IP addresses and ports of the destination servers to which the DNS requests are forwarded. You can enter up to six IP addresses and ports. Both private and public IP addresses are supported.
        # 
        # >  If you specify public IP addresses as the IP addresses of the external DNS servers and Elastic Compute Service (ECS) instances in the outbound virtual private cloud (VPC) are not assigned public IP addresses, you need to activate NAT Gateway for the VPC and create and manage SNAT entries on a NAT gateway.
        self.forward_ip = forward_ip
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # The name of the forwarding rule.
        self.name = name
        self.priority_forward_configs = priority_forward_configs
        # The ID of the forwarding rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id

    def validate(self):
        if self.forward_ip:
            for v1 in self.forward_ip:
                 if v1:
                    v1.validate()
        if self.priority_forward_configs:
            for v1 in self.priority_forward_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        result['PriorityForwardConfigs'] = []
        if self.priority_forward_configs is not None:
            for k1 in self.priority_forward_configs:
                result['PriorityForwardConfigs'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        self.forward_ip = []
        if m.get('ForwardIp') is not None:
            for k1 in m.get('ForwardIp'):
                temp_model = main_models.UpdateResolverRuleRequestForwardIp()
                self.forward_ip.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.priority_forward_configs = []
        if m.get('PriorityForwardConfigs') is not None:
            for k1 in m.get('PriorityForwardConfigs'):
                temp_model = main_models.UpdateResolverRuleRequestPriorityForwardConfigs()
                self.priority_forward_configs.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

class UpdateResolverRuleRequestPriorityForwardConfigs(DaraModel):
    def __init__(
        self,
        alidns_service_addresses: List[str] = None,
        custom_addresses: List[str] = None,
        enable_status: str = None,
        priority: int = None,
        protocol: str = None,
    ):
        self.alidns_service_addresses = alidns_service_addresses
        self.custom_addresses = custom_addresses
        self.enable_status = enable_status
        self.priority = priority
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alidns_service_addresses is not None:
            result['AlidnsServiceAddresses'] = self.alidns_service_addresses

        if self.custom_addresses is not None:
            result['CustomAddresses'] = self.custom_addresses

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlidnsServiceAddresses') is not None:
            self.alidns_service_addresses = m.get('AlidnsServiceAddresses')

        if m.get('CustomAddresses') is not None:
            self.custom_addresses = m.get('CustomAddresses')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class UpdateResolverRuleRequestForwardIp(DaraModel):
    def __init__(
        self,
        ip: str = None,
        port: int = None,
    ):
        # The IP address of the destination server.
        # 
        # >  You cannot specify the following IP addresses as the IP addresses of the external DNS servers because the IP addresses are reserved by the system: 100.100.2.136 to 100.100.2.138, and 100.100.2.116 to 100.100.2.118.
        self.ip = ip
        # The port of the destination server.
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

