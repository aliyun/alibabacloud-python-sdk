# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessControlListAttributeResponseBody(DaraModel):
    def __init__(
        self,
        acl_entrys: main_models.DescribeAccessControlListAttributeResponseBodyAclEntrys = None,
        acl_id: str = None,
        acl_name: str = None,
        address_ipversion: str = None,
        request_id: str = None,
    ):
        # The information about the access control policy.
        self.acl_entrys = acl_entrys
        # The ID of the access control policy.
        self.acl_id = acl_id
        # The name of the access control policy.
        self.acl_name = acl_name
        # The IP protocol version. Valid values: **ipv4** and **ipv6**.
        self.address_ipversion = address_ipversion
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.acl_entrys:
            self.acl_entrys.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

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
        # The entry description.
        self.acl_entry_comment = acl_entry_comment
        # The ACL entry.
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
            result['AclEntryIp'] = self.acl_entry_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryComment') is not None:
            self.acl_entry_comment = m.get('AclEntryComment')

        if m.get('AclEntryIp') is not None:
            self.acl_entry_ip = m.get('AclEntryIp')

        return self

