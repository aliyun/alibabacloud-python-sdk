# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagResourceRequest(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        key_id: str = None,
        secret_name: str = None,
        tags: str = None,
    ):
        # The ID of the certificate.
        # 
        # > You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.certificate_id = certificate_id
        # The ID of the customer master key (CMK). The ID must be globally unique.
        # 
        # > You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.key_id = key_id
        # The name of the secret.
        # 
        # > You can configure only one of the KeyId, SecretName, and CertificateId parameters.
        self.secret_name = secret_name
        # One or more tags that you want to add. The value is in the array format.
        # 
        # Tag attributes:
        # 
        # - TagKey: the tag key.
        # 
        # - TagValue: the tag value.
        # 
        # This parameter is required.
        self.tags = tags

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

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

