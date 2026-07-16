# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyAddressBookShrinkRequest(DaraModel):
    def __init__(
        self,
        ack_labels: List[main_models.ModifyAddressBookShrinkRequestAckLabels] = None,
        ack_namespaces: List[str] = None,
        address_list: str = None,
        asset_member_uids_shrink: str = None,
        asset_region_resource_types_shrink: str = None,
        auto_add_tag_ecs: str = None,
        description: str = None,
        group_name: str = None,
        group_uuid: str = None,
        lang: str = None,
        modify_mode: str = None,
        source_ip: str = None,
        tag_list: List[main_models.ModifyAddressBookShrinkRequestTagList] = None,
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
        self.asset_member_uids_shrink = asset_member_uids_shrink
        # The list of regions and resource types for the asset address book.
        self.asset_region_resource_types_shrink = asset_region_resource_types_shrink
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

        if self.asset_member_uids_shrink is not None:
            result['AssetMemberUids'] = self.asset_member_uids_shrink

        if self.asset_region_resource_types_shrink is not None:
            result['AssetRegionResourceTypes'] = self.asset_region_resource_types_shrink

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
                temp_model = main_models.ModifyAddressBookShrinkRequestAckLabels()
                self.ack_labels.append(temp_model.from_map(k1))

        if m.get('AckNamespaces') is not None:
            self.ack_namespaces = m.get('AckNamespaces')

        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('AssetMemberUids') is not None:
            self.asset_member_uids_shrink = m.get('AssetMemberUids')

        if m.get('AssetRegionResourceTypes') is not None:
            self.asset_region_resource_types_shrink = m.get('AssetRegionResourceTypes')

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
                temp_model = main_models.ModifyAddressBookShrinkRequestTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')

        return self

class ModifyAddressBookShrinkRequestTagList(DaraModel):
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

class ModifyAddressBookShrinkRequestAckLabels(DaraModel):
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

