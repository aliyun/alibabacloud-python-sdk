# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRenderingProjectShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        project_id: str = None,
        project_name: str = None,
        session_attribs_shrink: str = None,
    ):
        # Project description
        self.description = description
        # Project ID
        # 
        # This parameter is required.
        self.project_id = project_id
        # Default naming rules:
        # 
        # 1. Length 1-128
        # 
        # 2. Lowercase letters, numbers, underscores (_), hyphens (-), and periods (.).
        # 
        # 3. The first and last characters must be letters or digits. At least one of ProjectName, SessionAttribs, or Description must be specified.
        self.project_name = project_name
        # Session attributes
        self.session_attribs_shrink = session_attribs_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.session_attribs_shrink is not None:
            result['SessionAttribs'] = self.session_attribs_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SessionAttribs') is not None:
            self.session_attribs_shrink = m.get('SessionAttribs')

        return self

