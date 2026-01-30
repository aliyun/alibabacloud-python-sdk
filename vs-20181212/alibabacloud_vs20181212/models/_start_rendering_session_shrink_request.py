# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartRenderingSessionShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_id: str = None,
        client_params_shrink: str = None,
        patch_id: str = None,
        project_id: str = None,
    ):
        self.app_id = app_id
        # This parameter is required.
        self.client_id = client_id
        self.client_params_shrink = client_params_shrink
        self.patch_id = patch_id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_params_shrink is not None:
            result['ClientParams'] = self.client_params_shrink

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientParams') is not None:
            self.client_params_shrink = m.get('ClientParams')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

