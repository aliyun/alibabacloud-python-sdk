# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPptTemplatesRequest(DaraModel):
    def __init__(
        self,
        career_id: int = None,
        colour_id: int = None,
        max_results: int = None,
        next_token: str = None,
        scene_id: int = None,
        style_id: int = None,
        workspace_id: str = None,
    ):
        self.career_id = career_id
        self.colour_id = colour_id
        self.max_results = max_results
        self.next_token = next_token
        self.scene_id = scene_id
        self.style_id = style_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.career_id is not None:
            result['CareerId'] = self.career_id

        if self.colour_id is not None:
            result['ColourId'] = self.colour_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.style_id is not None:
            result['StyleId'] = self.style_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CareerId') is not None:
            self.career_id = m.get('CareerId')

        if m.get('ColourId') is not None:
            self.colour_id = m.get('ColourId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StyleId') is not None:
            self.style_id = m.get('StyleId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

