# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrFirewallsV2DetailResponseBody(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        firewall_description: str = None,
        firewall_eni_id: str = None,
        firewall_eni_vpc_id: str = None,
        firewall_eni_vswitch_id: str = None,
        firewall_id: str = None,
        firewall_name: str = None,
        firewall_status: str = None,
        firewall_subnet_cidr: str = None,
        firewall_switch_status: str = None,
        firewall_vpc_cidr: str = None,
        region_no: str = None,
        request_id: str = None,
        route_mode: str = None,
        tr_attachment_master_cidr: str = None,
        tr_attachment_master_zone: str = None,
        tr_attachment_slave_cidr: str = None,
        tr_attachment_slave_zone: str = None,
        transit_router_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        self.cen_id = cen_id
        # The description of the VPC firewall.
        self.firewall_description = firewall_description
        # The ID of the Elastic Network Interface (ENI) with which the VPC firewall is associated.
        self.firewall_eni_id = firewall_eni_id
        # The ID of the VPC to which the ENI is attached.
        self.firewall_eni_vpc_id = firewall_eni_vpc_id
        # The ID of the vSwitch with which the ENI is associated.
        self.firewall_eni_vswitch_id = firewall_eni_vswitch_id
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The name of the VPC firewall.
        self.firewall_name = firewall_name
        # The status of the VPC firewall. Valid values:
        # 
        # *   Creating
        # *   Deleting
        # *   Ready
        self.firewall_status = firewall_status
        # The subnet CIDR block of the VPC in which the ENI of the firewall is stored in automatic mode.
        self.firewall_subnet_cidr = firewall_subnet_cidr
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
        # > If you do not specify this parameter, VPC firewalls in all states are queried.
        self.firewall_switch_status = firewall_switch_status
        # The CIDR block that is allocated to the VPC created for the VPC firewall in automatic mode.
        self.firewall_vpc_cidr = firewall_vpc_cidr
        # The region ID of the transit router.
        self.region_no = region_no
        # The request ID.
        self.request_id = request_id
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **managed**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # The primary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_master_cidr = tr_attachment_master_cidr
        # In automatic mode, the primary availability zone of the subnet in the firewall VPC used for connecting to TR.
        self.tr_attachment_master_zone = tr_attachment_master_zone
        # The secondary subnet CIDR block that the VPC uses to connect to the transit router in automatic mode.
        self.tr_attachment_slave_cidr = tr_attachment_slave_cidr
        # In automatic mode, the backup availability zone for the subnet used to connect TR in the firewall VPC.
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

