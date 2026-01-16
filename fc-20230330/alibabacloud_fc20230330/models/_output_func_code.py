# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OutputFuncCode(DaraModel):
    def __init__(
        self,
        checksum: str = None,
        url: str = None,
    ):
        self.checksum = checksum
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checksum is not None:
            result['checksum'] = self.checksum

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

