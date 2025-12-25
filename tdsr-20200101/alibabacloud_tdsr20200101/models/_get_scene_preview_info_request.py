# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScenePreviewInfoRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        model_token: str = None,
    ):
        self.domain = domain
        self.enabled = enabled
        # This parameter is required.
        self.model_token = model_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.model_token is not None:
            result['ModelToken'] = self.model_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')

        return self

