# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachAppPolicyToIdentityResponseBody(DaraModel):
    def __init__(
        self,
        failed_policy_names: List[str] = None,
        non_exist_policy_names: List[str] = None,
        request_id: str = None,
    ):
        # The names of the policies that failed to be granted to the RAM user or RAM role.
        self.failed_policy_names = failed_policy_names
        # The names of the policies that were not found.
        self.non_exist_policy_names = non_exist_policy_names
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_policy_names is not None:
            result['FailedPolicyNames'] = self.failed_policy_names

        if self.non_exist_policy_names is not None:
            result['NonExistPolicyNames'] = self.non_exist_policy_names

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedPolicyNames') is not None:
            self.failed_policy_names = m.get('FailedPolicyNames')

        if m.get('NonExistPolicyNames') is not None:
            self.non_exist_policy_names = m.get('NonExistPolicyNames')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

