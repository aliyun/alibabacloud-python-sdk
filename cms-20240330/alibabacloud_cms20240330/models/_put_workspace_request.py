# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutWorkspaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        sls_project: str = None,
    ):
        # Description of the workspace
        self.description = description
        # Display name of the workspace
        self.display_name = display_name
        # Name of the Log Service project
        # 
        # This parameter is required.
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.sls_project is not None:
            result['slsProject'] = self.sls_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')

        return self

