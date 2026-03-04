# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ModuleVersionsValueComponentsValue(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        component_name: str = None,
        instance_property: List[main_models.ModuleVersionsValueComponentsValueInstanceProperty] = None,
        properties: Dict[str, main_models.ModuleVersionsValueComponentsValuePropertiesValue] = None,
        module_attr_status: int = None,
    ):
        self.component_code = component_code
        self.component_name = component_name
        self.instance_property = instance_property
        self.properties = properties
        self.module_attr_status = module_attr_status

    def validate(self):
        if self.instance_property:
            for v1 in self.instance_property:
                 if v1:
                    v1.validate()
        if self.properties:
            for v1 in self.properties.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        result['InstanceProperty'] = []
        if self.instance_property is not None:
            for k1 in self.instance_property:
                result['InstanceProperty'].append(k1.to_map() if k1 else None)

        result['Properties'] = {}
        if self.properties is not None:
            for k1, v1 in self.properties.items():
                result['Properties'][k1] = v1.to_map() if v1 else None

        if self.module_attr_status is not None:
            result['ModuleAttrStatus'] = self.module_attr_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        self.instance_property = []
        if m.get('InstanceProperty') is not None:
            for k1 in m.get('InstanceProperty'):
                temp_model = main_models.ModuleVersionsValueComponentsValueInstanceProperty()
                self.instance_property.append(temp_model.from_map(k1))

        self.properties = {}
        if m.get('Properties') is not None:
            for k1, v1 in m.get('Properties').items():
                temp_model = main_models.ModuleVersionsValueComponentsValuePropertiesValue()
                self.properties[k1] = temp_model.from_map(v1)

        if m.get('ModuleAttrStatus') is not None:
            self.module_attr_status = m.get('ModuleAttrStatus')

        return self

class ModuleVersionsValueComponentsValueInstanceProperty(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        value: str = None,
        values: List[main_models.ModuleVersionsValueComponentsValueInstancePropertyValues] = None,
    ):
        self.code = code
        self.name = name
        self.value = value
        self.values = values

    def validate(self):
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.ModuleVersionsValueComponentsValueInstancePropertyValues()
                self.values.append(temp_model.from_map(k1))

        return self

class ModuleVersionsValueComponentsValueInstancePropertyValues(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
        name: str = None,
    ):
        self.code = code
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

