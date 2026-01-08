# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNatFirewallListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: int = None,
        nat_gateway_id: str = None,
        page_no: int = None,
        page_size: int = None,
        proxy_id: str = None,
        proxy_name: str = None,
        region_no: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The language of the content within the response. Valid values:
        # *   **zh** (default)
        # *   **en**
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # Default value: **10**.**** Maximum value: **50**.
        self.page_size = page_size
        # The ID of the NAT firewall.
        self.proxy_id = proxy_id
        # The name of the NAT firewall. The name must be 4 to 50 characters in length, and can contain letters, digits, and underscores (_). The name cannot start with an underscore.
        self.proxy_name = proxy_name
        # The region ID of the virtual private cloud (VPC).
        self.region_no = region_no
        # The status of the NAT firewall. Valid values:
        # 
        # *   configuring
        # *   deleting
        # *   normal
        # *   abnormal
        # *   opening
        # *   closing
        # *   closed
        self.status = status
        # The ID of the VPC.
        self.vpc_id = vpc_id

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

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

