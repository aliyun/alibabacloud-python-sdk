# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkloadAccessTokenForUserIdRequest(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        workload_identity_name: str = None,
    ):
        self.user_id = user_id
        self.workload_identity_name = workload_identity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workload_identity_name is not None:
            result['WorkloadIdentityName'] = self.workload_identity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkloadIdentityName') is not None:
            self.workload_identity_name = m.get('WorkloadIdentityName')

        return self

