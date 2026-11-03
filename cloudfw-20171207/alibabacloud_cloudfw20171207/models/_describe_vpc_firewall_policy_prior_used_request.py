# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallPolicyPriorUsedRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        vpc_firewall_id: str = None,
    ):
        # The language of the request and response.
        # 
        # Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The ID of the access control policy group for the VPC border firewall. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to obtain the ID.
        # 
        # Valid values:
        # 
        # - When a VPC border firewall protects a Cloud Enterprise Network (CEN) instance, the policy group ID is the instance ID of the CEN instance.
        # 
        #   Example: cen-ervw0g12b5jbw*\\*\\*\\*
        # 
        # - When a VPC border firewall protects an Express Connect circuit, the policy group ID is the instance ID of the VPC border firewall.
        # 
        #   Example: vfw-a42bbb7b887148c9*\\*\\*\\*
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
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

