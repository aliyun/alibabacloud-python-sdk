# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyVpcFirewallControlPolicyPositionRequest(DaraModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
        new_order: str = None,
        old_order: str = None,
        vpc_firewall_id: str = None,
    ):
        # The unique ID of the access control policy.
        # 
        # To modify an access control policy, provide the unique ID of the policy. Call the [DescribeVpcFirewallControlPolicy](https://help.aliyun.com/document_detail/159758.html) operation to obtain the ID.
        self.acl_uuid = acl_uuid
        # The language of the request and response.
        # 
        # Valid values:
        # 
        # - **zh** (Default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The new priority of the access control policy.
        # 
        # > For more information about the valid range of priorities, see [DescribePolicyPriorities](https://help.aliyun.com/document_detail/474145.html).
        # 
        # This parameter is required.
        self.new_order = new_order
        # The original priority of the access control policy.
        # 
        # > This parameter is deprecated. Use the AclUuid parameter to specify the policy to modify.
        self.old_order = old_order
        # The ID of the policy group for the VPC firewall. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to obtain the ID.
        # 
        # Valid values:
        # 
        # - If the VPC firewall protects a Cloud Enterprise Network (CEN) instance, the ID of the policy group is the ID of the CEN instance.
        # 
        #   Example: cen-ervw0g12b5jbw\\*\\*\\*\\*
        # 
        # - If the VPC firewall protects an Express Connect circuit, the ID of the policy group is the ID of the VPC firewall instance.
        # 
        #   Example: vfw-a42bbb7b887148c9\\*\\*\\*\\*
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
        if self.acl_uuid is not None:
            result['AclUuid'] = self.acl_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.new_order is not None:
            result['NewOrder'] = self.new_order

        if self.old_order is not None:
            result['OldOrder'] = self.old_order

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NewOrder') is not None:
            self.new_order = m.get('NewOrder')

        if m.get('OldOrder') is not None:
            self.old_order = m.get('OldOrder')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

