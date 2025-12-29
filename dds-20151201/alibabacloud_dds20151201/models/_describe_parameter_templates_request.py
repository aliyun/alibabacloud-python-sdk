# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParameterTemplatesRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role: str = None,
    ):
        # The database engine of the instance. Set the value to **MongoDB**.
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance. Valid values:
        # 
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/61933.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The role of the instance. Valid values:
        # 
        # 1. db:  a shard node.
        # 
        # 1. cs:  a Configserver node.
        # 
        # 1. mongos:  a mongos node.
        # 
        # 1. normal: a replica set node.
        # 
        # 1. physical: a standalone node.
        # 
        # default: normal
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role is not None:
            result['Role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        return self

