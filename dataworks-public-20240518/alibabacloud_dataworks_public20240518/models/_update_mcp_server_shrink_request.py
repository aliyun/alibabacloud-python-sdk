# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMcpServerShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_headers_shrink: str = None,
        name: str = None,
        transport: str = None,
        url: str = None,
        visibility: str = None,
        visibility_scope_shrink: str = None,
    ):
        self.custom_headers_shrink = custom_headers_shrink
        # This parameter is required.
        self.name = name
        self.transport = transport
        self.url = url
        self.visibility = visibility
        self.visibility_scope_shrink = visibility_scope_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_headers_shrink is not None:
            result['CustomHeaders'] = self.custom_headers_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.transport is not None:
            result['Transport'] = self.transport

        if self.url is not None:
            result['Url'] = self.url

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        if self.visibility_scope_shrink is not None:
            result['VisibilityScope'] = self.visibility_scope_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHeaders') is not None:
            self.custom_headers_shrink = m.get('CustomHeaders')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Transport') is not None:
            self.transport = m.get('Transport')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        if m.get('VisibilityScope') is not None:
            self.visibility_scope_shrink = m.get('VisibilityScope')

        return self

