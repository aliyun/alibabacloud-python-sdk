# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class TransportEncryptionInfo(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.TransportCertificateInfo] = None,
        deploy_error: str = None,
        deploy_status: str = None,
        http_2enabled: bool = None,
        tls_policy: str = None,
    ):
        self.certificates = certificates
        self.deploy_error = deploy_error
        self.deploy_status = deploy_status
        self.http_2enabled = http_2enabled
        self.tls_policy = tls_policy

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['certificates'].append(k1.to_map() if k1 else None)

        if self.deploy_error is not None:
            result['deployError'] = self.deploy_error

        if self.deploy_status is not None:
            result['deployStatus'] = self.deploy_status

        if self.http_2enabled is not None:
            result['http2Enabled'] = self.http_2enabled

        if self.tls_policy is not None:
            result['tlsPolicy'] = self.tls_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('certificates') is not None:
            for k1 in m.get('certificates'):
                temp_model = main_models.TransportCertificateInfo()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('deployError') is not None:
            self.deploy_error = m.get('deployError')

        if m.get('deployStatus') is not None:
            self.deploy_status = m.get('deployStatus')

        if m.get('http2Enabled') is not None:
            self.http_2enabled = m.get('http2Enabled')

        if m.get('tlsPolicy') is not None:
            self.tls_policy = m.get('tlsPolicy')

        return self

