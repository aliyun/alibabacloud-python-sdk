# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallDefaultIPSConfigRequest(DaraModel):
    def __init__(
        self,
        member_uid: str = None,
        vpc_firewall_id: str = None,
    ):
        # The UID of the member account.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall. Valid values:
        # 
        # - If the VPC firewall protects a network instance in a Cloud Enterprise Network (CEN) instance, set this parameter to the ID of the CEN instance. To query the ID of a CEN instance of Basic Edition, call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation. To query the ID of a CEN instance of Enterprise Edition, call the [DescribeTrFirewallsV2List](https://help.aliyun.com/document_detail/2384695.html) operation.
        # 
        # - If the VPC firewall protects traffic between two VPCs connected by an Express Connect circuit, set this parameter to the ID of the VPC firewall instance. To query the ID of the VPC firewall instance, call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation.
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
        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

