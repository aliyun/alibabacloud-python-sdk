# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafRuleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule: main_models.DescribeDcdnWafRuleResponseBodyRule = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the protection rule.
        self.rule = rule

    def validate(self):
        if self.rule:
            self.rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule is not None:
            result['Rule'] = self.rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rule') is not None:
            temp_model = main_models.DescribeDcdnWafRuleResponseBodyRule()
            self.rule = temp_model.from_map(m.get('Rule'))

        return self

class DescribeDcdnWafRuleResponseBodyRule(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        gmt_modified: str = None,
        policy_id: int = None,
        rule_config: str = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_status: str = None,
    ):
        # The type of the protection policy. Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: IP address whitelist
        self.defense_scene = defense_scene
        # The time when the scaling group was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the protection policy.
        self.policy_id = policy_id
        # The configurations of the protection rule.
        self.rule_config = rule_config
        # The ID of the protection rule.
        self.rule_id = rule_id
        # The name of the protection rule.
        self.rule_name = rule_name
        # The status of the protection rule. Valid values:
        # 
        # *   on
        # *   off
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        return self

