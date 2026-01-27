# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UserCertificate(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        certificate: str = None,
        description: str = None,
        dns_names: List[str] = None,
        exp_time_unix: int = None,
        gmt_create_unix: int = None,
        gmt_modified_unix: int = None,
        name: str = None,
        private_key: str = None,
    ):
        self.cert_id = cert_id
        self.certificate = certificate
        self.description = description
        self.dns_names = dns_names
        self.exp_time_unix = exp_time_unix
        self.gmt_create_unix = gmt_create_unix
        self.gmt_modified_unix = gmt_modified_unix
        self.name = name
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.description is not None:
            result['Description'] = self.description

        if self.dns_names is not None:
            result['DnsNames'] = self.dns_names

        if self.exp_time_unix is not None:
            result['ExpTimeUnix'] = self.exp_time_unix

        if self.gmt_create_unix is not None:
            result['GmtCreateUnix'] = self.gmt_create_unix

        if self.gmt_modified_unix is not None:
            result['GmtModifiedUnix'] = self.gmt_modified_unix

        if self.name is not None:
            result['Name'] = self.name

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DnsNames') is not None:
            self.dns_names = m.get('DnsNames')

        if m.get('ExpTimeUnix') is not None:
            self.exp_time_unix = m.get('ExpTimeUnix')

        if m.get('GmtCreateUnix') is not None:
            self.gmt_create_unix = m.get('GmtCreateUnix')

        if m.get('GmtModifiedUnix') is not None:
            self.gmt_modified_unix = m.get('GmtModifiedUnix')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        return self

