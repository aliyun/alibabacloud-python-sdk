# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppLayoutShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        layout_shrink: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.client_token = client_token
        # This parameter is required.
        self.layout_shrink = layout_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.layout_shrink is not None:
            result['Layout'] = self.layout_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Layout') is not None:
            self.layout_shrink = m.get('Layout')

        return self

