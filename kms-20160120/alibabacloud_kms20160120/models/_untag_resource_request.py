# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourceRequest(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        key_id: str = None,
        secret_name: str = None,
        tag_keys: str = None,
    ):
        # The ID of the certificate.
        # 
        # > You must specify one and only one of the KeyId, SecretName, and CertificateId parameters.
        self.certificate_id = certificate_id
        # The ID of the key. This is the globally unique identifier (GUID) of the master key (CMK).
        # 
        # > You must specify one and only one of the KeyId, SecretName, and CertificateId parameters.
        self.key_id = key_id
        # The name of the credential.
        # 
        # > You must specify one and only one of the KeyId, SecretName, and CertificateId parameters.
        self.secret_name = secret_name
        # One or more tag keys. Separate multiple tag keys with commas (,).<br> You need to specify only tag keys, not tag values.<br> The tag key can be 1 to 128 bytes in length.<br><br>
        # 
        # This parameter is required.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

