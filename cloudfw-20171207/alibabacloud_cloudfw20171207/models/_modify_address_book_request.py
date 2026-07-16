# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyAddressBookRequest(DaraModel):
    def __init__(
        self,
        ack_labels: List[main_models.ModifyAddressBookRequestAckLabels] = None,
        ack_namespaces: List[str] = None,
        address_list: str = None,
        asset_member_uids: List[int] = None,
        asset_region_resource_types: List[main_models.ModifyAddressBookRequestAssetRegionResourceTypes] = None,
        auto_add_tag_ecs: str = None,
        description: str = None,
        group_name: str = None,
        group_uuid: str = None,
        lang: str = None,
        modify_mode: str = None,
        source_ip: str = None,
        tag_list: List[main_models.ModifyAddressBookRequestTagList] = None,
        tag_relation: str = None,
    ):
        # The list of labels for ACK cluster pods.
        # 
        # > A maximum of 10 labels are supported.
        self.ack_labels = ack_labels
        # The list of namespaces for ACK cluster pods.
        # > A maximum of 10 namespaces are supported.
        self.ack_namespaces = ack_namespaces
        # The addresses in the address book. Separate multiple addresses with commas (,). Use a space to separate an address from its description. This parameter is required when GroupType is set to **ip**, **port**, or **domain**.
        # 
        # - When GroupType is set to **ip**, specify IP addresses. Example: 1.2.XX.XX/32 Development CIDR block,10.0.0.X/24,1.2.XX.XX/24 Test CIDR block.
        # 
        # - When GroupType is set to **port**, specify ports or port ranges. Example: 80/80 HTTP port,100/200,3306 Database port.
        # 
        # - When GroupType is set to **domain**, specify domain names. Example: demo1.aliyun.com Test domain name,demo2.aliyun.com,www.aliyun.com Alibaba Cloud official website.
        self.address_list = address_list
        # The list of member accounts for the asset address book.
        self.asset_member_uids = asset_member_uids
        # The list of regions and resource types for the asset address book.
        self.asset_region_resource_types = asset_region_resource_types
        # Specifies whether the public IP addresses of Elastic Compute Service (ECS) instances that match new labels is automatically added to the address book.
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        # 
        # This parameter is required.
        self.description = description
        # The name of the address book.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The unique ID of the address book.
        # 
        # > You can obtain the value by calling the [DescribeAddressBook](~~DescribeAddressBook~~) operation.
        # 
        # This parameter is required.
        self.group_uuid = group_uuid
        # The language type. Valid values:
        # - **en**: English.
        # - **zh**: Chinese (default).
        self.lang = lang
        # The modification mode.
        # 
        # > When GroupType is set to **ip**, **ipv6**, **port**, or **domain**, the default value is **Cover** if this parameter is not specified.
        # >Notice: When GroupType is set to **tag**, this parameter must be left empty.</notice>
        self.modify_mode = modify_mode
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ECS tag list.
        self.tag_list = tag_list
        # The logical relationship among multiple ECS tags. Valid values:
        # - **or**: The public IP address of an ECS instance is added to the address book if the instance matches any of the specified tags.
        # - **and**: The public IP address of an ECS instance is added to the address book only if the instance matches all of the specified tags.
        self.tag_relation = tag_relation

    def validate(self):
        if self.ack_labels:
            for v1 in self.ack_labels:
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
        result['AckLabels'] = []
        if self.ack_labels is not None:
            for k1 in self.ack_labels:
                result['AckLabels'].append(k1.to_map() if k1 else None)

        if self.ack_namespaces is not None:
            result['AckNamespaces'] = self.ack_namespaces

        if self.address_list is not None:
            result['AddressList'] = self.address_list

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

        if self.group_uuid is not None:
            result['GroupUuid'] = self.group_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        if self.tag_relation is not None:
            result['TagRelation'] = self.tag_relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ack_labels = []
        if m.get('AckLabels') is not None:
            for k1 in m.get('AckLabels'):
                temp_model = main_models.ModifyAddressBookRequestAckLabels()
                self.ack_labels.append(temp_model.from_map(k1))

        if m.get('AckNamespaces') is not None:
            self.ack_namespaces = m.get('AckNamespaces')

        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('AssetMemberUids') is not None:
            self.asset_member_uids = m.get('AssetMemberUids')

        self.asset_region_resource_types = []
        if m.get('AssetRegionResourceTypes') is not None:
            for k1 in m.get('AssetRegionResourceTypes'):
                temp_model = main_models.ModifyAddressBookRequestAssetRegionResourceTypes()
                self.asset_region_resource_types.append(temp_model.from_map(k1))

        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupUuid') is not None:
            self.group_uuid = m.get('GroupUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.ModifyAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')

        return self

class ModifyAddressBookRequestTagList(DaraModel):
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

class ModifyAddressBookRequestAssetRegionResourceTypes(DaraModel):
    def __init__(
        self,
        asset_region_id: str = None,
        resource_type: main_models.ModifyAddressBookRequestAssetRegionResourceTypesResourceType = None,
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
            temp_model = main_models.ModifyAddressBookRequestAssetRegionResourceTypesResourceType()
            self.resource_type = temp_model.from_map(m.get('ResourceType'))

        return self

class ModifyAddressBookRequestAssetRegionResourceTypesResourceType(DaraModel):
    def __init__(
        self,
        ipv_4: main_models.ModifyAddressBookRequestAssetRegionResourceTypesResourceTypeIpv4 = None,
        ipv_6: main_models.ModifyAddressBookRequestAssetRegionResourceTypesResourceTypeIpv6 = None,
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
            temp_model = main_models.ModifyAddressBookRequestAssetRegionResourceTypesResourceTypeIpv4()
            self.ipv_4 = temp_model.from_map(m.get('Ipv4'))

        if m.get('Ipv6') is not None:
            temp_model = main_models.ModifyAddressBookRequestAssetRegionResourceTypesResourceTypeIpv6()
            self.ipv_6 = temp_model.from_map(m.get('Ipv6'))

        return self

class ModifyAddressBookRequestAssetRegionResourceTypesResourceTypeIpv6(DaraModel):
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

class ModifyAddressBookRequestAssetRegionResourceTypesResourceTypeIpv4(DaraModel):
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

class ModifyAddressBookRequestAckLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the ACK cluster pod label.
        self.key = key
        # The value of the ACK cluster pod label.
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

