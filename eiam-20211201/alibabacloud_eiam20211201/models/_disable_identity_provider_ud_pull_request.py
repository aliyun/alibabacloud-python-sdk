# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableIdentityProviderUdPullRequest(DaraModel):
    def __init__(
        self,
        identity_provider_id: str = None,
        instance_id: str = None,
    ):
        # Identity provider ID.
        # 
        # This parameter is required.
        self.identity_provider_id = identity_provider_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_provider_id is not None:
            result['IdentityProviderId'] = self.identity_provider_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityProviderId') is not None:
            self.identity_provider_id = m.get('IdentityProviderId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

