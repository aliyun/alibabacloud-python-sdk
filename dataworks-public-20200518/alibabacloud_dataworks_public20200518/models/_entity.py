# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Entity(DaraModel):
    def __init__(
        self,
        entity_content: Dict[str, Any] = None,
        qualified_name: str = None,
        tenant_id: int = None,
    ):
        # The properties of the entity, including:
        # 
        # *   **entityType**: The type of the entity. Examples: maxcompute-table and emr-table.
        # *   **name**: the name of the entity.
        # *   **projectName**: the name of the MaxCompute project.
        self.entity_content = entity_content
        # The unique identifier of the entity. Example: maxcompute-table.projectA.tableB.
        self.qualified_name = qualified_name
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_content is not None:
            result['EntityContent'] = self.entity_content

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityContent') is not None:
            self.entity_content = m.get('EntityContent')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

