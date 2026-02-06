# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateDownloadSecretKeyRequest(DaraModel):
    def __init__(
        self,
        app_decrypt_key: str = None,
        app_identification: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # A custom string of 16 to 32 characters in length. The string must contain uppercase letters, lowercase letters, and digits.
        # 
        # This parameter is required.
        self.app_decrypt_key = app_decrypt_key
        # The unique identifier of the app.
        # 
        # *   Android: the SHA-1 fingerprint of the keystore. The value is a string that contains a colon (:).
        # *   iOS: the bundle ID of the app.
        # *   Windows: the serial number in the digital signature certificate.
        # 
        # For more information about how to obtain the unique identifier of an app, see [Obtain the unique app identifier](~~86107#section-wtj-9d7-lg2~~).
        # 
        # This parameter is required.
        self.app_identification = app_identification
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_decrypt_key is not None:
            result['AppDecryptKey'] = self.app_decrypt_key

        if self.app_identification is not None:
            result['AppIdentification'] = self.app_identification

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDecryptKey') is not None:
            self.app_decrypt_key = m.get('AppDecryptKey')

        if m.get('AppIdentification') is not None:
            self.app_identification = m.get('AppIdentification')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

