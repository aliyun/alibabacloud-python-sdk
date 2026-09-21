# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TraceSiteShrinkRequest(DaraModel):
    def __init__(
        self,
        body_shrink: str = None,
        context_shrink: str = None,
        cookies_shrink: str = None,
        headers_shrink: str = None,
        method: str = None,
        protocol: str = None,
        url: str = None,
    ):
        # The HTTP request body.
        self.body_shrink = body_shrink
        # The environment context. This parameter is optional.
        self.context_shrink = context_shrink
        # The cookie parameters.
        self.cookies_shrink = cookies_shrink
        # The request headers.
        self.headers_shrink = headers_shrink
        # The HTTP method.
        self.method = method
        # The HTTP protocol.
        self.protocol = protocol
        # The URL of the request.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_shrink is not None:
            result['Body'] = self.body_shrink

        if self.context_shrink is not None:
            result['Context'] = self.context_shrink

        if self.cookies_shrink is not None:
            result['Cookies'] = self.cookies_shrink

        if self.headers_shrink is not None:
            result['Headers'] = self.headers_shrink

        if self.method is not None:
            result['Method'] = self.method

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body_shrink = m.get('Body')

        if m.get('Context') is not None:
            self.context_shrink = m.get('Context')

        if m.get('Cookies') is not None:
            self.cookies_shrink = m.get('Cookies')

        if m.get('Headers') is not None:
            self.headers_shrink = m.get('Headers')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

