# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDBMiniEngineVersionsRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dedicated_host_group_id: str = None,
        engine: str = None,
        engine_version: str = None,
        minor_version_tag: str = None,
        node_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        storage_type: str = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.dedicated_host_group_id = dedicated_host_group_id
        self.engine = engine
        self.engine_version = engine_version
        self.minor_version_tag = minor_version_tag
        self.node_type = node_type
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.minor_version_tag is not None:
            result['MinorVersionTag'] = self.minor_version_tag

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('MinorVersionTag') is not None:
            self.minor_version_tag = m.get('MinorVersionTag')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

