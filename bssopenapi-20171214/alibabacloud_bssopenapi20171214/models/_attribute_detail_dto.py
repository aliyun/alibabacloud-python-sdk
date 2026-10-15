# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class AttributeDetailDTO(DaraModel):
    def __init__(
        self,
        code: str = None,
        default_value: str = None,
        status: str = None,
        values: List[main_models.AttributeDetailDTOValues] = None,
    ):
        # The property code.
        self.code = code
        # The default value.
        self.default_value = default_value
        # The property status.
        self.status = status
        # The list of valid values for the property.
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

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.status is not None:
            result['Status'] = self.status

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.AttributeDetailDTOValues()
                self.values.append(temp_model.from_map(k1))

        return self



class AttributeDetailDTOValues(DaraModel):
    def __init__(
        self,
        cascading_attribute_values: List[main_models.AttributeDetailDTO] = None,
        value: str = None,
    ):
        # The list of cascading property values (recursive structure).
        self.cascading_attribute_values = cascading_attribute_values
        # The property value, which corresponds to the identifyKey in the property value definition.
        self.value = value

    def validate(self):
        if self.cascading_attribute_values:
            for v1 in self.cascading_attribute_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CascadingAttributeValues'] = []
        if self.cascading_attribute_values is not None:
            for k1 in self.cascading_attribute_values:
                result['CascadingAttributeValues'].append(k1.to_map() if k1 else None)

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cascading_attribute_values = []
        if m.get('CascadingAttributeValues') is not None:
            for k1 in m.get('CascadingAttributeValues'):
                temp_model = main_models.AttributeDetailDTO()
                self.cascading_attribute_values.append(temp_model.from_map(k1))

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

