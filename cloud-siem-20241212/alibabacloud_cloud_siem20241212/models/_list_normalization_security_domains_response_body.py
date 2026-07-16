# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListNormalizationSecurityDomainsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_security_domains: List[main_models.ListNormalizationSecurityDomainsResponseBodyNormalizationSecurityDomains] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned in this query.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or if no more results exist. If more results exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The list of security domains.
        self.normalization_security_domains = normalization_security_domains
        # Id of the request
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.normalization_security_domains:
            for v1 in self.normalization_security_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NormalizationSecurityDomains'] = []
        if self.normalization_security_domains is not None:
            for k1 in self.normalization_security_domains:
                result['NormalizationSecurityDomains'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.normalization_security_domains = []
        if m.get('NormalizationSecurityDomains') is not None:
            for k1 in m.get('NormalizationSecurityDomains'):
                temp_model = main_models.ListNormalizationSecurityDomainsResponseBodyNormalizationSecurityDomains()
                self.normalization_security_domains.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNormalizationSecurityDomainsResponseBodyNormalizationSecurityDomains(DaraModel):
    def __init__(
        self,
        normalization_security_domain_id: str = None,
        normalization_security_domain_name: str = None,
    ):
        # The security domain ID.
        self.normalization_security_domain_id = normalization_security_domain_id
        # The security domain name.
        self.normalization_security_domain_name = normalization_security_domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normalization_security_domain_id is not None:
            result['NormalizationSecurityDomainId'] = self.normalization_security_domain_id

        if self.normalization_security_domain_name is not None:
            result['NormalizationSecurityDomainName'] = self.normalization_security_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationSecurityDomainId') is not None:
            self.normalization_security_domain_id = m.get('NormalizationSecurityDomainId')

        if m.get('NormalizationSecurityDomainName') is not None:
            self.normalization_security_domain_name = m.get('NormalizationSecurityDomainName')

        return self

