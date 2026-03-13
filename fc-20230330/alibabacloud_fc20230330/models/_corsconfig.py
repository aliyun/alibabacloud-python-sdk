# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CORSConfig(DaraModel):
    def __init__(
        self,
        allow_credentials: bool = None,
        allow_headers: List[str] = None,
        allow_methods: List[str] = None,
        allow_origins: List[str] = None,
        expose_headers: List[str] = None,
        max_age: int = None,
    ):
        self.allow_credentials = allow_credentials
        self.allow_headers = allow_headers
        self.allow_methods = allow_methods
        self.allow_origins = allow_origins
        self.expose_headers = expose_headers
        self.max_age = max_age

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_credentials is not None:
            result['allowCredentials'] = self.allow_credentials

        if self.allow_headers is not None:
            result['allowHeaders'] = self.allow_headers

        if self.allow_methods is not None:
            result['allowMethods'] = self.allow_methods

        if self.allow_origins is not None:
            result['allowOrigins'] = self.allow_origins

        if self.expose_headers is not None:
            result['exposeHeaders'] = self.expose_headers

        if self.max_age is not None:
            result['maxAge'] = self.max_age

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowCredentials') is not None:
            self.allow_credentials = m.get('allowCredentials')

        if m.get('allowHeaders') is not None:
            self.allow_headers = m.get('allowHeaders')

        if m.get('allowMethods') is not None:
            self.allow_methods = m.get('allowMethods')

        if m.get('allowOrigins') is not None:
            self.allow_origins = m.get('allowOrigins')

        if m.get('exposeHeaders') is not None:
            self.expose_headers = m.get('exposeHeaders')

        if m.get('maxAge') is not None:
            self.max_age = m.get('maxAge')

        return self

