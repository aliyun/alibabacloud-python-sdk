# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAppDomainCertificateRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        certificate_name: str = None,
        certificate_type: str = None,
        domain_name: str = None,
        private_key: str = None,
        public_key: str = None,
    ):
        self.biz_id = biz_id
        self.certificate_name = certificate_name
        self.certificate_type = certificate_type
        self.domain_name = domain_name
        self.private_key = private_key
        self.public_key = public_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        return self

