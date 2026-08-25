# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class BatchCreateMetaEntitiesRequest(DaraModel):
    def __init__(
        self,
        entities: List[main_models.BatchCreateMetaEntitiesRequestEntities] = None,
    ):
        # The list of entities. A maximum of five entities are supported. All entities in the same batch must have the same entityType.
        # 
        # This parameter is required.
        self.entities = entities

    def validate(self):
        if self.entities:
            for v1 in self.entities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entities'] = []
        if self.entities is not None:
            for k1 in self.entities:
                result['Entities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entities = []
        if m.get('Entities') is not None:
            for k1 in m.get('Entities'):
                temp_model = main_models.BatchCreateMetaEntitiesRequestEntities()
                self.entities.append(temp_model.from_map(k1))

        return self

class BatchCreateMetaEntitiesRequestEntities(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        comment: str = None,
        custom_attributes: Dict[str, List[str]] = None,
        entity_type: str = None,
        name: str = None,
    ):
        # The entity attributes. Complex values must be serialized as JSON strings.
        self.attributes = attributes
        # The comment.
        self.comment = comment
        # The custom attribute values. The key is the custom attribute identifier, and the value currently supports only a single value.
        # <notice>The custom attributes used here must be created in advance by calling the CreateCustomAttribute operation. For example, after you call the API to create a custom attribute with the ID `custom-attribute:owner_name`, you can configure {\\"owner_name\\": [\\"Bob\\"]} here to complete the custom attribute configuration.</notice>
        self.custom_attributes = custom_attributes
        # The entity type. All entities in the same batch must have the same type. The following types are supported:
        # - Custom entity types, such as custom_entity-biz_api.
        # - Extension table types. If the metadata entity type custom_dw-table is registered, you can create objects of the corresponding database type custom_dw-database and table type custom_dw-table.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The entity name. The name can contain uppercase letters, lowercase letters, digits, and underscores (_). It must start with a letter and can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

