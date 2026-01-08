# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcFirewallDefaultIPSConfigRequest(DaraModel):
    def __init__(
        self,
        basic_rules: str = None,
        enable_all_patch: str = None,
        lang: str = None,
        member_uid: str = None,
        rule_class: str = None,
        run_mode: str = None,
        source_ip: str = None,
        vpc_firewall_id: str = None,
    ):
        # Specifies whether to enable basic protection. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        # 
        # This parameter is required.
        self.basic_rules = basic_rules
        # Specifies whether to enable virtual patching. Valid values:
        # 
        # *   **1**: yes.
        # *   **0**: no.
        # 
        # This parameter is required.
        self.enable_all_patch = enable_all_patch
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
        self.rule_class = rule_class
        # The mode of the intrusion prevention system (IPS). Valid values:
        # 
        # *   **1**: block mode.
        # *   **0**: monitor mode.
        # 
        # This parameter is required.
        self.run_mode = run_mode
        # The source IP address of the request.
        self.source_ip = source_ip
        # The instance ID of the VPC firewall.
        # 
        # *   If the VPC firewall protects traffic between a VPC and a network instance that is attached to a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance. The network instance can be a VPC, a virtual border router (VBR), or a Cloud Connect Network (CCN) instance. You can call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the IDs of CEN instances.
        # *   If the VPC firewall protects traffic between two VPCs that are connected by using an Express Connect circuit, the value of this parameter is the instance ID of the VPC firewall. You can call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the instance IDs of VPC firewalls.
        # 
        # This parameter is required.
        self.vpc_firewall_id = vpc_firewall_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules

        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')

        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

