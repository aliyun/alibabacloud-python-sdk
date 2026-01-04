# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLogStoreExistStatusResponseBody(DaraModel):
    def __init__(
        self,
        exist_status: bool = None,
        request_id: str = None,
    ):
        # Indicates whether a Logstore is created for Anti-DDoS Pro or Anti-DDoS Premium. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.exist_status = exist_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exist_status is not None:
            result['ExistStatus'] = self.exist_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistStatus') is not None:
            self.exist_status = m.get('ExistStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

