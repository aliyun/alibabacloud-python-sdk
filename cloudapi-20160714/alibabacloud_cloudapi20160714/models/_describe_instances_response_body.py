# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the instances.
        self.instances = instances
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance_attribute: List[main_models.DescribeInstancesResponseBodyInstancesInstanceAttribute] = None,
    ):
        self.instance_attribute = instance_attribute

    def validate(self):
        if self.instance_attribute:
            for v1 in self.instance_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceAttribute'] = []
        if self.instance_attribute is not None:
            for k1 in self.instance_attribute:
                result['InstanceAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_attribute = []
        if m.get('InstanceAttribute') is not None:
            for k1 in m.get('InstanceAttribute'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttribute()
                self.instance_attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttribute(DaraModel):
    def __init__(
        self,
        acl_id: str = None,
        acl_name: str = None,
        acl_status: str = None,
        acl_type: str = None,
        classic_egress_address: str = None,
        connect_cidr_blocks: str = None,
        connect_vpc_id: str = None,
        created_time: str = None,
        dedicated_instance_type: str = None,
        egress_ipv_6enable: bool = None,
        expired_time: str = None,
        https_policies: str = None,
        ipv6acl_id: str = None,
        ipv6acl_name: str = None,
        ipv6acl_status: str = None,
        ipv6acl_type: str = None,
        instance_charge_type: str = None,
        instance_cidr_block: str = None,
        instance_cluster_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_rps_limit: int = None,
        instance_spec: str = None,
        instance_spec_attributes: main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeInstanceSpecAttributes = None,
        instance_type: str = None,
        internet_egress_address: str = None,
        intranet_segments: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        network_interface_attributes: main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeNetworkInterfaceAttributes = None,
        new_vpc_egress_address: str = None,
        private_dns_list: main_models.DescribeInstancesResponseBodyInstancesInstanceAttributePrivateDnsList = None,
        region_id: str = None,
        status: str = None,
        support_ipv_6: bool = None,
        tags: main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeTags = None,
        user_vpc_id: str = None,
        user_vswitch_id: str = None,
        vpc_egress_address: str = None,
        vpc_intranet_enable: bool = None,
        vpc_owner_id: int = None,
        vpc_slb_intranet_enable: bool = None,
        zone_id: str = None,
        zone_local_name: str = None,
    ):
        # The ACL ID.
        self.acl_id = acl_id
        # The name of the access control list (ACL).
        self.acl_name = acl_name
        # Indicates whether the ACL is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.acl_status = acl_status
        # The ACL type. Valid values:
        # 
        # *   black: blacklist
        # *   white: whitelist
        self.acl_type = acl_type
        # The egress IP address.
        self.classic_egress_address = classic_egress_address
        # The internal CIDR block of the user\\"s VPC that can be accessed if the instance is a VPC integration instance.
        self.connect_cidr_blocks = connect_cidr_blocks
        # The ID of the user\\"s VPC if the instance is a VPC integration instance.
        self.connect_vpc_id = connect_vpc_id
        # The time when the instance was created.
        self.created_time = created_time
        # The type of the dedicated instance. Valid values:
        # 
        # *   vpc_connect: VPC integration instance
        # *   normal: conventional dedicated instance
        self.dedicated_instance_type = dedicated_instance_type
        # Indicates whether outbound IPv6 traffic is supported.
        self.egress_ipv_6enable = egress_ipv_6enable
        # The time when the instance expires.
        self.expired_time = expired_time
        # The HTTPS security policy.
        self.https_policies = https_policies
        # The ID of the IPv6 ACL.
        self.ipv6acl_id = ipv6acl_id
        # The name of the IPv6 ACL.
        self.ipv6acl_name = ipv6acl_name
        # Indicates whether the IPv6 ACL is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.ipv6acl_status = ipv6acl_status
        # The type of the IPv6 ACL. Valid values:
        # 
        # *   black: blacklist
        # *   white: whitelist
        self.ipv6acl_type = ipv6acl_type
        # The billing method of the instance. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PayAsYouGo: pay-as-you-go
        self.instance_charge_type = instance_charge_type
        # The CIDR block of the dedicated instance.
        # 
        # *   172.16.0.0/12
        # *   192.168.0.0/16
        self.instance_cidr_block = instance_cidr_block
        # The ID of the cluster to which the dedicated instance cluster belongs.
        self.instance_cluster_id = instance_cluster_id
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The requests per second (RPS) limit on the instance.
        self.instance_rps_limit = instance_rps_limit
        # The instance specification.
        self.instance_spec = instance_spec
        # The instance specification details.
        self.instance_spec_attributes = instance_spec_attributes
        # The instance type. Valid values:
        # 
        # *   VPC_SHARED: shared instance (VPC)
        # *   VPC_DEDICATED: dedicated instance (VPC)
        self.instance_type = instance_type
        # The outbound public IP address.
        self.internet_egress_address = internet_egress_address
        # The internal CIDR block that is allowed to access the API Gateway instance.
        self.intranet_segments = intranet_segments
        # The end time of the maintenance window. The time is in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_end_time = maintain_end_time
        # The start time of the maintenance window. The time is in the *HH:mm*Z format. The time is displayed in UTC.
        self.maintain_start_time = maintain_start_time
        # The network information of the user\\"s VPC if the instance is a VPC integration instance.
        self.network_interface_attributes = network_interface_attributes
        # The new VPC egress CIDR block.
        self.new_vpc_egress_address = new_vpc_egress_address
        # The private DNS list.
        self.private_dns_list = private_dns_list
        # The region ID.
        self.region_id = region_id
        # The instance status.
        self.status = status
        # Indicates whether IPv6 traffic is supported.
        self.support_ipv_6 = support_ipv_6
        # The tags of the instance.
        self.tags = tags
        # The user VPC ID.
        self.user_vpc_id = user_vpc_id
        # The user vSwitch ID.
        self.user_vswitch_id = user_vswitch_id
        # The VPC egress CIDR block.
        self.vpc_egress_address = vpc_egress_address
        # Indicates whether VPC access is enabled.
        self.vpc_intranet_enable = vpc_intranet_enable
        # The ID of the account to which the VPC-based instance belongs.
        self.vpc_owner_id = vpc_owner_id
        # Indicates whether virtual private cloud (VPC) Server Load Balancer (SLB) is enabled.
        self.vpc_slb_intranet_enable = vpc_slb_intranet_enable
        # The zone ID.
        self.zone_id = zone_id
        # The zone.
        self.zone_local_name = zone_local_name

    def validate(self):
        if self.instance_spec_attributes:
            self.instance_spec_attributes.validate()
        if self.network_interface_attributes:
            self.network_interface_attributes.validate()
        if self.private_dns_list:
            self.private_dns_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.classic_egress_address is not None:
            result['ClassicEgressAddress'] = self.classic_egress_address

        if self.connect_cidr_blocks is not None:
            result['ConnectCidrBlocks'] = self.connect_cidr_blocks

        if self.connect_vpc_id is not None:
            result['ConnectVpcId'] = self.connect_vpc_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.dedicated_instance_type is not None:
            result['DedicatedInstanceType'] = self.dedicated_instance_type

        if self.egress_ipv_6enable is not None:
            result['EgressIpv6Enable'] = self.egress_ipv_6enable

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.https_policies is not None:
            result['HttpsPolicies'] = self.https_policies

        if self.ipv6acl_id is not None:
            result['IPV6AclId'] = self.ipv6acl_id

        if self.ipv6acl_name is not None:
            result['IPV6AclName'] = self.ipv6acl_name

        if self.ipv6acl_status is not None:
            result['IPV6AclStatus'] = self.ipv6acl_status

        if self.ipv6acl_type is not None:
            result['IPV6AclType'] = self.ipv6acl_type

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_cidr_block is not None:
            result['InstanceCidrBlock'] = self.instance_cidr_block

        if self.instance_cluster_id is not None:
            result['InstanceClusterId'] = self.instance_cluster_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_rps_limit is not None:
            result['InstanceRpsLimit'] = self.instance_rps_limit

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.instance_spec_attributes is not None:
            result['InstanceSpecAttributes'] = self.instance_spec_attributes.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_egress_address is not None:
            result['InternetEgressAddress'] = self.internet_egress_address

        if self.intranet_segments is not None:
            result['IntranetSegments'] = self.intranet_segments

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.network_interface_attributes is not None:
            result['NetworkInterfaceAttributes'] = self.network_interface_attributes.to_map()

        if self.new_vpc_egress_address is not None:
            result['NewVpcEgressAddress'] = self.new_vpc_egress_address

        if self.private_dns_list is not None:
            result['PrivateDnsList'] = self.private_dns_list.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.support_ipv_6 is not None:
            result['SupportIpv6'] = self.support_ipv_6

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.user_vpc_id is not None:
            result['UserVpcId'] = self.user_vpc_id

        if self.user_vswitch_id is not None:
            result['UserVswitchId'] = self.user_vswitch_id

        if self.vpc_egress_address is not None:
            result['VpcEgressAddress'] = self.vpc_egress_address

        if self.vpc_intranet_enable is not None:
            result['VpcIntranetEnable'] = self.vpc_intranet_enable

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        if self.vpc_slb_intranet_enable is not None:
            result['VpcSlbIntranetEnable'] = self.vpc_slb_intranet_enable

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        if self.zone_local_name is not None:
            result['ZoneLocalName'] = self.zone_local_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('ClassicEgressAddress') is not None:
            self.classic_egress_address = m.get('ClassicEgressAddress')

        if m.get('ConnectCidrBlocks') is not None:
            self.connect_cidr_blocks = m.get('ConnectCidrBlocks')

        if m.get('ConnectVpcId') is not None:
            self.connect_vpc_id = m.get('ConnectVpcId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DedicatedInstanceType') is not None:
            self.dedicated_instance_type = m.get('DedicatedInstanceType')

        if m.get('EgressIpv6Enable') is not None:
            self.egress_ipv_6enable = m.get('EgressIpv6Enable')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('HttpsPolicies') is not None:
            self.https_policies = m.get('HttpsPolicies')

        if m.get('IPV6AclId') is not None:
            self.ipv6acl_id = m.get('IPV6AclId')

        if m.get('IPV6AclName') is not None:
            self.ipv6acl_name = m.get('IPV6AclName')

        if m.get('IPV6AclStatus') is not None:
            self.ipv6acl_status = m.get('IPV6AclStatus')

        if m.get('IPV6AclType') is not None:
            self.ipv6acl_type = m.get('IPV6AclType')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceCidrBlock') is not None:
            self.instance_cidr_block = m.get('InstanceCidrBlock')

        if m.get('InstanceClusterId') is not None:
            self.instance_cluster_id = m.get('InstanceClusterId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceRpsLimit') is not None:
            self.instance_rps_limit = m.get('InstanceRpsLimit')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('InstanceSpecAttributes') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeInstanceSpecAttributes()
            self.instance_spec_attributes = temp_model.from_map(m.get('InstanceSpecAttributes'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetEgressAddress') is not None:
            self.internet_egress_address = m.get('InternetEgressAddress')

        if m.get('IntranetSegments') is not None:
            self.intranet_segments = m.get('IntranetSegments')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('NetworkInterfaceAttributes') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeNetworkInterfaceAttributes()
            self.network_interface_attributes = temp_model.from_map(m.get('NetworkInterfaceAttributes'))

        if m.get('NewVpcEgressAddress') is not None:
            self.new_vpc_egress_address = m.get('NewVpcEgressAddress')

        if m.get('PrivateDnsList') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributePrivateDnsList()
            self.private_dns_list = temp_model.from_map(m.get('PrivateDnsList'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportIpv6') is not None:
            self.support_ipv_6 = m.get('SupportIpv6')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UserVpcId') is not None:
            self.user_vpc_id = m.get('UserVpcId')

        if m.get('UserVswitchId') is not None:
            self.user_vswitch_id = m.get('UserVswitchId')

        if m.get('VpcEgressAddress') is not None:
            self.vpc_egress_address = m.get('VpcEgressAddress')

        if m.get('VpcIntranetEnable') is not None:
            self.vpc_intranet_enable = m.get('VpcIntranetEnable')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        if m.get('VpcSlbIntranetEnable') is not None:
            self.vpc_slb_intranet_enable = m.get('VpcSlbIntranetEnable')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneLocalName') is not None:
            self.zone_local_name = m.get('ZoneLocalName')

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributeTags(DaraModel):
    def __init__(
        self,
        tag_info: List[main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeTagsTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for v1 in self.tag_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k1 in self.tag_info:
                result['TagInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k1 in m.get('TagInfo'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeTagsTagInfo()
                self.tag_info.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributeTagsTagInfo(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance.
        self.key = key
        # The tag value of the instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributePrivateDnsList(DaraModel):
    def __init__(
        self,
        private_dns: List[str] = None,
    ):
        self.private_dns = private_dns

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_dns is not None:
            result['PrivateDns'] = self.private_dns

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateDns') is not None:
            self.private_dns = m.get('PrivateDns')

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributeNetworkInterfaceAttributes(DaraModel):
    def __init__(
        self,
        network_interface_attribute: List[main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeNetworkInterfaceAttributesNetworkInterfaceAttribute] = None,
    ):
        self.network_interface_attribute = network_interface_attribute

    def validate(self):
        if self.network_interface_attribute:
            for v1 in self.network_interface_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInterfaceAttribute'] = []
        if self.network_interface_attribute is not None:
            for k1 in self.network_interface_attribute:
                result['NetworkInterfaceAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_interface_attribute = []
        if m.get('NetworkInterfaceAttribute') is not None:
            for k1 in m.get('NetworkInterfaceAttribute'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeNetworkInterfaceAttributesNetworkInterfaceAttribute()
                self.network_interface_attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributeNetworkInterfaceAttributesNetworkInterfaceAttribute(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        security_group_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The CIDR block of the vSwitch.
        self.cidr_block = cidr_block
        # The security group ID. Services in the same security group can access each other.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.vswitch_id = vswitch_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributeInstanceSpecAttributes(DaraModel):
    def __init__(
        self,
        spec_attribute: List[main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeInstanceSpecAttributesSpecAttribute] = None,
    ):
        self.spec_attribute = spec_attribute

    def validate(self):
        if self.spec_attribute:
            for v1 in self.spec_attribute:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SpecAttribute'] = []
        if self.spec_attribute is not None:
            for k1 in self.spec_attribute:
                result['SpecAttribute'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spec_attribute = []
        if m.get('SpecAttribute') is not None:
            for k1 in m.get('SpecAttribute'):
                temp_model = main_models.DescribeInstancesResponseBodyInstancesInstanceAttributeInstanceSpecAttributesSpecAttribute()
                self.spec_attribute.append(temp_model.from_map(k1))

        return self

class DescribeInstancesResponseBodyInstancesInstanceAttributeInstanceSpecAttributesSpecAttribute(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        value: str = None,
    ):
        # The variable name.
        self.local_name = local_name
        # The variable value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

