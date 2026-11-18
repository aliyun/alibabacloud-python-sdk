# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        basic_defense_enabled: str = None,
        firewall_service_mode: str = None,
        firewall_service_zones: List[str] = None,
        firewall_switch: str = None,
        fw_vswitch_zone_id: str = None,
        lang: str = None,
        master_vswitch_cidr: str = None,
        master_zone_id: str = None,
        nat_gateway_id: str = None,
        nat_mode: str = None,
        nat_route_entry_list: List[main_models.CreateSecurityProxyRequestNatRouteEntryList] = None,
        proxy_name: str = None,
        region_no: str = None,
        rule_class: str = None,
        run_mode: str = None,
        standby_vswitch_cidr: str = None,
        standby_zone_id: str = None,
        strict_mode: int = None,
        threat_intel_enabled: str = None,
        virtual_patch_enabled: str = None,
        vpc_id: str = None,
        vswitch_auto: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
    ):
        # Specifies whether to enable the basic protection policies of the IPS. If this parameter is not specified, the system default (enabled) is used. Valid values:
        # 
        # - **0**: disabled.
        # - **1**: enabled.
        self.basic_defense_enabled = basic_defense_enabled
        # The deployment mode of the firewall service. Valid values:
        # 
        # - **PrimaryStandby**: primary/secondary mode.
        # - **MultiPrimary**: active-active mode.
        self.firewall_service_mode = firewall_service_mode
        # The list of zone IDs used by the firewall service.
        self.firewall_service_zones = firewall_service_zones
        # The security protection switch. Valid values:
        # 
        # - **open**: enabled.
        # - **close**: disabled.
        self.firewall_switch = firewall_switch
        # The zone of the firewall vSwitch.
        self.fw_vswitch_zone_id = fw_vswitch_zone_id
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The vSwitch CIDR block of the GWLB endpoint (GWLBe) in the active zone. This parameter applies only to NAT firewalls that use the GWLB architecture. For the GWLB architecture, this parameter is required along with MasterZoneId, StandbyZoneId, and StandbyVSwitchCidr. If any of these parameters is missing, ErrorParameters is returned. The vSwitch is created by the firewall creation node based on this vSwitch CIDR block. This parameter is not read for the ENI architecture.
        self.master_vswitch_cidr = master_vswitch_cidr
        # The ID of the primary zone. This parameter applies only to NAT firewalls that use the GWLB architecture. For the GWLB architecture, this parameter is required along with MasterVSwitchCidr, StandbyZoneId, and StandbyVSwitchCidr. If any of these parameters is missing, ErrorParameters is returned. The value must be the same as the zone where the NAT gateway resides. This parameter is not read for the ENI architecture.
        self.master_zone_id = master_zone_id
        # The ID of the NAT gateway.
        # 
        # This parameter is required.
        self.nat_gateway_id = nat_gateway_id
        # The architecture type of the NAT firewall. Valid values: **eni** (traditional ENI architecture) and **gwlb** (new GWLB architecture). If this parameter is omitted or left empty, the firewall is created by using the ENI architecture, and no implicit selection is performed on the server side. You can obtain the recommended architecture from the response of the DescribeNatFirewallArchitecture operation and pass it back when you create the firewall.
        self.nat_mode = nat_mode
        # The list of routes to be switched for the NAT gateway.
        self.nat_route_entry_list = nat_route_entry_list
        # The name of the NAT firewall. The name must be 4 to 50 characters in length and can contain uppercase and lowercase letters, Chinese characters, digits, and underscores (_). It cannot start with an underscore.
        # 
        # This parameter is required.
        self.proxy_name = proxy_name
        # The region ID of the VPC.
        # 
        # > For more information about the regions supported by Cloud Firewall, see [Supported regions](https://help.aliyun.com/document_detail/195657.html).
        # 
        # This parameter is required.
        self.region_no = region_no
        # The level of the IPS rule group. This parameter is valid only in block mode. If this parameter is not specified, the system default (medium) is used. Valid values:
        # 
        # - **0**: none. The value is forced to 0 in monitor mode.
        # - **1**: loose.
        # - **2**: medium.
        # - **3**: strict.
        self.rule_class = rule_class
        # The IPS defense mode. This parameter is supported only by NAT firewalls that use the GWLB architecture. If this parameter is not specified, the system default (Block Mode) is used. Valid values:
        # 
        # - **0**: monitor mode. Only alerting is triggered, and traffic is not blocked.
        # - **1**: Block Mode.
        self.run_mode = run_mode
        # The vSwitch CIDR block of the GWLBe in the standby zone. This parameter applies only to NAT firewalls that use the GWLB architecture. For the GWLB architecture, this parameter is required along with MasterZoneId, MasterVSwitchCidr, and StandbyZoneId. If any of these parameters is missing, ErrorParameters is returned. The vSwitch is created by the firewall creation node based on this vSwitch CIDR block. This parameter is not read for the ENI architecture.
        self.standby_vswitch_cidr = standby_vswitch_cidr
        # The ID of the secondary zone. This parameter applies only to NAT firewalls that use the GWLB architecture. For the GWLB architecture, this parameter is required along with MasterZoneId, MasterVSwitchCidr, and StandbyVSwitchCidr. If any of these parameters is missing, ErrorParameters is returned. The value cannot be the same as MasterZoneId. If they are the same, ErrorZoneIdInvalid is returned. This parameter is not read for the ENI architecture.
        self.standby_zone_id = standby_zone_id
        # Specifies whether to enable strict mode. Valid values:
        # 
        # - **1**: enables strict mode.
        # - **0**: disables strict mode.
        self.strict_mode = strict_mode
        # Specifies whether to enable the threat intelligence rules of the IPS. If this parameter is not specified, the system default (enabled) is used. Valid values:
        # 
        # - **0**: disabled.
        # - **1**: enabled.
        self.threat_intel_enabled = threat_intel_enabled
        # Specifies whether to enable the Virtual Patches of the IPS. If this parameter is not specified, the system default (enabled) is used. Valid values:
        # 
        # - **0**: disabled.
        # - **1**: enabled.
        self.virtual_patch_enabled = virtual_patch_enabled
        # The instance ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # Specifies whether to use the automatic mode for the vSwitch. Valid values:
        # 
        # - **true**: automatic mode.
        # - **false**: manual mode.
        # 
        # > Default value: **true**. If VswitchAuto is set to true, VswitchCidr is required and must be a valid CIDR block. If VswitchAuto is set to false, VswitchId is required.
        self.vswitch_auto = vswitch_auto
        # The CIDR block of the vSwitch. This parameter is required when the automatic mode is used for the vSwitch.
        self.vswitch_cidr = vswitch_cidr
        # The ID of the vSwitch. This parameter is required when the manual mode is used for the vSwitch.
        self.vswitch_id = vswitch_id

    def validate(self):
        if self.nat_route_entry_list:
            for v1 in self.nat_route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_defense_enabled is not None:
            result['BasicDefenseEnabled'] = self.basic_defense_enabled

        if self.firewall_service_mode is not None:
            result['FirewallServiceMode'] = self.firewall_service_mode

        if self.firewall_service_zones is not None:
            result['FirewallServiceZones'] = self.firewall_service_zones

        if self.firewall_switch is not None:
            result['FirewallSwitch'] = self.firewall_switch

        if self.fw_vswitch_zone_id is not None:
            result['FwVswitchZoneId'] = self.fw_vswitch_zone_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.master_vswitch_cidr is not None:
            result['MasterVSwitchCidr'] = self.master_vswitch_cidr

        if self.master_zone_id is not None:
            result['MasterZoneId'] = self.master_zone_id

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_mode is not None:
            result['NatMode'] = self.nat_mode

        result['NatRouteEntryList'] = []
        if self.nat_route_entry_list is not None:
            for k1 in self.nat_route_entry_list:
                result['NatRouteEntryList'].append(k1.to_map() if k1 else None)

        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.standby_vswitch_cidr is not None:
            result['StandbyVSwitchCidr'] = self.standby_vswitch_cidr

        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        if self.threat_intel_enabled is not None:
            result['ThreatIntelEnabled'] = self.threat_intel_enabled

        if self.virtual_patch_enabled is not None:
            result['VirtualPatchEnabled'] = self.virtual_patch_enabled

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_auto is not None:
            result['VswitchAuto'] = self.vswitch_auto

        if self.vswitch_cidr is not None:
            result['VswitchCidr'] = self.vswitch_cidr

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicDefenseEnabled') is not None:
            self.basic_defense_enabled = m.get('BasicDefenseEnabled')

        if m.get('FirewallServiceMode') is not None:
            self.firewall_service_mode = m.get('FirewallServiceMode')

        if m.get('FirewallServiceZones') is not None:
            self.firewall_service_zones = m.get('FirewallServiceZones')

        if m.get('FirewallSwitch') is not None:
            self.firewall_switch = m.get('FirewallSwitch')

        if m.get('FwVswitchZoneId') is not None:
            self.fw_vswitch_zone_id = m.get('FwVswitchZoneId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MasterVSwitchCidr') is not None:
            self.master_vswitch_cidr = m.get('MasterVSwitchCidr')

        if m.get('MasterZoneId') is not None:
            self.master_zone_id = m.get('MasterZoneId')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatMode') is not None:
            self.nat_mode = m.get('NatMode')

        self.nat_route_entry_list = []
        if m.get('NatRouteEntryList') is not None:
            for k1 in m.get('NatRouteEntryList'):
                temp_model = main_models.CreateSecurityProxyRequestNatRouteEntryList()
                self.nat_route_entry_list.append(temp_model.from_map(k1))

        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('StandbyVSwitchCidr') is not None:
            self.standby_vswitch_cidr = m.get('StandbyVSwitchCidr')

        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        if m.get('ThreatIntelEnabled') is not None:
            self.threat_intel_enabled = m.get('ThreatIntelEnabled')

        if m.get('VirtualPatchEnabled') is not None:
            self.virtual_patch_enabled = m.get('VirtualPatchEnabled')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchAuto') is not None:
            self.vswitch_auto = m.get('VswitchAuto')

        if m.get('VswitchCidr') is not None:
            self.vswitch_cidr = m.get('VswitchCidr')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class CreateSecurityProxyRequestNatRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        route_table_id: str = None,
    ):
        # The destination CIDR block of the default route.
        # 
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # The next hop ID of the original NAT gateway.
        # 
        # This parameter is required.
        self.next_hop_id = next_hop_id
        # The network type of the next hop. Valid values: NatGateway.
        # 
        # This parameter is required.
        self.next_hop_type = next_hop_type
        # The ID of the route table to which the default route of the NAT gateway belongs.
        # 
        # This parameter is required.
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

