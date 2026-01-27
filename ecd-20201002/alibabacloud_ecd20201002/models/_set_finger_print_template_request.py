# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetFingerPrintTemplateRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        client_token: str = None,
        description: str = None,
        encrypted_finger_print_template: str = None,
        encrypted_key: str = None,
        finger_print_template: str = None,
        login_token: str = None,
        password: str = None,
        region_id: str = None,
        session_id: str = None,
    ):
        # The client ID. The system generates a unique ID for each client.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The client token to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the node.
        self.description = description
        # The encrypted fingerprint template.
        self.encrypted_finger_print_template = encrypted_finger_print_template
        # The encryption key.
        self.encrypted_key = encrypted_key
        # The fingerprint template.
        self.finger_print_template = finger_print_template
        # The logon credentials.
        # 
        # This parameter is required.
        self.login_token = login_token
        # The password that you want to encrypt.
        # 
        # This parameter is required.
        self.password = password
        # The region ID
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.encrypted_finger_print_template is not None:
            result['EncryptedFingerPrintTemplate'] = self.encrypted_finger_print_template

        if self.encrypted_key is not None:
            result['EncryptedKey'] = self.encrypted_key

        if self.finger_print_template is not None:
            result['FingerPrintTemplate'] = self.finger_print_template

        if self.login_token is not None:
            result['LoginToken'] = self.login_token

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

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptedFingerPrintTemplate') is not None:
            self.encrypted_finger_print_template = m.get('EncryptedFingerPrintTemplate')

        if m.get('EncryptedKey') is not None:
            self.encrypted_key = m.get('EncryptedKey')

        if m.get('FingerPrintTemplate') is not None:
            self.finger_print_template = m.get('FingerPrintTemplate')

        if m.get('LoginToken') is not None:
            self.login_token = m.get('LoginToken')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

