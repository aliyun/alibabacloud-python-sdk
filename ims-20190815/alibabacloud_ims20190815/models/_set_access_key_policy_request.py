# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccessKeyPolicyRequest(DaraModel):
    def __init__(
        self,
        access_key_policy: str = None,
        user_access_key_id: str = None,
        user_principal_name: str = None,
    ):
        # The network access restriction policy.
        # 
        # A JSON-formatted string. For more information, see the AccessKeyPolicy structure description.
        # 
        # This parameter is required.
        self.access_key_policy = access_key_policy
        # The AccessKey ID.
        # 
        # This parameter is required.
        self.user_access_key_id = user_access_key_id
        # The logon name of the RAM user. 
        # 
        # If this parameter is left empty, the network access restriction policy is set for the specified AccessKey pair of the current user by default.
        self.user_principal_name = user_principal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_policy is not None:
            result['AccessKeyPolicy'] = self.access_key_policy

        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id

        if self.user_principal_name is not None:
            result['UserPrincipalName'] = self.user_principal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPolicy') is not None:
            self.access_key_policy = m.get('AccessKeyPolicy')

        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')

        if m.get('UserPrincipalName') is not None:
            self.user_principal_name = m.get('UserPrincipalName')

        return self

