# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrFirewallV2Request(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_description: str = None,
        firewall_name: str = None,
        firewall_subnet_cidr: str = None,
        firewall_vpc_cidr: str = None,
        firewall_vpc_id: str = None,
        firewall_vswitch_id: str = None,
        lang: str = None,
        region_no: str = None,
        route_mode: str = None,
        tr_attachment_master_cidr: str = None,
        tr_attachment_master_zone: str = None,
        tr_attachment_slave_cidr: str = None,
        tr_attachment_slave_zone: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The description of the firewall.
        self.firewall_description = firewall_description
        # The name of the firewall.
        self.firewall_name = firewall_name
        # The subnet CIDR block of the VPC in which the ENI of the firewall is stored in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
        # The CIDR block that is allocated to the VPC created for the VPC firewall in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The ID of the VPC in which the ENI associated with the VPC firewall is created in manual mode.
        self.firewall_vpc_id = firewall_vpc_id
        # The ID of the vSwitch that is used to create the ENI in manual mode.
        self.firewall_vswitch_id = firewall_vswitch_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # The region ID of the route router.
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # The primary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # The primary zone for the vSwitch.
        self.tr_attachment_master_zone = tr_attachment_master_zone
        # The secondary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # The secondary zone for the vSwitch.
        self.tr_attachment_slave_zone = tr_attachment_slave_zone
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

        if self.firewall_description is not None:
            result['FirewallDescription'] = self.firewall_description

        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name

        if self.firewall_subnet_cidr is not None:
            result['FirewallSubnetCidr'] = self.firewall_subnet_cidr

        if self.firewall_vpc_cidr is not None:
            result['FirewallVpcCidr'] = self.firewall_vpc_cidr

        if self.firewall_vpc_id is not None:
            result['FirewallVpcId'] = self.firewall_vpc_id

        if self.firewall_vswitch_id is not None:
            result['FirewallVswitchId'] = self.firewall_vswitch_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.tr_attachment_master_cidr is not None:
            result['TrAttachmentMasterCidr'] = self.tr_attachment_master_cidr

        if self.tr_attachment_master_zone is not None:
            result['TrAttachmentMasterZone'] = self.tr_attachment_master_zone

        if self.tr_attachment_slave_cidr is not None:
            result['TrAttachmentSlaveCidr'] = self.tr_attachment_slave_cidr

        if self.tr_attachment_slave_zone is not None:
            result['TrAttachmentSlaveZone'] = self.tr_attachment_slave_zone

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('FirewallDescription') is not None:
            self.firewall_description = m.get('FirewallDescription')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        if m.get('FirewallSubnetCidr') is not None:
            self.firewall_subnet_cidr = m.get('FirewallSubnetCidr')

        if m.get('FirewallVpcCidr') is not None:
            self.firewall_vpc_cidr = m.get('FirewallVpcCidr')

        if m.get('FirewallVpcId') is not None:
            self.firewall_vpc_id = m.get('FirewallVpcId')

        if m.get('FirewallVswitchId') is not None:
            self.firewall_vswitch_id = m.get('FirewallVswitchId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('TrAttachmentMasterCidr') is not None:
            self.tr_attachment_master_cidr = m.get('TrAttachmentMasterCidr')

        if m.get('TrAttachmentMasterZone') is not None:
            self.tr_attachment_master_zone = m.get('TrAttachmentMasterZone')

        if m.get('TrAttachmentSlaveCidr') is not None:
            self.tr_attachment_slave_cidr = m.get('TrAttachmentSlaveCidr')

        if m.get('TrAttachmentSlaveZone') is not None:
            self.tr_attachment_slave_zone = m.get('TrAttachmentSlaveZone')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

