# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.DescribeDcdnWafPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The information about the protection policy.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.DescribeDcdnWafPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        domain_count: int = None,
        gmt_modified: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_status: str = None,
        policy_type: str = None,
        rule_configs: str = None,
        rule_count: int = None,
    ):
        # The type of the protection policy. Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: whitelist
        self.defense_scene = defense_scene
        # The number of domain names that use the protection policy.
        self.domain_count = domain_count
        # The time when the protection policy was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the protection policy.
        self.policy_id = policy_id
        # The name of the protection policy.
        self.policy_name = policy_name
        # The status of the protection policy. Valid values:
        # 
        # *   on
        # *   off
        self.policy_status = policy_status
        # Indicates whether the current policy is the default policy. Valid values:
        # 
        # *   default
        # *   custom
        self.policy_type = policy_type
        # The protection rule configurations corresponding to the protection policy. The configurations only support Bot management. For more information, see [BatchCreateDcdnWafRules](~~BatchCreateDcdnWafRules~~).
        self.rule_configs = rule_configs
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

        if self.rule_configs is not None:
            result['RuleConfigs'] = self.rule_configs

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

        if m.get('RuleConfigs') is not None:
            self.rule_configs = m.get('RuleConfigs')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

