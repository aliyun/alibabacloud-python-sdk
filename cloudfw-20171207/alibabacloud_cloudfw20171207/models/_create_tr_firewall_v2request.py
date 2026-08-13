# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateTrFirewallV2Request(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_attachment_zone: str = None,
        firewall_description: str = None,
        firewall_name: str = None,
        firewall_service_mode: str = None,
        firewall_service_zones: List[str] = None,
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
        tr_attachment_zones: List[str] = None,
        transit_router_id: str = None,
    ):
        # The ID of the CEN instance. This parameter is required. Create a CEN instance in the CEN console before calling this operation, and ensure that an Enterprise Edition transit router has been created.
        self.cen_id = cen_id
        # The zone ID used by the firewall connection.
        self.firewall_attachment_zone = firewall_attachment_zone
        # The description of the firewall.
        self.firewall_description = firewall_description
        # The name of the Cloud Firewall instance.
        self.firewall_name = firewall_name
        # The deployment mode of the firewall service. Valid values:
        # 
        # - **PrimaryStandby**: Primary/standby mode.
        # - **MultiPrimary**: Active-active mode.
        # 
        # > If this parameter is not specified, the system automatically selects a deployment mode based on the capabilities of the transit router. If an invalid value is specified, the error ErrorFwServiceMode (-360437) is returned. MultiPrimary mode does not support specifying zones.
        self.firewall_service_mode = firewall_service_mode
        # The list of zone IDs used by the firewall service.
        self.firewall_service_zones = firewall_service_zones
        # The subnet CIDR block used to store the firewall ENI in the firewall VPC in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
        # The CIDR block of the firewall VPC in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The ID of the VPC in which the firewall ENI is created in manual mode.
        self.firewall_vpc_id = firewall_vpc_id
        # The ID of the vSwitch in which the firewall ENI is created in manual mode.
        self.firewall_vswitch_id = firewall_vswitch_id
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The region ID of the Enterprise Edition transit router. This parameter is required.
        self.region_no = region_no
        # The routing mode. This parameter is required. Valid values: managed (automatic mode) and manual (manual mode). In managed mode, you must specify FirewallVpcCidr, FirewallSubnetCidr, TrAttachmentSlaveCidr, and TrAttachmentMasterCidr. In manual mode, you must specify FirewallVpcId, FirewallVswitchId, TrAttachmentSlaveZone, and TrAttachmentMasterZone.
        self.route_mode = route_mode
        # The primary subnet CIDR block used to connect to the TR in the firewall VPC in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # The primary zone of the vSwitch.
        self.tr_attachment_master_zone = tr_attachment_master_zone
        # The secondary subnet CIDR block used to connect to the TR in the firewall VPC in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # The secondary zone of the vSwitch.
        self.tr_attachment_slave_zone = tr_attachment_slave_zone
        # The list of zone IDs used by the TR connection.
        self.tr_attachment_zones = tr_attachment_zones
        # The ID of the Enterprise Edition transit router instance. This parameter is required. The transit router must belong to the CEN instance specified by CenId.
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

        if self.firewall_attachment_zone is not None:
            result['FirewallAttachmentZone'] = self.firewall_attachment_zone

        if self.firewall_description is not None:
            result['FirewallDescription'] = self.firewall_description

        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name

        if self.firewall_service_mode is not None:
            result['FirewallServiceMode'] = self.firewall_service_mode

        if self.firewall_service_zones is not None:
            result['FirewallServiceZones'] = self.firewall_service_zones

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

        if self.tr_attachment_zones is not None:
            result['TrAttachmentZones'] = self.tr_attachment_zones

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('FirewallAttachmentZone') is not None:
            self.firewall_attachment_zone = m.get('FirewallAttachmentZone')

        if m.get('FirewallDescription') is not None:
            self.firewall_description = m.get('FirewallDescription')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        if m.get('FirewallServiceMode') is not None:
            self.firewall_service_mode = m.get('FirewallServiceMode')

        if m.get('FirewallServiceZones') is not None:
            self.firewall_service_zones = m.get('FirewallServiceZones')

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

        if m.get('TrAttachmentZones') is not None:
            self.tr_attachment_zones = m.get('TrAttachmentZones')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

