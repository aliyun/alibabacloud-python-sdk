# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAddressBookResponseBody(DaraModel):
    def __init__(
        self,
        acls: List[main_models.DescribeAddressBookResponseBodyAcls] = None,
        page_no: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of address books.
        self.acls = acls
        # The page number of the current page.
        self.page_no = page_no
        # The number of address books on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of address books.
        self.total_count = total_count

    def validate(self):
        if self.acls:
            for v1 in self.acls:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Acls'] = []
        if self.acls is not None:
            for k1 in self.acls:
                result['Acls'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acls = []
        if m.get('Acls') is not None:
            for k1 in m.get('Acls'):
                temp_model = main_models.DescribeAddressBookResponseBodyAcls()
                self.acls.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAddressBookResponseBodyAcls(DaraModel):
    def __init__(
        self,
        ack_cluster_connector_id: str = None,
        ack_cluster_connector_name: str = None,
        ack_labels: List[main_models.DescribeAddressBookResponseBodyAclsAckLabels] = None,
        ack_namespaces: List[str] = None,
        address_list: List[str] = None,
        address_list_count: int = None,
        addresses: List[main_models.DescribeAddressBookResponseBodyAclsAddresses] = None,
        asset_member_uids: List[int] = None,
        asset_region_resource_types: List[main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypes] = None,
        auto_add_tag_ecs: int = None,
        description: str = None,
        group_name: str = None,
        group_type: str = None,
        group_uuid: str = None,
        reference_count: int = None,
        region_no: str = None,
        tag_list: List[main_models.DescribeAddressBookResponseBodyAclsTagList] = None,
        tag_relation: str = None,
    ):
        # The ID of the ACK cluster connector.
        self.ack_cluster_connector_id = ack_cluster_connector_id
        # The name of the ACK cluster connector.
        self.ack_cluster_connector_name = ack_cluster_connector_name
        # The list of pod labels in the ACK cluster.
        self.ack_labels = ack_labels
        # The list of pod namespaces in the ACK cluster.
        self.ack_namespaces = ack_namespaces
        # The address list of the address book.
        self.address_list = address_list
        # The number of addresses in the address book.
        self.address_list_count = address_list_count
        # The address list of the address book that includes descriptions for individual addresses.
        self.addresses = addresses
        # The list of member accounts for the asset address book.
        self.asset_member_uids = asset_member_uids
        # The list of regions and resource types for the asset address book.
        self.asset_region_resource_types = asset_region_resource_types
        # Indicates whether the public IP addresses of ECS instances that match new tags are automatically added to the address book. Valid values:
        # - **0**: The public IP addresses are not automatically added.
        # - **1**: The public IP addresses are automatically added.
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        self.description = description
        # The name of the address book.
        self.group_name = group_name
        # The type of the address book.
        self.group_type = group_type
        # The unique ID of the address book.
        self.group_uuid = group_uuid
        # The number of times the address book is referenced.
        self.reference_count = reference_count
        # The region of the ACK cluster connector to which the address book belongs when GroupType is an ACK address book.
        self.region_no = region_no
        # The list of ECS tags.
        self.tag_list = tag_list
        # The relationship between multiple ECS tags. Valid values:
        # - **or**: The relationship between multiple tags is OR. The public IP address of an ECS instance that matches any tag is added to the address book.
        # - **and**: The relationship between multiple tags is AND. The public IP address of an ECS instance that matches all tags is added to the address book.
        self.tag_relation = tag_relation

    def validate(self):
        if self.ack_labels:
            for v1 in self.ack_labels:
                 if v1:
                    v1.validate()
        if self.addresses:
            for v1 in self.addresses:
                 if v1:
                    v1.validate()
        if self.asset_region_resource_types:
            for v1 in self.asset_region_resource_types:
                 if v1:
                    v1.validate()
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_cluster_connector_id is not None:
            result['AckClusterConnectorId'] = self.ack_cluster_connector_id

        if self.ack_cluster_connector_name is not None:
            result['AckClusterConnectorName'] = self.ack_cluster_connector_name

        result['AckLabels'] = []
        if self.ack_labels is not None:
            for k1 in self.ack_labels:
                result['AckLabels'].append(k1.to_map() if k1 else None)

        if self.ack_namespaces is not None:
            result['AckNamespaces'] = self.ack_namespaces

        if self.address_list is not None:
            result['AddressList'] = self.address_list

        if self.address_list_count is not None:
            result['AddressListCount'] = self.address_list_count

        result['Addresses'] = []
        if self.addresses is not None:
            for k1 in self.addresses:
                result['Addresses'].append(k1.to_map() if k1 else None)

        if self.asset_member_uids is not None:
            result['AssetMemberUids'] = self.asset_member_uids

        result['AssetRegionResourceTypes'] = []
        if self.asset_region_resource_types is not None:
            for k1 in self.asset_region_resource_types:
                result['AssetRegionResourceTypes'].append(k1.to_map() if k1 else None)

        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid

        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckClusterConnectorId') is not None:
            self.ack_cluster_connector_id = m.get('AckClusterConnectorId')

        if m.get('AckClusterConnectorName') is not None:
            self.ack_cluster_connector_name = m.get('AckClusterConnectorName')

        self.ack_labels = []
        if m.get('AckLabels') is not None:
            for k1 in m.get('AckLabels'):
                temp_model = main_models.DescribeAddressBookResponseBodyAclsAckLabels()
                self.ack_labels.append(temp_model.from_map(k1))

        if m.get('AckNamespaces') is not None:
            self.ack_namespaces = m.get('AckNamespaces')

        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('AddressListCount') is not None:
            self.address_list_count = m.get('AddressListCount')

        self.addresses = []
        if m.get('Addresses') is not None:
            for k1 in m.get('Addresses'):
                temp_model = main_models.DescribeAddressBookResponseBodyAclsAddresses()
                self.addresses.append(temp_model.from_map(k1))

        if m.get('AssetMemberUids') is not None:
            self.asset_member_uids = m.get('AssetMemberUids')

        self.asset_region_resource_types = []
        if m.get('AssetRegionResourceTypes') is not None:
            for k1 in m.get('AssetRegionResourceTypes'):
                temp_model = main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypes()
                self.asset_region_resource_types.append(temp_model.from_map(k1))

        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')

        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeAddressBookResponseBodyAclsTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')

        return self

class DescribeAddressBookResponseBodyAclsTagList(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the ECS tag.
        self.tag_key = tag_key
        # The value of the ECS tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeAddressBookResponseBodyAclsAssetRegionResourceTypes(DaraModel):
    def __init__(
        self,
        asset_region_id: str = None,
        resource_type: main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceType = None,
    ):
        # The region ID of the asset.
        self.asset_region_id = asset_region_id
        # The asset type.
        self.resource_type = resource_type

    def validate(self):
        if self.resource_type:
            self.resource_type.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_region_id is not None:
            result['AssetRegionId'] = self.asset_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetRegionId') is not None:
            self.asset_region_id = m.get('AssetRegionId')

        if m.get('ResourceType') is not None:
            temp_model = main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceType()
            self.resource_type = temp_model.from_map(m.get('ResourceType'))

        return self

class DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceType(DaraModel):
    def __init__(
        self,
        ipv_4: main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceTypeIpv4 = None,
        ipv_6: main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceTypeIpv6 = None,
    ):
        # The IPv4 asset type.
        self.ipv_4 = ipv_4
        # The IPv6 asset type.
        self.ipv_6 = ipv_6

    def validate(self):
        if self.ipv_4:
            self.ipv_4.validate()
        if self.ipv_6:
            self.ipv_6.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4.to_map()

        if self.ipv_6 is not None:
            result['Ipv6'] = self.ipv_6.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4') is not None:
            temp_model = main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceTypeIpv4()
            self.ipv_4 = temp_model.from_map(m.get('Ipv4'))

        if m.get('Ipv6') is not None:
            temp_model = main_models.DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceTypeIpv6()
            self.ipv_6 = temp_model.from_map(m.get('Ipv6'))

        return self

class DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceTypeIpv6(DaraModel):
    def __init__(
        self,
        ai_gateway_eipv_6: bool = None,
        alb_ipv_6: bool = None,
        api_gateway_eipv_6: bool = None,
        ecs_ipv_6: bool = None,
        eni_eipv_6: bool = None,
        ga_eipv_6: bool = None,
        nlb_ipv_6: bool = None,
        slb_ipv_6: bool = None,
    ):
        # The asset type: AIGatewayEIPv6.
        self.ai_gateway_eipv_6 = ai_gateway_eipv_6
        # The asset type: AlbIPv6.
        self.alb_ipv_6 = alb_ipv_6
        # The asset type: ApigEIPv6.
        self.api_gateway_eipv_6 = api_gateway_eipv_6
        # The asset type: EcsIPv6.
        self.ecs_ipv_6 = ecs_ipv_6
        # The asset type: EniEIPv6.
        self.eni_eipv_6 = eni_eipv_6
        # The asset type: GaEIPv6.
        self.ga_eipv_6 = ga_eipv_6
        # The asset type: NlbIPv6.
        self.nlb_ipv_6 = nlb_ipv_6
        # The asset type: SlbIPv6.
        self.slb_ipv_6 = slb_ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_gateway_eipv_6 is not None:
            result['AiGatewayEIPv6'] = self.ai_gateway_eipv_6

        if self.alb_ipv_6 is not None:
            result['AlbIPv6'] = self.alb_ipv_6

        if self.api_gateway_eipv_6 is not None:
            result['ApiGatewayEIPv6'] = self.api_gateway_eipv_6

        if self.ecs_ipv_6 is not None:
            result['EcsIPv6'] = self.ecs_ipv_6

        if self.eni_eipv_6 is not None:
            result['EniEIPv6'] = self.eni_eipv_6

        if self.ga_eipv_6 is not None:
            result['GaEIPv6'] = self.ga_eipv_6

        if self.nlb_ipv_6 is not None:
            result['NlbIPv6'] = self.nlb_ipv_6

        if self.slb_ipv_6 is not None:
            result['SlbIPv6'] = self.slb_ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiGatewayEIPv6') is not None:
            self.ai_gateway_eipv_6 = m.get('AiGatewayEIPv6')

        if m.get('AlbIPv6') is not None:
            self.alb_ipv_6 = m.get('AlbIPv6')

        if m.get('ApiGatewayEIPv6') is not None:
            self.api_gateway_eipv_6 = m.get('ApiGatewayEIPv6')

        if m.get('EcsIPv6') is not None:
            self.ecs_ipv_6 = m.get('EcsIPv6')

        if m.get('EniEIPv6') is not None:
            self.eni_eipv_6 = m.get('EniEIPv6')

        if m.get('GaEIPv6') is not None:
            self.ga_eipv_6 = m.get('GaEIPv6')

        if m.get('NlbIPv6') is not None:
            self.nlb_ipv_6 = m.get('NlbIPv6')

        if m.get('SlbIPv6') is not None:
            self.slb_ipv_6 = m.get('SlbIPv6')

        return self

class DescribeAddressBookResponseBodyAclsAssetRegionResourceTypesResourceTypeIpv4(DaraModel):
    def __init__(
        self,
        ai_gateway_eip: bool = None,
        alb_eip: bool = None,
        api_gateway_eip: bool = None,
        bastion_host_egress_ip: bool = None,
        bastion_host_ip: bool = None,
        bastion_host_ingress_ip: bool = None,
        eip: bool = None,
        ecs_eip: bool = None,
        ecs_public_ip: bool = None,
        eni_eip: bool = None,
        ga_eip: bool = None,
        havip: bool = None,
        nat_eip: bool = None,
        nat_public_ip: bool = None,
        nlb_eip: bool = None,
        slb_eip: bool = None,
        slb_public_ip: bool = None,
    ):
        # The asset type: AIGatewayEIP.
        self.ai_gateway_eip = ai_gateway_eip
        # The asset type: AlbEIP.
        self.alb_eip = alb_eip
        # The asset type: ApigEIP.
        self.api_gateway_eip = api_gateway_eip
        # The asset type: BastionHostEgressIP.
        self.bastion_host_egress_ip = bastion_host_egress_ip
        # The asset type: BastionHostIP.
        self.bastion_host_ip = bastion_host_ip
        # The asset type: BastionHostIngressIP.
        self.bastion_host_ingress_ip = bastion_host_ingress_ip
        # The asset type: EIP.
        self.eip = eip
        # The asset type: EcsEIP.
        self.ecs_eip = ecs_eip
        # The asset type: EcsPublicIP.
        self.ecs_public_ip = ecs_public_ip
        # The asset type: EniEIP.
        self.eni_eip = eni_eip
        # The asset type: GaEIP.
        self.ga_eip = ga_eip
        # The asset type: HAVIP.
        self.havip = havip
        # The asset type: NatEIP.
        self.nat_eip = nat_eip
        # The asset type: NatPublicIP.
        self.nat_public_ip = nat_public_ip
        # The asset type: NlbEIP.
        self.nlb_eip = nlb_eip
        # The asset type: SlbEIP.
        self.slb_eip = slb_eip
        # The asset type: SlbPublicIP.
        self.slb_public_ip = slb_public_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_gateway_eip is not None:
            result['AiGatewayEIP'] = self.ai_gateway_eip

        if self.alb_eip is not None:
            result['AlbEIP'] = self.alb_eip

        if self.api_gateway_eip is not None:
            result['ApiGatewayEIP'] = self.api_gateway_eip

        if self.bastion_host_egress_ip is not None:
            result['BastionHostEgressIP'] = self.bastion_host_egress_ip

        if self.bastion_host_ip is not None:
            result['BastionHostIP'] = self.bastion_host_ip

        if self.bastion_host_ingress_ip is not None:
            result['BastionHostIngressIP'] = self.bastion_host_ingress_ip

        if self.eip is not None:
            result['EIP'] = self.eip

        if self.ecs_eip is not None:
            result['EcsEIP'] = self.ecs_eip

        if self.ecs_public_ip is not None:
            result['EcsPublicIP'] = self.ecs_public_ip

        if self.eni_eip is not None:
            result['EniEIP'] = self.eni_eip

        if self.ga_eip is not None:
            result['GaEIP'] = self.ga_eip

        if self.havip is not None:
            result['HAVIP'] = self.havip

        if self.nat_eip is not None:
            result['NatEIP'] = self.nat_eip

        if self.nat_public_ip is not None:
            result['NatPublicIP'] = self.nat_public_ip

        if self.nlb_eip is not None:
            result['NlbEIP'] = self.nlb_eip

        if self.slb_eip is not None:
            result['SlbEIP'] = self.slb_eip

        if self.slb_public_ip is not None:
            result['SlbPublicIP'] = self.slb_public_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiGatewayEIP') is not None:
            self.ai_gateway_eip = m.get('AiGatewayEIP')

        if m.get('AlbEIP') is not None:
            self.alb_eip = m.get('AlbEIP')

        if m.get('ApiGatewayEIP') is not None:
            self.api_gateway_eip = m.get('ApiGatewayEIP')

        if m.get('BastionHostEgressIP') is not None:
            self.bastion_host_egress_ip = m.get('BastionHostEgressIP')

        if m.get('BastionHostIP') is not None:
            self.bastion_host_ip = m.get('BastionHostIP')

        if m.get('BastionHostIngressIP') is not None:
            self.bastion_host_ingress_ip = m.get('BastionHostIngressIP')

        if m.get('EIP') is not None:
            self.eip = m.get('EIP')

        if m.get('EcsEIP') is not None:
            self.ecs_eip = m.get('EcsEIP')

        if m.get('EcsPublicIP') is not None:
            self.ecs_public_ip = m.get('EcsPublicIP')

        if m.get('EniEIP') is not None:
            self.eni_eip = m.get('EniEIP')

        if m.get('GaEIP') is not None:
            self.ga_eip = m.get('GaEIP')

        if m.get('HAVIP') is not None:
            self.havip = m.get('HAVIP')

        if m.get('NatEIP') is not None:
            self.nat_eip = m.get('NatEIP')

        if m.get('NatPublicIP') is not None:
            self.nat_public_ip = m.get('NatPublicIP')

        if m.get('NlbEIP') is not None:
            self.nlb_eip = m.get('NlbEIP')

        if m.get('SlbEIP') is not None:
            self.slb_eip = m.get('SlbEIP')

        if m.get('SlbPublicIP') is not None:
            self.slb_public_ip = m.get('SlbPublicIP')

        return self

class DescribeAddressBookResponseBodyAclsAddresses(DaraModel):
    def __init__(
        self,
        address: str = None,
        note: str = None,
    ):
        # The address information of the address book.
        self.address = address
        # The description of the individual address.
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.note is not None:
            result['Note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        return self

class DescribeAddressBookResponseBodyAclsAckLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the pod label in the ACK cluster.
        self.key = key
        # The value of the pod label in the ACK cluster.
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

