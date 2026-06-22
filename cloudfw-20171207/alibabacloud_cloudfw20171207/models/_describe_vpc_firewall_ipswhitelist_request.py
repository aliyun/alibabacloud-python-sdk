# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallIPSWhitelistRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: int = None,
        vpc_firewall_id: str = None,
    ):
        # The language of the request and response.
        # 
        # Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the Cloud Firewall member accounts.
        self.member_uid = member_uid
        # The instance ID of the VPC firewall. Valid values:
        # 
        # - If the VPC firewall protects network instances in a Cloud Enterprise Network (CEN) instance, the instance ID is the CEN instance ID. For CEN Basic Edition, call the [DescribeVpcFirewallCenList](https://help.aliyun.com/document_detail/345777.html) operation to query the CEN instance ID. For CEN Enterprise Edition, call the [DescribeTrFirewallsV2List](https://help.aliyun.com/document_detail/2384695.html) operation to query the CEN instance ID.
        # - If the VPC firewall protects traffic between two VPCs connected through Express Connect, the instance ID is the VPC firewall instance ID. Call the [DescribeVpcFirewallList](https://help.aliyun.com/document_detail/342932.html) operation to query the VPC firewall instance ID.
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

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

