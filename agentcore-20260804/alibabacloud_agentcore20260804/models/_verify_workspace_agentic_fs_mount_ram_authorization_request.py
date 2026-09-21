# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyWorkspaceAgenticFsMountRamAuthorizationRequest(DaraModel):
    def __init__(
        self,
        server: str = None,
    ):
        # The domain name of the target AccessPoint, obtained from the DomainName field of NAS ListAccessPoints. Do not include the protocol, port, or path.
        # 
        # This parameter is required.
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.server is not None:
            result['server'] = self.server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('server') is not None:
            self.server = m.get('server')

        return self

