# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVpcFirewallControlPolicyRequest(DaraModel):
    def __init__(
        self,
        acl_uuid: str = None,
        lang: str = None,
        vpc_firewall_id: str = None,
    ):
        # The UUID of the access control policy for the VPC firewall.
        # 
        # When you delete an access control policy, you must provide the UUID of the policy. You can call the [DescribeVpcFirewallControlPolicy](https://help.aliyun.com/document_detail/159758.html) operation to query the UUID.
        # 
        # This parameter is required.
        self.acl_uuid = acl_uuid
        # The language of the content within the request and response.
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The ID of the policy group for the VPC firewall. You can call the [DescribeVpcFirewallAclGroupList](https://help.aliyun.com/document_detail/159760.html) operation to query the ID.
        # 
        # Valid values:
        # 
        # - If the VPC firewall is used to protect a Cloud Enterprise Network (CEN) instance, the value of this parameter is the ID of the CEN instance.
        # 
        #   Example: cen-ervw0g12b5jbw\\*\\*\\*\\*
        # - If the VPC firewall is used to protect an Express Connect circuit, the value of this parameter is the ID of the VPC firewall instance.
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

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclUuid') is not None:
            self.acl_uuid = m.get('AclUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

