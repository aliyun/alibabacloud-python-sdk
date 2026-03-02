# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PdpSlsLogInfo(DaraModel):
    def __init__(
        self,
        sls_url: str = None,
    ):
        self.sls_url = sls_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sls_url is not None:
            result['slsUrl'] = self.sls_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('slsUrl') is not None:
            self.sls_url = m.get('slsUrl')

        return self

