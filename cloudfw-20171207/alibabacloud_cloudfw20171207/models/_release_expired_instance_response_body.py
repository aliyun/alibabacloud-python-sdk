# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleaseExpiredInstanceResponseBody(DaraModel):
    def __init__(
        self,
        http_status_code: int = None,
        release_status: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.http_status_code = http_status_code
        self.release_status = release_status
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.release_status is not None:
            result['ReleaseStatus'] = self.release_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('ReleaseStatus') is not None:
            self.release_status = m.get('ReleaseStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

