# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportKeyMaterialRequest(DaraModel):
    def __init__(
        self,
        encrypted_key_material: str = None,
        import_token: str = None,
        key_id: str = None,
        key_material_expire_unix: int = None,
    ):
        # The key material encrypted with the public key returned by **GetParametersForImport**, and then Base64-encoded.
        # 
        # This parameter is required.
        self.encrypted_key_material = encrypted_key_material
        # The import token obtained by calling **GetParametersForImport**.
        # 
        # This parameter is required.
        self.import_token = import_token
        # The ID of the CMK to be imported.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The time when the key material expires.
        # 
        # If this parameter is not specified or set this parameter to 0, the key material does not expire.
        # 
        # > The value cannot be earlier than the time when the operation is called (based on the server time).
        # 
        # This parameter is required.
        self.key_material_expire_unix = key_material_expire_unix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypted_key_material is not None:
            result['EncryptedKeyMaterial'] = self.encrypted_key_material

        if self.import_token is not None:
            result['ImportToken'] = self.import_token

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_material_expire_unix is not None:
            result['KeyMaterialExpireUnix'] = self.key_material_expire_unix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedKeyMaterial') is not None:
            self.encrypted_key_material = m.get('EncryptedKeyMaterial')

        if m.get('ImportToken') is not None:
            self.import_token = m.get('ImportToken')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyMaterialExpireUnix') is not None:
            self.key_material_expire_unix = m.get('KeyMaterialExpireUnix')

        return self

