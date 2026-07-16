# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class UpdateRenderingInstanceConfigurationRequest(DaraModel):
    def __init__(
        self,
        configuration: List[main_models.UpdateRenderingInstanceConfigurationRequestConfiguration] = None,
        rendering_instance_id: str = None,
    ):
        # The configuration content.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The ID of the cloud application service instance.
        # 
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        if self.configuration:
            for v1 in self.configuration:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configuration'] = []
        if self.configuration is not None:
            for k1 in self.configuration:
                result['Configuration'].append(k1.to_map() if k1 else None)

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configuration = []
        if m.get('Configuration') is not None:
            for k1 in m.get('Configuration'):
                temp_model = main_models.UpdateRenderingInstanceConfigurationRequestConfiguration()
                self.configuration.append(temp_model.from_map(k1))

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

class UpdateRenderingInstanceConfigurationRequestConfiguration(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.UpdateRenderingInstanceConfigurationRequestConfigurationAttributes] = None,
        module_name: str = None,
    ):
        # The list of properties for the module.
        # 
        # This parameter is required.
        self.attributes = attributes
        # The name of the real device simulation module. Valid values include the following:
        # 
        # 1. ctl: control module
        # 
        # 2. prop: property module
        # 
        # 3. location: location module
        # 
        # 4. battery: battery module
        # 
        # 5. network: network module
        # 
        # 6. bluetooth: bluetooth module
        # 
        # 7. sim: SIM card module
        # 
        # 8. display: device module
        # 
        # 9. system: basic module
        # 
        # This parameter is required.
        self.module_name = module_name

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.UpdateRenderingInstanceConfigurationRequestConfigurationAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        return self

class UpdateRenderingInstanceConfigurationRequestConfigurationAttributes(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: Any = None,
    ):
        # The name of the property.
        # 
        # This parameter is required.
        self.name = name
        # The value of the property.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

