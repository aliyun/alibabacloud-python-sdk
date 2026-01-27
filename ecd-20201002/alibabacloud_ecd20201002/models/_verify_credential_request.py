# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VerifyCredentialRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        credential: str = None,
        credential_type: str = None,
        encrypted_key: str = None,
        login_token: str = None,
        office_site_id: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The credential.
        # 
        # This parameter is required.
        self.credential = credential
        # The type of the logon credential that you want to clear.
        # 
        # Valid values:
        # 
        # *   MfaPasscode: the multi-factor verification code.
        # *   FingerPrint: the fingerprint.
        # *   Password: the password.
        self.credential_type = credential_type
        # The ID of the key that you want to encrypt.
        self.encrypted_key = encrypted_key
        # The logon token.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
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

        if self.credential is not None:
            result['Credential'] = self.credential

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Credential') is not None:
            self.credential = m.get('Credential')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

