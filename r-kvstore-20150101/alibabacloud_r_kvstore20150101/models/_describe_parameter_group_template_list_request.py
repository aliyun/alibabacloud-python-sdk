# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeParameterGroupTemplateListRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        character_type: str = None,
        engine_type: str = None,
        engine_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The product category. Valid values:
        # - **standard**: Redis Community Edition.
        # - **enterprise**: Tair (Enhanced Edition).
        # 
        # This parameter is required.
        self.category = category
        # The role type of the instance. Valid values:
        # * **logic**: cluster logical instance.
        # * **db**: cluster DB instance.
        # * **proxy**: cluster proxy instance.
        # * **cs**: cluster CS instance.
        # * **normal**: primary/secondary DB instance.
        self.character_type = character_type
        # The engine type. Valid values:
        # - **redis**: Redis Community Edition or Tair memory-optimized.
        # - **tair_pena**: Tair persistent memory-optimized.
        # - **tair_pdb**: Tair disk-based (ESSD/SSD).
        # 
        # This parameter is required.
        self.engine_type = engine_type
        # The compatible version. Valid values:
        # * Redis Community Edition supports **5.0**, **6.0**, and **7.0**.
        # * Tair memory-optimized instances are compatible with Redis 5.0, 6.0, and 7.0 protocols. Set this parameter to **5.0**, **6.0**, or **7.0**.
        # * Tair persistent memory-optimized instances are compatible with the Redis 6.0 protocol. Set this parameter to **1.0**.
        # * Tair disk-based (ESSD/SSD) instances are compatible with the Redis 6.0 protocol. To create an ESSD-based parameter template, set this parameter to **1.0**. To create an SSD-based parameter template, set this parameter to **2.0**.
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

        if self.character_type is not None:
            result['CharacterType'] = self.character_type

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

        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

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

