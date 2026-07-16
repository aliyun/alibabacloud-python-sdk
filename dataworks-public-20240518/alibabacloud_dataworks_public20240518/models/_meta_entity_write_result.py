# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MetaEntityWriteResult(DaraModel):
    def __init__(
        self,
        entity_type: str = None,
        error_message: str = None,
        id: str = None,
        name: str = None,
        success: bool = None,
    ):
        # The entity type.
        self.entity_type = entity_type
        # The error message if the operation fails for the entity.
        self.error_message = error_message
        # The entity ID.
        self.id = id
        # The entity name.
        self.name = name
        # Indicates whether the operation succeeded for the entity.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

