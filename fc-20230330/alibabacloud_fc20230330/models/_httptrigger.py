# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HTTPTrigger(DaraModel):
    def __init__(
        self,
        url_internet: str = None,
        url_intranet: str = None,
    ):
        self.url_internet = url_internet
        self.url_intranet = url_intranet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url_internet is not None:
            result['urlInternet'] = self.url_internet

        if self.url_intranet is not None:
            result['urlIntranet'] = self.url_intranet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('urlInternet') is not None:
            self.url_internet = m.get('urlInternet')

        if m.get('urlIntranet') is not None:
            self.url_intranet = m.get('urlIntranet')

        return self

