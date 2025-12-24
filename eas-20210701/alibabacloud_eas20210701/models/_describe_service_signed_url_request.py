# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceSignedUrlRequest(DaraModel):
    def __init__(
        self,
        expire: int = None,
        internal: bool = None,
        type: str = None,
    ):
        # The period of time for which the URL expires.
        self.expire = expire
        # Specifies whether to use the VPC connection.
        self.internal = internal
        # The page type.
        # 
        # Valid values:
        # 
        # *   webview
        # *   monitor
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire is not None:
            result['Expire'] = self.expire

        if self.internal is not None:
            result['Internal'] = self.internal

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Internal') is not None:
            self.internal = m.get('Internal')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

