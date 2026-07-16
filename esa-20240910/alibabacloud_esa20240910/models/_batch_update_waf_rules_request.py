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
        # The list of rule configurations. Specifies the detailed configuration for each rule.
        # 
        # **Required subfields for each phase** (applicable only to the two phases supported by this batch operation):
        # 
        # - `http_anti_scan`: You must provide `Type` and at least one of `ManagedList` or `RateLimit`.
        # - `http_bot`: You must provide the advanced mode bots configuration. The subfields are defined in the `WafRuleConfig` data structure.
        # 
        # > Note: Other phases such as `http_custom` and `http_whitelist` cannot use this batch operation. Use the single-rule operation `UpdateWafRule` instead. The subfield constraints for those phases are described in the single-rule operation documentation.
        # 
        # > Important: If `Configs` is missing or subfields are incomplete, the server returns `InvalidParameter(400)` or `Rule.Config.Malformed`.
        self.configs = configs
        # The WAF rule execution phase. This **batch operation supports only** the following two phases. For other phases, use the single-rule operation `UpdateWafRule`:
        # - `http_anti_scan`: scan protection rules
        # - `http_bot`: advanced mode bots
        # 
        # > Note: The `http_anti_scan` and `http_bot` phases **support only batch updates**. The single-rule operation `UpdateWafRule` does not accept these two values. Conversely, other phases such as `http_custom` and `http_whitelist` can be updated only by using the single-rule operation, not this batch operation.
        # 
        # **Required constraint**: Although this parameter is marked as optional (required: false) in the specification, it is **required** when you call this batch operation. The server cannot determine the target ruleset without the Phase parameter and returns `InvalidParameter(400)` if it is not provided.
        self.phase = phase
        # The ID of the WAF ruleset. You can call the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) operation to obtain the ruleset ID.
        self.ruleset_id = ruleset_id
        # The shared configuration for multiple rules. Specifies the common properties shared across multiple rules.
        # 
        # **Conditionally required**: Although this parameter is marked as optional (required: false) in the specification, it is **required** when `Phase=http_anti_scan`. The server returns `InvalidParameter(400)` if it is not provided.
        # 
        # **Subfield requirements**: When the phase is `http_anti_scan`, Shared must include the `Name` (rule name), `Expression` (match expression), and `Action` (rule action) shared fields. For other phases, the required subfields of Shared vary depending on the specific phase.
        self.shared = shared
        # The site ID. You can call the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation to obtain the site ID.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with version management enabled, you can use this parameter to specify the site version on which the configuration takes effect. The default value is 0.
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

