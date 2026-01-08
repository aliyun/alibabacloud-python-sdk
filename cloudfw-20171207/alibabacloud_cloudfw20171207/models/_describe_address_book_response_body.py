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
        # The information about the address book.
        self.acls = acls
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of the returned address books.
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
        self.ack_cluster_connector_id = ack_cluster_connector_id
        self.ack_cluster_connector_name = ack_cluster_connector_name
        self.ack_labels = ack_labels
        self.ack_namespaces = ack_namespaces
        # The addresses in the address book.
        self.address_list = address_list
        # The number of addresses in the address book.
        self.address_list_count = address_list_count
        # A list of addresses in the address book, each with a single address description.
        self.addresses = addresses
        # Indicates whether the public IP addresses of ECS instances are automatically added to the address book if the instances match the specified tags. The setting takes effect on both newly purchased ECS instances whose tag settings are complete and ECS instances whose tag settings are modified. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.auto_add_tag_ecs = auto_add_tag_ecs
        # The description of the address book.
        self.description = description
        # The name of the address book.
        self.group_name = group_name
        # The type of the address book. Valid values:
        # 
        # *   **ip**: IP address book
        # *   **domain**: domain address book
        # *   **port**: port address book
        # *   **tag**: ECS tag-based address book
        # *   **allCloud**: cloud service address book
        # *   **threat**: threat intelligence address book
        self.group_type = group_type
        # The UUID of the address book.
        self.group_uuid = group_uuid
        # The number of times that the address book is referenced.
        self.reference_count = reference_count
        self.region_no = region_no
        # The details about the ECS tags that can be automatically added to the address book.
        self.tag_list = tag_list
        # The logical relationship among ECS tags. Valid values:
        # 
        # *   **and**: Only the public IP addresses of ECS instances that match all the specified tags can be added to the address book.
        # *   **or**: The public IP addresses of ECS instances that match any of the specified tags can be added to the address book.
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

class DescribeAddressBookResponseBodyAclsAddresses(DaraModel):
    def __init__(
        self,
        address: str = None,
        note: str = None,
    ):
        # Address information in the address book.
        self.address = address
        # Single address description.
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
        self.key = key
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

