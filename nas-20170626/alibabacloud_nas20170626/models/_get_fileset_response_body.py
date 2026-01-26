# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class GetFilesetResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetFilesetResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetFilesetResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetFilesetResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        file_count_usage: int = None,
        file_system_id: str = None,
        file_system_path: str = None,
        fset_id: str = None,
        quota: main_models.GetFilesetResponseBodyDataQuota = None,
        space_usage: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # The time when the fileset was created.
        # 
        # Return format: `yyyy-MM-dd HH:mm:ss`
        self.create_time = create_time
        # Specifies whether the fileset is protected from being released through the console or the [DeleteFileset](https://help.aliyun.com/document_detail/2402263.html) operation.
        # 
        # *   true: Enables release protection. The fileset cannot be released.
        # *   false (default): Disables release protection. The fileset can be released.
        # 
        # >  This parameter can protect filesets only against manual releases, but not against automatic releases.
        self.deletion_protection = deletion_protection
        # The description of the fileset.
        self.description = description
        # The usage of the file quantity.
        # 
        # >  Only CPFS for LINGJUN V2.7.0 and later support this parameter.
        self.file_count_usage = file_count_usage
        # The ID of the file system.
        # 
        # *   The IDs of CPFS file systems must start with `cpfs-`. Example: cpfs-125487\\*\\*\\*\\*.
        # *   The IDs of CPFS for Lingjun file systems must start with `bmcpfs-`. Example: bmcpfs-0015\\*\\*\\*\\*.
        self.file_system_id = file_system_id
        # The directory of the fileset in the CPFS file system.
        self.file_system_path = file_system_path
        # The fileset ID.
        # 
        # >  This parameter is required for CPFS file systems.
        self.fset_id = fset_id
        # The quota information.
        # 
        # >  Only CPFS for Lingjun V2.7.0 and later support this parameter.
        self.quota = quota
        # The capacity usage. Unit: bytes.
        # 
        # >  Only CPFS for Lingjun V2.7.0 and later support this parameter.
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
        # Return format: `yyyy-MM-dd HH:mm:ss`
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
            temp_model = main_models.GetFilesetResponseBodyDataQuota()
            self.quota = temp_model.from_map(m.get('Quota'))

        if m.get('SpaceUsage') is not None:
            self.space_usage = m.get('SpaceUsage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetFilesetResponseBodyDataQuota(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        size_limit: int = None,
    ):
        # The file quantity quota. Valid values:
        # 
        # *   Minimum value: 10,000.
        # *   Maximum value: 10,000,000,000.
        self.file_count_limit = file_count_limit
        # The total quota capacity limit. Unit: bytes.
        # 
        # Valid values:
        # 
        # *   Minimum value: 10,737,418,240 (10 GiB).
        # *   Step size: 1,073,741,824 (1 GiB).
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

