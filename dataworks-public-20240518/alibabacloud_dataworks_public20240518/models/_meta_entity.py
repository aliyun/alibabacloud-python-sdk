# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class MetaEntity(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        comment: str = None,
        create_time: int = None,
        custom_attributes: Dict[str, List[str]] = None,
        entity_type: str = None,
        id: str = None,
        meta_entity_def: main_models.MetaEntityDef = None,
        modify_time: int = None,
        name: str = None,
        owner_id: str = None,
    ):
        # Entity attributes. Complex values are represented as JSON strings.
        self.attributes = attributes
        # Comment
        self.comment = comment
        # Creation time as a millisecond-level timestamp
        self.create_time = create_time
        # Custom attribute values. The key is the custom attribute identifier. The value is a list of attribute values.
        self.custom_attributes = custom_attributes
        # Entity type
        self.entity_type = entity_type
        # Entity ID
        self.id = id
        # Attribute definition of the custom entity.
        # >Notice: For historical reasons, this property is not returned and its value is empty. We recommend that you use the GetMetaEntityDef API to obtain the entity type definition.
        self.meta_entity_def = meta_entity_def
        # Modification time as a millisecond-level timestamp
        self.modify_time = modify_time
        # Entity name
        self.name = name
        # Owner ID. The default value is the Alibaba Cloud UID of the creator.
        self.owner_id = owner_id

    def validate(self):
        if self.meta_entity_def:
            self.meta_entity_def.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.id is not None:
            result['Id'] = self.id

        if self.meta_entity_def is not None:
            result['MetaEntityDef'] = self.meta_entity_def.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetaEntityDef') is not None:
            temp_model = main_models.MetaEntityDef()
            self.meta_entity_def = temp_model.from_map(m.get('MetaEntityDef'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self

