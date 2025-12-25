# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetScenePreviewDataRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        preview_token: str = None,
        show_tag: bool = None,
    ):
        self.domain = domain
        self.enabled = enabled
        # This parameter is required.
        self.preview_token = preview_token
        self.show_tag = show_tag

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

        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token

        if self.show_tag is not None:
            result['ShowTag'] = self.show_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')

        if m.get('ShowTag') is not None:
            self.show_tag = m.get('ShowTag')

        return self

