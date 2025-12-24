# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOfficeSiteSsoStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sso_status: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether SSO is enabled.
        self.sso_status = sso_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sso_status is not None:
            result['SsoStatus'] = self.sso_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SsoStatus') is not None:
            self.sso_status = m.get('SsoStatus')

        return self

