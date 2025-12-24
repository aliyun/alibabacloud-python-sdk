# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveRealtimeLogAuthorizedResponseBody(DaraModel):
    def __init__(
        self,
        authorized_status: str = None,
        request_id: str = None,
    ):
        # The authorization status. **true**: authorized **false**: not authorized
        self.authorized_status = authorized_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_status is not None:
            result['AuthorizedStatus'] = self.authorized_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedStatus') is not None:
            self.authorized_status = m.get('AuthorizedStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

