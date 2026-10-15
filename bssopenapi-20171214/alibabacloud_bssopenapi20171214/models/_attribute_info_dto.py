# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class AttributeInfoDTO(DaraModel):
    def __init__(
        self,
        attribute_categories: List[str] = None,
        attribute_source: str = None,
        attribute_type: str = None,
        code: str = None,
        composite_attributes: List[main_models.BaseAttributeInfoDTO] = None,
        description: str = None,
        description_attributes: List[main_models.BaseAttributeInfoDTO] = None,
        name: str = None,
        operational_attribute_config: str = None,
        operational_attribute_type: str = None,
        sub_attributes: List[main_models.AttributeInfoDTO] = None,
        unit: str = None,
        value_type: str = None,
        values: List[main_models.AttributeValueInfoDTO] = None,
    ):
        # The property categories.
        self.attribute_categories = attribute_categories
        # The property source.
        self.attribute_source = attribute_source
        # The property type.
        self.attribute_type = attribute_type
        # The property code.
        self.code = code
        # The composite properties (basic information).
        self.composite_attributes = composite_attributes
        # The property description (translated).
        self.description = description
        # The description properties (basic information).
        self.description_attributes = description_attributes
        # The property name (translated).
        self.name = name
        # The O&M property configuration.
        self.operational_attribute_config = operational_attribute_config
        # The O&M property type.
        self.operational_attribute_type = operational_attribute_type
        # The sub-properties (complete information).
        self.sub_attributes = sub_attributes
        # The unit.
        self.unit = unit
        # The value type.
        self.value_type = value_type
        # The property value list.
        self.values = values

    def validate(self):
        if self.composite_attributes:
            for v1 in self.composite_attributes:
                 if v1:
                    v1.validate()
        if self.description_attributes:
            for v1 in self.description_attributes:
                 if v1:
                    v1.validate()
        if self.sub_attributes:
            for v1 in self.sub_attributes:
                 if v1:
                    v1.validate()
        if self.values:
            for v1 in self.values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_categories is not None:
            result['AttributeCategories'] = self.attribute_categories

        if self.attribute_source is not None:
            result['AttributeSource'] = self.attribute_source

        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type

        if self.code is not None:
            result['Code'] = self.code

        result['CompositeAttributes'] = []
        if self.composite_attributes is not None:
            for k1 in self.composite_attributes:
                result['CompositeAttributes'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        result['DescriptionAttributes'] = []
        if self.description_attributes is not None:
            for k1 in self.description_attributes:
                result['DescriptionAttributes'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.operational_attribute_config is not None:
            result['OperationalAttributeConfig'] = self.operational_attribute_config

        if self.operational_attribute_type is not None:
            result['OperationalAttributeType'] = self.operational_attribute_type

        result['SubAttributes'] = []
        if self.sub_attributes is not None:
            for k1 in self.sub_attributes:
                result['SubAttributes'].append(k1.to_map() if k1 else None)

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        result['Values'] = []
        if self.values is not None:
            for k1 in self.values:
                result['Values'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeCategories') is not None:
            self.attribute_categories = m.get('AttributeCategories')

        if m.get('AttributeSource') is not None:
            self.attribute_source = m.get('AttributeSource')

        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.composite_attributes = []
        if m.get('CompositeAttributes') is not None:
            for k1 in m.get('CompositeAttributes'):
                temp_model = main_models.BaseAttributeInfoDTO()
                self.composite_attributes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.description_attributes = []
        if m.get('DescriptionAttributes') is not None:
            for k1 in m.get('DescriptionAttributes'):
                temp_model = main_models.BaseAttributeInfoDTO()
                self.description_attributes.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperationalAttributeConfig') is not None:
            self.operational_attribute_config = m.get('OperationalAttributeConfig')

        if m.get('OperationalAttributeType') is not None:
            self.operational_attribute_type = m.get('OperationalAttributeType')

        self.sub_attributes = []
        if m.get('SubAttributes') is not None:
            for k1 in m.get('SubAttributes'):
                temp_model = main_models.AttributeInfoDTO()
                self.sub_attributes.append(temp_model.from_map(k1))

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        self.values = []
        if m.get('Values') is not None:
            for k1 in m.get('Values'):
                temp_model = main_models.AttributeValueInfoDTO()
                self.values.append(temp_model.from_map(k1))

        return self

