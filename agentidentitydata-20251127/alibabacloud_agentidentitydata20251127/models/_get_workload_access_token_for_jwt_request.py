# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetWorkloadAccessTokenForJWTRequest(DaraModel):
    def __init__(
        self,
        user_token: str = None,
        workload_identity_name: str = None,
    ):
        self.user_token = user_token
        self.workload_identity_name = workload_identity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_token is not None:
            result['UserToken'] = self.user_token

        if self.workload_identity_name is not None:
            result['WorkloadIdentityName'] = self.workload_identity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserToken') is not None:
            self.user_token = m.get('UserToken')

        if m.get('WorkloadIdentityName') is not None:
            self.workload_identity_name = m.get('WorkloadIdentityName')

        return self

