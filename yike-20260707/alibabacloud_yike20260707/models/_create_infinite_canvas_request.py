# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInfiniteCanvasRequest(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        production_id: str = None,
        title: str = None,
        workspace_id: str = None,
    ):
        # The cover URL.
        self.cover_url = cover_url
        # The project ID.
        self.production_id = production_id
        # The project title.
        # 
        # This parameter is required.
        self.title = title
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.title is not None:
            result['Title'] = self.title

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

