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
        # The ID of the CEN instance. Create a CEN instance in the CEN console and make sure that an Enterprise Edition transit router is created.
        # 
        # > Note: Although the required field in the schema is set to false, this parameter is actually required. If this parameter is not specified, the API returns ErrorParameters(400).
        self.cen_id = cen_id
        # The zone ID used for the firewall connection.
        self.firewall_attachment_zone = firewall_attachment_zone
        # The description of the firewall.
        self.firewall_description = firewall_description
        # The name of the Cloud Firewall instance.
        self.firewall_name = firewall_name
        # The deployment mode of the firewall service. Valid values:
        # 
        # - **PrimaryStandby**: primary/secondary mode
        # - **MultiPrimary**: active-active mode
        # 
        # > If this parameter is not specified, the system automatically selects the deployment mode based on the capabilities of the transit router. If the value is invalid, ErrorFwServiceMode (-360437) is returned. The MultiPrimary mode does not support specifying zones.
        self.firewall_service_mode = firewall_service_mode
        # The list of zone IDs used by the firewall service.
        self.firewall_service_zones = firewall_service_zones
        # The CIDR block of the subnet that stores the firewall elastic network interface (ENI) in the firewall VPC in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
        # The CIDR block of the firewall VPC in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The ID of the VPC where the firewall ENI is created in manual mode.
        self.firewall_vpc_id = firewall_vpc_id
        # The ID of the vSwitch where the firewall ENI is created in manual mode.
        self.firewall_vswitch_id = firewall_vswitch_id
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The region ID of the Enterprise Edition transit router.
        # 
        # > Note: Although the required field in the schema is set to false, this parameter is actually required. If this parameter is not specified, the API returns ErrorParameters(400).
        self.region_no = region_no
        # The routing mode. Valid values: managed (automatic mode), manual (manual mode for custom VPCs), and semi-managed (manual mode for managed VPCs).
        # 
        # - In managed mode, you only need to specify FirewallVpcCidr. The FirewallSubnetCidr, TrAttachmentSlaveCidr, and TrAttachmentMasterCidr parameters are deprecated (deprecated:true) and do not need to be specified.
        # 
        # - In manual mode, you must specify FirewallVpcId, FirewallVswitchId, TrAttachmentSlaveZone, and TrAttachmentMasterZone.
        # 
        # - In semi-managed mode, you only need to specify FirewallVpcCidr.
        # 
        # > Note: Although the required field in the schema is set to false, this parameter is actually required. If this parameter is not specified, the API returns ErrorParameters(400).
        self.route_mode = route_mode
        # The primary CIDR block of the subnet used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # The primary zone of the vSwitch.
        self.tr_attachment_master_zone = tr_attachment_master_zone
        # The secondary CIDR block of the subnet used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # The secondary zone of the vSwitch.
        self.tr_attachment_slave_zone = tr_attachment_slave_zone
        # The list of zone IDs used for the transit router connection.
        self.tr_attachment_zones = tr_attachment_zones
        # The ID of the Enterprise Edition transit router instance. The transit router must belong to the CEN instance specified by CenId.
        # 
        # > Note: Although the required field in the schema is set to false, this parameter is actually required. If this parameter is not specified, the API returns ErrorParameters(400).
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

