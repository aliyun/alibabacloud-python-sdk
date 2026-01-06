# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class UpdateLakeStorageRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        description: str = None,
        lake_storage_id: str = None,
        permissions: List[main_models.UpdateLakeStorageRequestPermissions] = None,
        region_id: str = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster that is associated with the lake storage.
        self.dbcluster_id = dbcluster_id
        # The description of the lake storage.
        self.description = description
        # The unique identifier of the lake storage.
        self.lake_storage_id = lake_storage_id
        # The permissions on the lake storage.
        self.permissions = permissions
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.description is not None:
            result['Description'] = self.description

        if self.lake_storage_id is not None:
            result['LakeStorageId'] = self.lake_storage_id

        result['Permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['Permissions'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LakeStorageId') is not None:
            self.lake_storage_id = m.get('LakeStorageId')

        self.permissions = []
        if m.get('Permissions') is not None:
            for k1 in m.get('Permissions'):
                temp_model = main_models.UpdateLakeStorageRequestPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class UpdateLakeStorageRequestPermissions(DaraModel):
    def __init__(
        self,
        account: str = None,
        read: bool = None,
        type: str = None,
        write: bool = None,
    ):
        # The account ID.
        # 
        # This parameter is required.
        self.account = account
        # The read permissions.
        # 
        # This parameter is required.
        self.read = read
        # The account type.
        # 
        # This parameter is required.
        self.type = type
        # The write permissions.
        # 
        # This parameter is required.
        self.write = write

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.read is not None:
            result['Read'] = self.read

        if self.type is not None:
            result['Type'] = self.type

        if self.write is not None:
            result['Write'] = self.write

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Read') is not None:
            self.read = m.get('Read')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Write') is not None:
            self.write = m.get('Write')

        return self

