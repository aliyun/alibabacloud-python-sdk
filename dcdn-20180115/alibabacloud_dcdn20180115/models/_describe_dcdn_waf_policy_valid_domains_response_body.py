# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafPolicyValidDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.DescribeDcdnWafPolicyValidDomainsResponseBodyDomains] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the protected domain names.
        self.domains = domains
        # The page number of the returned page, which is the same as the PageNumber parameter in request parameters.
        self.page_number = page_number
        # The number of domain names returned per page, which is the same as the PageSize parameter in request parameters.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of domain names returned.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.DescribeDcdnWafPolicyValidDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnWafPolicyValidDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        policies: List[main_models.DescribeDcdnWafPolicyValidDomainsResponseBodyDomainsPolicies] = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The protected domain name.
        self.domain_name = domain_name
        # The policy that is bound to the domain name.
        self.policies = policies
        # The ID of the protection policy.
        self.policy_id = policy_id
        # The name of the protection policy.
        self.policy_name = policy_name
        # Indicates whether the protection policy is the default policy. Valid values:
        # 
        # *   default: The protection policy is the default policy.
        # *   custom: The protection policy is not the default policy.
        self.policy_type = policy_type

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeDcdnWafPolicyValidDomainsResponseBodyDomainsPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

class DescribeDcdnWafPolicyValidDomainsResponseBodyDomainsPolicies(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        # The ID of the rule.
        self.id = id
        # The name of the policy.
        self.name = name
        # The type of the policy.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

