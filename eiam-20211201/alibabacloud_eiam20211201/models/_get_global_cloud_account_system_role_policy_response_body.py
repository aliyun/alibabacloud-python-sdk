# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGlobalCloudAccountSystemRolePolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy_document: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.policy_document = policy_document
        # 本次请求的唯一标识。
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

