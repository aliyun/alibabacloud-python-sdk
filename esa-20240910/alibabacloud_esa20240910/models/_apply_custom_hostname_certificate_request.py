# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyCustomHostnameCertificateRequest(DaraModel):
    def __init__(
        self,
        hostname_id: int = None,
    ):
        # This parameter is required.
        self.hostname_id = hostname_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostname_id is not None:
            result['HostnameId'] = self.hostname_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostnameId') is not None:
            self.hostname_id = m.get('HostnameId')

        return self

