# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateProjectRequest(DaraModel):
    def __init__(
        self,
        project_id: str = None,
        title: str = None,
    ):
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The new name of the project.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

