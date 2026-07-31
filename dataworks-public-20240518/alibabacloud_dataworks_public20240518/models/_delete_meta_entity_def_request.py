# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMetaEntityDefRequest(DaraModel):
    def __init__(
        self,
        entity_type: str = None,
        force: bool = None,
    ):
        # The entity type.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # Specifies whether to force delete the entity definition. Default value: false. Valid values:
        # 
        # - true: Automatically deletes all entity objects created under this entity type.
        # - false: Checks whether entity objects exist under this entity type. If objects exist, the deletion is failed.
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.force is not None:
            result['Force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        return self

