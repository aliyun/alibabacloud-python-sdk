# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveEntityTagsShrinkRequest(DaraModel):
    def __init__(
        self,
        qualified_name: str = None,
        tag_keys_shrink: str = None,
    ):
        # The unique identifier of the entity. Example: maxcompute-table.projectA.tableA.
        # 
        # This parameter is required.
        self.qualified_name = qualified_name
        # The tag keys.
        # 
        # This parameter is required.
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')

        return self

