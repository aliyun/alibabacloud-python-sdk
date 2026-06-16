# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class ListPcaCaCertificateResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListPcaCaCertificateResponseBodyList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of CA certificates.
        self.list = list
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token for the next page of results. Leave this parameter empty to start the query from the first page. If this parameter is not returned, all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the result set.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

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
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListPcaCaCertificateResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPcaCaCertificateResponseBodyList(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        common_name: str = None,
        issuer_identifier: str = None,
        private_ca_instance_id: str = None,
        private_ca_region_id: str = None,
        status: str = None,
        user_id: str = None,
    ):
        # The certificate identifier. Use this identifier to query certificate details.
        self.cert_identifier = cert_identifier
        # The common name of the certificate. This value matches the CommonName field in the certificate Subject.
        self.common_name = common_name
        # The identifier of the issuer certificate. Use this identifier to query the issuer certificate.
        self.issuer_identifier = issuer_identifier
        # The ID of the private CA instance.
        self.private_ca_instance_id = private_ca_instance_id
        # The region ID of the private CA instance.
        self.private_ca_region_id = private_ca_region_id
        # The certificate status.
        self.status = status
        # The Alibaba Cloud account ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.issuer_identifier is not None:
            result['IssuerIdentifier'] = self.issuer_identifier

        if self.private_ca_instance_id is not None:
            result['PrivateCaInstanceId'] = self.private_ca_instance_id

        if self.private_ca_region_id is not None:
            result['PrivateCaRegionId'] = self.private_ca_region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('IssuerIdentifier') is not None:
            self.issuer_identifier = m.get('IssuerIdentifier')

        if m.get('PrivateCaInstanceId') is not None:
            self.private_ca_instance_id = m.get('PrivateCaInstanceId')

        if m.get('PrivateCaRegionId') is not None:
            self.private_ca_region_id = m.get('PrivateCaRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

