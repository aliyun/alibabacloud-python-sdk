# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallCenListRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        current_page: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        member_uid: str = None,
        network_instance_id: str = None,
        owner_id: str = None,
        page_size: str = None,
        region_no: str = None,
        route_mode: str = None,
        transit_router_type: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.current_page = current_page
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        # *   **configured**: The VPC firewall is configured but is not enabled.
        # 
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The UID of the member that is managed by your Alibaba Cloud account. The member is also an Alibaba Cloud account.
        self.member_uid = member_uid
        # The ID of the network instance.
        self.network_instance_id = network_instance_id
        self.owner_id = owner_id
        # The number of entries to return on each page.
        # 
        # Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The region ID of the VPC.
        # 
        # > For more information about the regions, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **auto**: automatic mode
        # *   **manual**: manual mode
        # 
        # > If you do not specify this parameter, VPC firewalls in all routing modes are queried.
        self.route_mode = route_mode
        # The type of the transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition transit router
        # *   **Enterprise**: Enterprise Edition transit router
        self.transit_router_type = transit_router_type
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

