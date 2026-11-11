# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class BatchUpdateWafRulesRequest(DaraModel):
    def __init__(
        self,
        configs: List[main_models.WafRuleConfig] = None,
        phase: str = None,
        ruleset_id: int = None,
        shared: main_models.WafBatchRuleShared = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The list of rule configurations, which specifies the detailed configuration of each rule.
        # 
        # **Required sub-fields for each phase** (applicable only to the two phases supported by this batch operation):
        # 
        # - `http_anti_scan`: You must provide `Type`, and at least one of `ManagedList` or `RateLimit`.
        # - `http_bot`: You must provide configurations related to advanced bot management. The sub-fields are subject to the definition of the `WafRuleConfig` data structure.
        # 
        # > Note: Other phases such as `http_custom` and `http_whitelist` cannot be updated by using this batch operation. Use the single-rule operation `UpdateWafRule` instead. The sub-field constraints are subject to the documentation of the single-rule operation.
        # 
        # > Note: If `Configs` is empty or sub-fields are missing, the server returns an `InvalidParameter(400)` or `Rule.Config.Malformed` error.
        self.configs = configs
        # The execution phase of WAF rules. This **batch operation supports only** the following two phases. For other phases, use the single-rule operation `UpdateWafRule`:
        # - `http_anti_scan`: scan protection rules
        # - `http_bot`: advanced bot management rules
        # 
        # > Note: The `http_anti_scan` and `http_bot` phases **support only batch updates**. The single-rule operation `UpdateWafRule` does not accept these two values. Conversely, other phases (such as `http_custom` and `http_whitelist`) can only be updated by using the single-rule operation and cannot be updated by using this batch operation.
        # 
        # **Required constraint**: Although this parameter is marked as optional (required: false) in the specification, it **must be specified** when you call this batch operation. The server cannot determine the target rule set without the Phase parameter. If this parameter is not provided, an `InvalidParameter(400)` error is returned.
        self.phase = phase
        # The ID of the WAF rule set. You can obtain the ID by calling the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) operation.
        self.ruleset_id = ruleset_id
        # The shared configuration for multiple rules, which specifies the common properties of multiple rules.
        # 
        # **Conditional requirement**: Although this parameter is marked as optional (required: false) in the specification, it is **actually required** when `Phase` is set to `http_anti_scan`. If this parameter is not provided, the server returns an `InvalidParameter(400)` error.
        # 
        # **Sub-field requirements**: In the `http_anti_scan` phase, the Shared parameter must include shared fields such as `Name` (rule name), `Expression` (match expression), and `Action` (rule action). For other phases, the required sub-fields of Shared depend on the specific phase.
        self.shared = shared
        # The ID of the site. You can obtain the ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version for which the configuration takes effect. Default value: 0.
        self.site_version = site_version

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()
        if self.shared:
            self.shared.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['Configs'].append(k1.to_map() if k1 else None)

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.shared is not None:
            result['Shared'] = self.shared.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k1 in m.get('Configs'):
                temp_model = main_models.WafRuleConfig()
                self.configs.append(temp_model.from_map(k1))

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('Shared') is not None:
            temp_model = main_models.WafBatchRuleShared()
            self.shared = temp_model.from_map(m.get('Shared'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

