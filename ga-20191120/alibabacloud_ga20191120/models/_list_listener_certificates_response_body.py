# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListListenerCertificatesResponseBody(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.ListListenerCertificatesResponseBodyCertificates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The certificates.
        self.certificates = certificates
        # The maximum number of entries returned.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The number of entries returned.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
                temp_model = main_models.ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListListenerCertificatesResponseBodyCertificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        domain: str = None,
        is_default: bool = None,
        state: str = None,
    ):
        # The certificate ID.
        self.certificate_id = certificate_id
        # The domain name associated with the additional certificate.
        # 
        # This parameter is not returned if the certificate is a default one.
        self.domain = domain
        # Indicates whether the certificate is a default one.
        # 
        # *   **true**
        # *   **false**
        self.is_default = is_default
        # The status of the certificate.
        # 
        # *   **active**: The certificate is associated with a listener and in effect.
        # *   **updating**: The additional certificate is being replaced.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

