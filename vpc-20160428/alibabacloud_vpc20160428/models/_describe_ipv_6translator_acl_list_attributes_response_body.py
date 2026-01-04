# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeIPv6TranslatorAclListAttributesResponseBody(DaraModel):
    def __init__(
        self,
        acl_entries: main_models.DescribeIPv6TranslatorAclListAttributesResponseBodyAclEntries = None,
        acl_id: str = None,
        acl_name: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The ACLs.
        self.acl_entries = acl_entries
        # The ACL ID.
        self.acl_id = acl_id
        # The name of the ACL.
        self.acl_name = acl_name
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.acl_entries:
            self.acl_entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_entries is not None:
            result['AclEntries'] = self.acl_entries.to_map()

        if self.acl_id is not None:
            result['AclId'] = self.acl_id

        if self.acl_name is not None:
            result['AclName'] = self.acl_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntries') is not None:
            temp_model = main_models.DescribeIPv6TranslatorAclListAttributesResponseBodyAclEntries()
            self.acl_entries = temp_model.from_map(m.get('AclEntries'))

        if m.get('AclId') is not None:
            self.acl_id = m.get('AclId')

        if m.get('AclName') is not None:
            self.acl_name = m.get('AclName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIPv6TranslatorAclListAttributesResponseBodyAclEntries(DaraModel):
    def __init__(
        self,
        acl_entry: List[main_models.DescribeIPv6TranslatorAclListAttributesResponseBodyAclEntriesAclEntry] = None,
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
                temp_model = main_models.DescribeIPv6TranslatorAclListAttributesResponseBodyAclEntriesAclEntry()
                self.acl_entry.append(temp_model.from_map(k1))

        return self

class DescribeIPv6TranslatorAclListAttributesResponseBodyAclEntriesAclEntry(DaraModel):
    def __init__(
        self,
        acl_entry_comment: str = None,
        acl_entry_id: str = None,
        acl_entry_ip: str = None,
    ):
        # The remarks of the ACL entry.
        self.acl_entry_comment = acl_entry_comment
        # The ID of the ACL entry.
        self.acl_entry_id = acl_entry_id
        # The IP address specified in the ACL entry.
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

        if self.acl_entry_id is not None:
            result['AclEntryId'] = self.acl_entry_id

        if self.acl_entry_ip is not None:
            result['AclEntryIp'] = self.acl_entry_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEntryComment') is not None:
            self.acl_entry_comment = m.get('AclEntryComment')

        if m.get('AclEntryId') is not None:
            self.acl_entry_id = m.get('AclEntryId')

        if m.get('AclEntryIp') is not None:
            self.acl_entry_ip = m.get('AclEntryIp')

        return self

