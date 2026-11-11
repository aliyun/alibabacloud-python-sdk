# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchCreateWafRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        configs_shrink: str = None,
        phase: str = None,
        ruleset_id: int = None,
        shared_shrink: str = None,
        site_id: int = None,
        site_version: int = None,
    ):
        # The list of rule configurations, which specifies the detailed configuration of each rule.
        # 
        # **Required subfields for each phase** (only applicable to the two phases supported by this batch operation):
        # 
        # - http_anti_scan: You must provide Type and at least one of ManagedList or RateLimit.
        # - http_bot: You must provide configurations related to advanced bots. The subfields are subject to the WafRuleConfig data structure definition.
        # 
        # > Note: Other phases such as http_custom and http_whitelist cannot use this batch operation. Use the single-item operation CreateWafRule instead. The subfield constraints are subject to the single-item operation documentation.
        # 
        # > Notice: If Configs is missing or subfields are missing, the service returns InvalidParameter(400) or Rule.Config.Malformed.
        self.configs_shrink = configs_shrink
        # The execution phase of the WAF rule. This **batch operation only supports** the following two phases. For other phases, use the single-item operations CreateWafRule or UpdateWafRule:
        # - http_anti_scan: Scan protection rules.
        # - http_bot: Advanced bots.
        # 
        # > Note: The http_anti_scan and http_bot phases **only support batch creation**. The single-item operation CreateWafRule does not accept these two values. Conversely, other phases (such as http_custom and http_whitelist) can only be created by using the single-item operation and cannot use this batch operation.
        # 
        # **Required constraint**: Although this parameter is marked as optional (required: false) in the specification, it **must be provided** when you call this batch operation. If it is not provided, the service returns InvalidParameter(400).
        # 
        # **Edition prerequisite**: http_anti_scan requires the site to have the **High edition or higher**. Calls from the Basic edition return Phase.HttpAntiScan.NotSupport. Verify the site edition before you call the operation.
        self.phase = phase
        # The ID of the WAF ruleset. You can obtain the ruleset ID by calling the [ListWafRulesets](https://help.aliyun.com/document_detail/2878359.html) operation.
        self.ruleset_id = ruleset_id
        # The shared configuration for multiple rules, which specifies the common attributes of the rules.
        # 
        # **Conditionally required**: Although this parameter is marked as optional (required: false) in the specification, it is **actually required** when Phase is set to http_anti_scan. If it is not provided, the service returns InvalidParameter(400).
        # 
        # **Subfield requirements**: In the http_anti_scan phase, Shared must include shared fields such as Name (rule name) and Action (rule action). For other phases, the required subfields of Shared depend on the specific phase.
        self.shared_shrink = shared_shrink
        # The site ID. You can obtain the site ID by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The version number of the site configuration. For sites with configuration version management enabled, you can use this parameter to specify the site version where the configuration takes effect. Default value: 0.
        self.site_version = site_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs_shrink is not None:
            result['Configs'] = self.configs_shrink

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.ruleset_id is not None:
            result['RulesetId'] = self.ruleset_id

        if self.shared_shrink is not None:
            result['Shared'] = self.shared_shrink

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_version is not None:
            result['SiteVersion'] = self.site_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs_shrink = m.get('Configs')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('RulesetId') is not None:
            self.ruleset_id = m.get('RulesetId')

        if m.get('Shared') is not None:
            self.shared_shrink = m.get('Shared')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteVersion') is not None:
            self.site_version = m.get('SiteVersion')

        return self

