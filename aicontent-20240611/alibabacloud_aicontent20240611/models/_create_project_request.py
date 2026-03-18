# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateProjectRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        project_type: str = None,
    ):
        self.project_name = project_name
        self.project_type = project_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.project_type is not None:
            result['projectType'] = self.project_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('projectType') is not None:
            self.project_type = m.get('projectType')

        return self

