# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceClusterInfoResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        instance_cluster_attribute: main_models.DescribeInstanceClusterInfoResponseBodyInstanceClusterAttribute = None,
        instance_cluster_id: str = None,
        instance_cluster_name: str = None,
        instance_cluster_status: str = None,
        instance_cluster_type: str = None,
        instance_cluster_version: str = None,
        instance_list: main_models.DescribeInstanceClusterInfoResponseBodyInstanceList = None,
        modified_time: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The time when the cluster was created.
        self.created_time = created_time
        # The cluster description, which can be up to 200 characters in length.
        self.description = description
        # The cluster details.
        self.instance_cluster_attribute = instance_cluster_attribute
        # The cluster ID.
        self.instance_cluster_id = instance_cluster_id
        # The cluster name.
        self.instance_cluster_name = instance_cluster_name
        # The cluster status.
        self.instance_cluster_status = instance_cluster_status
        # The cluster type.
        self.instance_cluster_type = instance_cluster_type
        # The cluster version.
        self.instance_cluster_version = instance_cluster_version
        # The dedicated instances contained in the cluster.
        self.instance_list = instance_list
        # The time when the cluster was last modified.
        self.modified_time = modified_time
        # The region ID of the cluster.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_cluster_attribute:
            self.instance_cluster_attribute.validate()
        if self.instance_list:
            self.instance_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_cluster_attribute is not None:
            result['InstanceClusterAttribute'] = self.instance_cluster_attribute.to_map()

        if self.instance_cluster_id is not None:
            result['InstanceClusterId'] = self.instance_cluster_id

        if self.instance_cluster_name is not None:
            result['InstanceClusterName'] = self.instance_cluster_name

        if self.instance_cluster_status is not None:
            result['InstanceClusterStatus'] = self.instance_cluster_status

        if self.instance_cluster_type is not None:
            result['InstanceClusterType'] = self.instance_cluster_type

        if self.instance_cluster_version is not None:
            result['InstanceClusterVersion'] = self.instance_cluster_version

        if self.instance_list is not None:
            result['InstanceList'] = self.instance_list.to_map()

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceClusterAttribute') is not None:
            temp_model = main_models.DescribeInstanceClusterInfoResponseBodyInstanceClusterAttribute()
            self.instance_cluster_attribute = temp_model.from_map(m.get('InstanceClusterAttribute'))

        if m.get('InstanceClusterId') is not None:
            self.instance_cluster_id = m.get('InstanceClusterId')

        if m.get('InstanceClusterName') is not None:
            self.instance_cluster_name = m.get('InstanceClusterName')

        if m.get('InstanceClusterStatus') is not None:
            self.instance_cluster_status = m.get('InstanceClusterStatus')

        if m.get('InstanceClusterType') is not None:
            self.instance_cluster_type = m.get('InstanceClusterType')

        if m.get('InstanceClusterVersion') is not None:
            self.instance_cluster_version = m.get('InstanceClusterVersion')

        if m.get('InstanceList') is not None:
            temp_model = main_models.DescribeInstanceClusterInfoResponseBodyInstanceList()
            self.instance_list = temp_model.from_map(m.get('InstanceList'))

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceClusterInfoResponseBodyInstanceList(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeInstanceClusterInfoResponseBodyInstanceListInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeInstanceClusterInfoResponseBodyInstanceListInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeInstanceClusterInfoResponseBodyInstanceListInstance(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        instance_id: str = None,
        instance_name: str = None,
        status: str = None,
    ):
        # The error message returned if the call fails.
        self.error_message = error_message
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeInstanceClusterInfoResponseBodyInstanceClusterAttribute(DaraModel):
    def __init__(
        self,
        connect_cidr_blocks: str = None,
        connect_vpc_id: str = None,
        egress_ipv_6enable: bool = None,
        https_policies: str = None,
        ipv4acl_id: str = None,
        ipv4acl_name: str = None,
        ipv4acl_status: str = None,
        ipv4acl_type: str = None,
        ipv6acl_id: str = None,
        ipv6acl_name: str = None,
        ipv6acl_status: str = None,
        ipv6acl_type: str = None,
        internet_egress_address: str = None,
        intranet_egress_address: str = None,
        intranet_segments: str = None,
        support_ipv_6: bool = None,
        user_vpc_id: str = None,
        user_vswitch_id: str = None,
        vip_type_list: str = None,
        vpc_intranet_enable: bool = None,
        vpc_owner_id: int = None,
        vpc_slb_intranet_enable: bool = None,
    ):
        # The internal CIDR block of the user VPC that can be accessed by the cluster if the cluster consists of VPC integration instances.
        self.connect_cidr_blocks = connect_cidr_blocks
        # The ID of the user VPC that is connected to the cluster if the cluster consists of VPC integration instances.
        self.connect_vpc_id = connect_vpc_id
        # Indicates whether outbound IPv6 traffic is supported.
        self.egress_ipv_6enable = egress_ipv_6enable
        # The HTTPS security policy.
        self.https_policies = https_policies
        # The ID of the IPv4 access control list (ACL).
        self.ipv4acl_id = ipv4acl_id
        # The name of the IPv4 ACL.
        self.ipv4acl_name = ipv4acl_name
        # Indicates whether IPv4 access control is enabled. Valid values:
        # 
        # *   on
        # *   off
        self.ipv4acl_status = ipv4acl_status
        # The type of the IPv4 ACL.
        # 
        # *   black: blacklist
        # *   white: whitelist
        self.ipv4acl_type = ipv4acl_type
        # The ID of the IPv6 ACL.
        self.ipv6acl_id = ipv6acl_id
        # The name of the IPv6 ACL.
        self.ipv6acl_name = ipv6acl_name
        # Indicates whether IPv6 access control is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.ipv6acl_status = ipv6acl_status
        # The type of the IPv6 ACL. Valid values:
        # 
        # *   black: blacklist
        # *   white: whitelist
        self.ipv6acl_type = ipv6acl_type
        # The outbound public IP address.
        self.internet_egress_address = internet_egress_address
        # The outbound private IP address.
        self.intranet_egress_address = intranet_egress_address
        # The custom CIDR block. The configured CIDR block is considered as a private block.
        self.intranet_segments = intranet_segments
        # Indicates whether IPv6 traffic is supported.
        self.support_ipv_6 = support_ipv_6
        # The ID of the client VPC.
        self.user_vpc_id = user_vpc_id
        # The vSwitch of the client VPC.
        self.user_vswitch_id = user_vswitch_id
        # The VIPs of the cluster.
        self.vip_type_list = vip_type_list
        # Indicates whether a virtual private cloud (VPC) domain name is enabled.
        self.vpc_intranet_enable = vpc_intranet_enable
        # The ID of the account to which the VPC belongs.
        self.vpc_owner_id = vpc_owner_id
        # Indicates whether self-calling is enabled.
        self.vpc_slb_intranet_enable = vpc_slb_intranet_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_cidr_blocks is not None:
            result['ConnectCidrBlocks'] = self.connect_cidr_blocks

        if self.connect_vpc_id is not None:
            result['ConnectVpcId'] = self.connect_vpc_id

        if self.egress_ipv_6enable is not None:
            result['EgressIpv6Enable'] = self.egress_ipv_6enable

        if self.https_policies is not None:
            result['HttpsPolicies'] = self.https_policies

        if self.ipv4acl_id is not None:
            result['IPV4AclId'] = self.ipv4acl_id

        if self.ipv4acl_name is not None:
            result['IPV4AclName'] = self.ipv4acl_name

        if self.ipv4acl_status is not None:
            result['IPV4AclStatus'] = self.ipv4acl_status

        if self.ipv4acl_type is not None:
            result['IPV4AclType'] = self.ipv4acl_type

        if self.ipv6acl_id is not None:
            result['IPV6AclId'] = self.ipv6acl_id

        if self.ipv6acl_name is not None:
            result['IPV6AclName'] = self.ipv6acl_name

        if self.ipv6acl_status is not None:
            result['IPV6AclStatus'] = self.ipv6acl_status

        if self.ipv6acl_type is not None:
            result['IPV6AclType'] = self.ipv6acl_type

        if self.internet_egress_address is not None:
            result['InternetEgressAddress'] = self.internet_egress_address

        if self.intranet_egress_address is not None:
            result['IntranetEgressAddress'] = self.intranet_egress_address

        if self.intranet_segments is not None:
            result['IntranetSegments'] = self.intranet_segments

        if self.support_ipv_6 is not None:
            result['SupportIpv6'] = self.support_ipv_6

        if self.user_vpc_id is not None:
            result['UserVpcId'] = self.user_vpc_id

        if self.user_vswitch_id is not None:
            result['UserVswitchId'] = self.user_vswitch_id

        if self.vip_type_list is not None:
            result['VipTypeList'] = self.vip_type_list

        if self.vpc_intranet_enable is not None:
            result['VpcIntranetEnable'] = self.vpc_intranet_enable

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        if self.vpc_slb_intranet_enable is not None:
            result['VpcSlbIntranetEnable'] = self.vpc_slb_intranet_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectCidrBlocks') is not None:
            self.connect_cidr_blocks = m.get('ConnectCidrBlocks')

        if m.get('ConnectVpcId') is not None:
            self.connect_vpc_id = m.get('ConnectVpcId')

        if m.get('EgressIpv6Enable') is not None:
            self.egress_ipv_6enable = m.get('EgressIpv6Enable')

        if m.get('HttpsPolicies') is not None:
            self.https_policies = m.get('HttpsPolicies')

        if m.get('IPV4AclId') is not None:
            self.ipv4acl_id = m.get('IPV4AclId')

        if m.get('IPV4AclName') is not None:
            self.ipv4acl_name = m.get('IPV4AclName')

        if m.get('IPV4AclStatus') is not None:
            self.ipv4acl_status = m.get('IPV4AclStatus')

        if m.get('IPV4AclType') is not None:
            self.ipv4acl_type = m.get('IPV4AclType')

        if m.get('IPV6AclId') is not None:
            self.ipv6acl_id = m.get('IPV6AclId')

        if m.get('IPV6AclName') is not None:
            self.ipv6acl_name = m.get('IPV6AclName')

        if m.get('IPV6AclStatus') is not None:
            self.ipv6acl_status = m.get('IPV6AclStatus')

        if m.get('IPV6AclType') is not None:
            self.ipv6acl_type = m.get('IPV6AclType')

        if m.get('InternetEgressAddress') is not None:
            self.internet_egress_address = m.get('InternetEgressAddress')

        if m.get('IntranetEgressAddress') is not None:
            self.intranet_egress_address = m.get('IntranetEgressAddress')

        if m.get('IntranetSegments') is not None:
            self.intranet_segments = m.get('IntranetSegments')

        if m.get('SupportIpv6') is not None:
            self.support_ipv_6 = m.get('SupportIpv6')

        if m.get('UserVpcId') is not None:
            self.user_vpc_id = m.get('UserVpcId')

        if m.get('UserVswitchId') is not None:
            self.user_vswitch_id = m.get('UserVswitchId')

        if m.get('VipTypeList') is not None:
            self.vip_type_list = m.get('VipTypeList')

        if m.get('VpcIntranetEnable') is not None:
            self.vpc_intranet_enable = m.get('VpcIntranetEnable')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        if m.get('VpcSlbIntranetEnable') is not None:
            self.vpc_slb_intranet_enable = m.get('VpcSlbIntranetEnable')

        return self

