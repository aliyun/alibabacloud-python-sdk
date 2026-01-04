# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcAttributeResponseBody(DaraModel):
    def __init__(
        self,
        associated_cens: main_models.DescribeVpcAttributeResponseBodyAssociatedCens = None,
        associated_propagation_sources: main_models.DescribeVpcAttributeResponseBodyAssociatedPropagationSources = None,
        cidr_block: str = None,
        classic_link_enabled: bool = None,
        cloud_resources: main_models.DescribeVpcAttributeResponseBodyCloudResources = None,
        creation_time: str = None,
        description: str = None,
        dhcp_options_set_id: str = None,
        dhcp_options_set_status: str = None,
        dns_hostname_status: str = None,
        enabled_ipv_6: bool = None,
        ipv_4gateway_id: str = None,
        ipv_6cidr_block: str = None,
        ipv_6cidr_blocks: main_models.DescribeVpcAttributeResponseBodyIpv6CidrBlocks = None,
        is_default: bool = None,
        owner_id: int = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        secondary_cidr_blocks: main_models.DescribeVpcAttributeResponseBodySecondaryCidrBlocks = None,
        status: str = None,
        support_ipv_4gateway: bool = None,
        tags: main_models.DescribeVpcAttributeResponseBodyTags = None,
        user_cidrs: main_models.DescribeVpcAttributeResponseBodyUserCidrs = None,
        vrouter_id: str = None,
        v_switch_ids: main_models.DescribeVpcAttributeResponseBodyVSwitchIds = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The list of Cloud Enterprise Network (CEN) instances to which the VPC is attached.
        # 
        # If the VPC is not attached to a CEN instance, the parameter is not returned.
        self.associated_cens = associated_cens
        # The route source associated with the VPC.
        self.associated_propagation_sources = associated_propagation_sources
        # The IPv4 CIDR block of the VPC.
        self.cidr_block = cidr_block
        # Indicates whether the ClassicLink feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.classic_link_enabled = classic_link_enabled
        # The list of resources deployed in the VPC.
        self.cloud_resources = cloud_resources
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
        # Indicates whether DNS hostname is enabled.
        self.dns_hostname_status = dns_hostname_status
        # Indicates whether the VPC enables IPv6 .
        # - true
        # - false
        self.enabled_ipv_6 = enabled_ipv_6
        # The ID of the IPv4 gateway.
        self.ipv_4gateway_id = ipv_4gateway_id
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_blocks = ipv_6cidr_blocks
        # Indicates whether the VPC is the default VPC. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.is_default = is_default
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.owner_id = owner_id
        # The ID of the region to which the VPC belongs.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The secondary IPv4 CIDR block of the VPC.
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # The status of the VPC. Valid values:
        # 
        # *   **Available**
        # *   **Pending**
        self.status = status
        # Indicates whether the VPC supports IPv4 gateways.
        # 
        # *   **true**
        # *   **false**
        self.support_ipv_4gateway = support_ipv_4gateway
        # The information about the tags.
        self.tags = tags
        # The user CIDR block. Multiple CIDR blocks are separated by commas (,). At most three CIDR blocks are returned.
        self.user_cidrs = user_cidrs
        # The ID of the vRouter that belongs to the VPC.
        self.vrouter_id = vrouter_id
        # The list of vSwitches deployed in the VPC.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        if self.associated_cens:
            self.associated_cens.validate()
        if self.associated_propagation_sources:
            self.associated_propagation_sources.validate()
        if self.cloud_resources:
            self.cloud_resources.validate()
        if self.ipv_6cidr_blocks:
            self.ipv_6cidr_blocks.validate()
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
        if self.associated_cens is not None:
            result['AssociatedCens'] = self.associated_cens.to_map()

        if self.associated_propagation_sources is not None:
            result['AssociatedPropagationSources'] = self.associated_propagation_sources.to_map()

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.classic_link_enabled is not None:
            result['ClassicLinkEnabled'] = self.classic_link_enabled

        if self.cloud_resources is not None:
            result['CloudResources'] = self.cloud_resources.to_map()

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

        if self.ipv_4gateway_id is not None:
            result['Ipv4GatewayId'] = self.ipv_4gateway_id

        if self.ipv_6cidr_block is not None:
            result['Ipv6CidrBlock'] = self.ipv_6cidr_block

        if self.ipv_6cidr_blocks is not None:
            result['Ipv6CidrBlocks'] = self.ipv_6cidr_blocks.to_map()

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.support_ipv_4gateway is not None:
            result['SupportIpv4Gateway'] = self.support_ipv_4gateway

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
        if m.get('AssociatedCens') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyAssociatedCens()
            self.associated_cens = temp_model.from_map(m.get('AssociatedCens'))

        if m.get('AssociatedPropagationSources') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyAssociatedPropagationSources()
            self.associated_propagation_sources = temp_model.from_map(m.get('AssociatedPropagationSources'))

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('ClassicLinkEnabled') is not None:
            self.classic_link_enabled = m.get('ClassicLinkEnabled')

        if m.get('CloudResources') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyCloudResources()
            self.cloud_resources = temp_model.from_map(m.get('CloudResources'))

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

        if m.get('Ipv4GatewayId') is not None:
            self.ipv_4gateway_id = m.get('Ipv4GatewayId')

        if m.get('Ipv6CidrBlock') is not None:
            self.ipv_6cidr_block = m.get('Ipv6CidrBlock')

        if m.get('Ipv6CidrBlocks') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyIpv6CidrBlocks()
            self.ipv_6cidr_blocks = temp_model.from_map(m.get('Ipv6CidrBlocks'))

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecondaryCidrBlocks') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodySecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(m.get('SecondaryCidrBlocks'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportIpv4Gateway') is not None:
            self.support_ipv_4gateway = m.get('SupportIpv4Gateway')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UserCidrs') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyUserCidrs()
            self.user_cidrs = temp_model.from_map(m.get('UserCidrs'))

        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeVpcAttributeResponseBodyVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcAttributeResponseBodyVSwitchIds(DaraModel):
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

