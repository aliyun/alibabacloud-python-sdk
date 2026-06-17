# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class AddAddressBookRequest(DaraModel):
    def __init__(
        self,
        ack_cluster_connector_id: str = None,
        ack_labels: List[main_models.AddAddressBookRequestAckLabels] = None,
        ack_namespaces: List[str] = None,
        address_list: str = None,
        auto_add_tag_ecs: str = None,
        description: str = None,
        group_name: str = None,
        group_type: str = None,
        lang: str = None,
        source_ip: str = None,
        tag_list: List[main_models.AddAddressBookRequestTagList] = None,
        tag_relation: str = None,
    ):
        # The ID of the ACK cluster connector. You can obtain this value from the following operation:
        # 
        # - [DescribeAckClusterConnectors](~~DescribeAckClusterConnectors~~): Queries a list of ACK cluster connectors.
        self.ack_cluster_connector_id = ack_cluster_connector_id
        # The list of ACK cluster pod labels.
        # 
        # > You can specify a maximum of 10 labels.
        self.ack_labels = ack_labels
        # The list of ACK cluster pod namespaces.
        # 
        # > You can specify a maximum of 10 namespaces.
        self.ack_namespaces = ack_namespaces
        # The list of addresses in the address book. Separate multiple addresses with commas (,). For each address, separate the address and its description with a space.
        # 
        # > This parameter is required when GroupType is set to `ip`, `port`, or `domain`.
        # 
        # - If you set GroupType to `ip`, enter IP addresses in the list. Example: 192.0.XX.XX/32 development segment,10.0.0.X/24,192.0.XX.XX/24 test segment.
        # 
        # - If you set GroupType to `port`, enter ports or port ranges in the list. Example: 80 HTTP port,100/200,3306 database port.
        # 
        # - If you set GroupType to `domain`, enter domain names in the list. Example: example.com test domain name,aliyundoc.com,www\\.aliyun.com Alibaba Cloud official website.
        self.address_list = address_list
        # Specifies whether to automatically add the public IP addresses of ECS instances that match the specified tags to the address book.
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        # 
        # This parameter is required.
        self.description = description
        # The name of the address book.
        # 
        # This parameter is required.
        self.group_name = group_name
        # The type of the address book.
        # 
        # This parameter is required.
        self.group_type = group_type
        # The language of the address book description.
        self.lang = lang
        # The source IP address of the visitor.
        self.source_ip = source_ip
        # The list of ECS tags.
        self.tag_list = tag_list
        # The logical relationship between multiple ECS tags.
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
        if self.ack_cluster_connector_id is not None:
            result['AckClusterConnectorId'] = self.ack_cluster_connector_id

        result['AckLabels'] = []
        if self.ack_labels is not None:
            for k1 in self.ack_labels:
                result['AckLabels'].append(k1.to_map() if k1 else None)

        if self.ack_namespaces is not None:
            result['AckNamespaces'] = self.ack_namespaces

        if self.address_list is not None:
            result['AddressList'] = self.address_list

        if self.auto_add_tag_ecs is not None:
            result['AutoAddTagEcs'] = self.auto_add_tag_ecs

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.lang is not None:
            result['Lang'] = self.lang

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
        if m.get('AckClusterConnectorId') is not None:
            self.ack_cluster_connector_id = m.get('AckClusterConnectorId')

        self.ack_labels = []
        if m.get('AckLabels') is not None:
            for k1 in m.get('AckLabels'):
                temp_model = main_models.AddAddressBookRequestAckLabels()
                self.ack_labels.append(temp_model.from_map(k1))

        if m.get('AckNamespaces') is not None:
            self.ack_namespaces = m.get('AckNamespaces')

        if m.get('AddressList') is not None:
            self.address_list = m.get('AddressList')

        if m.get('AutoAddTagEcs') is not None:
            self.auto_add_tag_ecs = m.get('AutoAddTagEcs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.AddAddressBookRequestTagList()
                self.tag_list.append(temp_model.from_map(k1))

        if m.get('TagRelation') is not None:
            self.tag_relation = m.get('TagRelation')

        return self

class AddAddressBookRequestTagList(DaraModel):
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



class AddAddressBookRequestAckLabels(DaraModel):
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

