# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProvisionExternalApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        scopes: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.scopes = scopes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.scopes is not None:
            result['Scopes'] = self.scopes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Scopes') is not None:
            self.scopes = m.get('Scopes')

        return self

