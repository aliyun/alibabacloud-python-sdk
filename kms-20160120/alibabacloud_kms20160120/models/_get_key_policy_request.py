# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKeyPolicyRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        policy_name: str = None,
    ):
        # The ID or Alibaba Cloud Resource Name (ARN) of the key.
        # 
        # > When you access a key in another Alibaba Cloud account, you must enter the ARN of the key. The ARN of a key is in the `acs:kms:${region}:${account}:key/${keyid}` format.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The name of the key policy. Only the static value default is supported.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

