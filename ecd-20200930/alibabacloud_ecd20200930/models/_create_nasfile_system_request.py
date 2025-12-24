# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNASFileSystemRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        encrypt_type: str = None,
        name: str = None,
        office_site_id: str = None,
        region_id: str = None,
        storage_type: str = None,
    ):
        # Description of the NAS file system.
        self.description = description
        # Whether the file system is encrypted. Uses KMS service-managed keys to encrypt the file system\\"s on-disk data. No decryption is required when reading and writing encrypted data. Possible values and their meanings:
        # 
        # - 0: Not encrypted.
        # - 1: Encrypted using NAS-managed keys.
        # 
        # Default value: 0
        self.encrypt_type = encrypt_type
        # Name of the NAS file system.
        # The file name must follow these rules:
        # - Length: 2 to 128 English or Chinese characters.
        # - Must start with an uppercase or lowercase letter or a Chinese character, cannot start with http:// or https://.
        # - Can include numbers, underscores (_), or hyphens (-).
        self.name = name
        # Workspace ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # Region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Storage specification type of the NAS file system. Allowed values:
        # 
        # - Capacity: Capacity type.
        # - Performance: Performance type.
        # 
        # Default value: Capacity
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

        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

