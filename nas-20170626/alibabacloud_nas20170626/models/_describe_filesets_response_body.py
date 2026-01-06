# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeFilesetsResponseBody(DaraModel):
    def __init__(
        self,
        entries: main_models.DescribeFilesetsResponseBodyEntries = None,
        file_system_id: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The fileset information.
        self.entries = entries
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        self.file_system_id = file_system_id
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.entries:
            self.entries.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entries is not None:
            result['Entries'] = self.entries.to_map()

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entries') is not None:
            temp_model = main_models.DescribeFilesetsResponseBodyEntries()
            self.entries = temp_model.from_map(m.get('Entries'))

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFilesetsResponseBodyEntries(DaraModel):
    def __init__(
        self,
        entrie: List[main_models.DescribeFilesetsResponseBodyEntriesEntrie] = None,
    ):
        self.entrie = entrie

    def validate(self):
        if self.entrie:
            for v1 in self.entrie:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entrie'] = []
        if self.entrie is not None:
            for k1 in self.entrie:
                result['Entrie'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entrie = []
        if m.get('Entrie') is not None:
            for k1 in m.get('Entrie'):
                temp_model = main_models.DescribeFilesetsResponseBodyEntriesEntrie()
                self.entrie.append(temp_model.from_map(k1))

        return self

class DescribeFilesetsResponseBodyEntriesEntrie(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        file_count_usage: int = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_id: str = None,
        quota: main_models.DescribeFilesetsResponseBodyEntriesEntrieQuota = None,
        space_usage: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The time when the fileset was created.
        # 
        # The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time
        # Specifies whether to enable deletion protection to allow you to release the fileset by using the console or by calling the [DeleteFileset](https://help.aliyun.com/document_detail/2402263.html) operation. Valid values:
        # 
        # *   true: enables release protection.
        # *   false: disables release protection.
        # 
        # > This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The fileset description.
        self.description = description
        # The usage of the file quantity.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support this parameter.
        self.file_count_usage = file_count_usage
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-099394bd928c\\*\\*\\*\\*.
        # *   The IDs of CPFS for LINGJUN file systems must start with `bmcpfs-`. Example: bmcpfs-290w65p03ok64ya\\*\\*\\*\\*.
        self.file_system_id = file_system_id
        # The fileset path.
        self.file_system_path = file_system_path
        # The fileset ID.
        self.fset_id = fset_id
        # The quota information.
        # 
        # >  Only CPFS for Lingjun V2.7.0 and later support this parameter.
        self.quota = quota
        # The capacity usage. Unit: bytes.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support this parameter.
        self.space_usage = space_usage
        # The fileset status. Valid values:
        # 
        # *   CREATING: The fileset is being created.
        # *   CREATED: The fileset has been created and is running properly.
        # *   RELEASING: The fileset is being released.
        # *   RELEASED: The fileset has been deleted.
        self.status = status
        # The time when the fileset was last updated.
        # 
        # The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.update_time = update_time

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.description is not None:
            result['Description'] = self.description

        if self.file_count_usage is not None:
            result['FileCountUsage'] = self.file_count_usage

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.file_system_path is not None:
            result['FileSystemPath'] = self.file_system_path

        if self.fset_id is not None:
            result['FsetId'] = self.fset_id

        if self.quota is not None:
            result['Quota'] = self.quota.to_map()

        if self.space_usage is not None:
            result['SpaceUsage'] = self.space_usage

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileCountUsage') is not None:
            self.file_count_usage = m.get('FileCountUsage')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('FileSystemPath') is not None:
            self.file_system_path = m.get('FileSystemPath')

        if m.get('FsetId') is not None:
            self.fset_id = m.get('FsetId')

        if m.get('Quota') is not None:
            temp_model = main_models.DescribeFilesetsResponseBodyEntriesEntrieQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('SpaceUsage') is not None:
            self.space_usage = m.get('SpaceUsage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeFilesetsResponseBodyEntriesEntrieQuota(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        # The file quantity quota. Valid values:
        # 
        # *   Minimum value: 10000.
        # *   Maximum value: 10000000000.
        self.file_count_limit = file_count_limit
        # The capacity quota. Unit: bytes.
        # 
        # *   Minimum value: 10737418240 (10 GiB).
        # *   Step size: 1073741824 (1 GiB).
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

