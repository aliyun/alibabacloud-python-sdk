# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetUserWafRulesetResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        ruleset: main_models.GetUserWafRulesetResponseBodyRuleset = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The WAF rule set.
        self.ruleset = ruleset

    def validate(self):
        if self.ruleset:
            self.ruleset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ruleset is not None:
            result['Ruleset'] = self.ruleset.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Ruleset') is not None:
            temp_model = main_models.GetUserWafRulesetResponseBodyRuleset()
            self.ruleset = temp_model.from_map(m.get('Ruleset'))

        return self

class GetUserWafRulesetResponseBodyRuleset(DaraModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        rules: List[main_models.GetUserWafRulesetResponseBodyRulesetRules] = None,
        shared: main_models.WafBatchRuleShared = None,
        status: str = None,
    ):
        # The description of the WAF rule set.
        self.description = description
        # The expression of the WAF rule set.
        self.expression = expression
        # The ID of the WAF rule set.
        self.id = id
        # The name of the WAF rule set.
        self.name = name
        # The evaluation phase of the WAF rule set. Valid values:
        # 
        # - `http_whitelist`: A whitelist rule.
        # 
        # - `http_custom`: A custom rule.
        # 
        # - `http_managed`: A managed rule.
        # 
        # - `http_anti_scan`: A scan protection rule.
        # 
        # - `http_ratelimit`: A rate limiting rule.
        # 
        # - `ip_access_rule`: An IP access rule.
        # 
        # - `http_bot`: A bot management rule.
        # 
        # - `http_security_level_rule`: A security level rule.
        self.phase = phase
        # The position of the WAF rule set.
        self.position = position
        # A list of rules in the WAF rule set.
        self.rules = rules
        # The shared configuration of the WAF rule set.
        self.shared = shared
        # The status of the WAF rule set.
        self.status = status

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.position is not None:
            result['Position'] = self.position

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.shared is not None:
            result['Shared'] = self.shared.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.GetUserWafRulesetResponseBodyRulesetRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('Shared') is not None:
            temp_model = main_models.WafBatchRuleShared()
            self.shared = temp_model.from_map(m.get('Shared'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetUserWafRulesetResponseBodyRulesetRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        characteristics_fields: List[str] = None,
        config: main_models.WafRuleConfig = None,
        fields: List[str] = None,
        id: int = None,
        name: str = None,
        phase: str = None,
        position: int = None,
        ruleset_id: int = None,
        skip: str = None,
        status: str = None,
        tags: List[str] = None,
        type: str = None,
        update_time: str = None,
    ):
        # The action for the rule. Valid values:
        # 
        # - `deny`: Blocks the request.
        # 
        # - `monitor`: Monitors the request.
        # 
        # - `js`: Triggers a JS challenge.
        # 
        # - `captcha`: Triggers a CAPTCHA challenge.
        self.action = action
        # A list of WAF rule statistics fields.
        self.characteristics_fields = characteristics_fields
        # The WAF rule configuration.
        self.config = config
        # A list of WAF rule match fields.
        self.fields = fields
        # The ID of the WAF rule.
        self.id = id
        # The name of the WAF rule.
        self.name = name
        # The evaluation phase of the WAF rule. Valid values:
        # 
        # - `http_whitelist`: A whitelist rule.
        # 
        # - `http_custom`: A custom rule.
        # 
        # - `http_managed`: A managed rule.
        # 
        # - `http_anti_scan`: A scan protection rule.
        # 
        # - `http_ratelimit`: A rate limiting rule.
        # 
        # - `ip_access_rule`: An IP access rule.
        # 
        # - `http_bot`: A bot management rule.
        # 
        # - `http_security_level_rule`: A security level rule.
        self.phase = phase
        # The position of the WAF rule.
        self.position = position
        # The ID of the WAF rule set.
        self.ruleset_id = ruleset_id
        # The skip mode for the WAF rule.
        self.skip = skip
        # The status of the WAF rule.
        self.status = status
        # The phases that the rule skips.
        self.tags = tags
        # The type of the WAF rule.
        self.type = type
        # The time the WAF rule was last updated.
        self.update_time = update_time

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.characteristics_fields is not None:
            result['CharacteristicsFields'] = self.characteristics_fields

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.fields is not None:
            result['Fields'] = self.fields

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.position is not None:
            result['Position'] = self.position

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.skip is not None:
            result['Skip'] = self.skip

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('CharacteristicsFields') is not None:
            self.characteristics_fields = m.get('CharacteristicsFields')

        if m.get('Config') is not None:
            temp_model = main_models.WafRuleConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('Skip') is not None:
            self.skip = m.get('Skip')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

