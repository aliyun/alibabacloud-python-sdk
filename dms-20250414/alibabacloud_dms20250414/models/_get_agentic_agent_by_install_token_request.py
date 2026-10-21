# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgenticAgentByInstallTokenRequest(DaraModel):
    def __init__(
        self,
        install_token: str = None,
    ):
        # The one-time install token issued by IssueAgenticInstallToken. The token starts with dit_ followed by 40 URL-safe Base64 characters, making a total length of 44 characters.
        # 
        # This parameter is required.
        self.install_token = install_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.install_token is not None:
            result['InstallToken'] = self.install_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstallToken') is not None:
            self.install_token = m.get('InstallToken')

        return self

