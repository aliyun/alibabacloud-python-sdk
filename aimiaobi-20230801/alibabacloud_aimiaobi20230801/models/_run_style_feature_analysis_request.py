# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RunStyleFeatureAnalysisRequest(DaraModel):
    def __init__(
        self,
        contents: List[str] = None,
        material_ids: List[int] = None,
        workspace_id: str = None,
    ):
        self.contents = contents
        self.material_ids = material_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contents is not None:
            result['Contents'] = self.contents

        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')

        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

