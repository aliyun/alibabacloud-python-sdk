# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeCertsResponseBody(DaraModel):
    def __init__(
        self,
        certs: List[main_models.DescribeCertsResponseBodyCerts] = None,
        request_id: str = None,
    ):
        # The certificate information about the website.
        self.certs = certs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certs:
            for v1 in self.certs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Certs'] = []
        if self.certs is not None:
            for k1 in self.certs:
                result['Certs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certs = []
        if m.get('Certs') is not None:
            for k1 in m.get('Certs'):
                temp_model = main_models.DescribeCertsResponseBodyCerts()
                self.certs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCertsResponseBodyCerts(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        common: str = None,
        domain_related: bool = None,
        end_date: str = None,
        id: int = None,
        issuer: str = None,
        name: str = None,
        start_date: str = None,
    ):
        # The global certificate ID, which is in the certificate ID-cn-hangzhou format. If the ID of the certificate is 123, CertIdentifier is 123-cn-hangzhou.
        self.cert_identifier = cert_identifier
        # The domain name that is associated with the certificate.
        self.common = common
        # Indicates whether the certificate is associated with the domain name. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.domain_related = domain_related
        # The expiration date of the certificate. The value is a string.
        self.end_date = end_date
        # The certificate ID.
        self.id = id
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer
        # The name of the certificate.
        self.name = name
        # The issuance date of the certificate. The value is a string.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.common is not None:
            result['Common'] = self.common

        if self.domain_related is not None:
            result['DomainRelated'] = self.domain_related

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.name is not None:
            result['Name'] = self.name

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('Common') is not None:
            self.common = m.get('Common')

        if m.get('DomainRelated') is not None:
            self.domain_related = m.get('DomainRelated')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

