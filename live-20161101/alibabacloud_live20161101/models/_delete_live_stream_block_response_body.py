# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveStreamBlockResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The result description. If the request was successful, ok is returned. If the request failed, the failure detail is returned.
        self.description = description
        # The request ID.
        self.request_id = request_id
        # The status. Valid values:
        # 
        # *   ok: The request was successful.
        # *   fail: The request failed.
        # 
        # >  If any parameter failed to be configured, the request failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

