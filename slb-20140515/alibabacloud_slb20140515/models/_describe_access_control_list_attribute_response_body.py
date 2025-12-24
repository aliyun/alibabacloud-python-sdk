# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessControlListAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_entrys: main_models.DescribeAccessControlListAttributeResponseBodyAclEntrys = None,
        acl_id: str = None,
        acl_name: str = None,
        address_ipversion: str = None,
        create_time: str = None,
        related_listeners: main_models.DescribeAccessControlListAttributeResponseBodyRelatedListeners = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: main_models.DescribeAccessControlListAttributeResponseBodyTags = None,
        total_acl_entry: int = None,
    ):
        # The information about the access control policy.
        self.acl_entrys = acl_entrys
        # The ACL ID.
        self.acl_id = acl_id
        # The ACL name.
        self.acl_name = acl_name
        # The IP version. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The time when the ACL was created. The time follows the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The listeners with which the ACL is associated.
        self.related_listeners = related_listeners
        # The ID of the request.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags added to the ACL.
        self.tags = tags
        # The total number of ACL entries.
        self.total_acl_entry = total_acl_entry

    def validate(self):
        if self.acl_entrys:
            self.acl_entrys.validate()
        if self.related_listeners:
            self.related_listeners.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_entrys is not None:
            result['AclEntrys'] = self.acl_entrys.to_map()

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.related_listeners is not None:
            result['RelatedListeners'] = self.related_listeners.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.total_acl_entry is not None:
            result['TotalAclEntry'] = self.total_acl_entry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntrys') is not None:
            temp_model = main_models.DescribeAccessControlListAttributeResponseBodyAclEntrys()
            self.acl_entrys = temp_model.from_map(m.get('AclEntrys'))

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RelatedListeners') is not None:
            temp_model = main_models.DescribeAccessControlListAttributeResponseBodyRelatedListeners()
            self.related_listeners = temp_model.from_map(m.get('RelatedListeners'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAccessControlListAttributeResponseBodyTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TotalAclEntry') is not None:
            self.total_acl_entry = m.get('TotalAclEntry')

        return self

class DescribeAccessControlListAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeAccessControlListAttributeResponseBodyTagsTag] = None,
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
                temp_model = main_models.DescribeAccessControlListAttributeResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAccessControlListAttributeResponseBodyTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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

class DescribeAccessControlListAttributeResponseBodyRelatedListeners(DaraModel):
    def __init__(
        self,
        related_listener: List[main_models.DescribeAccessControlListAttributeResponseBodyRelatedListenersRelatedListener] = None,
    ):
        self.related_listener = related_listener

    def validate(self):
        if self.related_listener:
            for v1 in self.related_listener:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RelatedListener'] = []
        if self.related_listener is not None:
            for k1 in self.related_listener:
                result['RelatedListener'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_listener = []
        if m.get('RelatedListener') is not None:
            for k1 in m.get('RelatedListener'):
                temp_model = main_models.DescribeAccessControlListAttributeResponseBodyRelatedListenersRelatedListener()
                self.related_listener.append(temp_model.from_map(k1))

        return self

class DescribeAccessControlListAttributeResponseBodyRelatedListenersRelatedListener(DaraModel):
    def __init__(
        self,
        acl_type: str = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        protocol: str = None,
    ):
        # The type of ACL. Valid values:
        # 
        # *   **black**
        # *   **white**
        self.acl_type = acl_type
        # The frontend port of the listener with which the ACL is associated.
        self.listener_port = listener_port
        # The CLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The type of protocol that the associated listener uses.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeAccessControlListAttributeResponseBodyAclEntrys(DaraModel):
    def __init__(
        self,
        acl_entry: List[main_models.DescribeAccessControlListAttributeResponseBodyAclEntrysAclEntry] = None,
    ):
        self.acl_entry = acl_entry

    def validate(self):
        if self.acl_entry:
            for v1 in self.acl_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclEntry'] = []
        if self.acl_entry is not None:
            for k1 in self.acl_entry:
                result['AclEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entry = []
        if m.get('AclEntry') is not None:
            for k1 in m.get('AclEntry'):
                temp_model = main_models.DescribeAccessControlListAttributeResponseBodyAclEntrysAclEntry()
                self.acl_entry.append(temp_model.from_map(k1))

        return self

class DescribeAccessControlListAttributeResponseBodyAclEntrysAclEntry(DaraModel):
    def __init__(
        self,
        acl_entry_comment: str = None,
        acl_entry_ip: str = None,
    ):
        # The remarks of the ACL entry.
        self.acl_entry_comment = acl_entry_comment
        # The IP entry in the ACL.
        self.acl_entry_ip = acl_entry_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_entry_comment is not None:
            result['AclEntryComment'] = self.acl_entry_comment

        if self.acl_entry_ip is not None:
            result['AclEntryIP'] = self.acl_entry_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryComment') is not None:
            self.acl_entry_comment = m.get('AclEntryComment')

        if m.get('AclEntryIP') is not None:
            self.acl_entry_ip = m.get('AclEntryIP')

        return self

