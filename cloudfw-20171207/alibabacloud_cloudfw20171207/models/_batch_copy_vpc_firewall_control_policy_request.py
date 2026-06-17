# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCopyVpcFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        source_vpc_firewall_id: str = None,
        target_vpc_firewall_id: str = None,
    ):
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the policy group for the source VPC firewall. Valid values:
        # 
        # - If the VPC firewall protects traffic between a network instance in a Cloud Enterprise Network (CEN) and a specified VPC, use the ID of the CEN instance. The network instance can be a VPC, a Virtual Border Router (VBR), or a Cloud Connect Network (CCN) instance.
        # 
        # - If the VPC firewall protects traffic between two VPCs connected by an Express Connect circuit, use the ID of the VPC firewall instance.
        # 
        # > Call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # This parameter is required.
        self.source_vpc_firewall_id = source_vpc_firewall_id
        # The ID of the policy group for the destination VPC firewall. Valid values:
        # 
        # - If the VPC firewall protects traffic between a network instance in a Cloud Enterprise Network (CEN) and a specified VPC, use the ID of the CEN instance. The network instance can be a VPC, a Virtual Border Router (VBR), or a Cloud Connect Network (CCN) instance.
        # 
        # - If the VPC firewall protects traffic between two VPCs connected by an Express Connect circuit, use the ID of the VPC firewall instance.
        # 
        # > Call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # This parameter is required.
        self.target_vpc_firewall_id = target_vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.source_vpc_firewall_id is not None:
            result['SourceVpcFirewallId'] = self.source_vpc_firewall_id

        if self.target_vpc_firewall_id is not None:
            result['TargetVpcFirewallId'] = self.target_vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SourceVpcFirewallId') is not None:
            self.source_vpc_firewall_id = m.get('SourceVpcFirewallId')

        if m.get('TargetVpcFirewallId') is not None:
            self.target_vpc_firewall_id = m.get('TargetVpcFirewallId')

        return self

