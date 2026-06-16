# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentSpaceRequest(DaraModel):
    def __init__(
        self,
        cms_workspace: str = None,
        description: str = None,
        client_token: str = None,
    ):
        self.cms_workspace = cms_workspace
        self.description = description
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cms_workspace is not None:
            result['cmsWorkspace'] = self.cms_workspace

        if self.description is not None:
            result['description'] = self.description

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cmsWorkspace') is not None:
            self.cms_workspace = m.get('cmsWorkspace')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

