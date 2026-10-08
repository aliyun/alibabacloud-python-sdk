# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertOrUpdateRegionRequest(DaraModel):
    def __init__(
        self,
        debug_enable: bool = None,
        description: str = None,
        id: int = None,
        mse_instance_id: str = None,
        region_name: str = None,
        region_tag: str = None,
        registry_type: str = None,
    ):
        # Specifies whether to enable remote debugging. Valid values:
        # 
        # - true: enables remote debugging.
        # 
        # - false: disables remote debugging.
        self.debug_enable = debug_enable
        # The description of the namespace. The description can be up to 128 characters in length.
        self.description = description
        # Specifies whether to create or modify the namespace. If this parameter is left empty or is set to 0, the namespace is created. Otherwise, the namespace is modified.
        self.id = id
        # The ID of the MSE registry.
        self.mse_instance_id = mse_instance_id
        # The name of the namespace. The name can be up to 63 characters in length.
        # 
        # This parameter is required.
        self.region_name = region_name
        # The ID of the namespace.
        # 
        # - The ID of a custom namespace is in the `Region ID:Namespace identifier` format. Example: cn-beijing:tdy218.
        # 
        # - The ID of the default namespace is in the `region ID` format. Example: cn-beijing.
        # 
        # This parameter is required.
        self.region_tag = region_tag
        # The type of the registry.
        # 
        # - default: the shared registry of Enterprise Distributed Application Service (EDAS)
        # 
        # - exclusive_mse: a Microservices Engine (MSE) registry
        self.registry_type = registry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.debug_enable is not None:
            result['DebugEnable'] = self.debug_enable

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.mse_instance_id is not None:
            result['MseInstanceId'] = self.mse_instance_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.region_tag is not None:
            result['RegionTag'] = self.region_tag

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugEnable') is not None:
            self.debug_enable = m.get('DebugEnable')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MseInstanceId') is not None:
            self.mse_instance_id = m.get('MseInstanceId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RegionTag') is not None:
            self.region_tag = m.get('RegionTag')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        return self

