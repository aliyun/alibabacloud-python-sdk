# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProjectDetailsLiteVO(DaraModel):
    def __init__(
        self,
        id: int = None,
        project_name: str = None,
    ):
        self.id = id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

