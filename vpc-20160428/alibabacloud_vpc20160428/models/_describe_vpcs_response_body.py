# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpcs: main_models.DescribeVpcsResponseBodyVpcs = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The details of the VPC.
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Vpcs') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m.get('Vpcs'))

        return self

class DescribeVpcsResponseBodyVpcs(DaraModel):
    def __init__(
        self,
        vpc: List[main_models.DescribeVpcsResponseBodyVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for v1 in self.vpc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Vpc'] = []
        if self.vpc is not None:
            for k1 in self.vpc:
                result['Vpc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k1 in m.get('Vpc'):
                temp_model = main_models.DescribeVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k1))

        return self

class DescribeVpcsResponseBodyVpcsVpc(DaraModel):
    def __init__(
        self,
        cen_status: str = None,
        cidr_block: str = None,
        creation_time: str = None,
        description: str = None,
        dhcp_options_set_id: str = None,
        dhcp_options_set_status: str = None,
        dns_hostname_status: str = None,
        enabled_ipv_6: bool = None,
        ipv_6cidr_block: str = None,
        ipv_6cidr_blocks: main_models.DescribeVpcsResponseBodyVpcsVpcIpv6CidrBlocks = None,
        is_default: bool = None,
        nat_gateway_ids: main_models.DescribeVpcsResponseBodyVpcsVpcNatGatewayIds = None,
        owner_id: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        router_table_ids: main_models.DescribeVpcsResponseBodyVpcsVpcRouterTableIds = None,
        secondary_cidr_blocks: main_models.DescribeVpcsResponseBodyVpcsVpcSecondaryCidrBlocks = None,
        status: str = None,
        tags: main_models.DescribeVpcsResponseBodyVpcsVpcTags = None,
        user_cidrs: main_models.DescribeVpcsResponseBodyVpcsVpcUserCidrs = None,
        vrouter_id: str = None,
        v_switch_ids: main_models.DescribeVpcsResponseBodyVpcsVpcVSwitchIds = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The status of the Cloud Enterprise Network (CEN) instance to which the VPC is attached. **Attached** is returned only if the VPC is attached to a CEN instance.
        self.cen_status = cen_status
        # The IPv4 CIDR block of the VPC.
        self.cidr_block = cidr_block
        # The time when the VPC was created.
        self.creation_time = creation_time
        # The description of the VPC.
        self.description = description
        # The ID of the DHCP options set.
        self.dhcp_options_set_id = dhcp_options_set_id
        # The status of the DHCP options set. Valid values:
        # 
        # *   **Available**
        # *   **InUse**
        # *   **Deleted**
        # *   **Pending**
        self.dhcp_options_set_status = dhcp_options_set_status
        # Indicates whether the Domain Name System (DNS) feature is enabled.
        self.dns_hostname_status = dns_hostname_status
        # Indicates whether the IPv6 is enabled.
        # 
        # Valid values:
        # 
        # - false: false
        # 
        # - true: true
        self.enabled_ipv_6 = enabled_ipv_6
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_blocks = ipv_6cidr_blocks
        # Indicates whether the VPC is the default VPC in the region. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_default = is_default
        # The ID of the Internet NAT gateway.
        self.nat_gateway_ids = nat_gateway_ids
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The ID of the region to which the VPC belongs.
        self.region_id = region_id
        # The ID of the resource group to which the VPC belongs.
        self.resource_group_id = resource_group_id
        # The information about the route table.
        self.router_table_ids = router_table_ids
        # The information about the secondary CIDR block.
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # The status of the VPC. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        self.status = status
        # The tag information about the VPC.
        self.tags = tags
        # The list of user CIDR blocks.
        self.user_cidrs = user_cidrs
        # The ID of the vRouter.
        self.vrouter_id = vrouter_id
        # The vSwitches in the VPC.
        # 
        # You can query up to 300 vSwitches in the VPC. The information about the latest vSwitches is returned. If you want to query the information about all vSwitches in a VPC, call the [DescribeVSwitches](https://help.aliyun.com/document_detail/35748.html) operation.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.ipv_6cidr_blocks:
            self.ipv_6cidr_blocks.validate()
        if self.nat_gateway_ids:
            self.nat_gateway_ids.validate()
        if self.router_table_ids:
            self.router_table_ids.validate()
        if self.secondary_cidr_blocks:
            self.secondary_cidr_blocks.validate()
        if self.tags:
            self.tags.validate()
        if self.user_cidrs:
            self.user_cidrs.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_status is not None:
            result['CenStatus'] = self.cen_status

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dhcp_options_set_id is not None:
            result['DhcpOptionsSetId'] = self.dhcp_options_set_id

        if self.dhcp_options_set_status is not None:
            result['DhcpOptionsSetStatus'] = self.dhcp_options_set_status

        if self.dns_hostname_status is not None:
            result['DnsHostnameStatus'] = self.dns_hostname_status

        if self.enabled_ipv_6 is not None:
            result['EnabledIpv6'] = self.enabled_ipv_6

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6cidr_blocks is not None:
            result['Ipv6CidrBlocks'] = self.ipv_6cidr_blocks.to_map()

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.nat_gateway_ids is not None:
            result['NatGatewayIds'] = self.nat_gateway_ids.to_map()

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.router_table_ids is not None:
            result['RouterTableIds'] = self.router_table_ids.to_map()

        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()

        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenStatus') is not None:
            self.cen_status = m.get('CenStatus')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DhcpOptionsSetId') is not None:
            self.dhcp_options_set_id = m.get('DhcpOptionsSetId')

        if m.get('DhcpOptionsSetStatus') is not None:
            self.dhcp_options_set_status = m.get('DhcpOptionsSetStatus')

        if m.get('DnsHostnameStatus') is not None:
            self.dns_hostname_status = m.get('DnsHostnameStatus')

        if m.get('EnabledIpv6') is not None:
            self.enabled_ipv_6 = m.get('EnabledIpv6')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6CidrBlocks') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcIpv6CidrBlocks()
            self.ipv_6cidr_blocks = temp_model.from_map(m.get('Ipv6CidrBlocks'))

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('NatGatewayIds') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcNatGatewayIds()
            self.nat_gateway_ids = temp_model.from_map(m.get('NatGatewayIds'))

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouterTableIds') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcRouterTableIds()
            self.router_table_ids = temp_model.from_map(m.get('RouterTableIds'))

        if m.get('SecondaryCidrBlocks') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcSecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(m.get('SecondaryCidrBlocks'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UserCidrs') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcUserCidrs()
            self.user_cidrs = temp_model.from_map(m.get('UserCidrs'))

        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcsResponseBodyVpcsVpcVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeVpcsResponseBodyVpcsVpcUserCidrs(DaraModel):
    def __init__(
        self,
        user_cidr: List[str] = None,
    ):
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        return self

class DescribeVpcsResponseBodyVpcsVpcTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVpcsResponseBodyVpcsVpcTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVpcsResponseBodyVpcsVpcTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
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

class DescribeVpcsResponseBodyVpcsVpcSecondaryCidrBlocks(DaraModel):
    def __init__(
        self,
        secondary_cidr_block: List[str] = None,
    ):
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')

        return self

class DescribeVpcsResponseBodyVpcsVpcRouterTableIds(DaraModel):
    def __init__(
        self,
        router_table_ids: List[str] = None,
    ):
        self.router_table_ids = router_table_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.router_table_ids is not None:
            result['RouterTableIds'] = self.router_table_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouterTableIds') is not None:
            self.router_table_ids = m.get('RouterTableIds')

        return self

class DescribeVpcsResponseBodyVpcsVpcNatGatewayIds(DaraModel):
    def __init__(
        self,
        nat_gateway_ids: List[str] = None,
    ):
        self.nat_gateway_ids = nat_gateway_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateway_ids is not None:
            result['NatGatewayIds'] = self.nat_gateway_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayIds') is not None:
            self.nat_gateway_ids = m.get('NatGatewayIds')

        return self

class DescribeVpcsResponseBodyVpcsVpcIpv6CidrBlocks(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: List[main_models.DescribeVpcsResponseBodyVpcsVpcIpv6CidrBlocksIpv6CidrBlock] = None,
    ):
        self.ipv_6cidr_block = ipv_6cidr_block

    def validate(self):
        if self.ipv_6cidr_block:
            for v1 in self.ipv_6cidr_block:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6CidrBlock'] = []
        if self.ipv_6cidr_block is not None:
            for k1 in self.ipv_6cidr_block:
                result['Ipv6CidrBlock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6cidr_block = []
        if m.get('Ipv6CidrBlock') is not None:
            for k1 in m.get('Ipv6CidrBlock'):
                temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcIpv6CidrBlocksIpv6CidrBlock()
                self.ipv_6cidr_block.append(temp_model.from_map(k1))

        return self

class DescribeVpcsResponseBodyVpcsVpcIpv6CidrBlocksIpv6CidrBlock(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: str = None,
        ipv_6isp: str = None,
    ):
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The type of IPv6 CIDR block. Valid values:
        # 
        # *   **BGP**
        # *   **ChinaMobile**
        # *   **ChinaUnicom**
        # *   **ChinaTelecom**
        # 
        # >  If your Alibaba Cloud account is allowed to activate single-ISP bandwidth, you can set this parameter to **ChinaTelecom**, **ChinaUnicom**, or **ChinaMobile**.
        self.ipv_6isp = ipv_6isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        return self

