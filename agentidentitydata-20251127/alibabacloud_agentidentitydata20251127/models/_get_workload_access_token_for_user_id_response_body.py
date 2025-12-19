# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkloadAccessTokenForUserIdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workload_access_token: str = None,
    ):
        self.request_id = request_id
        self.workload_access_token = workload_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workload_access_token is not None:
            result['WorkloadAccessToken'] = self.workload_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkloadAccessToken') is not None:
            self.workload_access_token = m.get('WorkloadAccessToken')

        return self

