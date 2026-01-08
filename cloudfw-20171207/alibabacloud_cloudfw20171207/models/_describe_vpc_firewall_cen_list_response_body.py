# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallCenListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vpc_firewalls: List[main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewalls] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The total number of VPC firewalls.
        self.total_count = total_count
        # The information about the VPC firewalls.
        self.vpc_firewalls = vpc_firewalls

    def validate(self):
        if self.vpc_firewalls:
            for v1 in self.vpc_firewalls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpcFirewalls'] = []
        if self.vpc_firewalls is not None:
            for k1 in self.vpc_firewalls:
                result['VpcFirewalls'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpc_firewalls = []
        if m.get('VpcFirewalls') is not None:
            for k1 in m.get('VpcFirewalls'):
                temp_model = main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewalls()
                self.vpc_firewalls.append(temp_model.from_map(k1))

        return self

class DescribeVpcFirewallCenListResponseBodyVpcFirewalls(DaraModel):
    def __init__(
        self,
        acl_config: main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsAclConfig = None,
        cen_id: str = None,
        cen_name: str = None,
        connect_type: str = None,
        firewall_switch_status: str = None,
        ips_config: main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig = None,
        local_vpc: main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc = None,
        member_uid: str = None,
        precheck_status: str = None,
        region_status: str = None,
        result_code: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # ACL engine mode.
        self.acl_config = acl_config
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The name of the CEN instance.
        self.cen_name = cen_name
        # The connection type of the VPC firewall. The value is fixed as cen, which indicates a CEN instance.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        self.firewall_switch_status = firewall_switch_status
        # The intrusion prevention system (IPS) configurations.
        self.ips_config = ips_config
        # The details about the VPC.
        self.local_vpc = local_vpc
        # The UID of the member that is manged by your Alibaba Cloud account. The member is also an Alibaba Cloud account.
        self.member_uid = member_uid
        # Indicates whether the VPC firewall can be automatically enabled to protect VPC traffic based on route learning. Valid values:
        # 
        # *   **passed**: The VPC firewall can be automatically enabled.
        # *   **failed**: The VPC firewall cannot be automatically enabled.
        # *   **unknown**: The VPC firewall is in an unknown state.
        self.precheck_status = precheck_status
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **Unauthorized**: Cloud Firewall is not authorized to access the VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **RegionDisable**: VPC Firewall is not supported in the region of the VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **OpsDisable**: You are not allowed to create the VPC firewall.
        # *   **VbrNotSupport**: The VPC firewall cannot be created for a VBR that is attached to the CEN instance.
        # *   Empty string: You can create a VPC firewall for the network instance.
        self.result_code = result_code
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id
        # The instance name of the VPC firewall.
        self.vpc_firewall_name = vpc_firewall_name

    def validate(self):
        if self.acl_config:
            self.acl_config.validate()
        if self.ips_config:
            self.ips_config.validate()
        if self.local_vpc:
            self.local_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_config is not None:
            result['AclConfig'] = self.acl_config.to_map()

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_name is not None:
            result['CenName'] = self.cen_name

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.firewall_switch_status is not None:
            result['FirewallSwitchStatus'] = self.firewall_switch_status

        if self.ips_config is not None:
            result['IpsConfig'] = self.ips_config.to_map()

        if self.local_vpc is not None:
            result['LocalVpc'] = self.local_vpc.to_map()

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.precheck_status is not None:
            result['PrecheckStatus'] = self.precheck_status

        if self.region_status is not None:
            result['RegionStatus'] = self.region_status

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vpc_firewall_name is not None:
            result['VpcFirewallName'] = self.vpc_firewall_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclConfig') is not None:
            temp_model = main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsAclConfig()
            self.acl_config = temp_model.from_map(m.get('AclConfig'))

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenName') is not None:
            self.cen_name = m.get('CenName')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('IpsConfig') is not None:
            temp_model = main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m.get('IpsConfig'))

        if m.get('LocalVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc()
            self.local_vpc = temp_model.from_map(m.get('LocalVpc'))

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PrecheckStatus') is not None:
            self.precheck_status = m.get('PrecheckStatus')

        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpc(DaraModel):
    def __init__(
        self,
        authorization_status: str = None,
        defend_cidr_list: List[str] = None,
        manual_vswitch_id: str = None,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        owner_id: int = None,
        region_no: str = None,
        route_mode: str = None,
        support_manual_mode: str = None,
        transit_router_type: str = None,
        vpc_cidr_table_list: List[main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether the VPC is granted the required permissions. The value is fixed as **authorized**, which indicates that the VPC is granted the required permissions.
        self.authorization_status = authorization_status
        # An array consisting of the CIDR blocks that are protected by the VPC firewall.
        self.defend_cidr_list = defend_cidr_list
        # The ID of the specified vSwitch when the routing mode is manual.
        self.manual_vswitch_id = manual_vswitch_id
        # The ID of the network instance.
        self.network_instance_id = network_instance_id
        # The name of the network instance.
        self.network_instance_name = network_instance_name
        # The type of the network instance. Valid values:
        # 
        # *   **VPC**
        # *   **VBR**
        # *   **CCN**
        self.network_instance_type = network_instance_type
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The region ID of the VPC.
        self.region_no = region_no
        # The routing mode of the VPC firewall. Valid values:
        # 
        # *   **auto**: automatic mode
        # *   **manual**: manual mode
        self.route_mode = route_mode
        # Indicates whether the manual routing mode is supported. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.support_manual_mode = support_manual_mode
        # The edition of the CEN transit router. Valid values:
        # 
        # *   **Basic**: Basic Edition transit router
        # *   **Enterprise**: Enterprise Edition transit router
        self.transit_router_type = transit_router_type
        # An array that consists of the CIDR blocks of the VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.vpc_cidr_table_list:
            for v1 in self.vpc_cidr_table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_status is not None:
            result['AuthorizationStatus'] = self.authorization_status

        if self.defend_cidr_list is not None:
            result['DefendCidrList'] = self.defend_cidr_list

        if self.manual_vswitch_id is not None:
            result['ManualVSwitchId'] = self.manual_vswitch_id

        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.route_mode is not None:
            result['RouteMode'] = self.route_mode

        if self.support_manual_mode is not None:
            result['SupportManualMode'] = self.support_manual_mode

        if self.transit_router_type is not None:
            result['TransitRouterType'] = self.transit_router_type

        result['VpcCidrTableList'] = []
        if self.vpc_cidr_table_list is not None:
            for k1 in self.vpc_cidr_table_list:
                result['VpcCidrTableList'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationStatus') is not None:
            self.authorization_status = m.get('AuthorizationStatus')

        if m.get('DefendCidrList') is not None:
            self.defend_cidr_list = m.get('DefendCidrList')

        if m.get('ManualVSwitchId') is not None:
            self.manual_vswitch_id = m.get('ManualVSwitchId')

        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RouteMode') is not None:
            self.route_mode = m.get('RouteMode')

        if m.get('SupportManualMode') is not None:
            self.support_manual_mode = m.get('SupportManualMode')

        if m.get('TransitRouterType') is not None:
            self.transit_router_type = m.get('TransitRouterType')

        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k1 in m.get('VpcCidrTableList'):
                temp_model = main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList(DaraModel):
    def __init__(
        self,
        route_entry_list: List[main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # An array that consists of the route entries for the VPC.
        self.route_entry_list = route_entry_list
        # The route table ID of the VPC.
        self.route_table_id = route_table_id

    def validate(self):
        if self.route_entry_list:
            for v1 in self.route_entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteEntryList'] = []
        if self.route_entry_list is not None:
            for k1 in self.route_entry_list:
                result['RouteEntryList'].append(k1.to_map() if k1 else None)

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry_list = []
        if m.get('RouteEntryList') is not None:
            for k1 in m.get('RouteEntryList'):
                temp_model = main_models.DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeVpcFirewallCenListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the VPC.
        self.next_hop_instance_id = next_hop_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop_instance_id is not None:
            result['NextHopInstanceId'] = self.next_hop_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHopInstanceId') is not None:
            self.next_hop_instance_id = m.get('NextHopInstanceId')

        return self

class DescribeVpcFirewallCenListResponseBodyVpcFirewallsIpsConfig(DaraModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic protection is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose.
        # *   **2**: medium.
        # *   **3**: strict.
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules

        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')

        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        return self

class DescribeVpcFirewallCenListResponseBodyVpcFirewallsAclConfig(DaraModel):
    def __init__(
        self,
        strict_mode: int = None,
    ):
        # Specifies whether to enable the strict mode. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.strict_mode = strict_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        return self

