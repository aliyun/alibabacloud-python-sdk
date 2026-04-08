# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExternalServicesRequest(DaraModel):
    def __init__(
        self,
        importable_only: bool = None,
        limit: int = None,
        name_like: str = None,
        pai_workspace_id: str = None,
        source_type: str = None,
    ):
        self.importable_only = importable_only
        self.limit = limit
        self.name_like = name_like
        self.pai_workspace_id = pai_workspace_id
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.importable_only is not None:
            result['importableOnly'] = self.importable_only

        if self.limit is not None:
            result['limit'] = self.limit

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.pai_workspace_id is not None:
            result['paiWorkspaceId'] = self.pai_workspace_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('importableOnly') is not None:
            self.importable_only = m.get('importableOnly')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('paiWorkspaceId') is not None:
            self.pai_workspace_id = m.get('paiWorkspaceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        return self

