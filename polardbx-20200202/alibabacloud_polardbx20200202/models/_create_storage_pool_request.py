# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStoragePoolRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        storage_pool_dnlist: str = None,
        storage_pool_name: str = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.storage_pool_dnlist = storage_pool_dnlist
        self.storage_pool_name = storage_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.storage_pool_dnlist is not None:
            result['StoragePoolDNList'] = self.storage_pool_dnlist

        if self.storage_pool_name is not None:
            result['StoragePoolName'] = self.storage_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StoragePoolDNList') is not None:
            self.storage_pool_dnlist = m.get('StoragePoolDNList')

        if m.get('StoragePoolName') is not None:
            self.storage_pool_name = m.get('StoragePoolName')

        return self

