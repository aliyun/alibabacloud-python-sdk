# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeCertDetailResponseBody(DaraModel):
    def __init__(
        self,
        cert_detail: main_models.DescribeCertDetailResponseBodyCertDetail = None,
        request_id: str = None,
    ):
        # The details of the certificate.
        self.cert_detail = cert_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cert_detail:
            self.cert_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_detail is not None:
            result['CertDetail'] = self.cert_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertDetail') is not None:
            temp_model = main_models.DescribeCertDetailResponseBodyCertDetail()
            self.cert_detail = temp_model.from_map(m.get('CertDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCertDetailResponseBodyCertDetail(DaraModel):
    def __init__(
        self,
        after_date: int = None,
        before_date: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain: str = None,
        sans: List[str] = None,
    ):
        # The time when the certificate expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.after_date = after_date
        # The time when the certificate was issued. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.before_date = before_date
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The primary domain name, which is a common name.
        self.common_name = common_name
        # The domain name that is associated with the certificate.
        self.domain = domain
        # The other domain names that are associated with the certificate.
        self.sans = sans

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.after_date is not None:
            result['AfterDate'] = self.after_date

        if self.before_date is not None:
            result['BeforeDate'] = self.before_date

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.sans is not None:
            result['Sans'] = self.sans

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AfterDate') is not None:
            self.after_date = m.get('AfterDate')

        if m.get('BeforeDate') is not None:
            self.before_date = m.get('BeforeDate')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        return self

