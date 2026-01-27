# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendTokenCodeRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_os: str = None,
        client_version: str = None,
        end_user_id: str = None,
        login_token: str = None,
        office_site_id: str = None,
        session_id: str = None,
        token_code: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The operating system on which the client runs.
        self.client_os = client_os
        # The client version. If you use an Alibaba Cloud Workspace client, you can view the client version in the "About" dialog box on the client logon page.
        self.client_version = client_version
        # The username of the account.
        self.end_user_id = end_user_id
        # The logon token.
        self.login_token = login_token
        # The office network ID.
        self.office_site_id = office_site_id
        # The session ID.
        self.session_id = session_id
        # If two-factor authentication is enabled for clients in the Elastic Desktop Service (EDS) Enterprise console, the system will send a verification code to the user\\"s email address if it detects that the current logged-on user is at risk. This parameter is required if you set `CurrentStage` to `TokenVerify`.
        self.token_code = token_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_os is not None:
            result['ClientOS'] = self.client_os

        if self.client_version is not None:
            result['ClientVersion'] = self.client_version

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.token_code is not None:
            result['TokenCode'] = self.token_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientOS') is not None:
            self.client_os = m.get('ClientOS')

        if m.get('ClientVersion') is not None:
            self.client_version = m.get('ClientVersion')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TokenCode') is not None:
            self.token_code = m.get('TokenCode')

        return self

