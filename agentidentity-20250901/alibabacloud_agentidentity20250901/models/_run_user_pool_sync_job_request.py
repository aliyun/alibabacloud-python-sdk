# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunUserPoolSyncJobRequest(DaraModel):
    def __init__(
        self,
        identity_provider_type: str = None,
        max_sync_users: str = None,
        user_pool_name: str = None,
    ):
        self.identity_provider_type = identity_provider_type
        self.max_sync_users = max_sync_users
        self.user_pool_name = user_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.max_sync_users is not None:
            result['MaxSyncUsers'] = self.max_sync_users

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('MaxSyncUsers') is not None:
            self.max_sync_users = m.get('MaxSyncUsers')

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        return self

