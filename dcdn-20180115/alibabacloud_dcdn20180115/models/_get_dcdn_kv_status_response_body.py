# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDcdnKvStatusResponseBody(DaraModel):
    def __init__(
        self,
        complete: bool = None,
        expire: str = None,
        request_id: str = None,
    ):
        # Specifies whether the configured key has taken effect on all points of presence (POPs).
        # 
        # *   **true**
        # *   **false**
        self.complete = complete
        # The timeout period of the configured key. The value is an absolute timestamp, such as 2023-09-11T15:39:44+08:00. This parameter is not returned if the key is permanently stored.
        self.expire = expire
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete is not None:
            result['Complete'] = self.complete

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Complete') is not None:
            self.complete = m.get('Complete')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

