# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateMetaEntityDefRequest(DaraModel):
    def __init__(
        self,
        attribute_defs: List[main_models.MetaEntityAttributeDef] = None,
        description: str = None,
        display_name: str = None,
        extend: str = None,
        name: str = None,
    ):
        # The attribute definition list for custom entities. This parameter cannot be specified when extend is set to TABLE.
        self.attribute_defs = attribute_defs
        # The description.
        self.description = description
        # The display name, up to 32 characters.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The extension mode. Valid values:
        # 
        # - NONE: default value. Indicates a custom entity with freely defined attributes.
        # - TABLE: indicates an extended table type. This type integrates in the same way as existing table types in DataWorks Data Map. You do not need to provide attribute definitions and can create corresponding Database/Table objects.
        self.extend = extend
        # The name of the type definition. Custom types must match `^[a-z0-9][a-z0-9_]*$`. Extended table types must match `^[a-z0-9][a-z0-9_]*-table$`.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.attribute_defs:
            for v1 in self.attribute_defs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeDefs'] = []
        if self.attribute_defs is not None:
            for k1 in self.attribute_defs:
                result['AttributeDefs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_defs = []
        if m.get('AttributeDefs') is not None:
            for k1 in m.get('AttributeDefs'):
                temp_model = main_models.MetaEntityAttributeDef()
                self.attribute_defs.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

