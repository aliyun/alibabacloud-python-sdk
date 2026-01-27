# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindUserDesktopRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_type: str = None,
        force: bool = None,
        login_token: str = None,
        region_id: str = None,
        session_id: str = None,
        user_desktop_id: str = None,
    ):
        # The client ID.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client type.
        self.client_type = client_type
        # Specifies whether to enable forced unbinding.
        # 
        # Valid values:
        # 
        # *   true: Even when end users connect to cloud computers, the forced unbinding is still enforced.
        # *   false: Forced unbinding is only enforced when end users are disconnected from cloud computers.
        self.force = force
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The cloud computer ID.
        # 
        # This parameter is required.
        self.user_desktop_id = user_desktop_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.force is not None:
            result['Force'] = self.force

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.user_desktop_id is not None:
            result['UserDesktopId'] = self.user_desktop_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('UserDesktopId') is not None:
            self.user_desktop_id = m.get('UserDesktopId')

        return self

