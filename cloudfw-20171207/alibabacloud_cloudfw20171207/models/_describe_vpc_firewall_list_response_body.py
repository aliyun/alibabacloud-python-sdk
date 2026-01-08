# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        vpc_firewalls: List[main_models.DescribeVpcFirewallListResponseBodyVpcFirewalls] = None,
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
                temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewalls()
                self.vpc_firewalls.append(temp_model.from_map(k1))

        return self

class DescribeVpcFirewallListResponseBodyVpcFirewalls(DaraModel):
    def __init__(
        self,
        acl_config: main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsAclConfig = None,
        bandwidth: int = None,
        connect_sub_type: str = None,
        connect_type: str = None,
        firewall_switch_status: str = None,
        ips_config: main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig = None,
        local_vpc: main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc = None,
        member_uid: str = None,
        peer_vpc: main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc = None,
        region_status: str = None,
        result_code: str = None,
        vpc_firewall_id: str = None,
        vpc_firewall_name: str = None,
    ):
        # ACL engine mode.
        self.acl_config = acl_config
        # The bandwidth of the Express Connect circuit. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The sub-type of the connection. Valid values:
        # 
        # *   **vpc2vpc**: Express Connect connection
        # *   **vpcpeer**: peer connection
        self.connect_sub_type = connect_sub_type
        # The connection type of the VPC firewall. The value is fixed as **expressconnect**, which indicates an Express Connect connection.
        self.connect_type = connect_type
        # The status of the VPC firewall. Valid values:
        # 
        # *   **opened**: The VPC firewall is enabled.
        # *   **closed**: The VPC firewall is disabled.
        # *   **notconfigured**: The VPC firewall is not configured.
        self.firewall_switch_status = firewall_switch_status
        # The intrusion prevention system (IPS) configurations.
        self.ips_config = ips_config
        # The details about the local VPC.
        self.local_vpc = local_vpc
        # The UID of the member that is managed by your Alibaba Cloud account.
        self.member_uid = member_uid
        # The details about the peer VPC.
        self.peer_vpc = peer_vpc
        # Indicates whether you can create a VPC firewall in a specified region. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.region_status = region_status
        # The result code of the operation that creates the VPC firewall. Valid values:
        # 
        # *   **Unauthorized**: Cloud Firewall is not authorized to access a VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **RegionDisable**: VPC Firewall is not supported in the region of a VPC for which the VPC firewall is created, and the VPC firewall cannot be created.
        # *   **Empty string**: You can create a VPC firewall for the network instance.
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
        if self.peer_vpc:
            self.peer_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_config is not None:
            result['AclConfig'] = self.acl_config.to_map()

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.connect_sub_type is not None:
            result['ConnectSubType'] = self.connect_sub_type

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

        if self.peer_vpc is not None:
            result['PeerVpc'] = self.peer_vpc.to_map()

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
            temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsAclConfig()
            self.acl_config = temp_model.from_map(m.get('AclConfig'))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ConnectSubType') is not None:
            self.connect_sub_type = m.get('ConnectSubType')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('FirewallSwitchStatus') is not None:
            self.firewall_switch_status = m.get('FirewallSwitchStatus')

        if m.get('IpsConfig') is not None:
            temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig()
            self.ips_config = temp_model.from_map(m.get('IpsConfig'))

        if m.get('LocalVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc()
            self.local_vpc = temp_model.from_map(m.get('LocalVpc'))

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PeerVpc') is not None:
            temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc()
            self.peer_vpc = temp_model.from_map(m.get('PeerVpc'))

        if m.get('RegionStatus') is not None:
            self.region_status = m.get('RegionStatus')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VpcFirewallName') is not None:
            self.vpc_firewall_name = m.get('VpcFirewallName')

        return self

class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpc(DaraModel):
    def __init__(
        self,
        authorization_status: str = None,
        owner_id: int = None,
        region_no: str = None,
        vpc_cidr_table_list: List[main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether Cloud Firewall is authorized to access the peer VPC. The value is fixed as **authorized**, which indicates that Cloud Firewall is authorized to access the peer VPC.
        self.authorization_status = authorization_status
        # The UID of the Alibaba Cloud account to which the peer VPC belongs.
        self.owner_id = owner_id
        # The region ID of the peer VPC.
        self.region_no = region_no
        # An array that consists of the CIDR blocks of the peer VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the peer VPC.
        self.vpc_id = vpc_id
        # The name of the peer VPC.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k1 in m.get('VpcCidrTableList'):
                temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableList(DaraModel):
    def __init__(
        self,
        route_entry_list: List[main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # An array that consists of the route entries of the peer VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the peer VPC.
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
                temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeVpcFirewallListResponseBodyVpcFirewallsPeerVpcVpcCidrTableListRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the peer VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the peer VPC.
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

class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpc(DaraModel):
    def __init__(
        self,
        authorization_status: str = None,
        owner_id: int = None,
        region_no: str = None,
        vpc_cidr_table_list: List[main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList] = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # Indicates whether Cloud Firewall is authorized to access the local VPC. The value is fixed as authorized, which indicates that Cloud Firewall is authorized to access the local VPC.
        self.authorization_status = authorization_status
        # The UID of the Alibaba Cloud account to which the local VPC belongs.
        self.owner_id = owner_id
        # The region ID of the local VPC.
        self.region_no = region_no
        # An array that consists of the CIDR blocks of the local VPC.
        self.vpc_cidr_table_list = vpc_cidr_table_list
        # The ID of the local VPC.
        self.vpc_id = vpc_id
        # The name of the local VPC.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        self.vpc_cidr_table_list = []
        if m.get('VpcCidrTableList') is not None:
            for k1 in m.get('VpcCidrTableList'):
                temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList()
                self.vpc_cidr_table_list.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableList(DaraModel):
    def __init__(
        self,
        route_entry_list: List[main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList] = None,
        route_table_id: str = None,
    ):
        # An array that consists of the route entries of the local VPC.
        self.route_entry_list = route_entry_list
        # The ID of the route table for the local VPC.
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
                temp_model = main_models.DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList()
                self.route_entry_list.append(temp_model.from_map(k1))

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeVpcFirewallListResponseBodyVpcFirewallsLocalVpcVpcCidrTableListRouteEntryList(DaraModel):
    def __init__(
        self,
        destination_cidr: str = None,
        next_hop_instance_id: str = None,
    ):
        # The destination CIDR block of the local VPC.
        self.destination_cidr = destination_cidr
        # The instance ID of the next hop for the local VPC.
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

class DescribeVpcFirewallListResponseBodyVpcFirewallsIpsConfig(DaraModel):
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
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
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

class DescribeVpcFirewallListResponseBodyVpcFirewallsAclConfig(DaraModel):
    def __init__(
        self,
        strict_mode: int = None,
    ):
        # Specifies whether to enable the strict mode. Valid values:
        # 
        # *   1: yes
        # *   0: no
        # 
        # This parameter is required.
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

