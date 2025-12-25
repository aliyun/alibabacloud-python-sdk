# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpApiVersionConfig(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        header_name: str = None,
        query_name: str = None,
        scheme: str = None,
        version: str = None,
    ):
        self.enable = enable
        self.header_name = header_name
        self.query_name = query_name
        self.scheme = scheme
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.header_name is not None:
            result['headerName'] = self.header_name

        if self.query_name is not None:
            result['queryName'] = self.query_name

        if self.scheme is not None:
            result['scheme'] = self.scheme

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('headerName') is not None:
            self.header_name = m.get('headerName')

        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')

        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

