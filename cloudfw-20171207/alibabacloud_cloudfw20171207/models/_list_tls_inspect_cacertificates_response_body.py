# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ListTlsInspectCACertificatesResponseBody(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.ListTlsInspectCACertificatesResponseBodyCertificates] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.certificates = certificates
        self.request_id = request_id
        self.total_count = total_count

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
        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.ListTlsInspectCACertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTlsInspectCACertificatesResponseBodyCertificates(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        alias_name: str = None,
        ca_cert_id: str = None,
        ca_cert_type: str = None,
        expiration_time: int = None,
        key_size: int = None,
        parent_ca_cert_id: str = None,
        sign_algorithm: str = None,
        status: str = None,
    ):
        self.algorithm = algorithm
        self.alias_name = alias_name
        self.ca_cert_id = ca_cert_id
        self.ca_cert_type = ca_cert_type
        self.expiration_time = expiration_time
        self.key_size = key_size
        self.parent_ca_cert_id = parent_ca_cert_id
        self.sign_algorithm = sign_algorithm
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.ca_cert_id is not None:
            result['CaCertId'] = self.ca_cert_id

        if self.ca_cert_type is not None:
            result['CaCertType'] = self.ca_cert_type

        if self.expiration_time is not None:
            result['ExpirationTime'] = self.expiration_time

        if self.key_size is not None:
            result['KeySize'] = self.key_size

        if self.parent_ca_cert_id is not None:
            result['ParentCaCertId'] = self.parent_ca_cert_id

        if self.sign_algorithm is not None:
            result['SignAlgorithm'] = self.sign_algorithm

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CaCertId') is not None:
            self.ca_cert_id = m.get('CaCertId')

        if m.get('CaCertType') is not None:
            self.ca_cert_type = m.get('CaCertType')

        if m.get('ExpirationTime') is not None:
            self.expiration_time = m.get('ExpirationTime')

        if m.get('KeySize') is not None:
            self.key_size = m.get('KeySize')

        if m.get('ParentCaCertId') is not None:
            self.parent_ca_cert_id = m.get('ParentCaCertId')

        if m.get('SignAlgorithm') is not None:
            self.sign_algorithm = m.get('SignAlgorithm')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

