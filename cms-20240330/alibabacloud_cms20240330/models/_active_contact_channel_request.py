# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActiveContactChannelRequest(DaraModel):
    def __init__(
        self,
        code: str = None,
        site: str = None,
    ):
        self.code = code
        self.site = site

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.site is not None:
            result['site'] = self.site

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('site') is not None:
            self.site = m.get('site')

        return self

