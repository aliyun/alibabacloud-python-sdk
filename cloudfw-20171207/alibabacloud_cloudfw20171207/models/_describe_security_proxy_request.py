# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        member_uid: str = None,
        nat_gateway_id: str = None,
        page_no: str = None,
        page_size: str = None,
        proxy_id: str = None,
        proxy_name: str = None,
        region_no: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The UID of the member account within the current Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the NAT Gateway.
        self.nat_gateway_id = nat_gateway_id
        # The page number of the current page.
        self.page_no = page_no
        # The maximum number of entries to return on each page. The maximum value is 50.
        self.page_size = page_size
        # The ID of the NAT firewall.
        self.proxy_id = proxy_id
        # The name of the NAT firewall. The name must be 4 to 50 characters in length. It can contain letters, digits, underscores (_), and Chinese characters. It cannot start with an underscore (_).
        self.proxy_name = proxy_name
        # The region ID of the VPC.
        self.region_no = region_no
        # The status of the Cloud Firewall. Valid values:
        # 
        # - **configuring**: The firewall is being created.
        # 
        # - **deleting**: The firewall is being deleted.
        # 
        # - **normal**: The firewall is running.
        # 
        # - **abnormal**: The firewall is not running as expected.
        # 
        # - **opening**: The firewall is being enabled.
        # 
        # - **closing**: The firewall is being disabled.
        # 
        # - **closed**: The firewall is disabled.
        self.status = status
        # The ID of the VPC instance.
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

