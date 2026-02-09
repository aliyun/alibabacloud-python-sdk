# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cors: bool = None,
        domain: str = None,
        dynamicfield: str = None,
        target_url: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.cors = cors
        self.domain = domain
        self.dynamicfield = dynamicfield
        # This parameter is required.
        self.target_url = target_url
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cors is not None:
            result['Cors'] = self.cors

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.dynamicfield is not None:
            result['Dynamicfield'] = self.dynamicfield

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Cors') is not None:
            self.cors = m.get('Cors')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Dynamicfield') is not None:
            self.dynamicfield = m.get('Dynamicfield')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

