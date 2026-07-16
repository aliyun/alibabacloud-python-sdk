# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccessKeyPolicyResponseBody(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_policy: str = None,
        request_id: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The network access restriction policy.
        # 
        # A JSON-formatted string. For more information, see the AccessKeyPolicy structure description.
        self.access_key_policy = access_key_policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_policy is not None:
            result['AccessKeyPolicy'] = self.access_key_policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeyPolicy') is not None:
            self.access_key_policy = m.get('AccessKeyPolicy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

