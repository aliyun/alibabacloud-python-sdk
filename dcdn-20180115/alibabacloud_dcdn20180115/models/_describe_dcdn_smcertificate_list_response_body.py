# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnSMCertificateListResponseBody(DaraModel):
    def __init__(
        self,
        certificate_list_model: main_models.DescribeDcdnSMCertificateListResponseBodyCertificateListModel = None,
        request_id: str = None,
    ):
        # The type of the certificate information.
        self.certificate_list_model = certificate_list_model
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateListModel') is not None:
            temp_model = main_models.DescribeDcdnSMCertificateListResponseBodyCertificateListModel()
            self.certificate_list_model = temp_model.from_map(m.get('CertificateListModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnSMCertificateListResponseBodyCertificateListModel(DaraModel):
    def __init__(
        self,
        cert_list: List[main_models.DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList] = None,
        count: int = None,
    ):
        # A list of certificates.
        self.cert_list = cert_list
        # The number of certificates that are returned.
        self.count = count

    def validate(self):
        if self.cert_list:
            for v1 in self.cert_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertList'] = []
        if self.cert_list is not None:
            for k1 in self.cert_list:
                result['CertList'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cert_list = []
        if m.get('CertList') is not None:
            for k1 in m.get('CertList'):
                temp_model = main_models.DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList()
                self.cert_list.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class DescribeDcdnSMCertificateListResponseBodyCertificateListModelCertList(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        cert_name: str = None,
        common: str = None,
        issuer: str = None,
    ):
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The common name of the certificate.
        self.common = common
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common is not None:
            result['Common'] = self.common

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        return self

