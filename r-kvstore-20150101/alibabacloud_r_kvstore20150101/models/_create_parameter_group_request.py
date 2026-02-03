# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateParameterGroupRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        engine_type: str = None,
        engine_version: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_group_desc: str = None,
        parameter_group_name: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The service category. Valid values:
        # 
        # *   **standard**: Community Edition
        # *   **enterprise**: Enhanced Edition (Tair)
        # 
        # This parameter is required.
        self.category = category
        # The engine type. Valid values:
        # 
        # *   **redis**: ApsaraDB for Redis Community Edition instance or Tair DRAM-based instance
        # *   **tair_pena**: Tair persistent memory-optimized instance
        # *   **tair_pdb**: Tair ESSD/SSD-based instance
        # 
        # This parameter is required.
        self.engine_type = engine_type
        # The compatible engine version. Valid values:
        # 
        # *   For ApsaraDB for Redis Community Edition instances, set the parameter to **5.0**, **6.0**, or **7.0**.
        # *   For Tair DRAM-based instances that are compatible with Redis 5.0, 6.0, or 7.0, set the parameter to **5.0**, **6.0**, or **7.0**.
        # *   For Tair persistent memory-optimized instances that are compatible with Redis 6.0, set the parameter to **1.0**.
        # *   For Tair ESSD-based instances that are compatible with Redis 6.0, set the parameter to **1.0**. For Tair SSD-based instances that are compatible with Redis 6.0, set the parameter to **2.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The description of the parameter template. The description must be 0 to 200 characters in length.
        self.parameter_group_desc = parameter_group_desc
        # The new name of the parameter template. The name must meet the following requirements:
        # 
        # *   The name can contain letters, digits, and underscores (_). It must start with a letter and cannot contain Chinese characters.
        # *   The name can be 8 to 64 characters in length.
        # 
        # This parameter is required.
        self.parameter_group_name = parameter_group_name
        # A JSON-formatted object that specifies the parameter-value pairs. Format: {"Parameter 1":"Value 1","Parameter 2":"Value 2"...}. The specified value overwrites the original content.
        # 
        # >  The parameters that can be added for different editions are displayed in the console.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
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

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

