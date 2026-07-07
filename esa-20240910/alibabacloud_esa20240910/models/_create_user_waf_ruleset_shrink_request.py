# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateUserWafRulesetShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        instance_id: str = None,
        name: str = None,
        phase: str = None,
        rules_shrink: str = None,
        shared_shrink: str = None,
        status: str = None,
    ):
        # The description of the WAF ruleset.
        self.description = description
        # The match expression of the WAF ruleset. Rules in this ruleset are evaluated only when a request matches this expression.
        # 
        # Examples:
        # - `http.host eq "example.com"` — Only requests with the host example.com enter this ruleset.
        # - `starts_with(http.uri.path, "/api/")` — Only requests with the /api/ prefix enter this ruleset.
        # 
        # > The complete expression syntax and available field set are subject to the server-side wirefilter dialect.
        # 
        # This parameter is required.
        self.expression = expression
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the WAF ruleset.
        # 
        # **Naming suggestion**: Use a combination of letters, digits, and underscores for easy reference. The specific character set, maximum length, and uniqueness constraints are subject to the WAF ruleset service naming conventions.
        # 
        # This parameter is required.
        self.name = name
        # The phase to which the WAF ruleset belongs. Valid values:
        # 
        # - http_whitelist: whitelist rules
        # - http_custom: custom rules
        # - http_managed: managed rules
        # - http_anti_scan: scan protection rules
        # - http_ratelimit: rate limiting rules
        # 
        # > Note: The supported fields (Expression match fields, Action values, and others) vary by phase. For more information, refer to the rule configuration documentation for the corresponding phase.
        # 
        # This parameter is required.
        self.phase = phase
        # The list of rule configurations in the WAF ruleset. Each element corresponds to a rule.
        # 
        # - The field structure of each rule is subject to the `WafRuleConfig` data structure, which includes Expression, Action, Name, and other fields.
        self.rules_shrink = rules_shrink
        # The shared fields across multiple rules in this ruleset, such as a unified Action or Name prefix.
        # 
        # > The field structure is subject to the `WafBatchRuleShared` data structure. If you do not need to share properties, you can leave this parameter empty.
        self.shared_shrink = shared_shrink
        # The status of the WAF ruleset. Valid values:
        # 
        # - on: Enabled. The rules in the ruleset participate in matching and blocking.
        # - off: Disabled. The ruleset is retained but does not participate in matching.
        # 
        # > The complete set of valid values is subject to the server-side enum.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        if self.shared_shrink is not None:
            result['Shared'] = self.shared_shrink

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        if m.get('Shared') is not None:
            self.shared_shrink = m.get('Shared')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

