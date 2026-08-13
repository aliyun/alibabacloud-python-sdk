# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrFirewallsV2DetailResponseBody(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_attachment_zone: str = None,
        firewall_description: str = None,
        firewall_eni_id: str = None,
        firewall_eni_vpc_id: str = None,
        firewall_eni_vswitch_id: str = None,
        firewall_id: str = None,
        firewall_name: str = None,
        firewall_service_mode: str = None,
        firewall_service_zones: List[str] = None,
        firewall_status: str = None,
        firewall_subnet_cidr: str = None,
        firewall_switch_status: str = None,
        firewall_vpc_cidr: str = None,
        region_no: str = None,
        request_id: str = None,
        route_mode: str = None,
        tr_attachment_id: str = None,
        tr_attachment_master_cidr: str = None,
        tr_attachment_master_zone: str = None,
        tr_attachment_slave_cidr: str = None,
        tr_attachment_slave_zone: str = None,
        tr_attachment_zones: List[main_models.DescribeTrFirewallsV2DetailResponseBodyTrAttachmentZones] = None,
        transit_router_id: str = None,
    ):
        # The instance ID of the Cloud Enterprise Network (CEN).
        self.cen_id = cen_id
        # The zone ID used by the firewall connection.
        self.firewall_attachment_zone = firewall_attachment_zone
        # The description of the firewall.
        self.firewall_description = firewall_description
        # The ENI ID of the firewall.
        self.firewall_eni_id = firewall_eni_id
        # The ID of the VPC to which the firewall ENI belongs.
        self.firewall_eni_vpc_id = firewall_eni_vpc_id
        # The ID of the vSwitch to which the firewall ENI belongs.
        self.firewall_eni_vswitch_id = firewall_eni_vswitch_id
        # The instance ID of the virtual private cloud (VPC) firewalls.
        self.firewall_id = firewall_id
        # The name of the virtual private cloud (VPC) firewalls instance.
        self.firewall_name = firewall_name
        # The deployment mode of the TR firewall service. Valid values: **PrimaryStandby** (active/standby mode) and **MultiPrimary** (active-active mode).
        self.firewall_service_mode = firewall_service_mode
        # The list of zone IDs used by the TR firewall service.
        self.firewall_service_zones = firewall_service_zones
        # The status of the firewall. Valid values:
        # 
        # - Creating: The firewall is being created.
        # 
        # - Deleting: The firewall is being deleted.
        # 
        # - Ready: The firewall is ready.
        self.firewall_status = firewall_status
        # The subnet CIDR block that hosts the firewall ENI in the firewall VPC in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
        # The status of the virtual private cloud (VPC) firewalls. Valid values:
        # 
        # - **opened**: enabled
        # 
        # - **closed**: disabled
        # 
        # - **notconfigured**: The VPC firewall is not configured.
        # 
        # - **configured**: The VPC firewall is configured.
        # 
        # - **creating**: The VPC firewall is being created.
        # 
        # - **opening**: The VPC firewall is being enabled.
        # 
        # - **deleting**: The VPC firewall is being deleted.
        # 
        # 
        # > If this parameter is not specified, virtual private cloud (VPC) firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The CIDR block of the firewall VPC in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The region ID of the transit router instance.
        self.region_no = region_no
        # The request ID.
        self.request_id = request_id
        # The routing mode. Valid values:
        # 
        # - **managed**: automatic mode
        # 
        # - **manual**: manual mode
        self.route_mode = route_mode
        # The attachment ID used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_id = tr_attachment_id
        # The primary subnet CIDR block used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # The primary zone used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_master_zone = tr_attachment_master_zone
        # The secondary subnet CIDR block used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # The secondary zone used to connect to the transit router in the firewall VPC in automatic mode.
        self.tr_attachment_slave_zone = tr_attachment_slave_zone
        # The list of zones and vSwitch CIDR blocks for the transit router connection.
        self.tr_attachment_zones = tr_attachment_zones
        # The instance ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.tr_attachment_zones:
            for v1 in self.tr_attachment_zones:
                 if v1:
                    v1.validate()

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

        if self.firewall_eni_id is not None:
            result['FirewallEniId'] = self.firewall_eni_id

        if self.firewall_eni_vpc_id is not None:
            result['FirewallEniVpcId'] = self.firewall_eni_vpc_id

        if self.firewall_eni_vswitch_id is not None:
            result['FirewallEniVswitchId'] = self.firewall_eni_vswitch_id

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.firewall_name is not None:
            result['FirewallName'] = self.firewall_name

        if self.firewall_service_mode is not None:
            result['FirewallServiceMode'] = self.firewall_service_mode

        if self.firewall_service_zones is not None:
            result['FirewallServiceZones'] = self.firewall_service_zones

        if self.firewall_status is not None:
            result['FirewallStatus'] = self.firewall_status

        if self.firewall_subnet_cidr is not None:
            result['FirewallSubnetCidr'] = self.firewall_subnet_cidr

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.firewall_vpc_cidr is not None:
            result['FirewallVpcCidr'] = self.firewall_vpc_cidr

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.tr_attachment_id is not None:
            result['TrAttachmentId'] = self.tr_attachment_id

        if self.tr_attachment_master_cidr is not None:
            result['TrAttachmentMasterCidr'] = self.tr_attachment_master_cidr

        if self.tr_attachment_master_zone is not None:
            result['TrAttachmentMasterZone'] = self.tr_attachment_master_zone

        if self.tr_attachment_slave_cidr is not None:
            result['TrAttachmentSlaveCidr'] = self.tr_attachment_slave_cidr

        if self.tr_attachment_slave_zone is not None:
            result['TrAttachmentSlaveZone'] = self.tr_attachment_slave_zone

        result['TrAttachmentZones'] = []
        if self.tr_attachment_zones is not None:
            for k1 in self.tr_attachment_zones:
                result['TrAttachmentZones'].append(k1.to_map() if k1 else None)

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

        if m.get('FirewallEniId') is not None:
            self.firewall_eni_id = m.get('FirewallEniId')

        if m.get('FirewallEniVpcId') is not None:
            self.firewall_eni_vpc_id = m.get('FirewallEniVpcId')

        if m.get('FirewallEniVswitchId') is not None:
            self.firewall_eni_vswitch_id = m.get('FirewallEniVswitchId')

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('FirewallName') is not None:
            self.firewall_name = m.get('FirewallName')

        if m.get('FirewallServiceMode') is not None:
            self.firewall_service_mode = m.get('FirewallServiceMode')

        if m.get('FirewallServiceZones') is not None:
            self.firewall_service_zones = m.get('FirewallServiceZones')

        if m.get('FirewallStatus') is not None:
            self.firewall_status = m.get('FirewallStatus')

        if m.get('FirewallSubnetCidr') is not None:
            self.firewall_subnet_cidr = m.get('FirewallSubnetCidr')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('FirewallVpcCidr') is not None:
            self.firewall_vpc_cidr = m.get('FirewallVpcCidr')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('TrAttachmentId') is not None:
            self.tr_attachment_id = m.get('TrAttachmentId')

        if m.get('TrAttachmentMasterCidr') is not None:
            self.tr_attachment_master_cidr = m.get('TrAttachmentMasterCidr')

        if m.get('TrAttachmentMasterZone') is not None:
            self.tr_attachment_master_zone = m.get('TrAttachmentMasterZone')

        if m.get('TrAttachmentSlaveCidr') is not None:
            self.tr_attachment_slave_cidr = m.get('TrAttachmentSlaveCidr')

        if m.get('TrAttachmentSlaveZone') is not None:
            self.tr_attachment_slave_zone = m.get('TrAttachmentSlaveZone')

        self.tr_attachment_zones = []
        if m.get('TrAttachmentZones') is not None:
            for k1 in m.get('TrAttachmentZones'):
                temp_model = main_models.DescribeTrFirewallsV2DetailResponseBodyTrAttachmentZones()
                self.tr_attachment_zones.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class DescribeTrFirewallsV2DetailResponseBodyTrAttachmentZones(DaraModel):
    def __init__(
        self,
        v_switch_cidr: str = None,
        v_switch_zone_id: str = None,
    ):
        # The CIDR block of the vSwitch for the transit router connection.
        self.v_switch_cidr = v_switch_cidr
        # The zone ID of the vSwitch for the transit router connection.
        self.v_switch_zone_id = v_switch_zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_cidr is not None:
            result['VSwitchCidr'] = self.v_switch_cidr

        if self.v_switch_zone_id is not None:
            result['VSwitchZoneId'] = self.v_switch_zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchCidr') is not None:
            self.v_switch_cidr = m.get('VSwitchCidr')

        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')

        return self

