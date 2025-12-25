# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceInstanceCertsResponseBody(DaraModel):
    def __init__(
        self,
        certs: List[main_models.DescribeResourceInstanceCertsResponseBodyCerts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The certificates.
        self.certs = certs
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certs = []
        if m.get('Certs') is not None:
            for k1 in m.get('Certs'):
                temp_model = main_models.DescribeResourceInstanceCertsResponseBodyCerts()
                self.certs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeResourceInstanceCertsResponseBodyCerts(DaraModel):
    def __init__(
        self,
        after_date: int = None,
        before_date: int = None,
        cert_identifier: str = None,
        cert_name: str = None,
        common_name: str = None,
        domain: str = None,
        is_chain_completed: bool = None,
    ):
        # The time when the certificate expires.
        self.after_date = after_date
        # The time when the certificate was issued.
        self.before_date = before_date
        # The globally unique ID of the certificate. The value is in the "Certificate ID-cn-hangzhou" format. For example, if the ID of the certificate is 123, the value of CertIdentifier is 123-cn-hangzhou.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The common name.
        self.common_name = common_name
        # The domain name for which the certificate is issued.
        self.domain = domain
        # Indicates whether the certificate chain is complete.
        self.is_chain_completed = is_chain_completed

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

        if self.is_chain_completed is not None:
            result['IsChainCompleted'] = self.is_chain_completed

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

        if m.get('IsChainCompleted') is not None:
            self.is_chain_completed = m.get('IsChainCompleted')

        return self

