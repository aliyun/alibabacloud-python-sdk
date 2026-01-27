# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangePasswordRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        end_user_id: str = None,
        login_token: str = None,
        new_password: str = None,
        office_site_id: str = None,
        old_password: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The user ID.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The new password.
        # 
        # This parameter is required.
        self.new_password = new_password
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The current password.
        # 
        # This parameter is required.
        self.old_password = old_password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.new_password is not None:
            result['NewPassword'] = self.new_password

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.old_password is not None:
            result['OldPassword'] = self.old_password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('NewPassword') is not None:
            self.new_password = m.get('NewPassword')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OldPassword') is not None:
            self.old_password = m.get('OldPassword')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

