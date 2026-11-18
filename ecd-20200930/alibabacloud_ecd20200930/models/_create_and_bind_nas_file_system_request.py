# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAndBindNasFileSystemRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        desktop_group_id: str = None,
        encrypt_type: int = None,
        end_user_ids: List[str] = None,
        file_system_name: str = None,
        office_site_id: str = None,
        region_id: str = None,
        size_quota: int = None,
        storage_type: str = None,
    ):
        # The description of the NAS file system.
        self.description = description
        # The ID of the shared cloud desktop.
        self.desktop_group_id = desktop_group_id
        # Specifies whether the file system uses Key Management Service (KMS) managed keys to encrypt data at rest. No decryption is required when reading or writing encrypted data.
        # 
        # > When `FileSystemType` is set to `standard` or `extreme`, NAS-managed keys are supported. When `FileSystemType` is set to `extreme`, user-managed keys are supported.
        self.encrypt_type = encrypt_type
        # The list of user IDs.
        self.end_user_ids = end_user_ids
        # The name of the NAS file system.
        # 
        # This parameter is required.
        self.file_system_name = file_system_name
        # The ID of the office network.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The user VHD capacity tier in GiB. Valid values: 5, 20, 50, 100, and 500. Default value: 500.
        self.size_quota = size_quota
        # The storage type of the NAS file system.
        # 
        # This parameter is required.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.size_quota is not None:
            result['SizeQuota'] = self.size_quota

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SizeQuota') is not None:
            self.size_quota = m.get('SizeQuota')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

