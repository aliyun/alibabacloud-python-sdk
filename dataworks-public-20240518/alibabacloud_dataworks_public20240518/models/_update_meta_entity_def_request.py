# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class UpdateMetaEntityDefRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        entity_type: str = None,
        new_attribute_defs: List[main_models.MetaEntityAttributeDef] = None,
        update_attribute_defs: List[main_models.MetaEntityAttributeDef] = None,
    ):
        # The new description.
        self.description = description
        # The new display name. The maximum length is 32 characters.
        self.display_name = display_name
        # The entity type.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The new attribute definitions. New attributes must be optional.
        self.new_attribute_defs = new_attribute_defs
        # The updates to existing attribute definitions. You can modify only the display name and description. You can also add enumerated values for attributes of the ENUM type.
        self.update_attribute_defs = update_attribute_defs

    def validate(self):
        if self.new_attribute_defs:
            for v1 in self.new_attribute_defs:
                 if v1:
                    v1.validate()
        if self.update_attribute_defs:
            for v1 in self.update_attribute_defs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        result['NewAttributeDefs'] = []
        if self.new_attribute_defs is not None:
            for k1 in self.new_attribute_defs:
                result['NewAttributeDefs'].append(k1.to_map() if k1 else None)

        result['UpdateAttributeDefs'] = []
        if self.update_attribute_defs is not None:
            for k1 in self.update_attribute_defs:
                result['UpdateAttributeDefs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        self.new_attribute_defs = []
        if m.get('NewAttributeDefs') is not None:
            for k1 in m.get('NewAttributeDefs'):
                temp_model = main_models.MetaEntityAttributeDef()
                self.new_attribute_defs.append(temp_model.from_map(k1))

        self.update_attribute_defs = []
        if m.get('UpdateAttributeDefs') is not None:
            for k1 in m.get('UpdateAttributeDefs'):
                temp_model = main_models.MetaEntityAttributeDef()
                self.update_attribute_defs.append(temp_model.from_map(k1))

        return self

