# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOAuthAuthorizationSessionRequest(DaraModel):
    def __init__(
        self,
        session_uri: str = None,
    ):
        # The authorization session URI.
        # 
        # > Returned by the FetchOAuthAuthenticationToken call.
        # 
        # This parameter is required.
        self.session_uri = session_uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_uri is not None:
            result['sessionUri'] = self.session_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionUri') is not None:
            self.session_uri = m.get('sessionUri')

        return self

