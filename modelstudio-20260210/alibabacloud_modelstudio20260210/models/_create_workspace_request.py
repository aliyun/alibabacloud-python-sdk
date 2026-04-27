# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkspaceRequest(DaraModel):
    def __init__(
        self,
        service_site: str = None,
        workspace_name: str = None,
    ):
        self.service_site = service_site
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_site is not None:
            result['serviceSite'] = self.service_site

        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceSite') is not None:
            self.service_site = m.get('serviceSite')

        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')

        return self

