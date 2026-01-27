# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EncryptPasswordRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        directory_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        password: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The ID of the client. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The directory ID.
        self.directory_id = directory_id
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The office network ID.
        self.office_site_id = office_site_id
        # The password that you want to encrypt.
        # 
        # This parameter is required.
        self.password = password
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The session ID.
        # 
        # This parameter is required.
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

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.password is not None:
            result['Password'] = self.password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

