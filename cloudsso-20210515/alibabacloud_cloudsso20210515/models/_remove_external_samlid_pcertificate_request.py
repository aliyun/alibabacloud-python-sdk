# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveExternalSAMLIdPCertificateRequest(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        directory_id: str = None,
    ):
        # The ID of the certificate.
        # 
        # You can call the [ListExternalSAMLIdPCertificates](https://help.aliyun.com/document_detail/341629.html) operation to query the IDs of certificates.
        self.certificate_id = certificate_id
        # The ID of the directory.
        self.directory_id = directory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        return self

