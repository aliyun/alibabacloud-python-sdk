# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParameterGroupSupportParamRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        engine_type: str = None,
        engine_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The product category. Valid values:
        # * **standard**: Open-source Redis.
        # * **enterprise**: Tair (Redis Enterprise Edition).
        self.category = category
        # The engine type. Valid values:
        # * **redis**: Open-source Redis or memory-optimized Tair.
        # * **tair_pena**: Persistent memory-optimized Tair.
        # * **tair_pdb**: Disk-optimized Tair (ESSD/SSD).
        self.engine_type = engine_type
        # The compatible engine version. Valid values:
        # * Open-source Redis supports **5.0**, **6.0**, and **7.0**.
        # * Memory-optimized Tair is compatible with the Redis 5.0 and Redis 6.0 protocols. Set the value to **5.0** or **6.0**.
        # * Persistent memory-optimized Tair is compatible with the Redis 6.0 protocol. Set the value to **1.0**.
        # * Disk-optimized Tair (ESSD/SSD) is compatible with the Redis 6.0 protocol. Set the value to **1.0** for ESSD-based parameter templates or **2.0** for SSD-based parameter templates.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

