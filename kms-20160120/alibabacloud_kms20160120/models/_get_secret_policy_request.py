# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecretPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_name: str = None,
        secret_name: str = None,
    ):
        # The name of the credential policy. Only the static field default is supported.
        self.policy_name = policy_name
        # The name or Alibaba Cloud Resource Name (ARN) of the credential.
        # 
        # > If you access a credential that belongs to another Alibaba Cloud account, you must specify the ARN of the credential. The ARN of a credential must be in the `acs:kms:${region}:${account}:secret/${secret-name}` format.
        # 
        # This parameter is required.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

