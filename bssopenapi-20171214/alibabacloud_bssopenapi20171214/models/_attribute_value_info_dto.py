# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class AttributeValueInfoDTO(DaraModel):
    def __init__(
        self,
        bounded_value: main_models.AttributeValueInfoDTOBoundedValue = None,
        code: str = None,
        default_value: str = None,
        description: str = None,
        description_attribute_values: List[main_models.AttributeValueInfoDTO] = None,
        identify_key: str = None,
        max: str = None,
        min: str = None,
        operation_tags: List[str] = None,
        step: str = None,
        sub_attribute_values: Dict[str, List[main_models.AttributeValueInfoDTO]] = None,
        value: str = None,
        value_name: str = None,
    ):
        # The upper and lower bounds.
        self.bounded_value = bounded_value
        # The property code.
        self.code = code
        # The default value.
        self.default_value = default_value
        # The description (translated).
        self.description = description
        # The description property values.
        self.description_attribute_values = description_attribute_values
        # The unique identifier.
        self.identify_key = identify_key
        # The maximum value.
        self.max = max
        # The minimum value.
        self.min = min
        # The operation tags.
        self.operation_tags = operation_tags
        # The step size.
        self.step = step
        # The sub-property values.
        self.sub_attribute_values = sub_attribute_values
        # The enum value.
        self.value = value
        # The value name (translated).
        self.value_name = value_name

    def validate(self):
        if self.bounded_value:
            self.bounded_value.validate()
        if self.description_attribute_values:
            for v1 in self.description_attribute_values:
                 if v1:
                    v1.validate()
        if self.sub_attribute_values:
            for v1 in self.sub_attribute_values.values():
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bounded_value is not None:
            result['BoundedValue'] = self.bounded_value.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        result['DescriptionAttributeValues'] = []
        if self.description_attribute_values is not None:
            for k1 in self.description_attribute_values:
                result['DescriptionAttributeValues'].append(k1.to_map() if k1 else None)

        if self.identify_key is not None:
            result['IdentifyKey'] = self.identify_key

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        if self.operation_tags is not None:
            result['OperationTags'] = self.operation_tags

        if self.step is not None:
            result['Step'] = self.step

        result['SubAttributeValues'] = {}
        if self.sub_attribute_values is not None:
            for k1, v1 in self.sub_attribute_values.items():
                l1 = []
                for k2 in v1:
                    l1.append(k2.to_map() if k2 else None)
                result['SubAttributeValues'][k1] = l1

        if self.value is not None:
            result['Value'] = self.value

        if self.value_name is not None:
            result['ValueName'] = self.value_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundedValue') is not None:
            temp_model = main_models.AttributeValueInfoDTOBoundedValue()
            self.bounded_value = temp_model.from_map(m.get('BoundedValue'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.description_attribute_values = []
        if m.get('DescriptionAttributeValues') is not None:
            for k1 in m.get('DescriptionAttributeValues'):
                temp_model = main_models.AttributeValueInfoDTO()
                self.description_attribute_values.append(temp_model.from_map(k1))

        if m.get('IdentifyKey') is not None:
            self.identify_key = m.get('IdentifyKey')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        if m.get('OperationTags') is not None:
            self.operation_tags = m.get('OperationTags')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        self.sub_attribute_values = {}
        if m.get('SubAttributeValues') is not None:
            for k1, v1 in m.get('SubAttributeValues').items():
                l1 = []
                for k2 in v1:
                    temp_model = main_models.AttributeValueInfoDTO()
                    l1.append(temp_model.from_map(k2))
                self.sub_attribute_values[k1] = l1

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueName') is not None:
            self.value_name = m.get('ValueName')

        return self

class AttributeValueInfoDTOBoundedValue(DaraModel):
    def __init__(
        self,
        lower_bound: List[main_models.AttributeValueInfoDTO] = None,
        upper_bound: List[main_models.AttributeValueInfoDTO] = None,
    ):
        # The lower bound list.
        self.lower_bound = lower_bound
        # The upper bound list.
        self.upper_bound = upper_bound

    def validate(self):
        if self.lower_bound:
            for v1 in self.lower_bound:
                 if v1:
                    v1.validate()
        if self.upper_bound:
            for v1 in self.upper_bound:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LowerBound'] = []
        if self.lower_bound is not None:
            for k1 in self.lower_bound:
                result['LowerBound'].append(k1.to_map() if k1 else None)

        result['UpperBound'] = []
        if self.upper_bound is not None:
            for k1 in self.upper_bound:
                result['UpperBound'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lower_bound = []
        if m.get('LowerBound') is not None:
            for k1 in m.get('LowerBound'):
                temp_model = main_models.AttributeValueInfoDTO()
                self.lower_bound.append(temp_model.from_map(k1))

        self.upper_bound = []
        if m.get('UpperBound') is not None:
            for k1 in m.get('UpperBound'):
                temp_model = main_models.AttributeValueInfoDTO()
                self.upper_bound.append(temp_model.from_map(k1))

        return self

