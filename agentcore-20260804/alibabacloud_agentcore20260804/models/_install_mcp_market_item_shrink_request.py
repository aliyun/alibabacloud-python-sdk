# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InstallMcpMarketItemShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        client_token: str = None,
        template_version: str = None,
    ):
        # The MCP configuration submitted when installing the template. The configuration must comply with the input schema of the template.
        self.body_shrink = body_shrink
        # The reserved query request identifier. The console backend does not read this parameter and does not provide idempotency guarantees, such as deduplication or recovery of the original processing result, based on this identifier.
        self.client_token = client_token
        # The template version to install. You can query available versions by calling GetMcpMarketItem.
        # 
        # This parameter is required.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['body'] = self.body_shrink

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.template_version is not None:
            result['templateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body_shrink = m.get('body')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('templateVersion') is not None:
            self.template_version = m.get('templateVersion')

        return self

