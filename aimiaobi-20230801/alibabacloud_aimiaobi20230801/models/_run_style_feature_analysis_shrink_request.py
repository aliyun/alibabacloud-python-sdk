# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunStyleFeatureAnalysisShrinkRequest(DaraModel):
    def __init__(
        self,
        contents_shrink: str = None,
        material_ids_shrink: str = None,
        workspace_id: str = None,
    ):
        self.contents_shrink = contents_shrink
        self.material_ids_shrink = material_ids_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contents_shrink is not None:
            result['Contents'] = self.contents_shrink

        if self.material_ids_shrink is not None:
            result['MaterialIds'] = self.material_ids_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents_shrink = m.get('Contents')

        if m.get('MaterialIds') is not None:
            self.material_ids_shrink = m.get('MaterialIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

