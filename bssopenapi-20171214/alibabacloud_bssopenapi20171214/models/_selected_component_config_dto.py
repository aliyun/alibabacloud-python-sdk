# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class SelectedComponentConfigDTO(DaraModel):
    def __init__(
        self,
        attribute_configs: List[main_models.SelectedComponentConfigDTOAttributeConfigs] = None,
        code: str = None,
        tag: str = None,
    ):
        # The property configuration list.
        self.attribute_configs = attribute_configs
        # The component code.
        self.code = code
        # The unique identifier of the component, used in multi-node and multi-disk scenarios.
        self.tag = tag

    def validate(self):
        if self.attribute_configs:
            for v1 in self.attribute_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeConfigs'] = []
        if self.attribute_configs is not None:
            for k1 in self.attribute_configs:
                result['AttributeConfigs'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_configs = []
        if m.get('AttributeConfigs') is not None:
            for k1 in m.get('AttributeConfigs'):
                temp_model = main_models.SelectedComponentConfigDTOAttributeConfigs()
                self.attribute_configs.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class SelectedComponentConfigDTOAttributeConfigs(DaraModel):
    def __init__(
        self,
        bounded_value: main_models.SelectedComponentConfigDTOAttributeConfigsBoundedValue = None,
        code: str = None,
        value: str = None,
    ):
        # The upper and lower bound values, used for bounded properties.
        self.bounded_value = bounded_value
        # The property code.
        self.code = code
        # The property value.
        self.value = value

    def validate(self):
        if self.bounded_value:
            self.bounded_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bounded_value is not None:
            result['BoundedValue'] = self.bounded_value.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundedValue') is not None:
            temp_model = main_models.SelectedComponentConfigDTOAttributeConfigsBoundedValue()
            self.bounded_value = temp_model.from_map(m.get('BoundedValue'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SelectedComponentConfigDTOAttributeConfigsBoundedValue(DaraModel):
    def __init__(
        self,
        lower_bound: main_models.SelectedComponentConfigDTOAttributeConfigsBoundedValueLowerBound = None,
        upper_bound: main_models.SelectedComponentConfigDTOAttributeConfigsBoundedValueUpperBound = None,
    ):
        # The lower bound.
        self.lower_bound = lower_bound
        # The upper bound.
        self.upper_bound = upper_bound

    def validate(self):
        if self.lower_bound:
            self.lower_bound.validate()
        if self.upper_bound:
            self.upper_bound.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lower_bound is not None:
            result['LowerBound'] = self.lower_bound.to_map()

        if self.upper_bound is not None:
            result['UpperBound'] = self.upper_bound.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LowerBound') is not None:
            temp_model = main_models.SelectedComponentConfigDTOAttributeConfigsBoundedValueLowerBound()
            self.lower_bound = temp_model.from_map(m.get('LowerBound'))

        if m.get('UpperBound') is not None:
            temp_model = main_models.SelectedComponentConfigDTOAttributeConfigsBoundedValueUpperBound()
            self.upper_bound = temp_model.from_map(m.get('UpperBound'))

        return self

class SelectedComponentConfigDTOAttributeConfigsBoundedValueUpperBound(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property value.
        self.value = value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class SelectedComponentConfigDTOAttributeConfigsBoundedValueLowerBound(DaraModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # The property code.
        self.code = code
        # The property value.
        self.value = value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

