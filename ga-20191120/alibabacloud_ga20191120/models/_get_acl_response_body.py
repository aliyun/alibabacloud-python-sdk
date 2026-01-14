# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class GetAclResponseBody(DaraModel):
    def __init__(
        self,
        acl_entries: List[main_models.GetAclResponseBodyAclEntries] = None,
        acl_id: str = None,
        acl_name: str = None,
        acl_status: str = None,
        address_ipversion: str = None,
        related_listeners: List[main_models.GetAclResponseBodyRelatedListeners] = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.GetAclResponseBodyTags] = None,
    ):
        # The entries of the ACL.
        self.acl_entries = acl_entries
        # The ID of the request.
        self.acl_id = acl_id
        # The ID of the GA instance.
        self.acl_name = acl_name
        # The IP version of the network ACL. Valid values:
        # 
        # *   **IPv4**
        # *   **IPv6**
        self.acl_status = acl_status
        # The ID of the network ACL.
        self.address_ipversion = address_ipversion
        # The listeners that are associated with the ACL.
        self.related_listeners = related_listeners
        # The ID of the network ACL.
        self.request_id = request_id
        # The name of the network ACL.
        self.resource_group_id = resource_group_id
        # The tag of the ACL.
        self.tags = tags

    def validate(self):
        if self.acl_entries:
            for v1 in self.acl_entries:
                 if v1:
                    v1.validate()
        if self.related_listeners:
            for v1 in self.related_listeners:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k1 in self.acl_entries:
                result['AclEntries'].append(k1.to_map() if k1 else None)

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k1 in self.related_listeners:
                result['RelatedListeners'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k1 in m.get('AclEntries'):
                temp_model = main_models.GetAclResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k1))

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k1 in m.get('RelatedListeners'):
                temp_model = main_models.GetAclResponseBodyRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAclResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetAclResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is add to the ACL.
        self.key = key
        # The value of tag N that is add to the ACL.
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

class GetAclResponseBodyRelatedListeners(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        acl_type: str = None,
        listener_id: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # The type of the ACL. Valid values:
        # 
        # *   **white**: Only requests from the IP addresses or CIDR blocks in the ACL are forwarded. Whitelists are suitable for scenarios in which you want to allow access from specific IP addresses to an application. If a whitelist is improperly configured, risks may arise. After a whitelist is configured for a listener, only requests from the IP addresses that are added to the whitelist are distributed by the listener. If a whitelist is enabled but no IP address is added to the whitelist, the listener forwards all requests.
        # *   **black**: All requests from the IP addresses or CIDR blocks in the ACL are rejected. Blacklists are suitable for scenarios in which you want to deny access from specific IP addresses to an application. If a blacklist is enabled but no IP address is added to the blacklist, the listener forwards all requests.
        self.acl_type = acl_type
        # The ID of the listener.
        self.listener_id = listener_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.acl_type is not None:
            result['AclType'] = self.acl_type

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AclType') is not None:
            self.acl_type = m.get('AclType')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        return self

class GetAclResponseBodyAclEntries(DaraModel):
    def __init__(
        self,
        entry: str = None,
        entry_description: str = None,
    ):
        # An IP address entry (192.168.XX.XX) or a CIDR block entry (10.0.XX.XX/24).
        self.entry = entry
        # The description of the ACL entry.
        self.entry_description = entry_description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry is not None:
            result['Entry'] = self.entry

        if self.entry_description is not None:
            result['EntryDescription'] = self.entry_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')

        if m.get('EntryDescription') is not None:
            self.entry_description = m.get('EntryDescription')

        return self