class DescribeVpcAttributeResponseBodyUserCidrs(DaraModel):
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

class DescribeVpcAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeVpcAttributeResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeVpcAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeVpcAttributeResponseBodyTagsTag(DaraModel):
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

class DescribeVpcAttributeResponseBodySecondaryCidrBlocks(DaraModel):
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

class DescribeVpcAttributeResponseBodyIpv6CidrBlocks(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: List[main_models.DescribeVpcAttributeResponseBodyIpv6CidrBlocksIpv6CidrBlock] = None,
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
                temp_model = main_models.DescribeVpcAttributeResponseBodyIpv6CidrBlocksIpv6CidrBlock()
                self.ipv_6cidr_block.append(temp_model.from_map(k1))

        return self

class DescribeVpcAttributeResponseBodyIpv6CidrBlocksIpv6CidrBlock(DaraModel):
    def __init__(
        self,
        ipv_6cidr_block: str = None,
        ipv_6isp: str = None,
    ):
        # The IPv6 CIDR block of the VPC.
        self.ipv_6cidr_block = ipv_6cidr_block
        # The IPv6 CIDR block type of the VPC. Valid values:
        # 
        # *   **BGP** (default)
        # *   **ChinaMobile**
        # *   **ChinaUnicom**
        # *   **ChinaTelecom**
        # 
        # >  If you are allowed to use single-ISP bandwidth, valid values are **ChinaTelecom**, **ChinaUnicom**, and **ChinaMobile**
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

class DescribeVpcAttributeResponseBodyCloudResources(DaraModel):
    def __init__(
        self,
        cloud_resource_set_type: List[main_models.DescribeVpcAttributeResponseBodyCloudResourcesCloudResourceSetType] = None,
    ):
        self.cloud_resource_set_type = cloud_resource_set_type

    def validate(self):
        if self.cloud_resource_set_type:
            for v1 in self.cloud_resource_set_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudResourceSetType'] = []
        if self.cloud_resource_set_type is not None:
            for k1 in self.cloud_resource_set_type:
                result['CloudResourceSetType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_resource_set_type = []
        if m.get('CloudResourceSetType') is not None:
            for k1 in m.get('CloudResourceSetType'):
                temp_model = main_models.DescribeVpcAttributeResponseBodyCloudResourcesCloudResourceSetType()
                self.cloud_resource_set_type.append(temp_model.from_map(k1))

        return self

class DescribeVpcAttributeResponseBodyCloudResourcesCloudResourceSetType(DaraModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        # The number of resources in the VPC.
        self.resource_count = resource_count
        # The type of resource deployed in the VPC. Valid values: Valid values:
        # 
        # *   **VSwitch**
        # *   **VRouter**
        # *   **RouteTable**
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class DescribeVpcAttributeResponseBodyAssociatedPropagationSources(DaraModel):
    def __init__(
        self,
        associated_propagation_sources: List[main_models.DescribeVpcAttributeResponseBodyAssociatedPropagationSourcesAssociatedPropagationSources] = None,
    ):
        self.associated_propagation_sources = associated_propagation_sources

    def validate(self):
        if self.associated_propagation_sources:
            for v1 in self.associated_propagation_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedPropagationSources'] = []
        if self.associated_propagation_sources is not None:
            for k1 in self.associated_propagation_sources:
                result['AssociatedPropagationSources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_propagation_sources = []
        if m.get('AssociatedPropagationSources') is not None:
            for k1 in m.get('AssociatedPropagationSources'):
                temp_model = main_models.DescribeVpcAttributeResponseBodyAssociatedPropagationSourcesAssociatedPropagationSources()
                self.associated_propagation_sources.append(temp_model.from_map(k1))

        return self

class DescribeVpcAttributeResponseBodyAssociatedPropagationSourcesAssociatedPropagationSources(DaraModel):
    def __init__(
        self,
        route_propagated: bool = None,
        source_instance_id: str = None,
        source_owner_id: int = None,
        source_type: str = None,
        status: str = None,
    ):
        # Indicates whether routes are advertised to the VPC.
        self.route_propagated = route_propagated
        # The instance ID of the source.
        self.source_instance_id = source_instance_id
        # The account ID of the source.
        self.source_owner_id = source_owner_id
        # The source type.
        # 
        # *   **CEN**
        # *   **VPN**
        # *   **TR**
        # *   **ECR**
        self.source_type = source_type
        # The binding status.
        # 
        # *   **Attaching**
        # *   **Attached**
        # *   **Detaching**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_propagated is not None:
            result['RoutePropagated'] = self.route_propagated

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.source_owner_id is not None:
            result['SourceOwnerId'] = self.source_owner_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoutePropagated') is not None:
            self.route_propagated = m.get('RoutePropagated')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('SourceOwnerId') is not None:
            self.source_owner_id = m.get('SourceOwnerId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeVpcAttributeResponseBodyAssociatedCens(DaraModel):
    def __init__(
        self,
        associated_cen: List[main_models.DescribeVpcAttributeResponseBodyAssociatedCensAssociatedCen] = None,
    ):
        self.associated_cen = associated_cen

    def validate(self):
        if self.associated_cen:
            for v1 in self.associated_cen:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssociatedCen'] = []
        if self.associated_cen is not None:
            for k1 in self.associated_cen:
                result['AssociatedCen'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_cen = []
        if m.get('AssociatedCen') is not None:
            for k1 in m.get('AssociatedCen'):
                temp_model = main_models.DescribeVpcAttributeResponseBodyAssociatedCensAssociatedCen()
                self.associated_cen.append(temp_model.from_map(k1))

        return self

class DescribeVpcAttributeResponseBodyAssociatedCensAssociatedCen(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cen_owner_id: int = None,
        cen_status: str = None,
    ):
        # The ID of the CEN instance to which the VPC is attached.
        self.cen_id = cen_id
        # The ID of the account to which the CEN instance belongs.
        self.cen_owner_id = cen_owner_id
        # The status of the CEN instance.
        # 
        # **Attached** is returned only when the VPC is attached to a CEN instance.
        self.cen_status = cen_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.cen_status is not None:
            result['CenStatus'] = self.cen_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CenStatus') is not None:
            self.cen_status = m.get('CenStatus')

        return self

