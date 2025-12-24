# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSnapshotCallbackAuthRequest(DaraModel):
    def __init__(
        self,
        callback_auth_key: str = None,
        callback_req_auth: str = None,
        domain_name: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The custom key that is used for callback authentication.
        # 
        # This parameter is required.
        self.callback_auth_key = callback_auth_key
        # Specifies whether to enable callback authentication. Valid values:
        # 
        # *   **yes**: enables callback authentication.
        # *   **no**: disables callback authentication.
        # 
        # This parameter is required.
        self.callback_req_auth = callback_req_auth
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callback_auth_key is not None:
            result['CallbackAuthKey'] = self.callback_auth_key

        if self.callback_req_auth is not None:
            result['CallbackReqAuth'] = self.callback_req_auth

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackAuthKey') is not None:
            self.callback_auth_key = m.get('CallbackAuthKey')

        if m.get('CallbackReqAuth') is not None:
            self.callback_req_auth = m.get('CallbackReqAuth')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

