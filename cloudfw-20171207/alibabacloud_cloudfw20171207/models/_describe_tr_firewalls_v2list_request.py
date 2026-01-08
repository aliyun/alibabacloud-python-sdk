# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrFirewallsV2ListRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        current_page: int = None,
        firewall_id: str = None,
        firewall_name: str = None,
        firewall_switch_status: str = None,
        lang: str = None,
        owner_id: str = None,
        page_size: int = None,
        region_no: str = None,
        route_mode: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The name of the VPC firewall.
        self.firewall_name = firewall_name
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not created.
        # *   **configured**: The VPC firewall is created but is not enabled.
        # *   **creating**: The VPC firewall is being created.
        # *   **opening**: The VPC firewall is being enabled.
        # *   **deleting**: The VPC firewall is being deleted.
        # 
        # >  If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        self.owner_id = owner_id
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The region ID of the transit router.
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        # 
        # >  If you do not specify this parameter, VPC firewalls in all routing modes are queried.
        self.route_mode = route_mode
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

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

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

