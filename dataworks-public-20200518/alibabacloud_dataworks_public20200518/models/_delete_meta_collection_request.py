# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMetaCollectionRequest(DaraModel):
    def __init__(
        self,
        qualified_name: str = None,
    ):
        # The unique identifier of the collection.
        # 
        # This parameter is required.
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

