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
        storage_type: str = None,
    ):
        # The description of the NAS file system.
        self.description = description
        # The ID of the desktop group.
        # 
        # This parameter is required.
        self.desktop_group_id = desktop_group_id
        # Specifies whether to encrypt data in the NAS file system. You can use keys that are hosted by Key Management Service (KMS) to encrypt data in a file system. When you read and write the encrypted data, the data is automatically decrypted. Valid values:
        # 
        # *   0: does not encrypt data in the NAS file system.
        # *   1: encrypts data in the NAS file system by using a NAS-managed key. ` If you set  `FileSystemType`  to  `standard`  or  `extreme`, you can use a NAS-managed key to encrypt data in a NAS file system.`
        # *   2: encrypts data in the NAS file system by using a KMS-managed key. `If` you set FileSystemType`  to  `extreme`, you can use a KMS-managed key to encrypt data in a NAS file system.`
        # 
        # Default value: 0.
        self.encrypt_type = encrypt_type
        # The list of users.
        self.end_user_ids = end_user_ids
        # The name of the NAS file system.
        # 
        # This parameter is required.
        self.file_system_name = file_system_name
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The storage type of the NAS file system. Valid values:
        # 
        # *   Capacity
        # *   Performance
        # 
        # Default value: Capacity.
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

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

