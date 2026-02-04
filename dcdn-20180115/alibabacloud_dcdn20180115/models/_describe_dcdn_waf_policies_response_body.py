# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policies: List[main_models.DescribeDcdnWafPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page. Valid values: **1** to **100000**. Default value: **1**.
        self.page_number = page_number
        # The number of protection policies returned per page. Valid values: an integer from **1** to **500**. Default value: **20**.
        self.page_size = page_size
        # The information about protection policies.
        self.policies = policies
        # The ID of the request.
        self.request_id = request_id
        # The total number of protection policies.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeDcdnWafPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDcdnWafPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        domain_count: int = None,
        gmt_modified: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_status: str = None,
        policy_type: str = None,
        rule_count: int = None,
    ):
        # The type of the protection policy, which is the same as the DefenseScenes field in the QueryArgs parameter.
        self.defense_scene = defense_scene
        # The number of domain names that use the protection policy.
        self.domain_count = domain_count
        # The time when the protection policy was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the protection policy.
        self.policy_id = policy_id
        # The name of the protection policy.
        self.policy_name = policy_name
        # The status of the protection policy, which is the same as the PolicyStatus field in the QueryArgs parameter.
        self.policy_status = policy_status
        # Indicates whether this protection policy is the default policy, which is the same as the PolicyType field in the QueryArgs parameter.
        self.policy_type = policy_type
        # The number of protection rules in the protection policy.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

